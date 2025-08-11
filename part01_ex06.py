import sys
import threading
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel("버튼을 눌러서 작업 시작", self)
        self.btn = QPushButton('작업 시작', self)
        self.btn.clicked.connect(self.start_task)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn)
        self.setLayout(layout)

        self.setWindowTitle('스레드로 UI 멈춤 방지')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def start_task(self):
        self.long_task()
       
    # def start_task(self):
    #     # UI 멈춤 방지를 위해 스레드에서 작업 실행
    #     t = threading.Thread(target=self.long_task)
    #     t.start()

    def long_task(self):
        for i in range(5):
            time.sleep(1)  # 오래 걸리는 작업 시뮬레이션
            self.label.setText(f"작업 진행중... {i+1}/5")
        self.label.setText("작업 완료!")
 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())