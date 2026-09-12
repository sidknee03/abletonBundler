"""Building the bundle folder: copying in the .als file and found samples."""

from pathlib import Path
from typing import List

from .models import Sample


def buildBundle(bundleDir: Path, alsPath: Path, samples: List[Sample]) -> None:
    """Create bundleDir, copy the .als file in, copy every existing sample in, skip missing ones."""
    # TODO: implement
    pass
