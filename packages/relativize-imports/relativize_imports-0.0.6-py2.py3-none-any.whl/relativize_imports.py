import argparse
import ast
import glob
import os
import re
from pathlib import Path
from typing import MutableMapping
from typing import Optional
from typing import Sequence
from typing import Tuple
import configparser

def _find_relative_depth(parts: Sequence[str], module: str) -> int:
    depth = 0
    for n, _ in enumerate(parts, start=1):
        if module.startswith(".".join(parts[:n])):
            depth += 1
        else:
            break
    return depth


def _is_python_file_or_dir(path: str) -> bool:
    return os.path.exists(path + ".py") or os.path.isdir(path)


class Visitor(ast.NodeVisitor):
    def __init__(self, parts: Sequence[str], root_path: str) -> None:
        self.parts = parts
        self.root_path = root_path
        self.to_replace: MutableMapping[int, Tuple[str, str]] = {}

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        level = node.level
        is_relative = level > 0

        if is_relative:
            self.generic_visit(node)
            return

        module_parts = node.module.split(".")

        if not _is_python_file_or_dir(os.path.join(self.root_path, *module_parts)):
            # Can't convert to relative, might be third-party
            return

        depth = _find_relative_depth(self.parts, node.module)
        if depth == 0:
            # don't attempt relative import beyond top-level package
            return
        inverse_depth = len(self.parts) - depth
        if node.module == ".".join(self.parts[:depth]):
            # e.g from a.b.c import d -> from . import d
            n_dots = inverse_depth
        else:
            # e.g. from a.b.c import d -> from ..c import d
            n_dots = inverse_depth - 1

        replacement = f'\\1{"." * n_dots}'
        self.to_replace[node.lineno] = (
            rf'(from\s+){".".join(module_parts[:depth])}',
            replacement,
        )
        self.generic_visit(node)
        return


def relativize_imports(file_path: str, root_path: str) -> bool:
    full_path = Path(file_path).resolve()
    relative_path = full_path.relative_to(root_path)

    content = full_path.read_text()
    tree = ast.parse(content)

    visitor = Visitor(relative_path.parts, root_path)
    visitor.visit(tree)

    if not visitor.to_replace:
        return False

    newlines = []
    for lineno, line in enumerate(content.splitlines(keepends=True), start=1):
        if lineno in visitor.to_replace:
            re1, re2 = visitor.to_replace[lineno]
            subbed = re.sub(re1, re2, line)
            print(f"{file_path}:{lineno} :: '{line.strip()}' -> '{subbed.strip()}'")
            line = subbed
        newlines.append(line)
    with open(file_path, "w", encoding="utf-8", newline="") as fd:
        fd.write("".join(newlines))
    return True


def main(argv: Optional[Sequence[str]] = None):
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*")
    args = parser.parse_args(argv)

    root = os.getcwd()

    file_paths = args.files or ["."]
    changed_count = 0
    for path in file_paths:
        current_root = root
        excluded_file_paths = []
        if path.endswith(".py"):
            file_paths = [path]
        else:
            file_paths = [path for path in glob.glob(os.path.join(path, "**", "*.py"), recursive=True)]
            current_root = os.path.join(root, path)
            if os.path.exists(os.path.join(path, "tox.ini")):
                config = configparser.ConfigParser()
                config.read(os.path.join(path, "tox.ini"))
                excluded_file_paths = [os.path.join(path, file_path) for file_path in config["relativize-imports"]["ignore"].split(",")]
        for file_path in file_paths:
            if any(file_path.startswith(excluded_path) for excluded_path in excluded_file_paths):
                continue
            changed = relativize_imports(file_path, current_root)
            if changed:
                changed_count += 1

    if not changed_count:
        print("Nothing changed 👌")
    else:
        print(f"{changed_count} files converted 🔨")


if __name__ == "__main__":
    main()
