import argparse
import urllib.request as ur
from bs4 import BeautifulSoup as bs

url:str = None#'www.baidu.com'
file:str = None#'D:/work/file/demo.html'     #'../test.html'
file_name:str = None                    #'test.html'
tag:str =  'div'#'tr'                       #不能为空
attrname:str = None#'text'                   #'type','text'
keyword = None#'crack','password','胖次'     #关键词

# 获取源代码
def get_html(the_url):
    try:
        html = ur.urlopen(the_url)
        html = html.read()
        filename = html.decode()
        print("[True] 获取源代码成功")
        return filename
    except:
        print('[False] 网站打开失败')
        return None
# 打印至demo.md文档
def print_demo(file,file_name):
    if file_name == None:
        create_file = open("demo.html","w",encoding="utf-8")
        print("[True] 已创建demo.html文档")
    else:
        create_file = open(file_name,"w",encoding="utf-8")
        print("[True] 已创建{name}文档".format(name = file_name))
    create_file.write(file)
    print("[True] 已打印至demo.html文档")
    return create_file
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
    if type(the_keyword) == tuple:
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
def select_tags(tags,attrname,the_keyword):
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

def main(args):
    if args.file != None:
        try:
            file = open(args.file,"r",encoding="utf-8")
            file = file.read()
            print('[True] 文件打开成功')
        except:
            print('[False] 文件打开失败')
            return
        tags = get_tag(file,args.tag)
        select_tags(tags,args.attrname,args.keyword)
    else:
        filename = get_html(args.url)
        if filename == None:
            return
        else:
            print_demo(filename,args.file_name)
            tags = get_tag(filename,args.tag)
            select_tags(tags,args.attrname,args.keyword)
    pass



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, default=url, help="网站ip地址")
    parser.add_argument("--file", type=str, default=file, help="文档位置,不存在文件时搜索网站ip地址并生成html格式网页文件")
    parser.add_argument("--file_name", type=str, default=file_name, help="不存在文件时用于定义ip地址生成HTML文件的名称，默认None生成demo.html文件")
    parser.add_argument("--tag", type=str, default=tag, help="所寻找HTML文件中的tag节点,默认为div，可在网页元素审查中搜索")
    parser.add_argument("--attrname", type=str, default=attrname, help="查询tag节点元素，默认None查询全部，可选择查询：class或text")
    parser.add_argument("--keyword", type=str, default=keyword, help="索引关键词,若默认为None则全部查询")
    args = parser.parse_args()
    main(args)
