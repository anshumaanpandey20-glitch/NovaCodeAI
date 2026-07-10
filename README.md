# NovaCode AI Code Generator

A Flask web app scaffold for an AI code generator. It includes pages for home,
login, registration, dashboard, generator, history, and profile.

## Current Project Status

The app is mostly a Flask UI scaffold. Authentication registration writes to a
MySQL database. The generator, dashboard, history, profile, services, and helper
files are present as placeholders for future work.

## Requirements

- Python 3.10 or newer
- MySQL Server running locally or on a reachable host
- A MySQL user that can create databases and tables

Python packages are listed in `requirements.txt`.

## Setup

1. Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\activate
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:

```env
SECRET_KEY=ChangeThisToAnyRandomString123

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=root
DB_NAME=novacode_ai

GEMINI_API_KEY=
```

4. Start MySQL.

5. Run the Flask app:

```powershell
python app.py
```

6. Open the app:

```text
http://127.0.0.1:5000
```

## Database

The database schema lives in `database/schema.sql`.

When the app starts or first opens a database connection, it runs
`initialize_database()` from `database/connection.py`. That function:

- creates the configured database if it does not exist
- runs every statement in `database/schema.sql`
- uses `CREATE TABLE IF NOT EXISTS` so it is safe to run again

The current tables are:

- `users`: stores registered users
- `generations`: stores future generated-code history

If you see an error like this:

```text
pymysql.err.ProgrammingError: (1146, "Table '...users' doesn't exist")
```

check that:

- MySQL is running
- `.env` has the correct `DB_HOST`, `DB_USER`, `DB_PASSWORD`, and `DB_NAME`
- the MySQL user has permission to create databases and tables
- `database/schema.sql` contains the `users` table

## Project Structure

```text
app.py                  Main Flask app and page routes
config.py               Loads environment variables from .env
database/connection.py  MySQL connection and schema initialization
database/schema.sql     Database tables
routes/                 Future Flask blueprint route files
services/               Future business logic and API integrations
templates/              Jinja HTML templates
static/css/             Stylesheets
static/js/              Browser JavaScript
utils/                  Future helper functions
test_db.py              Quick database connection test
```

## Changing The Database Later

For a new table, add a `CREATE TABLE IF NOT EXISTS ...;` statement to
`database/schema.sql`.

For a new column on an existing table, use an `ALTER TABLE` migration carefully.
Do not add destructive SQL such as `DROP TABLE` unless you have backed up your
data.

Recommended future improvement: create a `migrations/` folder and track schema
changes as numbered migration files once the app grows.

## Adding Future Features

- Add user-facing routes in `app.py` or convert the files in `routes/` into
  registered Flask blueprints.
- Put API/database business logic in `services/`.
- Put validation helpers in `utils/validators.py`.
- Put security helpers in `utils/security.py`.
- Keep secrets in `.env`; never hard-code API keys or database passwords.

## Useful Commands

Test the database connection:

```powershell
python test_db.py
```

Run the app in debug mode:

```powershell
python app.py
```

Install a new dependency and update `requirements.txt`:

```powershell
pip install package-name
pip freeze > requirements.txt
```

## Notes

- `app.py` currently owns the active routes.
- `routes/auth.py` is not registered in `app.py` yet, so changes there will not
  affect the running `/register` page until blueprints are wired in.
- The app uses bcrypt for password hashing in the active registration route.
