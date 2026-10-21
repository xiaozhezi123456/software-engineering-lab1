"""成绩单文本报表。"""

from .models import GradeBook
from .stats import ranking


def render_ranking(book: GradeBook) -> str:
    """把学生排名渲染为等宽文本报表。"""
    header = f"{'排名':<4}{'学号':<10}{'姓名':<6}{'平均分':>8}{'科目数':>6}"
    lines = [header, "-" * 36]
    for row in ranking(book):
        lines.append(
            f"{row['rank']:<4}{row['student_id']:<10}{row['name']:<6}"
            f"{row['average']:>8.2f}{row['count']:>6}"
        )
    return "\n".join(lines)
