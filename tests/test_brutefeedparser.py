from datetime import datetime
import unittest

from brutefeedparser import BruteFeedParser


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


class BruteFeedParserFeedTest(unittest.TestCase):

    def test_is_valid__true_youtube(self):
        reader = BruteFeedParser.parse(webpage_samtime_youtube_rss)

        # call tested function
        self.assertTrue(reader.is_valid())

    def test_is_valid__true(self):
        reader = BruteFeedParser.parse(webpage_old_pubdate_rss)
        entries = reader.entries

        # call tested function
        self.assertTrue(reader.is_valid())

    def test_is_valid__geek_true(self):
        reader = BruteFeedParser.parse(geekwire_feed)
        entries = reader.entries

        # call tested function
        self.assertTrue(reader.is_valid())

    def test_is_valid__warhammer_true(self):
        reader = BruteFeedParser.parse(warhammer_community_rss)
        entries = reader.entries

        # call tested function
        self.assertTrue(reader.is_valid())

    def test_get_title__rss(self):
        reader = BruteFeedParser.parse(webpage_rss_cdata)

        # call tested function
        self.assertTrue(reader.is_valid())
        self.assertEqual(reader.feed.title, "SAMTIME on Odysee")

    def test_get_title__youtube(self):
        # default language
        reader = BruteFeedParser.parse(youtube_channel_rss_linus_tech_tips)
        self.assertEqual(reader.feed.title, "Linus Tech Tips")
        self.assertTrue(reader.is_valid())

    def test_get_description(self):
        reader = BruteFeedParser.parse(webpage_rss_cdata)

        # call tested function
        self.assertEqual(reader.feed.description, "SAMTIME channel description")

    def test_get_language(self):
        reader = BruteFeedParser.parse(webpage_rss_cdata)

        # call tested function
        self.assertEqual(reader.feed.language, "ci")
        self.assertTrue(reader.is_valid())

    def test_get_thumbnail(self):
        reader = BruteFeedParser.parse(webpage_rss_cdata)

        # call tested function
        self.assertEqual(
            reader.feed.image["url"],
            "https://thumbnails.lbry.com/UCd6vEDS3SOhWbXZrxbrf_bw",
        )
        self.assertTrue(reader.is_valid())

    def test_get_author(self):
        reader = BruteFeedParser.parse(webpage_rss_cdata)

        # call tested function
        self.assertEqual(reader.feed.author, "SAMTIME author")
        self.assertTrue(reader.is_valid())

    def test_reddit(self):
        # default language
        p = BruteFeedParser.parse(reddit_rss_text)
        self.assertEqual(p.feed.title, "RSS - Really Simple Syndication")
        self.assertEqual(p.feed.link, "https://www.reddit.com/r/rss/.rss")
        self.assertEqual(len(p.entries), 26)

    def test_youtube(self):
        # default language
        p = BruteFeedParser.parse(webpage_youtube_airpano_feed)
        self.assertEqual(p.feed.title, "AirPano VR")
        self.assertEqual(
            p.feed.link,
            "http://www.youtube.com/feeds/videos.xml?channel_id=UCUSElbgKZpE4Xdh5aFWG-Ig",
        )
        self.assertEqual(len(p.entries), 15)

    def test_the_hill(self):
        # default language
        p = BruteFeedParser.parse(thehill_rss)
        self.assertEqual(p.feed.title, "The Hill News")
        self.assertEqual(p.feed.link, "https://thehill.com")
        self.assertEqual(len(p.entries), 100)

    def test_hacker_news(self):
        # default language
        p = BruteFeedParser.parse(webpage_hackernews_rss)
        self.assertEqual(p.feed.title, "Hacker News: Front Page")
        self.assertEqual(p.feed.link, "https://news.ycombinator.com/")

        self.assertEqual(len(p.entries), 20)

        self.assertTrue(p.entries[0].description.find("Article URL") >= 0)


class BruteFeedParserEntriesTest(unittest.TestCase):

    def test_entries__len(self):
        reader = BruteFeedParser.parse(webpage_rss_cdata)

        # call tested function
        entries = reader.entries

        entries = list(entries)
        self.assertEqual(len(entries), 15)

        entry = entries[0]
        self.assertEqual(entry.title, "First entry title")
        self.assertEqual(entry.description, "First entry description")
        self.assertTrue(reader.is_valid())

    def test_entries__old_date(self):
        # default language
        reader = BruteFeedParser.parse(webpage_old_pubdate_rss)
        entries = reader.entries
        entries = list(entries)
        self.assertEqual(len(entries), 1)

        entry = entries[0]
        self.assertEqual(entry.title, "First entry title")
        self.assertEqual(entry.description, "First entry description")
        self.assertTrue(entry.published.find("2020") >= 0)
        self.assertTrue(reader.is_valid())

    def test_entries__current_year(self):
        reader = BruteFeedParser.parse(webpage_no_pubdate_rss)

        # call tested function
        entries = reader.entries
        entries = list(entries)

        self.assertEqual(len(entries), 1)

        current_date_time = datetime.now()

        entry = entries[0]
        self.assertEqual(entry.title, "First entry title")
        self.assertEqual(entry.description, "First entry description")
        self.assertFalse(entry.published)
        self.assertTrue(reader.is_valid())

    def test_entries__rss(self):
        reader = BruteFeedParser.parse(webpage_old_pubdate_rss)

        # call tested function
        entries = list(reader.entries)

        self.assertTrue(len(entries) > 0)

    def test_entries__geek(self):
        reader = BruteFeedParser.parse(geekwire_feed)

        # call tested function
        entries = list(reader.entries)

        self.assertTrue(len(entries) > 0)

    def test_entries__hackernews(self):
        reader = BruteFeedParser.parse(webpage_hackernews_rss)

        # call tested function
        entries = list(reader.entries)

        self.assertTrue(len(entries) > 0)

        self.assertIn("author", entries[0])
        self.assertTrue(entries[0]["author"])

    def test_entries__reddit(self):
        reader = BruteFeedParser.parse(reddit_rss_text)

        # call tested function
        entries = list(reader.entries)

        self.assertTrue(len(entries) > 0)

        self.assertIn("author", entries[0])
        self.assertTrue(entries[0].author)
