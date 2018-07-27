while True:
    PATH = input("경로를 입력해주세용")
    try:
        f = open(PATH, 'r')
        data=f.read()
        f.close()
        data=data.replace(";",";\n");
        f = open(PATH,'w');
        f.write(data)
        f.close()
        break
    except:
        print ("지정되지 않은 경로입니다")
        print ("다시 입력해 주세요")
        continue
