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

def file_upload(NETWORK_PATH,USB_PATH):
    a = glob.glob(USB_PATH+'\\*')
    b = a[:]
    i = 0
    while i < len(a):
        a[i] = a[i].replace(USB_PATH, NETWORK_PATH)
        if a[i] == NETWORK_PATH+'\\System Volume Information':
            del a[i]
            del b[i]
            continue
        i = i + 1
    i = 0
    while i < len(a):
        try:
            shutil.copy(b[i], a[i])
        except:
            shutil.copytree(b[i], a[i])
        finally:
            i = i + 1

USB,USB_COUNT,NETWORK=get_read_drive()
if USB_COUNT == 1:
   file_upload(str(NETWORK),str(USB))
elif USB_COUNT > 1:
    i=0
    while i < USB_COUNT:
        file_upload(str(NETWORK)),USB[i]
        i= i + 1
else:
    print('USB가 없엉')