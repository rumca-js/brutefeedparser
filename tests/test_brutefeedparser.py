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


class BruteFeedParserTest(unittest.TestCase):

    def test_is_valid__true_youtube(self):
        reader = BruteFeedParser.parse(webpage_samtime_youtube_rss)

        # call tested function
        self.assertTrue(reader.is_valid())

    def test_is_valid__true(self):
        reader = BruteFeedParser.parse(webpage_old_pubdate_rss)
        entries = reader.get_entries()

        # call tested function
        self.assertTrue(reader.is_valid())

    def test_is_valid__geek_true(self):
        reader = BruteFeedParser.parse(geekwire_feed)
        entries = reader.get_entries()

        # call tested function
        self.assertTrue(reader.is_valid())

    def test_is_valid__warhammer_true(self):
        reader = BruteFeedParser.parse(warhammer_community_rss)
        entries = reader.get_entries()

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
            reader.feed.media_thumbnail["url"],
            "https://thumbnails.lbry.com/UCd6vEDS3SOhWbXZrxbrf_bw",
        )
        self.assertTrue(reader.is_valid())

    def test_get_author(self):
        reader = BruteFeedParser.parse(webpage_rss_cdata)

        # call tested function
        self.assertEqual(reader.feed.author, "SAMTIME author")
        self.assertTrue(reader.is_valid())

    def test_get_entries__len(self):
        reader = BruteFeedParser.parse(webpage_rss_cdata)

        # call tested function
        entries = reader.get_entries()

        entries = list(entries)
        self.assertEqual(len(entries), 15)

        entry = entries[0]
        self.assertEqual(entry["title"], "First entry title")
        self.assertEqual(entry["description"], "First entry description")
        self.assertTrue(reader.is_valid())

    def test_get_entries__old_date(self):
        # default language
        reader = BruteFeedParser.parse(webpage_old_pubdate_rss)
        entries = reader.get_entries()
        entries = list(entries)
        self.assertEqual(len(entries), 1)

        entry = entries[0]
        self.assertEqual(entry["title"], "First entry title")
        self.assertEqual(entry["description"], "First entry description")
        self.assertEqual(entry["date_published"].year, 2020)
        self.assertTrue(reader.is_valid())

    def test_get_entries__current_year(self):
        reader = BruteFeedParser.parse(webpage_no_pubdate_rss)

        # call tested function
        entries = reader.get_entries()
        entries = list(entries)

        self.assertEqual(len(entries), 1)

        current_date_time = datetime.now()

        entry = entries[0]
        self.assertEqual(entry["title"], "First entry title")
        self.assertEqual(entry["description"], "First entry description")
        self.assertEqual(entry["date_published"].year, current_date_time.year)
        self.assertTrue(reader.is_valid())

    def test_get_entries__page_rating(self):
        reader = BruteFeedParser.parse(webpage_no_pubdate_rss)

        # call tested function
        entries = reader.get_entries()
        entries = list(entries)

        self.assertEqual(len(entries), 1)

        entry = entries[0]
        self.assertTrue(entry["page_rating"] > 0)

    def test_get_entries__rss(self):
        reader = BruteFeedParser.parse(webpage_old_pubdate_rss)

        # call tested function
        entries = list(reader.get_entries())

        self.assertTrue(len(entries) > 0)

    def test_get_entries__geek(self):
        reader = BruteFeedParser.parse(geekwire_feed)

        # call tested function
        entries = list(reader.get_entries())

        self.assertTrue(len(entries) > 0)

    def test_get_entries__hackernews(self):
        reader = BruteFeedParser.parse(webpage_hackernews_rss)

        # call tested function
        entries = list(reader.get_entries())

        self.assertTrue(len(entries) > 0)

        self.assertIn("author", entries[0])
        self.assertTrue(entries[0]["author"])

    def test_get_entries__reddit(self):
        reader = BruteFeedParser.parse(reddit_rss_text)

        # call tested function
        entries = list(reader.get_entries())

        self.assertTrue(len(entries) > 0)

        self.assertIn("author", entries[0])
        self.assertTrue(entries[0]["author"])
