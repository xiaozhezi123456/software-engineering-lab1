"""JSON 持久化单元测试（Issue #1）。"""

import tempfile
import unittest
from pathlib import Path

from grade_manager.models import GradeBook, ScoreRecord, Student
from grade_manager.storage import load_gradebook, save_gradebook


class StorageTest(unittest.TestCase):
    def test_save_and_load_roundtrip(self):
        book = GradeBook()
        book.add_student(Student("20240101", "张三"))
        book.add_score(ScoreRecord("20240101", "软件工程", 92.5))
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "gradebook.json"
            save_gradebook(book, path)
            loaded = load_gradebook(path)
        self.assertEqual(len(loaded.students), 1)
        self.assertEqual(loaded.students[0].name, "张三")
        self.assertEqual(loaded.records[0].score, 92.5)


if __name__ == "__main__":
    unittest.main()
