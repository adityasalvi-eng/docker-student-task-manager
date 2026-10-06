import os
import socket
import sqlite3

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Database file is stored next to app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "tasks.db")


def get_db():
    """Open a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # lets us use column names like row["title"]
    return conn


def init_db():
    """Create the tasks table if it does not exist yet."""
    conn = get_db()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()


@app.route("/")
def index():
    """Homepage: show all tasks."""
    conn = get_db()
    tasks = conn.execute(
        "SELECT id, title, created_at FROM tasks ORDER BY id DESC"
    ).fetchall()
    conn.close()
    # socket.gethostname() returns the container ID when running in Docker
    return render_template("index.html", tasks=tasks, hostname=socket.gethostname())


@app.route("/add", methods=["POST"])
def add_task():
    """Add a new task from the form."""
    title = request.form.get("title", "").strip()
    if title:
        conn = get_db()
        conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        conn.commit()
        conn.close()
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    """Delete a task by its id."""
    conn = get_db()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


# Create the table when the app starts
init_db()

if __name__ == "__main__":
    # host="0.0.0.0" -> accept connections from outside the container
    # port=5000      -> the port Flask listens on
    app.run(host="0.0.0.0", port=5000)
    #this is the main code for the task manager project
    