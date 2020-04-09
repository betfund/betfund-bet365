"""
Betfund Bet365 API Wrapper.



"""
import os
import requests

from typing import Optional
from urllib.parse import urljoin


class Bet365(object):
    """
    Bet365 API Wrapper.

    TODO: Docstring

    """

    def __init__(self):
        self.base_url = "https://bet365-sports-odds.p.rapidapi.com/v1/bet365/"
        self.headers = {
            "x-rapidapi-host": os.getenv("BET365_HOST"),
            "x-rapidapi-key": os.getenv("BET365_KEY"),
        }

    def get(self, url_extras: str, params: dict):
        """"""
        url = urljoin(self.base_url, url_extras)

        response = requests.get(
            url=url, headers=self.headers, params=self._prune(params)
        )

        return response

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

        return self.get(url_extras="prematch", params=querystring)

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
    ):
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
