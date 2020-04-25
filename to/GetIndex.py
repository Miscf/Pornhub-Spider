import requests
import re
import random
from lxml import etree
import os


ualist = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]


def getstr(text, s):
    exa = 'var {}=(.*?);'.format(s)
    res = re.findall(exa, text)

    return res[0]


def index(url, file_name):
    headers = {
        'User-Agent': random.choice(ualist),
        'origin': 'https://cn.pornhub.com',
        # 'Cookie': 'ua=952637548dc3e67d2638455ee5804af8; platform_cookie_reset=pc; platform=pc; bs=ugxax4soeyduag2djh1e7hjkul4xjxw9; ss=376961331525925125; _ga=GA1.2.2008759265.1587742192; _gid=GA1.2.82975103.1587742192; RNLBSERVERID=ded7422; performance_timing=search; RNKEY=17426239*19011043:2445256804:2072561131:1; _gat=1'
    }

    title_re = '<span class="inlineFree">(.*?)</span>'

    while True:
        try:
            res = requests.get(url, headers=headers).text
            break

        except:
            pass

    index_html = etree.HTML(res)

    keys = index_html.xpath('//ul[@id="relatedVideosCenter"]/li/@_vkey')

    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    with open(base_path + '\\log\\' + file_name + '.txt', 'r', encoding="utf8") as f:
        content_list = f.read().split('\n')

    with open(base_path + '\\log\\' + file_name + '.txt', 'a+', encoding='utf8') as f:
        for key in keys:
            if key not in content_list:
                if '#' + key not in content_list:
                    f.write('https://cn.pornhub.com/view_video.php?viewkey=' + str(key) + '\n')

    title = re.findall(title_re, res)
    title = title[0]

    full_url = str()
    if 'quality_1080' in res:
        print('quality_1080')
        p_720 = str(re.findall('quality_1080p=(.*?);', res)[0])

        useful_list = list()
        for i in p_720.split(' + */'):
            useful = i.split('+ /*')[0]
            if '/*' not in useful:
                useful_list.append(useful.replace(' ', ''))

        full_url = str()
        for i in useful_list:
            full_url += getstr(res, i)

    elif 'quality_720' in res:
        print('quality_720')
        p_720 = str(re.findall('quality_720p=(.*?);', res)[0])

        useful_list = list()
        for i in p_720.split(' + */'):
            useful = i.split('+ /*')[0]
            if '/*' not in useful:
                useful_list.append(useful.replace(' ', ''))

        full_url = str()
        for i in useful_list:
            full_url += getstr(res, i)

    elif 'quality_480' in res:
        print('quality_480')
        p_720 = str(re.findall('quality_480p=(.*?);', res)[0])

        useful_list = list()
        for i in p_720.split(' + */'):
            useful = i.split('+ /*')[0]
            if '/*' not in useful:
                useful_list.append(useful.replace(' ', ''))

        full_url = str()
        for i in useful_list:
            full_url += getstr(res, i)

    return title, full_url.replace('\"', '').replace(' + ', '')


if __name__ == '__main__':
    print(index('https://cn.pornhub.com/view_video.php?viewkey=ph5bd4e44badd9f'))
