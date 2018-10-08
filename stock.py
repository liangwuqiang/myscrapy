import requests
from bs4 import BeautifulSoup
import re


def get_html_text(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def get_stock_list(lst, stock_url):
    html = get_html_text(stock_url)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue


def get_stock_info(lst, stock_url, filename):
    count = 0
    for stock in lst:
        url = stock_url + stock + ".html"  # 构造每只股票的url
        html = get_html_text(url)  # 通过url获取一只股票的网页
        try:
            if html == "":  # 空的网页，跳过
                continue
            info_dict = {}  # 字典，用于存放股票信息
            soup = BeautifulSoup(html, 'html.parser')  # 开始解析网页
            stock_info = soup.find('div', attrs={'class': 'stock-bets'})  # 提取网页中有用的数据块
            name = stock_info.find_all(attrs={'class': 'bets-name'})[0]  # 从数据块中提取股票名称
            info_dict.update({'股票名称': name.text.split()[0]})  # 将股票名称添加到字典中

            key_list = stock_info.find_all('dt')
            value_list = stock_info.find_all('dd')
            for i in range(len(key_list)):
                key = key_list[i].text
                val = value_list[i].text
                info_dict[key] = val

            with open(filename, 'a', encoding='utf-8') as f:
                f.write(str(info_dict) + '\n')
                count = count + 1
                print("\r当前进度: {:.2f}%".format(count * 100 / len(lst)), end="")
        except:
            count = count + 1
            print("\r当前进度: {:.2f}%".format(count * 100 / len(lst)), end="")
            continue


def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'  # 东方财富网
    stock_info_url = 'https://gupiao.baidu.com/stock/'  # 百度股票
    output_file = 'output/BaiduStockInfo.txt'  # 数据输出文件
    stock_list = []  # 股票列表
    get_stock_list(stock_list, stock_list_url)  # 获取全部股票代号
    get_stock_info(stock_list, stock_info_url, output_file)  # 通过代号获取股票信息


if __name__ == '__main__':
    main()

