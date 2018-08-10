import win32api as wa
import win32file as wf
import sys
from PyQt5.QtWidgets import *


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.get_drive()
        self.show()

    # 현재 인식된 드라이브의 목록을 문자열로 반환하는 함수
    def get_drive(self):
        drive = wa.GetLogicalDriveStrings()
        drive = drive.split('\000')[:-1]
        usb_drive = []

        for drv in drive:
            if wf.GetDriveType(drv) == wf.DRIVE_REMOVABLE:
                usb_drive.append(drv)
        if not usb_drive:
            self.usb_check()
        else:
            print('usb 인식 성공')
            self.openFileNamesDialog()

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)

    def usb_check(self):
        buttonReply = QMessageBox.question(self, 'connect check fail', "usb connected again??",
                                           QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)
        if buttonReply == QMessageBox.Ok:
            print('OK clicked.')
            self.get_drive()
        else:
            print('Cancel clicked.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
