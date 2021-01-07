from selenium.webdriver.common.keys import Keys

from screenpy import Actor
from screenpy.actions import Enter, Wait
from screenpy.pacing import beat

    from ..user_interface.amazon_search_text_field import *
    from ..user_interface.amazon_search_result import *


    class SearchAmazon:
        def __init__(self, search_query):
            self.search_query = search_query

        @staticmethod
        def for_text(search_query: str) -> "SearchAmazon":
            return SearchAmazon(search_query)
        
        @beat("{0} searches Amazon for '{search_query}'")
        def perform_as(self, the_actor: Actor) -> None:
            the_actor.attempts_to(
                Enter.the_text(self.search_query).into(SEARCH_INPUT).then_hit(Keys.RETURN),
                Wait.for_the(RESULT_STATS)) # noise error



