from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


class TACInstr:
    def to_line(self) -> str:  # pragma: no cover
        raise NotImplementedError


@dataclass(frozen=True)
class TACAssign(TACInstr):
    target: str
    value: str

    def to_line(self) -> str:
        return f"{self.target} = {self.value}"


@dataclass(frozen=True)
class TACBinary(TACInstr):
    target: str
    left: str
    op: str
    right: str

    def to_line(self) -> str:
        return f"{self.target} = {self.left} {self.op} {self.right}"


@dataclass(frozen=True)
class TACPrint(TACInstr):
    value: str

    def to_line(self) -> str:
        return f"print {self.value}"


@dataclass(frozen=True)
class TACLabel(TACInstr):
    name: str

    def to_line(self) -> str:
        return f"{self.name}:"


@dataclass(frozen=True)
class TACIfFalse(TACInstr):
    left: str
    op: str
    right: str
    goto_label: str

    def to_line(self) -> str:
        return f"ifFalse {self.left} {self.op} {self.right} goto {self.goto_label}"


@dataclass(frozen=True)
class TACGoto(TACInstr):
    goto_label: str

    def to_line(self) -> str:
        return f"goto {self.goto_label}"

