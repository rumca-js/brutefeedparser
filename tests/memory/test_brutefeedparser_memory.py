from datetime import datetime
import unittest
import gc
import lxml.etree as ET

from brutefeedparser import BruteFeedParser

from utils.memorychecker import MemoryChecker


from tests.fakeinternetdata import (
    webpage_no_pubdate_rss,
    webpage_old_pubdate_rss,
    webpage_rss_cdata,
)
from tests.fake.youtube import (
    webpage_samtime_youtube_rss,  # you
    youtube_channel_rss_linus_tech_tips,  # uses feed
    webpage_youtube_airpano_feed,
)
from tests.fake.geekwirecom import (
    geekwire_feed,
)
from tests.fake.warhammercommunity import (
    warhammer_community_rss,
)
from tests.fake.hackernews import (
    webpage_hackernews_rss,
)
from tests.fake.reddit import (
    reddit_rss_text,
)
from tests.fake.thehill import (
    thehill_rss,
)
from tests.fake.indexhu import (
    index_hu,
)


class BruteFeedParserMemoryTest(unittest.TestCase):
    """
    Generic feed tests
    """
    def setUp(self):
        self.ignore_memory = False
        self.memory_checker = MemoryChecker()
        memory_increase = self.memory_checker.get_memory_increase()

    def tearDown(self):
        gc.collect()

        if not self.ignore_memory:
            memory_increase = self.memory_checker.get_memory_increase()
            self.assertTrue(memory_increase < 0.1)

    def test_memory_leak(self):
        for number in range(1, 1000):
            reader = BruteFeedParser.parse(webpage_samtime_youtube_rss)

            # call tested function
            self.assertTrue(reader.is_valid())
