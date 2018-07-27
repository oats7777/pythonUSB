import shutil
import glob
'''
최종수정
2018/07/19

프로그램 설명
USB에 있는 내용을 원하는 폴더로 옳기는 프로그램
'''
a=glob.glob("D:\\*")
b=a[:]
i=0
while i < len(a):
    a[i]=a[i].replace("D:\\","C:\\USBCOPY\\")
    if a[i] == 'C:\\USBCOPY\\System Volume Information':
        del a[i]
        del b[i]
        continue
    i=i+1
print (a)
i=0
while i < len(a):
    try:
        shutil.copy(b[i],a[i])
    except:
        shutil.copytree(b[i],a[i])
    finally:
        i=i+1