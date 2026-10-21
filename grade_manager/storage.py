"""成绩册的 JSON 持久化。"""

import json
from pathlib import Path

from .models import GradeBook, ScoreRecord, Student


def save_gradebook(book: GradeBook, path: str | Path) -> None:
    """把成绩册保存为 UTF-8 编码的 JSON 文件。"""
    data = {
        "students": [
            {"student_id": student.student_id, "name": student.name}
            for student in book.students
        ],
        "records": [
            {"student_id": record.student_id, "course": record.course, "score": record.score}
            for record in book.records
        ],
    }
    Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def load_gradebook(path: str | Path) -> GradeBook:
    """从 JSON 文件读取成绩册。"""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    book = GradeBook()
    for item in data.get("students", []):
        book.add_student(Student(**item))
    for item in data.get("records", []):
        book.add_score(ScoreRecord(**item))
    return book
