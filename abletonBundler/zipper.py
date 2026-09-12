"""Zipper — zips the finished bundle folder into a .zip."""

from pathlib import Path


class Zipper:
    def zipBundle(self, bundleDir: Path, zipPath: Path) -> Path:
        """Zip every file under bundleDir into a single archive at zipPath,
        nesting them under a top-level folder named after bundleDir so the
        zip unpacks into one self-contained folder, and return zipPath."""
        # TODO: implement
        pass
