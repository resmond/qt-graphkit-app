from qt_graphkit_app.main import MainWindow


def test_window_builds_with_one_binding(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    assert window.bindings == {"qtpy": "PySide6", "pyqtgraph": "PySide6"}
    assert window.console is not None
