# WordCloud

## 功能描述

根据输入词条，爬取百度百科，将文本保存至`姓名.txt`文件，图片保存至`姓名.jpg`文件中，根据这两个文件生成词云。  

### 举例

`python3 word.py`

> 请输入要生成词云的词条：姜文  
> Building prefix dict from the default dictionary ...  
> Loading model from cache
> C:\Users\30400\AppData\Local\Temp\jieba.cache  
> Loading model cost 0.981 seconds. 
> Prefix dict has been built succesfully. 

原图：  
![姜文原图](https://raw.githubusercontent.com/RealEasyin/WordCloud/master/%E5%A7%9C%E6%96%87.jpg)
词云图：
![姜文词云图]
()

## 依赖库

词云：wordcloud  
爬虫：bs4、urllib  
中文分词：jieba
