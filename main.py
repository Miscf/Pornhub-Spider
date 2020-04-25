from to.GetIndex import index
from to.t import get_video
from threading import Thread
import time
import os


def mains(url, file_name):
    start = time.time()
    s = index(url, file_name)

    print(s)

    get_video(s, url, file_name)

    end = time.time()

    print('完成线程 %s 用时 %.5f;' % (s[0], end - start))


if __name__ == '__main__':
    file_name = str(int(time.time()))
    with open('log/' + file_name + '.txt', 'w+', encoding='utf8') as f:
        f.write(input('起始url:'))

    os.mkdir('F:/ph/' + file_name)

    while True:
        # 起始url
        with open('log/' + file_name + '.txt', 'r+') as f:
            urls = f.read().split('\n')

        print(urls)
        thread_list = list()
        for url in urls:
            # 排除空url
            if url != '':
                # 识别已爬取url
                if url[0] != '#':
                    # 设置最大线程数
                    if len(thread_list) <= 8:
                        thread_list.append(Thread(
                            target=mains,
                            args=(url, file_name)
                        ))

        print('运行线程 %s' % str(len(thread_list)))

        for i in thread_list:
            i.start()

        for i in thread_list:
            i.join()
