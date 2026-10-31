# StudySprint

A small flashcard and quiz trainer you run in the terminal. Load a deck of cards
from a JSON file, quiz yourself, and see your score at the end. This is your
squad's starting product for Elite 101 - you'll grow it one ticket at a time.

## Run it

```bash
python main.py
```

## Run the tests

```bash
python -m unittest
```

## How it's laid out

| File | What it does |
|---|---|
| `main.py` | The menu loop you interact with |
| `storage.py` | Loads and saves the JSON data file |
| `features/core.py` | The deck, the quiz loop, and small helpers |
| `features/reports.py` | Summary reports (half-built - finish it via a ticket) |
| `data/studysprint.json` | The card deck and score history |
| `tests/test_core.py` | Example tests to copy from |

## Team

<!-- Add yourself here on your Git lesson: - Your Name (role) -->

- Muhammad --> StudySprint

## Where to start

Pick a ticket from the `tickets/` folder (or the Issues tab once your section
repo exists). Read `CONTRIBUTING.md` for the Definition of Done every pull
request has to meet.
Ticket #1:
What changed: Now, there is a new function called review_missed that checks through a list of True or False booleans that represent the incorrect or correct cards from the latest quiz. It returns all of the cards that were missed. There are 2 tests to make sure that it properly runs in the case that the results are mixed with incorrect and correct, and still runs properly in the case that the results are all correct.

Ticket #2:
What changed: After this ticket, the function category_reports is now fully finished and successfully operates according to its intended function. When it runs, it looks through the entire sample of cards it was referred to when the function was called, and returns a list of all the categories present in the card bank it was given and how many cards are in each category. Unit tests were made and they output OK.
