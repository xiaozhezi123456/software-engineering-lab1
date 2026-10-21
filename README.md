# grade-manager（学生成绩管理系统）

[![CI](https://github.com/xiaozhezi123456/software-engineering-lab1/actions/workflows/ci.yml/badge.svg)](https://github.com/xiaozhezi123456/software-engineering-lab1/actions/workflows/ci.yml)

软件工程实验一示例项目：以“学生成绩管理系统”为载体，实践 Git 版本控制与基于
Issue / Pull Request 的协作开发流程。

- 远程仓库：https://github.com/xiaozhezi123456/software-engineering-lab1
- Issues：https://github.com/xiaozhezi123456/software-engineering-lab1/issues
- Pull Requests：https://github.com/xiaozhezi123456/software-engineering-lab1/pulls
- Actions：https://github.com/xiaozhezi123456/software-engineering-lab1/actions
- Releases：https://github.com/xiaozhezi123456/software-engineering-lab1/releases

## 目录结构

- `grade_manager/`：项目源码
- `tests/`：单元测试
- `docs/`：Issue 清单、Sprint 计划、PR 记录
- `.github/`：CI 工作流、Issue 与 PR 模板

## 协作规范

- 分支策略：`main` 只由经过评审的发布 PR 合入；`develop` 集成日常开发；功能分支
  命名为 `feature/issue-<编号>-<简述>`，缺陷修复为 `fix/issue-<编号>-<简述>`，
  文档改动为 `docs/issue-<编号>-<简述>`。
- 提交规范：`<类型>: <简述> (refs #编号)`，类型包括 `feat`、`fix`、`docs`、
  `test`、`chore`、`revert`。
- 合并策略：功能分支通过 Pull Request 合并到 `develop`，使用 `--merge` 方式
  在 GitHub 上保留合并提交；发布时由 `develop` 向 `main` 提交发布 PR。
- 评审要求：PR 必须有关联 Issue、变更说明与自检清单，评审者至少给出结论性评论。
- 版本与发布：使用附注标签 `vX.Y.Z` 与 GitHub Release 记录版本。

## 快速开始

```bash
git clone https://github.com/xiaozhezi123456/software-engineering-lab1.git
cd software-engineering-lab1
python -m unittest discover -s tests -v
```
