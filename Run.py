from PyQt5 import QtWidgets
import sys
import os

# Add Code/ to sys.path so all modules (including QRC_FILES) are found
# Skip when frozen (PyInstaller bundle already has Code/ on path)
if not getattr(sys, 'frozen', False):
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Code'))

from SSC import Ui_SSC
import SSC as ssc_module

if __name__ == "__main__":
    # Auto-initialize SQLite DB if not present (first run or frozen EXE)
    from init_sqlite import init_db
    init_db()

    app = QtWidgets.QApplication(sys.argv)
    SSC_window = QtWidgets.QMainWindow()

    # Inject SSC into SSC.py's global namespace so start_action's SSC.hide() works
    ssc_module.SSC = SSC_window

    ui = Ui_SSC()
    ui.setupUi(SSC_window)
    SSC_window.show()
    sys.exit(app.exec_())
