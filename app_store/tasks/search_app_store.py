from screenpy import Actor
from screenpy.abilities import BrowseTheWeb
from screenpy.actions import Wait
from screenpy.pacing import beat

from app_store.user_interface.app_store_search_result_page import RESULTS_MESSAGE


class SearchAppStore:
    @staticmethod
    def __init__(self, search_query):
        self.search_query = search_query

    def for_text(search_query: str) -> "SearchAppStore":
        return SearchAppStore(search_query)

    @beat("{0} search App Store for '{search_query}'")
    def perform_as(self, the_actor: Actor) -> None:
        browser = the_actor.ability_to(BrowseTheWeb).browser   # fixing by exception
        browser.get(self.URL)                                  # fixing by exception
        the_actor.attempts_to(Wait.for_the(RESULTS_MESSAGE))


