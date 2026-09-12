"""ProjectScanner — walks the XML tree to find every sample, patch, and
plugin reference so the bundle can be a complete carbon copy of the project."""

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Optional

from .models import PluginReference, SampleReference


class ProjectScanner:
    def __init__(self, projectDir: Path):
        self.projectDir = Path(projectDir)

    def findSamples(self, root: ET.Element) -> List[SampleReference]:
        """Walk every SampleRef/FileRef element in the project XML, resolve
        each one to an absolute path (using the Path value if present, or
        projectDir + RelativePath otherwise), check whether it exists on
        disk, tag it with kind=SAMPLE and a best-effort sourceLibrary (via
        _identifySourceLibrary), and return a de-duplicated list of
        SampleReference objects."""
        # TODO: implement
        pass

    def findPatches(self, root: ET.Element) -> List[SampleReference]:
        """Walk preset/patch file references that live outside the raw
        SampleRef elements — e.g. Wavetable table files, Sampler multisample
        zone files, and User Library device presets — resolve and check each
        one exactly like findSamples does, tag it with kind=PATCH, and
        return a de-duplicated list. Exists so "not one missing sample or
        patch" holds: patches get the same missing/bundled tracking as audio
        samples, not just audio files."""
        # TODO: implement
        pass

    def findPlugins(self, root: ET.Element) -> List[PluginReference]:
        """Walk every device under each Devices element in the project XML,
        classify it as VST/VST3/AU/Max for Live (third-party) or Stock
        (native Ableton device, which ships with Ableton and needs nothing
        extra), attach a purchase/info link via pluginLinks.lookupPluginLink
        when one is known, and return a de-duplicated list of
        PluginReference objects keyed by (name, type)."""
        # TODO: implement
        pass

    def _identifySourceLibrary(self, path: str) -> Optional[str]:
        """Check path against known external sample/preset library folder
        patterns (e.g. Splice's default `~/Music/Splice/Sounds/...`, plus
        other common marketplaces) and return the library name if matched,
        or None otherwise. Informational only — a sample under an
        unrecognized folder is still found and bundled the same way, since
        findSamples/findPatches resolve absolute paths anywhere on disk."""
        # TODO: implement
        pass
