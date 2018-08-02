from win32api import *
from win32file import *
import os
import subprocess

"""Drive Types
    0 Unknown               //win32file.DRIVE_UNKNOWN
    1 No_Root_Directory     //win32file.DRIVE_NO_ROOT_DIR
    2 Removable_Disk        //win32file.DRIVE_REMOVABLE
    3 Local_Disk            //win32file.DRIVE_FIXED
    4 Network_Disk          //win32file.DRIVE_REMOTE
    5 Compact_Disk          //win32file.DRIVE_CDROM
    6 Ram_Disk              //win32file.DRIVE_RAMDISK
"""

# 그냥 재미삼아서 class로 해놨음 이러는게 캡슐화?도 되고
# 뭔가 좋다고 생각해서..
# 그리고 전에 코드 분석해봤다고 가정하고 주석 안달아놓음
# 전에 복붙했던 코드 보면서 하면 되니까


class USB:
    def __init__(self):
        self._drives = (drive for drive in GetLogicalDriveStrings().split("\000") if drive)
        self._drive_list = []
        self._rdrive = []

    def _get_drive(self):
        for drive in self._drives:
            if GetDriveType(drive) == DRIVE_REMOVABLE:
                self._drive_list.append(drive)

        for drv in self._drive_list:
            try:
                if os.path.getsize(drv) >= 0:
                    self._rdrive.append(drv)
            except OSError:
                pass

        if not self._rdrive:
            return True
        else:
            return False

    def connect_usb(self):
        dirpath = self._rdrive
        if self._get_drive() is True:
            print('usb 인식 실패!! usb를 다시 꽂아주세요')
        else:
            print('usb 인식 성공!!')
            # subprocess.call(['robocopy', dirpath, 'C:\\USBCOPY\\', '/MIR', '/LOG:C:\\log1.txt'])

            # 이거 왜 주석 처리 했냐면 Window 깔려 있는 드라이브가 C인지 D인지 모르니까 이렇게
            # 일단 해놨음. 저기 C되있는 부분만 바꿔주면 됨 다른건 딱히 안건드려도 돼
            # 아 코드 설명하자면, robocopy는 윈도우즈 내장된 시스템 불러오는거고, dirpath는
            # 이동식 드라이브 경로(복사할 내용), C:\\USBCOPY\\는 복사될 경로, /MIR은 인터넷에 치면
            # 나보다 더 설명잘 한거 있음, 그리고 뒤에 /LOG:샬랴샬라는 거기에 log파일 생성하는거임


usb = USB()
usb.connect_usb()
