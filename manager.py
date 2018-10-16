import requests


class Manager:
    # 构造函数
    def __init__(self, url, num, filename):
        # 要下载的数据连接
        self.url = url
        # 要开的线程数
        self.num = num
        # 存储文件的名字，从url最后面取
        self.filename = filename
        # head方法去请求url
        r = requests.head(self.url)
        # headers中取出数据的长度
        self.total = int(r.headers["Content-Length"])

    def get_range(self):
        ranges = []
        # 比如total是50,线程数是4个。offset就是12
        offset = int(self.total / self.num)
        for i in range(self.num):
            if i == self.num - 1:
                # 最后一个线程，不指定结束位置，取到最后
                ranges.append((i * offset, ""))
            else:
                # 每个线程取得区间
                ranges.append((i * offset, (i + 1) * offset))
        # range大概是[(0,12),(12,24),(25,36),(36,'')]
        return ranges
