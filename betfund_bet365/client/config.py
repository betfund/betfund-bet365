"""Configuration File for Bet365 Client."""
from enum import Enum


class Bet365SportId(Enum):
    """
    Bet365 API SportId Enumeration.
    """

    SOCCER = 1
    CRICKET = 3
    RUGBY_UNION = 8
    BOXING_UFC = 9
    AMERICAN_FOOTBALL = 12
    TENNIS = 13
    SNOOKER = 14
    DARTS = 15
    BASEBALL = 16
    ICE_HOCKEY = 17
    BASKETBALL = 18
    RUGBY_LEAGUE = 19
    AUSTRALIAN_RULES = 36
    BOWLS = 66
    GAELIC_SPORTS = 75
    HANDBALL = 78
    FUTSAL = 83
    FLOORBALL = 90
    VOLLEYBALL = 91
    TABLE_TENNIS = 92
    BADMINTON = 94
    BEACH_VOLLEYBALL = 95
    SQUASH = 107
    WATER_POLO = 110
    E_SPORTS = 151


RESPONSE_OBJECT_FACTORY = {
    "result": "ResultResponse",
    "inplay_filter": "InPlayFilterResponse",
    "event": "InPlayOddsResponse",
    "prematch": "PreMatchOddsResponse",
    "inplay": "InPlayEventsResponse",
    "upcoming": "UpcomingEventsResponse",
}