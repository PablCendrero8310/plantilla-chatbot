import logging
import os
from datetime import datetime, timezone
from functools import lru_cache
from logging import Logger
from typing import Any, Dict

import mwparserfromhell
import pywikibot
from pywikibot.bot import BaseSite, SingleSiteBot
from pywikibot.comms.eventstreams import EventStreams

import plantilla_chatbot.filters.thresholds as thresholds
from plantilla_chatbot.analyse.tests import RegexTests

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class PlantillaChatbotBOT(SingleSiteBot):
    def __init__(self, site: BaseSite | bool | None = True, **kwargs: Any) -> None:
        super().__init__(site, **kwargs)
        self.logger: Logger = self._setup_logging()

    def treat(self, page: pywikibot.Page):
        text = page.get()
        if text.endswith("\n"):
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
            score = self.score(page)
            passed = score > thresholds.TESTS_THRESHOLD
            if not self.valid(change) or not passed:
                continue
            self.treat(page)
            self._log_answer(score, passed, change.get("user"))

    def valid(self, change: Dict) -> bool:
        username: str = change.get("user", "")
        diff: int = change.get("length")["new"] - change.get("length")["old"]
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

    def _setup_logging(self):

        logger = logging.getLogger(f"PlantillaChatbotBOT~{self.site.code}")
        logger.setLevel(logging.INFO)

        if logger.handlers:
            return logger

        # Solo stdout (K8s captura esto automáticamente)
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)

        # Formato simple y claro
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(message)s", datefmt="%Y-%m-%dT%H:%M:%SZ"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger

    def _log_answer(self, score: float, result: bool, user: str):
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
        ts_unix = int(datetime.now(timezone.utc).timestamp())

        message = f"{score}\t{result}\t{user}\t{timestamp}\t{ts_unix}"
        level = logging.WARNING if result else logging.INFO
        self.logger.log(level, message)
