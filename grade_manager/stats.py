"""成绩统计、课程平均分与学生排名。"""

from .models import GradeBook


def average(scores: list[float]) -> float:
    """计算平均分；当成绩列表为空时返回 0.0（Issue #4 修复）。"""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def pass_rate(scores: list[float], pass_line: float = 60.0) -> float:
    """计算及格率；当成绩列表为空时返回 0.0（Issue #4 修复）。"""
    if not scores:
        return 0.0
    return sum(1 for score in scores if score >= pass_line) / len(scores)


def course_average(book: GradeBook, course: str) -> float:
    """计算某门课程的平均分。"""
    scores = [record.score for record in book.records if record.course == course]
    return average(scores)


def student_averages(book: GradeBook) -> list[dict]:
    """按学生汇总平均分与科目数。"""
    rows = []
    for student in book.students:
        scores = [record.score for record in book.records_of(student.student_id)]
        rows.append(
            {
                "student_id": student.student_id,
                "name": student.name,
                "average": round(average(scores), 2),
                "count": len(scores),
            }
        )
    return rows


def ranking(book: GradeBook) -> list[dict]:
    """按平均分从高到低排名。"""
    rows = student_averages(book)
    rows.sort(key=lambda row: row["average"], reverse=True)
    for index, row in enumerate(rows, start=1):
        row["rank"] = index
    return rows
