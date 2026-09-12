"""DebriefGenerator — writes debrief.txt summarizing plugins used and flagging missing samples/patches."""

from pathlib import Path
from typing import List

from .models import PluginReference, SampleReference


class DebriefGenerator:
    def __init__(self, bundleDir: Path):
        self.bundleDir = Path(bundleDir)

    def generate(
        self,
        plugins: List[PluginReference],
        samples: List[SampleReference],
        projectName: str,
    ) -> Path:
        """Write debrief.txt into self.bundleDir listing:
        - every non-stock plugin used (de-duplicated), printing its link
          when PluginReference.link is set, or just its name otherwise —
          since the plugin binary itself can't be bundled;
        - every sample or patch (from the combined samples list, regardless
          of kind) that couldn't be found on disk, so nothing goes missing
          silently.
        Return the path to the written file."""
        # TODO: implement
        pass
