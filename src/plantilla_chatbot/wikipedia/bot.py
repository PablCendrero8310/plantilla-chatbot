import pywikibot
from pywikibot.bot import SingleSiteBot
from pywikibot.comms.eventstreams import EventStreams


class PlantillaChatbotBOT(SingleSiteBot):
    def treat(self, page: pywikibot.Page):
        pass

    def valid(self, change):
        return change["title"] == "Wikipedia:Café/Archivo/Ayuda/Actual"

    def run(self):
        stream = EventStreams(streams="recentchange")
        stream.register_filter(
            wiki="eswiki",
            namespace=(1, 3),
            type="edit",
        )

        for change in stream:
            page = pywikibot.Page(
                self.site,
                change["title"],
            )
            self.treat(page)
