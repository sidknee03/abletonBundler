"""ALSProject — loads and decompresses the .als file, exposes the parsed XML tree."""

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional


class ALSProject:
    def __init__(self, alsPath: Path):
        self.alsPath = Path(alsPath)
        self._root: Optional[ET.Element] = None

    def exists(self) -> bool:
        """Return True if self.alsPath points at a real file on disk."""
        # TODO: implement
        pass

    def load(self) -> None:
        """Gzip-decompress self.alsPath, parse the resulting XML, and store
        it in self._root. Raise if the file is missing or not valid gzipped
        XML."""
        # TODO: implement
        pass

    def getRoot(self) -> ET.Element:
        """Return the parsed XML root element, calling load() first if the
        project hasn't been loaded yet."""
        # TODO: implement
        pass
