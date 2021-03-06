import win32api as wa
import win32file as wf
import os
import glob
import shutil


def get_read_drive():
    # 현재 인식된 드라이브의 목록을 문자열로 반환하는 메소드
    drive = wa.GetLogicalDriveStrings()
    drive = drive.split('\000')[:-1]
    usb_drive_list = []
    network_drive_list = []
    rdrive = []
    r_count = 0

    # 이동식 드라이브를 확인하는 반복문
    for drv in drive:
        if wf.GetDriveType(drv) == wf.DRIVE_REMOVABLE:
            usb_drive_list.append(drv)
            # 이동식 드라이브를 찾으면 +1 을 해준다.
            r_count += 1
        elif wf.GetDriveType(drv) == wf.DRIVE_REMOTE:
            network_drive_list.append(drv)
    for drv in range(r_count):
        if os.path.getsize(usb_drive_list[drv]) >= 0:
            rdrive.append(usb_drive_list[drv])
    return rdrive, r_count, network_drive_list

def DrivePATH(NETWORK_PATH,USB_PATH):
    network = glob.glob(USB_PATH+'*')
    usb = network[:]
    i = 0
    while i < len(network):
        network[i] = network[i].replace(USB_PATH, NETWORK_PATH)
        if network[i] == NETWORK_PATH+'System Volume Information':
            del network[i]
            del usb[i]
            continue
        i = i + 1
    return network,usb

def file_upload(NETWORK_PATH,USB_PATH):
    network,usb=DrivePATH(NETWORK_PATH,USB_PATH)
    i = 0
    while i < len(network):
        try:
            shutil.copy(usb[i], network[i])
        except:
            shutil.copytree(usb[i], network[i])
        finally:
            i = i + 1
def GetTime(NETWORK,USB):
    network,usb=DrivePATH(NETWORK,USB)
    TimeLIst=[]
    for USB_PATH in usb:
        TimeLIst.append(os.path.getmtime(USB_PATH))
    return TimeLIst
USB, USB_COUNT, NETWORK = get_read_drive()
print(USB)
NETWORK_PATH=[]
USB_PATH=[]
FileTime=[]
if USB_COUNT == 1:
    NETWORK_PATH, USB_PATH = DrivePATH(NETWORK[0]+"한민규\\USBPy\\", USB[0])
    print("복사를 진행합니다")
    FileTime.extend(GetTime(USB[0],NETWORK[0]))
    print(FileTime)
    file_upload(NETWORK[0]+'한민규\\USBCOPy\\',USB[0])
    print("복사가 종료되었습니다")
    i=0
    while True:
        if i == len(FileTime)-1:
            i = 0
        Temp = []
        Temp.extend(GetTime(USB[0], NETWORK[0]))
        if FileTime[i] < Temp[i]:
            # 이젠 파일업로드가 문제다,,,,
            os.remove(NETWORK_PATH[i])
            try:
                shutil.copy(USB_PATH[i], NETWORK_PATH[i])
            except:
                shutil.copytree(USB_PATH[i], NETWORK_PATH[i])
        i = i + 1





elif USB_COUNT > 1:
    i=0
    print("복사를 진행합니다")
    while i < USB_COUNT:
        file_upload(NETWORK[0],USB[i])
        i= i + 1
    print("복사가 종료되었습니다")