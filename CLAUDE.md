# qt-graphkit-app

Standalone host and test bed for the qt-graphkit component (`../qt-graphkit`, editable path
dependency). Plan of record: https://claude.ai/artifact/CgX62Bsf13sPmqfjKStLvo.
Decisions live in `../qt-graphkit/docs/decisions.md`.

## Rules for Claude
1. Component logic belongs in qt-graphkit; this repo holds only app glue (window, menus, console,
   example scripts, packaging).
2. The app picks the Qt binding: PySide6 6.11.3. Import qt_graphkit's Qt module before
   pyqtgraph so every layer uses the same binding; `check_bindings()` runs at startup.
3. `uv run ruff check`, `uv run ruff format --check .` and `uv run pytest` pass before each commit.
4. Commit with a clear message after each working change.
