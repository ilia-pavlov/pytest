from typing import Generator

import pytest
from selenium.webdriver import Chrome

from screenpy import Actor, AnActor, given, then, when
from screenpy.abilities import BrowseTheWeb

from screenpy.actions import Open
from screenpy.pacing import act, scene
from screenpy.resolutions import (
    ReadsExactly,
)

from ..user_interface.app_store_home_page import URL
from ..tasks.search_app_store import SearchAppStore
from ..questions.search_results_message import SearchResultsMessage


@pytest.fixture(scope="function", name="ilia")
def fixture_actor() -> Generator:
    the_actor = Actor.named("ilia").who_can(BrowseTheWeb.using(Chrome)) # probably place it in /usr/bin or
    yield the_actor                                                                  # /usr/local/bin.
    the_actor.exit_stage_left


@act("Search")
@scene("Search for Apple Store welcome page")
def test_search_for_main_page(ilia: AnActor) -> None:
    given(ilia).was_able_to(Open.their_browser_on(URL))
    when(ilia).attempts_to(SearchAppStore.for_text("Shop online"))
    then(ilia).should_see_that(
        SearchResultsMessage(), ReadsExactly("Shop online")
    )
