"""Orchestrating the full export pipeline — the one function a CLI or GUI calls."""

from pathlib import Path

from .alsLoader import loadAls
from .builder import buildBundle
from .debrief import writeDebrief
from .scanner import findPlugins, findSamples
from .zipper import zipBundle


def exportProject(alsPath: Path, outputDir: Path) -> Path:
    """Run the whole pipeline (load -> scan -> build -> debrief -> zip) and return the final zip path."""
    # TODO: implement
    pass
