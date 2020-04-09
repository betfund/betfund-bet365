"""Default runner for `betfund_bet365` wrapper."""
from betfund_bet365 import Bet365


def main(sport_id: str):  # pragma: no cover
    client = Bet365()

    upcoming_events = client.upcoming_events(sport_id=sport_id)

    return upcoming_events


if __name__ == '__main__':  # pragma: no cover
    main(sport_id="151")
