import win32api as wa
import win32file as wf
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, QCoreApplication


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'password input'
        self.left = 150
        self.top = 150
        self.width = 400
        self.height = 170
        self.part()
        self.show()

    def windowUI(self):
        # window size
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # 'Enter'라는 버튼을 설정
        self.pushButton = QPushButton('Enter', self)
        self.pushButton.move(130, 120)
        self.pushButton.setToolTip('button')

        # label 설정
        self.label = QLabel('비밀번호 입력:', self)
        self.label.move(20, 20)
        self.label.resize(150, 30)

        # 비밀번호 입력창
        self.textedit = QLineEdit(self)
        font = self.textedit.font()
        font.setPointSize(13)
        self.textedit.setFont(font)
        self.textedit.setPlaceholderText("input password")
        self.textedit.setEchoMode(self.textedit.Password)
        self.textedit.resize(300, 30)
        self.textedit.move(20, 50)

        # signal connect라는 함수가 없으면 밑에 @pyqtSlot()이
        # 실행이 안된다.
        self.textedit.returnPressed.connect(self.on_key)
        self.pushButton.clicked.connect(self.on_key)

    @pyqtSlot()
    def on_key(self):
        val = self.textedit.text()
        print(val)
        QCoreApplication.exit()

    # 현재 인식된 드라이브의 목록을 문자열로 반환하는 함수
    def get_drive(self):
        drive = wa.GetLogicalDriveStrings()
        drive = drive.split('\000')[:-1]
        usb_drive = []

        for drv in drive:
            if wf.GetDriveType(drv) == wf.DRIVE_REMOVABLE:
                usb_drive.append(drv)
        return usb_drive

    def usb_check(self):
        buttonReply = QMessageBox.question(self, 'Failed', "please usb connect try again",
                                           QMessageBox.Ok)
        if buttonReply == QMessageBox.Ok:
            sys.exit()

    def part(self):
        if not self.get_drive():
            self.usb_check()
        else:
            self.windowUI()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
