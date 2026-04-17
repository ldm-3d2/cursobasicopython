from __future__ import annotations

from dataclasses import dataclass
from itertools import count

from flask import Flask, abort, redirect, render_template, request, url_for


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False


def create_app() -> Flask:
    app = Flask(__name__)

    tasks: list[Task] = []
    next_id = count(1)

    @app.get("/")
    def index():
        return render_template("index.html", tasks=tasks)

    @app.post("/tasks")
    def add_task():
        title = request.form.get("title", "").strip()
        if title:
            tasks.append(Task(id=next(next_id), title=title))
        return redirect(url_for("index"))

    @app.post("/tasks/<int:task_id>/complete")
    def complete_task(task_id: int):
        task = next((item for item in tasks if item.id == task_id), None)
        if task is None:
            abort(404)
        task.completed = True
        return redirect(url_for("index"))

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
