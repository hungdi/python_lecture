from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class Ui_MainWindow:
    def setupUi(self):
        self.setWindowTitle("다중상속 UI 예제")
        self.setGeometry(100, 100, 300, 200)

        self.pushButton = QPushButton("클릭하세요", self)
        self.pushButton.setGeometry(100, 80, 100, 30)


class EventHandler:
    def setup_event_handlers(self):
        self.pushButton.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        print("버튼이 클릭되었습니다")


class MainWindow(QMainWindow, Ui_MainWindow, EventHandler):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.setup_event_handlers()
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec_()


