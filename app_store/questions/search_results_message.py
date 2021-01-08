from screenpy import Actor
from screenpy.pacing import beat
from screenpy.questions import Text

from app_store.user_interface.app_store_search_result_page import RESULTS_MESSAGE


class SearchResultsMessage:
    @beat("{0} checks the results message...")
    def answered_by(self, the_actor: Actor) -> str:
        return Text.of(RESULTS_MESSAGE).answered_by(the_actor)