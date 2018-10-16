import contextlib

import requests

from lock import LOCK


class Downloader:
    # 构造函数
    def __init__(self, manager, start=0, end=None):
        # 要下载的数据连接
        self.url = manager.url
        # 要开的线程数
        self.num = manager.num
        # 存储文件的名字，从url最后面取
        self.filename = manager.filename
        # headers中取出数据的长度
        self.total = manager.total
        self.start = start
        if end is None:
            self.end = ""
        else:
            self.end = end
        print("{} - {}".format(self.start, self.end))

    def run(self):
        # 拼出Range参数 获取分片数据
        headers = {"Range": "Bytes={}-{}".format(self.start, self.end), "Accept-Encoding": "*"}
        r = requests.get(self.url, headers=headers, stream=True)
        with contextlib.closing(r) as resp:
            accepts = 0
            for data in resp.iter_content(chunk_size=8):
                if LOCK.acquire(True):
                    f = open(self.filename, "wb")
                    # seek到相应位置
                    f.seek(accepts + self.start)
                    # 写数据
                    f.write(data)
                    accepts += len(data)
                    progress = accepts / int(resp.headers["Content-Length"]) * 100
                    f.close()
                    LOCK.release()
