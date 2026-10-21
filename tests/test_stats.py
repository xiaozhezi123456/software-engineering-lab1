"""成绩统计单元测试（Issue #3）。"""

import unittest

from grade_manager.models import GradeBook, ScoreRecord, Student
from grade_manager.stats import average, course_average, pass_rate, ranking


def make_book() -> GradeBook:
    book = GradeBook()
    data = {
        "20240101": ("张三", [("软件工程", 90), ("高等数学", 80)]),
        "20240102": ("李四", [("软件工程", 70), ("高等数学", 60)]),
        "20240103": ("王五", [("软件工程", 50), ("高等数学", 100)]),
    }
    for student_id, (name, scores) in data.items():
        book.add_student(Student(student_id, name))
        for course, score in scores:
            book.add_score(ScoreRecord(student_id, course, score))
    return book


class StatsTest(unittest.TestCase):
    def test_average(self):
        self.assertAlmostEqual(average([90.0, 80.0, 70.0]), 80.0)

    def test_pass_rate(self):
        self.assertAlmostEqual(pass_rate([90.0, 50.0, 60.0]), 2 / 3)

    def test_course_average(self):
        book = make_book()
        self.assertAlmostEqual(course_average(book, "软件工程"), 70.0)

    def test_ranking(self):
        book = make_book()
        rows = ranking(book)
        self.assertEqual([row["student_id"] for row in rows], ["20240101", "20240103", "20240102"])
        self.assertEqual([row["rank"] for row in rows], [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
