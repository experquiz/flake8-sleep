import ast
import sys
from typing import Any
from typing import Generator
from typing import List
from typing import Tuple
from typing import Type

if sys.version_info < (3, 8):  # pragma: no cover (<PY38)
    import importlib_metadata
else:  # pragma: no cover (PY38+)
    import importlib.metadata as importlib_metadata

SLP100 = "SLP100 sleep found"
SLP101 = "SLP101 sleep used as a function name."


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.errors: List[Tuple[int, int, str]] = []
        super().__init__()

    def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
        if node.name == "sleep":
            self.errors.append((node.lineno, node.col_offset, SLP101))
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> Any:
        if isinstance(node.func, ast.Name) and node.func.id == "sleep":
            self.errors.append(
                (node.func.lineno, node.func.col_offset, SLP100),
            )
        if isinstance(node.func, ast.Attribute) and node.func.attr == "sleep":
            self.errors.append(
                (node.func.lineno, node.func.col_offset, SLP100),
            )
        self.generic_visit(node)


class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST):
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)
        for line, col, msg in visitor.errors:
            yield line, col, msg, type(self)
