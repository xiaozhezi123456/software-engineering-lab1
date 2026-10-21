"""简易成绩管理工具的命令行入口。"""

import argparse

from .models import GradeBook, ScoreRecord, Student
from .report import render_ranking
from .storage import load_gradebook, save_gradebook


def build_demo_gradebook() -> GradeBook:
    """构造用于演示的成绩册。"""
    book = GradeBook()
    data = {
        "20240101": ("张三", [("软件工程", 92), ("高等数学", 88)]),
        "20240102": ("李四", [("软件工程", 85), ("高等数学", 79)]),
        "20240103": ("王五", [("软件工程", 76), ("高等数学", 91)]),
    }
    for student_id, (name, scores) in data.items():
        book.add_student(Student(student_id=student_id, name=name))
        for course, score in scores:
            book.add_score(ScoreRecord(student_id=student_id, course=course, score=score))
    return book


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="简易学生成绩管理工具")
    parser.add_argument("--data", metavar="PATH", help="从 JSON 文件读取成绩册")
    parser.add_argument("--save", metavar="PATH", help="把当前成绩册保存为 JSON 文件")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.data:
        book = load_gradebook(args.data)
        print(f"已加载成绩册：{args.data}")
    else:
        book = build_demo_gradebook()
    if args.save:
        save_gradebook(book, args.save)
        print(f"成绩册已保存到：{args.save}")
    print(render_ranking(book))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
