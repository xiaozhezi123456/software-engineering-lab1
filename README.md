# grade-manager（学生成绩管理系统）

软件工程实验一示例项目：以“学生成绩管理系统”为载体，实践 Git 版本控制与基于
Issue / Pull Request 的协作开发流程。

- 远程仓库：https://github.com/xiaozhezi123456/software-engineering-lab1
- 主干分支：`main`（可发布版本）、`develop`（集成开发）
- 持续集成：GitHub Actions（每次 push / PR 自动运行单元测试）

## 目录结构

- `grade_manager/`：项目源码
- `tests/`：单元测试
- `docs/`：Issue 清单、Sprint 计划、PR 记录
- `.github/`：CI 工作流、Issue 与 PR 模板

## 快速开始

```bash
git clone https://github.com/xiaozhezi123456/software-engineering-lab1.git
cd software-engineering-lab1
python -m unittest discover -s tests -v
```
