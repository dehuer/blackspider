# blacksprider 0.2
针对网页关键词查询的简单爬虫，仅供用于学习交流
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