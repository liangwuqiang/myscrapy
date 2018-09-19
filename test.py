from urllib import request
from bs4 import BeautifulSoup


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

url = 'file:///home/ubuntu/Scrapy/example/test.html'
req = request.Request(url, headers=headers)
res = request.urlopen(req)
html = res.read().decode('utf-8')

if 'blog.jobbole.com' in url:  # 伯乐在线
    title_key = '.entry-header'
    content_key = '.entry'
    print('伯乐在线 http://blog.jobbole.com')
elif 'file:///' in url:  # csdn
#     title_key = '.link_title'
#     content_key = '#article_content'
    title_key = '.title-article'
    content_key = '.htmledit_views'
    print('csdn http://blog.csdn.net')
elif 'www.codingpy.com' in url:  # 编程派网址
    title_key = '.header h1'
    content_key = '.article-content'
    print('编程派网址 http://www.codingpy.com')
elif 'www.cnblogs.com' in url:  # 博客园
    title_key = '.postTitle2'
    content_key = '.blogpost-body'
    print('博客园 https://www.cnblogs.com')
elif 'www.jianshu.com' in url:  # 简书
    title_key = '.title'
    content_key = '.article'
    print('简书 https://www.jianshu.com 由于图片中包含两个src，提取不成功')
else:
    print('其它')


soup = BeautifulSoup(html, 'html.parser')
title = soup.select(title_key)[0].text.strip()  # 文章标题
print('文章标题：', title)
content = soup.select(content_key)[0]  # 文章内容

# filename = "测试文件" + ".html"
# with open(filename, "w", encoding='UTF-8') as f:
#     f.write(html)