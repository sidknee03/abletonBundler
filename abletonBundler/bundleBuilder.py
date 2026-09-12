"""BundleBuilder — creates the output folder and copies the .als file, samples, and patches into it."""

from pathlib import Path
from typing import List

from .models import SampleReference


class BundleBuilder:
    def __init__(self, bundleDir: Path):
        self.bundleDir = Path(bundleDir)

    def createBundleDir(self) -> Path:
        """Create self.bundleDir on disk, along with Samples/ and Patches/
        subfolders inside it, and return the bundle directory path."""
        # TODO: implement
        pass

    def copyAlsFile(self, alsPath: Path) -> Path:
        """Copy the .als project file into self.bundleDir and return the
        path it was copied to."""
        # TODO: implement
        pass

    def copySamples(self, samples: List[SampleReference]) -> None:
        """Copy every SampleReference that exists on disk into
        self.bundleDir/Samples (kind=SAMPLE) or self.bundleDir/Patches
        (kind=PATCH), skipping missing ones without raising, avoiding
        filename collisions between files from different source folders,
        and setting each copied reference's targetPath to its location in
        the bundle. Samples and patches get identical treatment here —
        origin (e.g. Splice) doesn't change how they're copied."""
        # TODO: implement
        pass
