"""Writing debrief.txt: non-stock plugins used, and any missing samples."""

from pathlib import Path
from typing import List

from .models import Plugin, Sample


def writeDebrief(bundleDir: Path, plugins: List[Plugin], samples: List[Sample]) -> Path:
    """Write debrief.txt listing non-stock plugins used and any samples that couldn't be found."""
    # TODO: implement
    pass
