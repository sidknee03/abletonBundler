"""Later phase: simple GUI with an "Export & Share" button.

Should call ExportManager.exportProject() as its only integration point
with the rest of the package — no export logic belongs in here.
"""

from pathlib import Path


class ExportGUI:
    def __init__(self):
        """Set up the window and widgets: a file picker for the .als
        project, a folder picker for the output directory, an "Export &
        Share" button, and a status/progress area."""
        # TODO: implement
        pass

    def onExportClicked(self, alsPath: Path, outputDir: Path) -> None:
        """Handle the "Export & Share" button click: construct an
        ExportManager for alsPath/outputDir, call exportProject(), and
        surface the resulting zip path or any error back to the user."""
        # TODO: implement
        pass

    def run(self) -> None:
        """Start the GUI event loop and block until the window is closed."""
        # TODO: implement
        pass
