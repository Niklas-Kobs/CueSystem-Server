<img width="1280" height="640" alt="Git_Repo_Coverart-4" src="https://github.com/user-attachments/assets/2b1c1106-01f4-4597-8e63-5b7ad381c827" />


Welcome to **CueSystem-Server (API)**, a lightweight Flask-based web server and REST API designed to host waiting room displays and manage live queue updates!

This server provides endpoints for displaying current queue statuses, updating patient data, handling popup alerts, and executing remote system triggers.

---

## Key Features

- **Web Display Interface:** Serves the main waiting room web page (`index.html`) via Flask templates.
- **Production Server Ready:** Powered by Waitress WSGI server with multi-threading support for high reliability.
- **REST API Endpoints:** Handles incoming POST requests for live queue updates, popup alerts, system execution commands, and heartbeat checks.
- **JSON State Management:** Leverages `jsonLib` to save, update, and manage persistent queue data (`files/list.json`).
- **Built-in Error Handling & Fallback:** Retries file access on reading errors and displays a fallback error screen if the queue file is missing or unreadable after multiple attempts.

---

## Installation & Setup

### Requirements

Ensure you have Python installed, then install the required dependencies:

```bash
pip install flask waitress
```

*(Note: Make sure your custom `jsonLib` module is placed in the project root directory and the `files/` folder exists.)*

### Running the Server

Start the web server by running:

```bash
python Queue.py
```

The server will launch on port `55000` with 6 threads:
`http://0.0.0.0:55000/`

---

## API Endpoints

- `GET /` — Renders the main web interface (`index.html`).
- `GET /show` — Returns the current queue and popup status as JSON.
- `POST /update` — Receives full queue data updates (up to 5 patient slots + popup state) and updates `list.json`.
- `POST /message` — Directly updates popup notifications (`POP_H`, `POP_T`, `call_6`).
- `POST /execute` — Triggers automated commands (e.g., toggling popup resets).
- `POST /alive` — Simple health-check endpoint returning server availability status.

---

## Feedback & Bug Reporting

Found a bug or running into issues? Please open an issue on GitHub or contact your administrator!
