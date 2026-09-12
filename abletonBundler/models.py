"""Sample and Plugin — the two small data shapes passed between steps."""

from dataclasses import dataclass


@dataclass
class Sample:
    path: str
    exists: bool


@dataclass
class Plugin:
    name: str
    isStock: bool
