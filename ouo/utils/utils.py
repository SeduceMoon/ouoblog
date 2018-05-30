import os


# 获取某目录文件数量
def fileNum(path):
    fileNum=0
    for lists in os.listdir(path):
        sub_path = os.path.join(path, lists)
        print(sub_path)
        if os.path.isfile(sub_path):
            fileNum = fileNum+1
    return str(fileNum)
#文章过滤器
def wzInfal(data):
    #过滤操作
    return data