# -*- coding: utf-8 -*-

from selenium import webdriver
import csv

# url = 'file:///home/ubuntu/Scrapy/example/test.html'
url = 'https://music.163.com/#/discover/playlist'  # 用于测试

# 无界面调用‘火狐’浏览器的方法
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)
# print(help(webdriver.Firefox))  # 查看方法的配置信息
driver.get(url)

csv_file = open('playlist.csv', 'w', newline='')
writer = csv.writer(csv_file)
writer.writerow(['标题', '播放数', '链接'])


driver.switch_to.frame("contentFrame")
# data = driver.find_element_by_id("m-pl-container").find_element_by_tag_name("li")
data = driver.find_element_by_xpath('//*[@id="m-pl-container"]')
data.
print(driver.page_source)
with open('temp.html', 'w') as f:
    f.write(driver.page_source)
# print(len(data))
# for i in range(len(data)):
#     print(i)
    # 获取播放数
    # nb = data[i].find_element_by_class_name("nb").text
    # if '万' in nb and int(nb.split("万")[0]) > 500:
    #     msk = data[i].find_element_by_css_selector("a.msk")
    #     writer.writerow([msk.get_attribute("title"), nb, msk.get_attribute("href")])


csv_file.close()

# data = driver.title
# print(data)
print('结束')

def temp():

    # 网易云音乐第一页的地址
    #
    url = r'http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'


    # 准备好存储歌单的csv文件
    csv_file = open('playlist.csv', 'w', newline='')
    writer = csv.writer(csv_file)
    writer.writerow(['标题', '播放数', '链接'])

    # 解析每一页，直到下一页为空
    while url != 'javascript:void(0)':
        # 用WebDriver加载画面
        driver.get(url=url)
        # 切换到内容的iframe
        driver.switch_to.iframe("contentFrame")
        # 定位歌单标签
        data = driver.find_element_by_id("m-pl-container"). \
            find_element_by_tag_name("li")

        # 解析一页中的所有歌单
        for i in range(len(data)):
            # 获取播放数
            nb = data[i].find_element_by_class_name("nb").text
            if '万' in nb and int(nb.split("万")[0]) > 500:
                # 获取播放数大于500万的歌曲封面
                msk = data[i].find_element_by_css_selector("a.msk")
                # 把封面上的标题和链接播放数写到同一个文件中
                writer.writerow([msk.get_attribute("title"), nb, msk.get_attribute("href")])

        # 定位下一页
        url = driver.find_element_by_css_selector("a.zbtn.znxt").get_attribute('href')

    csv_file.close()
