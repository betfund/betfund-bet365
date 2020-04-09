"""
Facade `Response Object` Delegations

Bet365 API Responses contain 2 common components
Bet365Response object is tasked to parse:
    "success": int
    "results": list

Further delegation for facade access to responses are subclassed

`InPlayFilterResponse`
`InPlayOddsResponse`
`PreMatchOddsResponse`
`PreMatchOddsResponse`
`InPlayEventsResponse`
`UpcomingEventsResponse`

The objects are accessible via dot notation or via `.get(..)`
"""

from typing import List, Union


class Bet365Response(dict):
    """Base ResponseObject creator for Bet365 API Response."""

    def __init__(self, data: dict):
        super(Bet365Response, self).__init__(data)

    @property
    def success(self) -> int:
        return self.get("success")

    @property
    def _results(self) -> Union[list, None]:  # This is overloaded hence the `_*`
        return self.get("results")


class Pager(dict):
    """
    Reusable component for dot notation access of `pager` object in API Response.
    (e.g.)
    >>> data = {
    ...     "page": 1,
    ...     "per_page": 50,
    ...     "total": 730
    ... }

    >>> UpcomingEventsResponse(data).pager.page
    >>> 1

    >>> UpcomingEventsResponse(data).pager.per_page
    >>> 50
    """

    def __init__(self, data: dict):
        super(Pager, self).__init__(data)

    @property
    def pager(self) -> dict:
        return self

    @property
    def page(self) -> Union[int, None]:
        pager = self.pager
        return pager.get("page") if pager else None

    @property
    def per_page(self) -> Union[int, None]:
        pager = self.pager
        return pager.get("per_page") if pager else None


class IdNameMeta(dict):
    """
    Reusable component for dot notation for objects with "id" and "name".

    (e.g.)
    >>> data = {
    ...     "league":{
    ...         "id":"10037409",
    ...         "name":"Mexico Liga MX Femenil"
    ...     }
    ... }

    >>> id_name = IdNameMeta(data.get("league"))

    >>> id_name.id
    >>> "10037409"

    """

    def __init__(self, data: dict):
        super(IdNameMeta, self).__init__(data)

    @property
    def id(self) -> str:
        return self.get("id")

    @property
    def name(self) -> str:
        return self.get("name")


class UpcomingEvent(dict):
    """
    Reusable component for dot notation access of `results` from UpcomingEvent Endpoint.

    (e.g.)
    >>> data = {
    ...   "id":"86576599",
    ...   "sport_id":"1",
    ...   "away":{
    ...       "id":"10361085",
    ...       "name":"Chivas Guadalajara Women"
    ...    },
    ...    "ss": None,
    ...    "our_event_id":"2130836",
    ...    "updated_at":"1581990232"
    ... }

    >>> UpcomingEvent(data).id
    >>> "86576599"

    >>> UpcomingEvent(data).away.id
    >>> "10361085"
    """

    def __init__(self, data: dict):
        super(UpcomingEvent, self).__init__(data)

    @property
    def id(self) -> str:
        return self.get("id")

    @property
    def sport_id(self) -> str:
        return self.get("sport_id")

    @property
    def time(self) -> str:
        return self.get("time")

    @property
    def time_status(self) -> str:
        return self.get("time_status")

    @property
    def league(self) -> IdNameMeta:
        return IdNameMeta(self.get("league"))

    @property
    def home(self) -> IdNameMeta:
        return IdNameMeta(self.get("home"))

    @property
    def away(self) -> IdNameMeta:
        return IdNameMeta(self.get("away"))

    @property
    def ss(self) -> str:
        return self.get("ss")

    @property
    def our_event_id(self) -> str:
        return self.get("our_event_id")

    @property
    def updated_at(self) -> str:
        return self.get("updated_at")


class UpcomingEventsResponse(Bet365Response):
    """
    Response Object Facade for UpcomingEvents Endpoint.

    The object wraps the response and exposes dot notation access

    The top level accesses for `upcoming` endpoint are:
        "success": int
        "pager": dict
        "results": list

    The `results` object is parsed into `UpcomingEvent` facades
    Say you have a parsed response from UpcomingEvents Endpoint
    >>> response_object.results
    >>> [
    ...   {
    ...     "id": "12345",
    ...     "our_event_id":"2294461",
    ...     "updated_at": "1586461906"
    ...   },
    ... ]

    >>> response_object.results[0].our_event_id
    >>> "2294461"

    >>> response_object.results[0].updated_at
    >>> "1586461906"
    """

    def __init__(self, data):
        super(UpcomingEventsResponse, self).__init__(data)
        self.pager = Pager(data.get("pager"))

    @property
    def results(self) -> Union[List[UpcomingEvent], None]:
        """

        """
        if not self._results:
            return None

        parsed_results = []
        for record in self._results:
            parsed_results.append(UpcomingEvent(record))

        return parsed_results
