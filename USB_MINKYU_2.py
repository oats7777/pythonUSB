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
    i = 0
    while i < len(NETWORK_PATH):
        try:
            shutil.copy(USB_PATH[i], NETWORK_PATH[i])
        except:
            shutil.copytree(USB_PATH[i], NETWORK_PATH[i])
        finally:
            i = i + 1

def GetFileEditTime(USB):
    FileTimeList=[]
    for U in USB:
        FileTimeList.append(os.path.getmtime(U))
    return FileTimeList
while True:
    USB, USB_COUNT, NETWORK = get_read_drive()
    NETWORK_PATH=[]
    USB_PATH=[]
    if USB_COUNT == 1:
        NETWORK_PATH, USB_PATH = DrivePATH(NETWORK[0]+"home\\", USB[0])
        file_upload(NETWORK_PATH,USB_PATH)
        Time=GetFileEditTime(USB_PATH)
        i=0
        while True:
            if i is len(Time):
                i=0
            ResetTime=GetFileEditTime(USB_PATH)
            if Time[i] < ResetTime[i]:
                # 이젠 파일업로드가 문제다,,,,
                os.remove(NETWORK_PATH[i])
                try:
                    shutil.copy(USB_PATH[i], NETWORK_PATH[i])
                    Time[i]=ResetTime[i]
                except:
                    shutil.copytree(USB_PATH[i], NETWORK_PATH[i])
                    Time[i] = ResetTime[i]
            i = i + 1