import time
import argparse
import blackspider as bk
import Manage as ma

number = "v1.0.2"
logo = """\033[31m
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
=========================================================================\033[0m
""".format(numbers = number)

# 获取data文件
def get_data(file,url):
    try:
        data = open("{file}/{file}.html".format(file=args.file),"r",encoding="utf-8")
        print(bk.true+"从本地获取源代码")
    except:
        data = bk.get_html(url)
        ma.create_file(file,data)
    return data

def main(args):
    if args.scan == "on":
        ls = ma.init()
    print(logo)
    bk.dictionary.read('.Manage.ini',encoding="utf-8")
    if args.file == None:
        if args.url == None:
            print(bk.false+"请至少输入url或文件名称")
            exit()
        else:
            try:
                args.file = bk.get_file(args.url)
                data = get_data(args.file,args.url)
                bk.dictionary.set("group",args.file,args.url)
                bk.dictionary.set("test",args.file,args.url)
                bk.dictionary.write(open(".Manage.ini",mode="w",encoding="utf-8"))
                print(bk.true+"已更新字典{file}:{url}".format(file=args.file,url=args.url))
            except:
                print(bk.warn+"无法设置字典,请检查url格式")
    else:
        try:
            url_test = bk.dictionary.get("group",args.file)
            choose = input(bk.choose_+"已获取文件对应url:{},是否替换(Y/n):".format(url_test))
            if choose in bk.choose_true:
                args.url = url_test
                data = get_data(args.file,args.url)
            else:
                try:
                    data = get_data(args.file,args.url)
                    bk.dictionary.set("group",args.file,args.url)
                    bk.dictionary.set("test",args.file,args.url)
                    bk.dictionary.write(open(".Manage.ini",mode="w",encoding="utf-8"))
                    print(bk.true+"已更新字典{file}:{url}".format(file=args.file,url=args.url))
                except:
                    print(bk.warn+"无法设置字典,请检查url格式")
        except:
            if args.url == None:
                print(bk.warn+"未找到url")
            else:
                try:
                    data = get_data(args.file,args.url)
                    bk.dictionary.set("group",args.file,args.url)
                    bk.dictionary.set("test",args.file,args.url)
                    bk.dictionary.write(open(".Manage.ini",mode="w",encoding="utf-8"))
                    print(bk.true+"已更新字典{file}:{url}".format(file=args.file,url=args.url))
                except:
                    print(bk.warn+"无法设置字典,请检查url格式")
    tags = bk.get_tag(data,args.tag)
    if args.attrname == None:
        print(bk.true+'查询到以下tag：')
        for one_tag in tags:
            if args.keyword == None:
                print(one_tag)
            elif bk.bool_keyword(args.keyword,one_tag.text):
                print(one_tag)
    elif args.attrname == 'text':
        print(bk.true+'查询到以下tag文本：')
        for one_tag in tags:
            if args.keyword == None:
                print(one_tag.text)
            elif bk.bool_keyword(args.keyword,one_tag.text):
                print(one_tag.text)
    elif args.tag == 'img' and args.attrname == 'src':
        choose = bk.find_picture(tags,args.keyword,args.attrname)
        if choose in bk.choose_true:
            picture_num = 0
            all_num = len(bk.picture_dic)
            for picture in bk.picture_dic:
                picture_num += 1
                bk.get_picture(args.file,picture,args.url)
                time.sleep(0.5)
            print(bk.true+'已完成图片保存')
        else:
            print(bk.false+'结束操作')
    else:
        try:
            print(bk.true+'查询到以下tag元素：')
            for one_tag in tags:
                if the_keyword == None:
                    print(one_tag[args.attrname])
                elif bool_keyword(the_keyword,one_tag.text):
                    print(one_tag[args.attrname])
        except:
            print(bk.false+'无法查询attrname，请检查是否存在对应元素')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u","--url", dest="url", default=None, help="网站ip地址，例如：--url http://www.baidu.com或-u http://www.baidu.com")
    parser.add_argument("-f","--file", dest="file", default=None, help="对爬取网站储存为的文件名，例如：--file baidu或-f baidu")
    parser.add_argument("-t","--tag", dest="tag", default="body", help="html文件中的tag节点,默认为<body>,一般可<F12>元素审查查看节点，例如：--tag div或-t div")
    parser.add_argument("-a","--attrname", dest="attrname", default=None, help="查询tag节点元素，默认None查询全部，--attrname text查询文本，下载图片:-t img -a src")
    parser.add_argument("-k","--keyword", dest="keyword", default=None, help="索引关键词,默认None为全部查询，支持多关键词查询,例如：-k auto,sql或--keyword tool")
    parser.add_argument("-s","--scan", dest="scan",default="on", help="文件安全管理,关闭方法为:-s off或--scan off")
    args = parser.parse_args()
    main(args)
