# Task API - Week 2 Assignment (FlyRank Backend Track)

A lightweight, in-memory CRUD To-Do List API built using **Python**, **FastAPI**, and **Pydantic**.

---

## Features
- **In-Memory Storage**: Fast execution with zero database setup required.
- **Full CRUD Support**: Create, Read, Update, and Delete tasks.
- **Input Validation**: Rejects empty or invalid task titles with proper error codes.
- **Interactive Documentation**: Auto-generated Swagger UI.

---

## Endpoints Table

| Method | Path | Description | Status Codes |
| :--- | :--- | :--- | :--- |
| **GET** | `/` | API Root self-description | `200 OK` |
| **GET** | `/health` | Server health check | `200 OK` |
| **GET** | `/tasks` | List all tasks | `200 OK` |
| **GET** | `/tasks/{id}` | Get a single task by ID | `200 OK`, `404 Not Found` |
| **POST** | `/tasks` | Create a new task | `201 Created`, `400 Bad Request` |
| **PUT** | `/tasks/{id}` | Update an existing task | `200 OK`, `400 Bad Request`, `404 Not Found` |
| **DELETE** | `/tasks/{id}` | Remove a task | `204 No Content`, `404 Not Found` |

---

## How to Install & Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ahmadrayan-create/task-api.git](https://github.com/ahmadrayan-create/task-api.git)
   cd task-api

```

2. **Create and activate a virtual environment:**
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```


4. **Start the server:**
```bash
uvicorn main:app --reload --port 8000

```


5. **Open Swagger UI:**
Navigate to `http://localhost:8000/docs` in your browser.

---

## Sample curl Output

```powershell
PS C:\Users\iamom> irm -Method POST -Uri "http://localhost:8000/tasks" -ContentType "application/json" -Body '{"title":"Test task"}'

id title      done
-- -----      ----
 4 Test task False

```

---

## Swagger UI Verification

```
<img width="1893" height="864" alt="image" src="https://github.com/user-attachments/assets/6737d423-a821-4f02-8bb3-07de5349406d" />

```
