# blacksprider
针对网页关键词查询的简单爬虫，仅供用于学习交流
```bash
=========================================================================
'||'''|,'||`            '||     .|'''|.            ..     ||`            
 ||   || ||              ||     ||                 ''     ||             
 ||;;;;  ||  '''|. .|'', || //` `|'''|,'||''|,'||''|| .|''|| .|''|,'||''|
 ||   || || .|''|| ||    ||\{   ..   || ||  || ||  || ||  || ||..|| ||
.||...|'.||.`|..||.`|..'.|| \\. '|...|' ||..|'.||..||.`|..||.`|... .||.
                                        ||
                                       .||
地  址：https://github.com/CryingN/blackspider
版本号：0.3.1
邮  箱：CryingNights7v@gmail.com
=========================================================================
```
![blackspider.png](blackspider.png)
### 环境
* python 推荐使用3.9.9版本
* argparse，urllib，bs4库
### 环境布置方式
下载[python](https://www.python.org/downloads/),在cmd或者powershell使用pip命令布置第三方库,推荐使用国内镜像源进行下载，这里使用中科大源：
```bash
pip install -i https://pypi.mirrors.ustc.edu.cn/simple/ urllib3==1.26.12
pip install -i https://pypi.mirrors.ustc.edu.cn/simple/ bs4==0.0.1
```
## 0.3.1 BUG修复
因理解偏差，经检验0.3以前无法直接在终端中使用多关键词查询，现已修复bug；
同时源代码中不再支持tuple格式进行多关键词查询，多关键词查询可在str格式中用","进行分割，如下例子：
```python
keyword:str = 'Auto,SQL,tool'
```
## 0.3版本使用说明书
### 使用示例
$\color{#FF0000}使用须知：为维护网络环境，切勿对同一网站进行多次访问。$
```bash
usage: blackspider.py [-h] [--url URL] [--file FILE] [--file_name FILE_NAME] [--tag TAG]
                      [--attrname ATTRNAME] [--keyword KEYWORD]
optional arguments:
  -h, --help            show this help message and exit
  --url URL             网站ip地址，例如：--url 'http://www.baidu.com'
  --file FILE           文件位置,当不存在文件时会搜索网站地址并生成对应文件，例如：--file '百度'
  --file_name FILE_NAME
                        用于定义网站地址生成的文件名称，例如：--file_name '百度'
  --tag TAG             html文件中的tag节点,默认为<body>，可通过元素审查搜索对应节点，例如：--tag 'div'
  --attrname ATTRNAME   查询tag节点元素，默认None查询全部，'text'为查询文本，下载图片为：--tag 'img' --attrname
                        'src'
  --keyword KEYWORD     索引关键词,若默认为None则全部查询，例如：--keyword 'Auto','SQL','tool'
```
### 更新内容
* 添加了虽然没什么用但是可以看起来很酷炫的logo；
* 重构了储存方式，网站将以文件夹形式储存；
* 增加了图片爬取功能，可通过``` --tag 'img' --attrname 'src'```对网页图片进行爬取；
* ```--file [文件名] --file_name [文件名]```中的`[文件名]`变更为文件夹名，不再需要输入文件后缀名；
* 增加了选择功能，可通过(Y,y,yes)三种方式进行操作。
### 使用示例
#### 对网站爬取
```bash
py blackspider.py --url 'http://www.baidu.com' --file_name '百度' --tag 'a' --attrname 'text' --keyword '百度' 
```
返还值：
```bash
=========================================================================
 '||'''|,'||`            '||     .|'''|.            ..     ||`
  ||   || ||              ||     ||                 ''     ||
  ||;;;;  ||  '''|. .|'', || //` `|'''|,'||''|,'||''|| .|''|| .|''|,'||''|
  ||   || || .|''|| ||    ||\{   ..   || ||  || ||  || ||  || ||..|| ||
 .||...|'.||.`|..||.`|..'.|| \\. '|...|' ||..|'.||..||.`|..||.`|... .||.
                                         ||
                                        .||
 地  址：https://github.com/CryingN/blackspider
 版本号：0.3                                                                               
 邮  箱：CryingNights7v@gmail.com                                                          
 =========================================================================                                                                                                           [True] 获取源代码成功                                                                     [Ture] 已创建文件夹: 百度                                                                 [True] 已创建百度文档                                                                     [True] 已打印至demo.html文档                                                              [True] 已从原文档中获取                                                                   [True] 查询到以下tag文本：
 百度首页
 查看全部百度产品 >
 关于百度
使用百度前必读 
```
#### 对文件爬取
```bash
py blackspider.py --file '百度' --tag 'img' --attrname 'src'
```
返还值：
```bash
=========================================================================
'||'''|,'||`            '||     .|'''|.            ..     ||`
 ||   || ||              ||     ||                 ''     ||
 ||;;;;  ||  '''|. .|'', || //` `|'''|,'||''|,'||''|| .|''|| .|''|,'||''|
 ||   || || .|''|| ||    ||\{   ..   || ||  || ||  || ||  || ||..|| ||
.||...|'.||.`|..||.`|..'.|| \\. '|...|' ||..|'.||..||.`|..||.`|... .||.
                                        ||
                                       .||
地  址：https://github.com/CryingN/blackspider
版本号：0.3
邮  箱：CryingNights7v@gmail.com
=========================================================================
[True] 已找到源网站地址
[True] 文件打开成功
[True] 已从原文档中获取
[True] 查询到以下tag图片所在网址：
https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/topnav/newfanyi-da0cea8f7e.png
https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/topnav/newxueshuicon-a5314d5c83.png
https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/topnav/newwenku-d8c9b7b0fb.png
https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/topnav/newbaike-889054f349.png
https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/topnav/newzhidao-da1cf444b0.png
https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/topnav/newjiankang-f03b804b4b.png
https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/topnav/yingxiaoicon-612169cc36.png
https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/topnav/newzhibo-a6a0831ecd.png
https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/topnav/newyinyue-03ecd1e9b9.png
//www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png
//www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png
//www.baidu.com/img/PCfb_5bf082d29588c07f842ccde3f97243ea.png
//www.baidu.com/img/flexible/logo/pc/result.png
//www.baidu.com/img/flexible/logo/pc/result@2.png
//www.baidu.com/img/flexible/logo/pc/peak-result.png
http://ss.bdimg.com/static/superman/img/footer/aria-3006e33cce.png
http://ss.bdimg.com/static/superman/img/qrcode/qrcode@2x-daf987ad02.png
http://ss.bdimg.com/static/superman/img/qrcode/qrcode-hover@2x-f9b106a848.png
[Choose] 统计图片总共有：18份，要下载吗？(Y/n):y
[True] 获取图片(1/18)
[True] 获取图片(2/18)
[True] 获取图片(3/18)
[True] 获取图片(4/18)
[True] 获取图片(5/18)
[True] 获取图片(6/18)
[True] 获取图片(7/18)
[True] 获取图片(8/18)
[True] 获取图片(9/18)
[False] PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png下载失败
[Analyse] 图片地址：http://www.baidu.com//www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png
[False] PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png下载失败
[Analyse] 图片地址：http://www.baidu.com//www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png
[False] PCfb_5bf082d29588c07f842ccde3f97243ea.png下载失败
[Analyse] 图片地址：http://www.baidu.com//www.baidu.com/img/PCfb_5bf082d29588c07f842ccde3f97243ea.png
[False] result.png下载失败
[Analyse] 图片地址：http://www.baidu.com//www.baidu.com/img/flexible/logo/pc/result.png
[False] result@2.png下载失败
[Analyse] 图片地址：http://www.baidu.com//www.baidu.com/img/flexible/logo/pc/result@2.png
[False] peak-result.png下载失败
[Analyse] 图片地址：http://www.baidu.com//www.baidu.com/img/flexible/logo/pc/peak-result.png
[True] 获取图片(16/18)
[True] 获取图片(17/18)
[True] 获取图片(18/18)
[True] 已完成图片保存
```
## 0.2版本使用说明书
### 使用示例
$\color{#FF0000}使用须知：为维护网络环境，切勿对同一网站进行多次访问。$
```bash
usage: blackspider.py [-h] [--url URL] [--file FILE] [--file_name FILE_NAME] [--tag TAG]
                      [--attrname ATTRNAME] [--keyword KEYWORD]
optional arguments:
  -h, --help            show this help message and exit
  --url URL             网站ip地址
  --file FILE           文档位置,不存在文件时搜索网站ip地址并生成html格式网页文件
  --file_name FILE_NAME
                        不存在文件时用于定义ip地址生成HTML文件的名称，默认None生成demo.html文件
  --tag TAG             所寻找HTML文件中的tag节点,默认为div，可在网页元素审查中搜索
  --attrname ATTRNAME   查询tag节点元素，默认None查询全部，可选择查询：class或text
  --keyword KEYWORD     索引关键词,若默认为None则全部查询
```
#### 查询网页并生成文件
```bash
# 查询百度并生成“百度.html”文件
py blackspider.py --url 'http://www.baidu.com' --file_name '百度.html' --tag 'a' --attrname 'text' --keyword '百度'
```
返还值：
```bash
[True] 获取源代码成功
[True] 已创建百度.html文档
[True] 已打印至demo.html文档
[True] 已从原文档中获取
[True] 查询到以下tag文本：
百度首页
查看全部百度产品 >
关于百度
使用百度前必读
```
#### 查询文件
```bash
# 从上面网页生成的文件进行查询
py blackspider.py --file '百度.html' --tag 'a' --attrname 'text' --keyword '百度'
```
返还值：
```bash
[True] 文件打开成功
[True] 已从原文档中获取
[True] 查询到以下tag文本：
百度首页
查看全部百度产品 >
关于百度
使用百度前必读
```
