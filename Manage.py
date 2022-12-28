import os
import shutil
import time
from blackspider import choose_true,true,false,warn,choose_

# 受保护文件会存放在protected_file
protected_file = {
    "main.py",
    "blackspider.py",
    "Manage.py",
    "LICENSE",
    ".git",
    "__pycache__",
    "readme.md",
    ".Manage.ini"
}
ls = []

#创建文件夹
def create_file(file,data):
    if file in ls:
        choose = input(choose_+"存在重复文件名重复,需要覆盖吗?(Y/n):")
        if choose in choose_true:
            remove_file(file)
            time.sleep(1)
        else:
            exit()
    os.mkdir(file)
    print(true+"{}文件夹创建成功".format(file))
    try:
        give_data = open("{file}/{file}.html".format(file=file),"w")
        give_data.write(data)
        print(true+"data数据写入成功")
    except:
        print(warn+"data数据写入失败")

# 删除文件夹
def remove_file(file):
    if file in protected_file:
        choose = input(choose_+"删除文件属于受保护文件,要删除吗?(Y/n:)")
        if choose not in choose_true:
            exit()
    shutil.rmtree(file)
    print(true+"{}删除成功".format(file_name))

# 更新文件信息


# 默认打开文件保护机制
def init():
    global ls
    ls_bool:bool = True
    ls = os.listdir()
    for name in protected_file:
        if name in ls:
            print(true+"扫描到{}文件".format(name))
        else:
            ls_bool = False
            print(false+"检查到{}文件丢失".format(name))
    if ls_bool:
        print(true+"扫描未丢失受保护文件")
    else:
        choose = input(choose_+"是否要找回?(Y/n):")
        if choose in choose_true:
            print("恢复方法被微软吞了")
        # 异步,再说,垃圾微软
    return ls
