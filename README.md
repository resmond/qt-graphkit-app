# qt-graphkit-app

Standalone app that hosts and tests [qt-graphkit](https://github.com/resmond/qt-graphkit). It expects `qt-graphkit` checked
out next to it (`../qt-graphkit`, an editable uv path dependency).

```
uv sync
uv run qt-graphkit-app      # main window: graph area + Python console
uv run pytest
```

Status: skeleton. The graph view arrives with qt-graphkit Phase 1b; the app's own work is Phase 1c.

License: LGPL-2.1-or-later. See [LICENSE](LICENSE).
