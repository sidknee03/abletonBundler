"""Scanning the parsed .als XML for sample and plugin references."""

from pathlib import Path
from typing import List

from .models import Plugin, Sample


def findSamples(root, projectDir: Path) -> List[Sample]:
    """Walk SampleRef/FileRef elements, resolve each path, check it exists, return the list."""
    # TODO: implement
    pass


def findPlugins(root) -> List[Plugin]:
    """Walk device elements, collect de-duplicated plugin names, flag which are stock vs third-party."""
    # TODO: implement
    pass
