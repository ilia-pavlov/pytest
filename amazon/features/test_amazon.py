from typing import Generator

import pytest
from screenpy import Actor, AnActor, given, then, when
from screenpy.abilities import BrowseTheWeb
from screenpy.actions import Open
from screenpy.pacing import act, scene
from selenium.webdriver import Chrome

from ..tasks.search_amazon import SearchAmazon
from ..user_interface.amazon_home_page import URL


@pytest.fixture(scope="function", name="ilia")
def fixture_actor() -> Generator:
    the_actor = Actor.named("ilia").who_can(BrowseTheWeb.using(Chrome()))
    yield the_actor
    the_actor.exit_stage_left()


@act("Search")
@scene("Search for lightsaber in Amazon")
def test_search_for_light_saber(ilia: AnActor) -> None:
    given(ilia).was_able_to(Open.their_browser_on(URL))
    when(ilia).attempts_to(SearchAmazon.for_text('"lightsaber"'))
    then(ilia).should_see_that(
        # questions!
    )
