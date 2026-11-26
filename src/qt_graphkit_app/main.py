"""Main window skeleton: graph area (placeholder until Phase 1b) and a Python console dock."""

# ruff: noqa: I001  (qt_graphkit._qt must load before pyqtgraph so both pick PySide6)
from __future__ import annotations

import sys

import qt_graphkit
from qt_graphkit import _qt
from qt_graphkit._qt import Qt, QtWidgets

from pyqtgraph.console import ConsoleWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(f"qt-graphkit app {qt_graphkit.__version__}")
        self.resize(1200, 800)

        placeholder = QtWidgets.QLabel("Graph view goes here (Phase 1b).")
        placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(placeholder)

        self.console = ConsoleWidget(
            namespace={"app_window": self, "qt_graphkit": qt_graphkit},
            text="qt-graphkit console. Names: app_window, qt_graphkit.",
        )
        dock = QtWidgets.QDockWidget("Console", self)
        dock.setObjectName("console-dock")
        dock.setWidget(self.console)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, dock)

        self.bindings = _qt.check_bindings()
        self.statusBar().showMessage(
            "Qt bindings: " + ", ".join(f"{k}={v}" for k, v in self.bindings.items())
        )


def main() -> int:
    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
