.PHONY: black
black:
	black betfund_bet365

.PHONY: tests
tests:
	pytest -vv --cov=betfund_bet365 --cov-report term-missing

.PHONY: lint
lint:
	pylint betfund_bet365/

.PHONY: flake
flake:
	flake8 betfund_bet365