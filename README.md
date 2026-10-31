# UoP Meeting Booking

A web application for scheduling meetings between professors and students at the University of the Peloponnese, based on the time slots that professors publish.

## Status

Version 0.1.0: first working prototype. The web page, the API and the database work end to end, but the project is still at an early stage.

## Features

- Publish a time slot for an existing professor, with validation (the end must be after the start, and the location is required).
- List all published slots, including the professor's name.

## Tech stack

- Python 3.12, FastAPI
- SQLAlchemy (ORM) over SQLite
- pytest and ruff
- Plain HTML and JavaScript for the web page

## Requirements

- Python 3.12 or later
- Git

## Installation

```bash
git clone https://github.com/bocoseduardo-dot/uop-meeting-booking
cd uop-meeting-booking
python3.12 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Configuration

| Variable       | Purpose                                    | Default                          |
| -------------- | ------------------------------------------ | -------------------------------- |
| `DATABASE_URL` | Database connection URL used by SQLAlchemy | `sqlite:///./meeting_booking.db` |

If `DATABASE_URL` is not set, a local SQLite file is created in the repository root. To use a different database, set the variable before starting the server:

```bash
export DATABASE_URL="sqlite:///./other.db"
python3 -m uvicorn app.main:app --reload
```

Never write a URL containing credentials in the code or commit it to the repository. Use an environment variable or a `.env` file, which is ignored by Git.

The automated tests use their own in-memory database, so they are not affected by `DATABASE_URL` and never modify your data.

## Running

Run all commands from the repository root, with the virtual environment activated.

1. Create the test data (a fictional professor):

   ```bash
   python3 -m app.seed
   ```

2. Start the server:

   ```bash
   python3 -m uvicorn app.main:app --reload
   ```

3. Open:
   - Web page: <http://127.0.0.1:8000/>
   - API documentation: <http://127.0.0.1:8000/docs>

## Tests

```bash
python3 -m pytest -v
ruff check app/ tests/
```

## Project structure

```
app/       Backend: API, models, schemas, database configuration and seed script
static/    Web page (HTML and JavaScript)
tests/     Automated tests (pytest)
docs/      Project deliverables
```

## Known limitations

- Times are stored without a time zone and interpreted as local time in Greece.
- There is no authentication yet.
- Meetings are not implemented yet; only slots can be published and listed.
- Overlapping slots for the same professor are not detected.
- The web page is minimal, and API error messages are shown in raw form.
- Only the main cases are covered by automated tests.

## Documentation

Project deliverables (D1, D2,D3) are in `docs/`.

