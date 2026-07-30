# Task API - Week 2 + 3 Assignment (FlyRank Backend Track)

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
<img width="1893" height="864" alt="image" src="https://github.com/user-attachments/assets/607dbf6c-650b-4c55-b3c0-e9d5dc0135b9" />


# Task API - Week 3 Assignment (BE-02: SQLite Database Integration)

An upgraded, persistent CRUD To-Do List API built using **Python**, **FastAPI**, **SQLModel**, and **SQLite**. 

---

## 📌 Assignment Context & Evolution
This repository contains the evolution of **Assignment 1 (BE-01: In-Memory CRUD API)** into a production-ready database-backed application for **Assignment 2 (BE-02)**:
* **Assignment 1:** Data lived strictly in a temporary memory list and was wiped out on every server restart.
* **Assignment 2 (Current):** Replaced the in-memory array with a lightweight, file-based **SQLite database (`tasks.db`)** managed via **SQLModel**. Data now securely persists across server restarts while keeping the exact same API contract.

---

## 🚀 Features
* **Persistent SQLite Storage:** Tasks are saved to a local `tasks.db` file and survive server reboots.
* **Automatic Schema & Seeding:** Tables are created automatically on startup, and pre-seeded with 3 initial tasks only if the database is empty.
* **Full CRUD Support:** Create (`POST`), Read (`GET`), Update (`PUT`), and Delete (`DELETE`) tasks.
* **Input Validation:** Rejects empty or invalid task titles with proper `400 Bad Request` status codes.
* **Interactive Documentation:** Auto-generated Swagger UI available out-of-the-box.

---

## 📋 Endpoints Table

| Method | Path | Description | Status Codes |
| :--- | :--- | :--- | :--- |
| **GET** | `/` | API Root self-description | `200 OK` |
| **GET** | `/health` | Server health check | `200 OK` |
| **GET** | `/tasks` | List all tasks from SQLite | `200 OK` |
| **GET** | `/tasks/{id}` | Get a single task by ID | `200 OK`, `404 Not Found` |
| **POST** | `/tasks` | Create a new task in database | `201 Created`, `400 Bad Request` |
| **PUT** | `/tasks/{id}` | Update an existing task | `200 OK`, `400 Bad Request`, `404 Not Found` |
| **DELETE** | `/tasks/{id}` | Remove a task from database | `204 No Content`, `404 Not Found` |

---

## 🛠️ How to Install & Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ahmadrayan-create/task-api.git](https://github.com/ahmadrayan-create/task-api.git)
   cd task-api

```

2. **Create and activate a virtual environment:**
```bash
python -m venv venv
# Windows PowerShell:
venv\Scripts\Activate.ps1
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


*(Note: The `tasks.db` file will automatically be created and seeded in your root directory upon startup).*
5. **Open Swagger UI:**
Navigate to `http://localhost:8000/docs` in your browser.

---

## 🧪 Sample Execution (`irm` / PowerShell)

Testing database write and persistence:

```powershell
# Create a new task
$body = @{ title = "Test database write" } | ConvertTo-Json
irm -Uri "http://localhost:8000/tasks" -Method Post -ContentType "application/json" -Body $body

# Output response:
# id title                done
# -- -----                ----
#  4 Test database write False

```

---

## 📸 Swagger UI Verification
<img width="689" height="299" alt="image" src="https://github.com/user-attachments/assets/15804921-5f3b-4c09-935e-b49e6ec02fda" />
<img width="608" height="289" alt="image" src="https://github.com/user-attachments/assets/abb3afd6-b773-4b0d-9ec2-556c888b2dfa" />
<img width="617" height="286" alt="image" src="https://github.com/user-attachments/assets/1fa8677a-1b5e-4d64-bf8d-82cbee03237a" />
<img width="606" height="290" alt="image" src="https://github.com/user-attachments/assets/2392aeb3-5618-4696-93b6-462ba9ce039f" />


