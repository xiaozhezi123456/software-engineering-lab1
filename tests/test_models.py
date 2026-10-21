"""数据模型单元测试（Issue #1）。"""

import unittest

from grade_manager.models import GradeBook, ScoreRecord, Student


class StudentTest(unittest.TestCase):
    def test_create_student(self):
        student = Student(student_id="20240101", name="张三")
        self.assertEqual(student.student_id, "20240101")
        self.assertEqual(student.name, "张三")


class ScoreRecordTest(unittest.TestCase):
    def test_score_in_range(self):
        self.assertEqual(ScoreRecord("20240101", "软件工程", 100).score, 100)

    def test_score_out_of_range(self):
        with self.assertRaises(ValueError):
            ScoreRecord("20240101", "软件工程", 101)
        with self.assertRaises(ValueError):
            ScoreRecord("20240101", "软件工程", -1)


class GradeBookTest(unittest.TestCase):
    def setUp(self):
        self.book = GradeBook()
        self.book.add_student(Student("20240101", "张三"))

    def test_add_and_query_score(self):
        self.book.add_score(ScoreRecord("20240101", "软件工程", 92))
        records = self.book.records_of("20240101")
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].course, "软件工程")

    def test_duplicate_student(self):
        with self.assertRaises(ValueError):
            self.book.add_student(Student("20240101", "张三"))

    def test_score_of_unknown_student(self):
        with self.assertRaises(ValueError):
            self.book.add_score(ScoreRecord("20249999", "软件工程", 80))


if __name__ == "__main__":
    unittest.main()
