import argparse
import urllib.request as ur
from bs4 import BeautifulSoup as bs
import os
import shutil
import time

url:str = None              #'http://www.baidu.com'
file:str = None             #'百度'
file_name:str = None        #'百度'
tag:str = 'body'             #'tr'
attrname:str = None         #'type','text','src'
keyword = None              #'Auto,SQL,tool'                 #关键词
picture_dic = []

number = "0.3.1"
choose_true = ('yes','y','Y')
# logo
logo = """
=========================================================================
'||'''|,'||`            '||     .|'''|.            ..     ||`            
 ||   || ||              ||     ||                 ''     ||             
 ||;;;;  ||  '''|. .|'', || //` `|'''|,'||''|,'||''|| .|''|| .|''|,'||''|
 ||   || || .|''|| ||    ||\{{   ..   || ||  || ||  || ||  || ||..|| ||
.||...|'.||.`|..||.`|..'.|| \\\\. '|...|' ||..|'.||..||.`|..||.`|... .||.
                                        ||
                                       .||
地  址：https://github.com/CryingN/blackspider
版本号：{numbers}
邮  箱：CryingNights7v@gmail.com
=========================================================================
""".format(numbers = number)

# 默认file名字
def get_urlname(url,file_name):
    if file_name == None:
        try:
            file_name = url.split('.')
            file_name = file_name[1][8:16:]
        except:
            file_name = args.url[:8:]
    return file_name
    
# 获取源代码
def get_html(the_url,filename):
    try:
        html = ur.urlopen(the_url)
        html = html.read()
        file = html.decode()
        print("[True] 获取源代码成功")
    except:
        print('[False] 网站打开失败')
        return
    get_file(filename)
    create_url = open("{name}/url.txt".format(name = filename),"w",encoding="utf-8")
    create_file = open("{name}/{name}.html".format(name = filename),"w",encoding="utf-8")
    print("[True] 已创建{name}文档".format(name = filename))
    create_file.write(file)
    create_url.write(the_url)
    print("[True] 已打印至demo.html文档")
    return file

# 获取对应tag节点所需物品
def get_tag(file,tag):
    try:
        soup = bs(file,features="html.parser")
    except:
        print("[False] 解析文档失败，无法解析为html文件")
        return
    tags = soup.find_all(tag)
    print("[True] 已从原文档中获取")
    return tags

# keyword多查询与单查询函数
def bool_keyword(the_keyword,text):
    the_keyword = the_keyword.split(",")
    if len(the_keyword) != 1:
        bool_key = True
        for i in the_keyword:
            if i not in text:
                bool_key = False
        return bool_key
    elif the_keyword in text:
        return True
    else:
        return False

# 查询方法
def select_tags(tags,attrname,the_keyword,tag,name,the_url):
    if attrname == None:
        print('[True] 查询到以下tag：')
        for one_tag in tags:
            if the_keyword == None:
                print(one_tag)
            elif bool_keyword(the_keyword,one_tag.text):
                print(one_tag)
    elif attrname == 'text':
        print('[True] 查询到以下tag文本：')
        for one_tag in tags:
            if the_keyword == None:
                print(one_tag.text)
            elif bool_keyword(the_keyword,one_tag.text):
                print(one_tag.text)
    elif tag == 'img' and attrname == 'src':
        print('[True] 查询到以下tag图片所在网址：')
        for one_tag in tags:
            if the_keyword == None:
                picture_dic_src(one_tag,attrname)
            elif bool_keyword(the_keyword,one_tag.text):
                picture_dic_src(one_tag,attrname)
        choose = input('[Choose] 统计图片总共有：{number}份，要下载吗？(Y/n):'.format(number = len(picture_dic)))
        if choose in choose_true:
            picture_num = 0
            all_num = len(picture_dic)
            for pic in picture_dic:
                picture_num += 1               
                get = get_picture(name,pic,the_url)
                if get == True:
                    print("[True] 获取图片({num}/{all_num})".format(num = picture_num,all_num = all_num))
                time.sleep(0.5)
            print('[True] 已完成图片保存')
        else:
            print('[False] 结束操作')
            pass
    else:
        try:
            print('[True] 查询到以下tag元素：')
            for one_tag in tags:
                if the_keyword == None:
                    print(one_tag[attrname])
                elif bool_keyword(the_keyword,one_tag.text):
                    print(one_tag[attrname])
        except:
            print('[False] 无法查询attrname，请检查是否存在对应元素')

# 创建文件夹
def get_file(file_name):
    try:
        os.mkdir(file_name)
        print('[Ture] 已创建文件夹:',file_name)
    except:
        choose = input('[Choose] 已创建过{name}文件夹，要覆盖吗？(Y/n):'.format(name = file_name))
        if choose in choose_true:
            shutil.rmtree(file_name)
            time.sleep(0.5)
            os.mkdir(file_name)
            print('[Ture] 已创建文件夹:',file_name)
        else:
            print('[False] 继续编辑原文件夹')
            return

# 保存图片:picture_dic_src将图片链接导入字典，get_picture导入图片
def picture_dic_src(one_tag,attrname):
    scr = one_tag[attrname]
    print(scr)
    picture_dic.append(scr)
    
def get_picture(file_name,picture,url):
    try:
        name = picture.split('/')
        if name[0] != 'https:' and name[0] != 'http:' :
            picture = url + picture
        name = name[len(name)-1]
        data = ur.urlopen(picture,timeout = 10)
        text = file_name+'/'+name
        picture_data = open(text,'wb')
        picture_data.write(data.read())
        get = True
    except:
        print('[False] {name}下载失败\n[Analyse] 图片地址：{error}'.format(name = name,error = picture))
        get = False
    return get

def main(args):
    if args.file != None:
        try:
            url = open("{file}/url.txt".format(file = args.file),"r")
            url = url.read()
            print('[True] 已找到源网站地址')        
        except:
            print('[False] 找不到源网站')
        try:
            file = open("{file}/{file}.html".format(file = args.file),"r",encoding="utf-8")
            file = file.read()
            print('[True] 文件打开成功')
        except:
            print('[False] 文件打开失败')
            return
        tags = get_tag(file,args.tag)
        select_tags(tags,args.attrname,args.keyword,args.tag,args.file,url)
    elif args.url == None:
        print('[False] 请输入ip地址或文件位置')
        return
    else:
        name = get_urlname(args.url,args.file_name)
        file = get_html(args.url,name)
        tags = get_tag(file,args.tag)
        select_tags(tags,args.attrname,args.keyword,args.tag,name,args.url)
    pass



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, default=url, help="网站ip地址，例如：--url 'http://www.baidu.com'")
    parser.add_argument("--file", type=str, default=file, help="文件位置,当不存在文件时会搜索网站地址并生成对应文件，例如：--file '百度'")
    parser.add_argument("--file_name", type=str, default=file_name, help="用于定义网站地址生成的文件名称，例如：--file_name '百度'")
    parser.add_argument("--tag", type=str, default=tag, help="html文件中的tag节点,默认为<body>，可通过元素审查搜索对应节点，例如：--tag 'div'")
    parser.add_argument("--attrname", type=str, default=attrname, help="查询tag节点元素，默认None查询全部，'text'为查询文本，下载图片为：--tag 'img' --attrname 'src'")
    parser.add_argument("--keyword", type=str, default=keyword, help="索引关键词,若默认为None则全部查询，例如：--keyword 'Auto','SQL','tool'")
    args = parser.parse_args()
    print(logo)
    main(args)
