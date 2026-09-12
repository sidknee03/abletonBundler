"""Entry point: python -m abletonBundler export --als ... --output ..."""

import sys

from .cli import CLI


def main() -> None:
    """Run the CLI against sys.argv and exit the process with its return code."""
    # TODO: sys.exit(CLI().run())
    pass


if __name__ == "__main__":
    main()
