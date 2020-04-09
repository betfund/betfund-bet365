"""Response namespace."""

from .base import (
    Bet365Response,
    MetaBase,
    PagerBase
)

from .in_play_events import (
    InPlayEventsResponse,
    InPlayResult
)

from .result import (
    Result,
    ResultEvent,
    ResultResponse
)

from .upcoming_events import (
    UpcomingEvent,
    UpcomingEventsResponse
)

__all__ = [
    "Bet365Response",
    "InPlayEventsResponse",
    "InPlayResult",
    "MetaBase",
    "PagerBase",
    "Result",
    "ResultEvent",
    "ResultResponse",
    "UpcomingEvent",
    "UpcomingEventsResponse"
]
