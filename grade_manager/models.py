"""成绩管理的数据模型。"""

from dataclasses import dataclass


@dataclass
class Student:
    """学生基本信息。"""

    student_id: str
    name: str


@dataclass
class ScoreRecord:
    """一条课程成绩记录。"""

    student_id: str
    course: str
    score: float

    def __post_init__(self) -> None:
        if not 0 <= self.score <= 100:
            raise ValueError(f"成绩必须在 0~100 之间：{self.score}")


class GradeBook:
    """成绩册：维护学生与其课程成绩。"""

    def __init__(self) -> None:
        self._students: dict[str, Student] = {}
        self._records: list[ScoreRecord] = []

    def add_student(self, student: Student) -> None:
        if student.student_id in self._students:
            raise ValueError(f"学号重复：{student.student_id}")
        self._students[student.student_id] = student

    def add_score(self, record: ScoreRecord) -> None:
        if record.student_id not in self._students:
            raise ValueError(f"学生不存在：{record.student_id}")
        self._records.append(record)

    @property
    def students(self) -> list[Student]:
        return list(self._students.values())

    @property
    def records(self) -> list[ScoreRecord]:
        return list(self._records)

    def records_of(self, student_id: str) -> list[ScoreRecord]:
        """返回指定学生的全部成绩记录。"""
        return [r for r in self._records if r.student_id == student_id]
