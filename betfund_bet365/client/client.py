"""
Betfund Bet365 API Wrapper.

Bet365 Serves as a Client to make requests to Bet365 API

Bet365 Exposes 6 Endpoints:
    Bet365 Result ["GET"]
    Bet365 InPlay Filter ["GET"]
    Bet365 InPlay Odds ["GET"]
    Bet365 PreMatch odds ["GET"]
    Bet365 InPlay Events ["GET"]
    Bet365 Upcoming Events ["GET"]

Responses are parsed into Facade Access objects


"""
import os
import requests

from typing import Optional
from urllib.parse import urljoin

import betfund_bet365.response.facades as facades

from betfund_bet365.response.facades import Bet365Response
from betfund_bet365.client.config import RESPONSE_OBJECT_FACTORY


class Bet365(object):
    """
    Bet365 API Wrapper.

    TODO: Docstring

    """

    def __init__(self):
        self.base_url = "https://bet365-sports-odds.p.rapidapi.com/{}/bet365/"
        self.headers = {
            "x-rapidapi-host": os.getenv("BET365_HOST"),
            "x-rapidapi-key": os.getenv("BET365_KEY"),
        }

    def get(self, url_extras: str, params: dict, version: str = "v1") -> Bet365Response:
        """
        TODO docstring

        """
        url = urljoin(self.base_url.format(version), url_extras)

        response = requests.get(
            url=url, headers=self.headers, params=self._prune(params)
        )

        response.raise_for_status()

        delegation = getattr(facades, RESPONSE_OBJECT_FACTORY.get(url_extras))
        delegate_object = delegation(response.json())

        return delegate_object

    def result(self, event_id: str):
        """TODO DOCSTRING"""
        querystring = {
            "event_id": event_id
        }

        return self.get(url_extras="result", params=querystring)

    def in_play_filter(
        self,
        sport_id: Optional[str] = None,
        league_id: Optional[str] = None
    ):
        """
        tODO: Docstring
        """
        querystring = {
            "sport_id": sport_id,
            "league_id": league_id
        }

        return self.get(url_extras="inplay_filter", params=querystring)

    def in_play_odds(
        self,
        fi: str,
        raw: Optional[str] = None,
        lineup: Optional[str] = None,
        stats: Optional[str] = None,
    ):
        """
        TODO: Docstring
        """
        querystring = {
            "FI": fi,
            "raw": raw,
            "lineup": lineup,
            "stats": stats
        }

        return self.get(url_extras="event", params=querystring)

    def pre_match_odds(self, fi: str, raw: Optional[str] = None):
        """
        TODO: Docstring
        """
        querystring = {
            "FI": fi,
            "raw": raw
        }

        return self.get(url_extras="prematch", params=querystring, version="v2")

    def in_play_events(self, raw: Optional[str] = None):
        """
        TODO: Docstring
        """
        querystring = {
            "raw": raw
        }

        return self.get(url_extras="inplay", params=querystring)

    def upcoming_events(
        self,
        sport_id: str,
        page: Optional[str] = None,
        lng_id: Optional[str] = None,
        day: Optional[str] = None,
        league_id: Optional[str] = None,
    ) -> Bet365Response:
        """
        TODO: Docstring.

        Args:
            sport_id (str): Identifier for sport type
            page (Optional[str]):
            lng_id (Optional[str]):
            day (Optional[str]):
            league_id (Optional[str]):

        Returns:

        """
        querystring = {
            "sport_id": sport_id,
            "page": page,
            "LNG_ID": lng_id,
            "day": day,
            "league_id": league_id,
        }

        return self.get(url_extras="upcoming", params=querystring)

    @staticmethod
    def _prune(params: dict):
        """
        Cleaner of `params` dictionary for API Request

        If `value` for `key` is `NoneType` this key will be removed

        Args:
            params (dict): `params` dictionary for API request
            (e.g.)
                { "sport_id": "19", "lng_id": None }

        Returns:
            pruned_params (dict): `params` dict without `None` values or keys
            (e.g.)
                { "sport_id": "19" }
        """
        pruned_params = dict((k, v) for k, v in params.items() if v)

        return pruned_params


if __name__ == '__main__':
    client = Bet365()
    resp = client.upcoming_events(sport_id="92")

    import pdb; pdb.set_trace()