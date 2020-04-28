# betfund-bet365

## Installation

From source
```bash
$ git clone https://github.com/betfund/betfund-bet365.git
$ cd betfund-lines

$ python3.7 -m venv venv
$ pip install -e .

# For test dependencies
$ pip install -e ".[testing]"
```

## Usage
GET Request to Upcoming Events Endpoint
```python
from betfund_bet365 import Bet365

client = Bet365(api_host="someHost", api_key="someKey")
upcoming_events = client.upcoming_events(sport_id="49")

print(upcoming_events)
```

```bash
{
  "success": 1,
  "pager": {
    "page": 1,
    "per_page": 50,
    "total": 102
  },
  "results": [
    {
      "id": "88107197",
      "sport_id": "92",
      "time": "1586480400",
      "time_status": "0",
      "league": {
        "id": "10036652",
        "name": "Moscow Liga Pro"
      },
      "home": {
        "id": "10423098",
        "name": "Evgenii Kryuchkov"
      },
      "away": {
        "id": "10433218",
        "name": "Aik Lulikyan"
      },
      "ss": null,
      "our_event_id": "2297143",
      "updated_at": "1586478473"
    }
  ]
}
```

Access response objects with dot notation
```python
from betfund_bet365 import Bet365

client = Bet365(api_host="someHost", api_key="someKey")
upcoming_events = client.upcoming_events(sport_id="49")

print(upcoming_events.success)
```

```bash
1
```

Access of array type `results` objects
```python
from betfund_bet365 import Bet365

client = Bet365(api_host="someHost", api_key="someKey")
upcoming_events = client.upcoming_events(sport_id="49")

print(upcoming_events.results[0].id)
```

```bash
"88107197"
```


## Environment Variables

+ BET365_HOST
    + `$ export BET365_HOST=yourHost`


+ BET365_KEY
    + `$ export BET365_KEY=yourSecretKey`


## Testing
```bash
pip install -e ".[testing]"

# Test with pytest
make tests

# Lint with flake8
make flake

# Lint with pylint
make lint
```