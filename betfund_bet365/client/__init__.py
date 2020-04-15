"""
Betfund Bet365 API Wrapper.

Bet365 Serves as a Client to make requests to Bet365 API
see for documentation: (https://1394697259.gitbook.io/bet365-api/)

Bet365 Exposes 6 Endpoints:
    Result ["GET"]
    InPlay Filter ["GET"]
    InPlay Odds ["GET"]
    PreMatch odds ["GET"]
    InPlay Events ["GET"]
    Upcoming Events ["GET"]

Responses are parsed into Facade Access objects (Base Bet365Response)
"""


__title__ = "betfund-bet365"
__version__ = "0.0.4"
__author__ = "Leon Kozlowski"
__license__ = "MIT"

from .client import Bet365  # noqa: F401
from .config import Bet365SportId  # noqa: F401
