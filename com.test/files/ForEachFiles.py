import os,sys


#创建文件
def mkdirs():
    dir="C:\\Users\\Administrator\\Desktop\\1111\\"
    # os.mknod(dir+"test.txt")  Windows上的Python不支持mknod函数
    # files.write("hello world")
    # files.fl
    fp = open(dir+"file_name.txt",'w')  #直接打开一个文件，如果文件不存在则创建文件
    fp.close()
    # with open(dir+"file_name.txt", a +) as fp

def readmkdirs():
    dir="C:\\Users\\Administrator\\Desktop\\11111111.txt"
    with open(dir) as file_obj:
        content = file_obj.read()
        print('content:',content)
    # 解释：在上面的程序中，因为Python在读取文件之后将其存入对象file_obj
    # 中，我们通过对该对象进行循环来遍历文件中的每一行，但是却发现，多了空白行，因为在这个文件中，有看不见的换行符，且print语句语句也会加上一个换行符，因此每行的末尾会有两个换行符。要消除多于的空白行可在print语句中调用rstrip()
    # 方法，
    # file_obj  每行存在一个对象内
    with open(dir) as file_obj:
        for content in file_obj:
            print(content)
    with open(dir) as file_obj:
        for content in file_obj:
            print(content.rstrip())
    # fp.close()

def readLines():
    dir = "C:\\Users\\Administrator\\Desktop\\11111111.txt"
    fo = open(dir)
    for line in fo.readlines():  # 依次读取每行
        line = line.strip()  # 去掉每行头尾空白
        print("读取的数据为: %s" % (line))
    fo.close()

def readLine():
    dir = "C:\\Users\\Administrator\\Desktop\\11111111.txt"
    fo = open(dir)
    print('fo.readline(1):',len(fo.readline()))
    print('fo.readline(2):',len(fo.readline()))
    print('fo.readline(3):',len(fo.readline()))
    print('fo.readline(4):',len(fo.readline()))
    print('fo.readline(5):',len(fo.readline())==0)
    fo.close()

def writersFile():
    dir = "C:\\Users\\Administrator\\Desktop\\11111111.txt"
    # fo = open(dir,'w+r')  a 追加模式   writer直接覆盖了
    # 写入模式
    # with open(dir, 'w') as wf:
    #附加模式
    with open(dir, 'a') as wf:
        wf.write('today is a nice day\n')
        wf.write('do you want to take a trip.')
    # str = 'I LOVE CHINE'
    # fo.write(str)
    # fo.close()

def writersFiles():
    dir = "C:\\Users\\Administrator\\Desktop\\11111111.txt"
    # fo = open(dir,'w+r')  a 追加模式   writer直接覆盖了
    #读写模式
    with open(dir,'a+') as rwf:
        rwf.write('This is myfile.\n')
        rwf.write("The end.")
        content=rwf.read()
        print('content1111:',content)
    return content
    # fo.write(str)
    # fo.close()

def writersFilesss():
    dir = "C:\\Users\\Administrator\\Desktop\\11111111.txt"

    # f = open(dir, 'a+')
    # # os.linesep代表当前操作系统上的换行符
    # f.write('我爱Python' + os.linesep)
    fd = open(dir, 'a+')
    # 写入字符串
    fd.write('123')
    # ret = fd.write("This is runoob.com site")
    # 输入返回值
    print("写入的位数为: ")
    # print(ret)

def mainTest():
    dirRead = "C:\\Users\\Administrator\\Desktop\\11111111.txt"
    dirWriter = "C:\\Users\\Administrator\\Desktop\\222.txt"
    writer = open(dirWriter,'w',encoding='utf-8')  #a 追加模式   writer直接覆盖了
    #读写模式
    with open(dirRead,encoding='utf-8') as rwf:
        for line in rwf.readlines():  # 依次读取每行
            line = line.strip()  # 去掉每行头尾空白
            print("读取的数据为: %s" % (line))
            writer.write(line)
            writer.write('\r')
            # writer.write('\r\n')
            # writer.write(os.linesep)
    writer.close()
    rwf.close()
    # fo.write(str)
    # fo.close()

print('hello')
# mkdirs()
# readmkdirs()
# readLine()
# writersFile()
# writersFiles()
mainTest()

# 自动遍历
def forEachFiles():
    dir="C:\\Users\\Administrator\\Desktop\\新建文件夹"
    files=os.walk(dir)
    for parent, dirnames, filenames in files:
        print('parent:',parent)
        print('dirnames:',dirnames)
        print('filenames:',filenames)
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            extensions = os.path.splitext(file_path)[1]
            print(file_path)
            print(extensions)

# os.walk 自动遍历
# os.listdir 递归遍历
def show_files(path, all_files):
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    # 准备循环判断每个元素是否是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            show_files(cur_path, all_files)
        else:
            all_files.append(file)
    return all_files