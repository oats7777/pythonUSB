#!/usr/bin/python
#-*-coding:utf-8 -*-
"""

	2013-05-30

	Made by d0ct0ro

	Homepage : blog.d-c.kr

	upload.php에 바이너리로 파일전송

	Filename = post_file.py

"""
import socket,sys,os
#웹서버 주소설정
Ip = "1.229.153.21"
Port = 80
# 소켓객체 생성 AF_INET 는 IPv4 를 사용한다는 뜻이다. 두번째 전달인자는 소켓타입 보통 스트림을 많이사용
Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Socket.connect((Ip,Port))
def  File_Post_Site(Data):
	try :
		Socket.send(Data)
	except :
		print ("에러")
		return
#python을 실행하기전 받은 인자값을 확인 없을시 스크립트 종료
if len(sys.argv) is 1:
	print ("읽을 파일명을 입력해주세용")
	exit(1)
#파일이름이 있을경우 변수에 이름을 담음
Filename = sys.argv[1]
try :
	#바이너리 모드로 파일을 연다
	f = open(Filename,'rb')
	#헤더 Content-Length에 담을 사이즈 구하기
	Filesize = os.path.getsize(Filename)
	#추가 사이즈 구하기
	Size = """-----------------------------7dd5a16200bc
Content-Disposition: form-data; name="file"; filename="%s"
Content-Type: text/plain
-----------------------------7dd5a16200bc--"""% (Filename)
	Filesize = len(Size) + Filesize
	#헤더만들기
	Header = """POST /upload.php HTTP/1.1
Accept: image/gif, image/jpeg, image/pjpeg, image/pjpeg, application/x-shockwave-flash, */*
Referer: http://%s/
Accept-Language: ko
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727)
Content-Type: multipart/form-data; boundary=---------------------------7dd5a16200bc
Accept-Encoding: gzip, deflate
Host: %s
Content-Length: %s
Connection: Keep-Alive
Cache-Control: no-cache
-----------------------------7dd5a16200bc
Content-Disposition: form-data; name="file"; filename="%s"
Content-Type: text/plain
""" % (Ip,Ip,Filesize,Filename)
	#헤더를 만들었으니 헤더를 보냄
	File_Post_Site(Header)
	while True :
		#1024 byte씩 읽고 보냄
		byte = f.read(1024)
		File_Post_Site(byte)
		#끝까지 다읽은경우 맨밑해더를 보낸후 while문을 break
		if byte == '':
			File_Post_Site("\n-----------------------------7dd5a16200bc--\n")
			break
	#파일닫기
	f.close()
#오류 처리
except IOError:
	print ("파일을 열수 없습니다.")