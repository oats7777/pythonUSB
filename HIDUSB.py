# -*- coding: utf-8 -*-

from pywinusb import hid
import time

#usb Vendor ID
vendor_num = 0x2045
#usb Product ID
product_num = 0x0805

'''
hid 데이터 읽는 함수
'''
def read_handler(data):
    print("Raw data: {0}".format(data))


def main():

  # hid 디바이스 필터 생성
  # Vendor와 product를 입력한다.
  filter = hid.HidDeviceFilter(vendor_id = vendor_num, product_id = product_num)

  # usb 확인
  devices = filter.get_devices()

  #usb가 잇다면
  if devices:
    device = devices[0]

    # usb 열기
    device.open()

    #읽기 핸들러 연결
    device.set_raw_data_handler(read_handler)

    #쓰기 포트 찾기
    out_report = device.find_output_reports()

    # 배열 선언 9바이트
    buffer = [0x0]*9  # raw data(8bytes) + report ID(1byte)

    buffer[0]=0x00 # report ID

    buffer[1]=0x00 # raw data 1
    buffer[2]=0x00 # raw data 2
    buffer[3]=0x00 # raw data 3
    buffer[4]=0x00 # raw data 4
    buffer[5]=0x00 # raw data 5
    buffer[6]=0x00 # raw data 6
    buffer[7]=0x00 # raw data 7

    #데이터 전송 설정
    out_report[0].set_raw_data(buffer)
    # 전송!
    out_report[0].send()

    #잠깐 대기(1초)
    time.sleep(1)

    #usb 닫기
    device.close()

#시작
main()