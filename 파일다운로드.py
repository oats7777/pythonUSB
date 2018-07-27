from urllib.request import urlopen

BUFSIZE=1024*256

fileurl='https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe'
filename=fileurl.split('/')[-1]
try:
    with urlopen(fileurl) as f:
        with open(filename,'wb') as h:
            buf=f.read(BUFSIZE)
            while buf:
                h.write(buf)
                buf=f.read(BUFSIZE)
except Exception as e:
    print (e)