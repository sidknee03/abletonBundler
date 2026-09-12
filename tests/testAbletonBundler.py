"""Smoke tests: a synthetic .als with a found sample, a missing sample, a
missing patch, a third-party plugin, and a stock device, run through
exportProject() end to end."""

import unittest


class TestExportProject(unittest.TestCase):
    def testBundlesFoundSampleAndFlagsMissingSample(self):
        """Build a synthetic gzip-compressed .als fixture with one sample
        that exists on disk and one that doesn't, run
        ExportManager.exportProject(), and assert the resulting zip contains
        the found sample while debrief.txt flags the missing one."""
        # TODO: implement
        pass

    def testFlagsMissingPatchAlongsideMissingSample(self):
        """Build a fixture with a missing preset/patch reference (e.g. a
        Wavetable table file) in addition to a missing sample, and assert
        debrief.txt flags both — patches get the same "nothing missing
        silently" treatment as audio samples."""
        # TODO: implement
        pass

    def testDebriefListsNonStockPluginsDeduplicated(self):
        """Build a fixture where the same third-party plugin is referenced
        on multiple tracks alongside a stock device, and assert debrief.txt
        lists the third-party plugin exactly once and omits the stock
        device entirely."""
        # TODO: implement
        pass

    def testDebriefFallsBackToNameWhenPluginLinkUnknown(self):
        """Build a fixture referencing a third-party plugin not present in
        pluginLinks' static table, and assert debrief.txt still lists the
        plugin by name alone rather than erroring or omitting it."""
        # TODO: implement
        pass


if __name__ == "__main__":
    unittest.main()
