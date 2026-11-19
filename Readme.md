# Notes CRUD API

A RESTful Notes Management API built using **Python, FastAPI, PostgreSQL, and SQLAlchemy**. This project provides CRUD operations to create, retrieve, update, and delete notes, with request validation and automated API testing.

## Features

- Create new notes with title, context, and category.
- Retrieve all notes.
- Retrieve an individual note using its ID.
- Update existing notes.
- Delete notes.
- Validate incoming requests using Pydantic.
- Handle missing records using HTTP exceptions.
- Store data in PostgreSQL.
- Use SQLAlchemy ORM for database operations.
- Automated API testing using Pytest and FastAPI TestClient.
- Separate test database for automated tests.
- Logging for important API operations.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API development |
| PostgreSQL | Relational database |
| SQLAlchemy | ORM and database operations |
| Pydantic | Request and response validation |
| Pytest | Automated testing |
| HTTPX | API testing support |
| Uvicorn | ASGI server |

## Project Structure

```text
notes-crud-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── model.py
│   └── schemas.py
│
├── tests/
│   ├── __init__.py
│   └── test_notes.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd notes-crud-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/notes_db
```

Replace `YOUR_PASSWORD` with your PostgreSQL password.

Do not commit your `.env` file to GitHub.

### 5. Create the database

Create a PostgreSQL database named:

```sql
CREATE DATABASE notes_db;
```

Create the database tables using your project setup.

### 6. Start the application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| POST | `/insert-data` | Create a new note |
| GET | `/notes` | Retrieve all notes |
| GET | `/notes/{note_id}` | Retrieve a note by ID |
| PUT | `/update-data/{note_id}` | Update an existing note |
| DELETE | `/delete-note/{note_id}` | Delete a note |

## API Usage Examples

### 1. Create a Note

**POST** `/insert-data`

Request body:

```json
{
    "title": "Learn FastAPI",
    "context": "Understand REST API development",
    "category": "Learning"
}
```

### 2. Retrieve All Notes

**GET** `/notes`

Returns all stored notes, ordered by descending ID.

### 3. Retrieve a Note by ID

**GET** `/notes/1`

Returns the note associated with the specified ID.

### 4. Update a Note

**PUT** `/update-data/1`

Request body:

```json
{
    "title": "Learn Advanced FastAPI"
}
```

Only the supplied fields are updated.

### 5. Delete a Note

**DELETE** `/delete-note/1`

Deletes the note associated with the specified ID.

## API Documentation

FastAPI automatically generates interactive API documentation.

After starting the application, visit:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

You can use Swagger UI to execute and test API endpoints directly from your browser.

## Automated Testing

This project uses Pytest and FastAPI TestClient to verify API functionality.

A separate PostgreSQL test database is used to avoid modifying development data.

Run the tests:

```bash
pytest -v
```

### Test Cases

| Test | Description |
|---|---|
| `test_create_note` | Verifies note creation |
| `test_get_all_notes` | Verifies retrieval of all notes |
| `test_update_note` | Verifies note updates |
| `test_delete_note` | Verifies note deletion |
| `test_note_not_found` | Checks handling of missing notes |
| `test_invalid_note` | Checks request validation |

**Test result:** 6 tests passed.

## Key Learnings

Through this project, I gained practical experience with:

- Building REST APIs using FastAPI.
- Connecting PostgreSQL with Python applications.
- Working with SQLAlchemy ORM models.
- Separating database models from Pydantic schemas.
- Implementing CRUD operations.
- Managing database sessions through dependency injection.
- Handling HTTP errors and validation failures.
- Writing automated API tests using Pytest.
- Debugging integration issues between application layers.

## Future Improvements

- Add pagination and filtering.
- Implement user authentication and authorization.
- Add Docker support.
- Deploy the application to a cloud platform.
- Introduce database migrations using Alembic.

## Author

**Charan Teja**

GitHub: https://github.com/cherry-achyuth