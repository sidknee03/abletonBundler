"""ExportManager — orchestrator; the single entry point a GUI or CLI should call."""

from pathlib import Path


class ExportManager:
    def __init__(self, alsPath: Path, outputDir: Path):
        self.alsPath = Path(alsPath)
        self.outputDir = Path(outputDir)

    def _makeBundleName(self) -> str:
        """Build a bundle name from the project name plus today's date
        (e.g. "MyTrack_2026-09-11"), appending a counter suffix if a bundle
        or zip with that name already exists in outputDir, so repeat
        exports never collide."""
        # TODO: implement
        pass

    def exportProject(self) -> Path:
        """Run the full export pipeline in order so the result is a
        complete carbon copy of the project: load the .als, scan it for
        samples, patches, and plugins (ProjectScanner.findSamples +
        findPatches + findPlugins), build the bundle folder and copy every
        sample/patch found on disk into it, write the debrief (listing
        non-stock plugins with links and flagging anything still missing),
        and zip the result. Return the path to the final zip file. This is
        the single method a CLI or GUI should call."""
        # TODO: implement
        pass
