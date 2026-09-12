"""CLI — argparse wrapper exposing an `export` command."""

import argparse
from typing import List, Optional


class CLI:
    def _buildParser(self) -> argparse.ArgumentParser:
        """Build and return an argparse.ArgumentParser with an "export"
        subcommand that takes required --als and --output arguments."""
        # TODO: implement
        pass

    def run(self, argv: Optional[List[str]] = None) -> int:
        """Parse argv (or sys.argv if None), and for the "export" command
        construct an ExportManager and call exportProject(), printing the
        resulting zip path on success or an error message on failure.
        Return a process exit code (0 for success, non-zero for failure)."""
        # TODO: implement
        pass
