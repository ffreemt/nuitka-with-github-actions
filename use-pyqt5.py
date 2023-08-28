import sys

# from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QGridLayout, QWidget, QApplication


class MainUi(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        self.start()

    def start(self):
        pass


if __name__ == '__main__':
    """
    Main run
    """

    app = QApplication(sys.argv)

    ui = MainUi()
    ui.show()

    sys.exit(app.exec_())


"""

nuitka --mingw64 --standalone --enable-plugin=pyqt5 use_pyqt5.py

"""