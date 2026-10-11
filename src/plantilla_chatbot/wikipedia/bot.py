from functools import lru_cache
from typing import Dict

import mwparserfromhell
import pywikibot
from pywikibot.bot import SingleSiteBot
from pywikibot.comms.eventstreams import EventStreams

import plantilla_chatbot.filters.thresholds as thresholds
from plantilla_chatbot.analyse.tests import RegexTests


class PlantillaChatbotBOT(SingleSiteBot):
    def treat(self, page: pywikibot.Page):
        text = page.get()
        if text[-1] == "\n":
            page.text += ":{{subst:chatbot}} ~~~~"
        else:
            page.text += "\n:{{subst:chatbot}} ~~~~"
        page.save(summary="Respondiendo autómaticamente a mensaje generado por LLM")

    def run(self):
        stream = EventStreams(streams="recentchange")
        stream.register_filter(
            wiki="eswiki",
            namespace=(4),
            type="edit",
            title="Wikipedia:Café/Archivo/Ayuda/Actual",
        )

        for change in stream:
            page = pywikibot.Page(
                self.site,
                change["title"],
            )
            if (
                not self.valid(change)
                and not self.score(page) > thresholds.TESTS_THRESHOLD
            ):
                continue
            self.treat(page)

    def valid(self, change: Dict) -> bool:
        username: str = change.get("user", "")
        diff: int = change.get("lenght")["new"] - change.get("lenght")["old"]
        user_groups = self.retrieve_user(username).groups()
        return diff > 0 and "autoconfirmed" not in user_groups

    def score(self, page: pywikibot.Page) -> float:
        text = page.get()
        wikicode = mwparserfromhell.parse(text)
        last_comment = wikicode.get_sections(levels=(2,))[-1]
        regex_test = RegexTests(str(last_comment))
        return regex_test.score()

    @lru_cache(maxsize=500)
    def retrieve_user(self, username: str) -> pywikibot.User:
        return pywikibot.User(self.site, username)
