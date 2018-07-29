import win32api as wa
import win32file as wf
import os
import sys

# 우리는 이동식 드라이브 USB 만 읽으면 되므로 다른 함수는
# 필요치 않다.

def get_read_drive():
    # 현재 인식된 드라이브의 목록을 문자열로 반환하는 메소드
    drive = wa.GetLogicalDriveStrings()
    # 드라이브의 목록을 '\000'으로 나눠서 'list'로 변환한다.
    drive = drive.split('\000')[:-1]
    drive_list = []
    # USB의 경로를 담아서 반환할 변수
    rdrive = []
    r_count = 0

    # 이동식 드라이브를 확인하는 반복문
    for drv in drive:
        # 만약 drive list 에서 이동식 드라이브가 있다면
        # drive_list 에다 추가한다.
        # 그럼 이동식 드라이브의 경로가 drive_list 에 추가되겠지?
        if wf.GetDriveType(drv) == wf.DRIVE_REMOVABLE:
            drive_list.append(drv)
            # 이동식 드라이브를 찾으면 +1 을 해준다.
            r_count += 1

    # 이동식 드라이브를 찾았을 때 +해준 r_count 를 이용해서
    # 찾은 이동식 드라이브의 경로를 rdrive 에 추가한다.
    # 이 부분의 코드가 블로그에 나와있는 예제랑 다르게 작성됨
    for drv in range(r_count):
        if os.path.getsize(drive_list[drv]) >= 0:
            rdrive.append(drive_list[drv])
    return rdrive, r_count


# USB 를 안꽂으면 아무것도 출력이 안된다.
# 여기는 조잡하지만 확인해보려고 만든 조건문
g_rd, r_count = get_read_drive()
if r_count == 0:
    print('꽂혀있는 USB가 없습니다.')
    sys.exit(1)
RMA_count = 'RE_MOVE_ABLE_DRIVE : ' + str(r_count)
print(g_rd)
print(RMA_count)