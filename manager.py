import threading

import requests

from handler import Handler
from lock import LOCK


def handler(start, end, url, file):
    h = Handler(start, end, url, file)
    h.run()
    return h


class Manager:
    def __init__(self, url_of_file, number_of_threads=1, filename=None):
        self.url = url_of_file
        self.threads = number_of_threads
        if not filename:
            self.filename = url_of_file.split("/")[-1]
        else:
            self.filename = filename
        r = requests.head(url_of_file)
        try:
            self.size = int(r.headers["content-length"])
        except:
            self.size = -1

    def __len__(self):
        return self.size

    def prepare(self):
        LOCK.acquire()
        fp = open(self.filename, "wb")
        fp.write(b"\x00" * self.size)
        fp.close()
        LOCK.release()

    def run(self):
        file = open(self.filename, "r+b")
        part = self.size // self.threads
        end = -1
        while end < self.size:
            start = end + 1
            end = start + part
            if end > self.size:
                end = self.size
            t = threading.Thread(target=handler,
                                 kwargs={"start": start, "end": end, "url": self.url, "file": file})
            t.setDaemon(True)
            t.start()
        main_thread = threading.current_thread()
        for t in threading.enumerate():
            if t is main_thread:
                continue
            t.join()
        file.close()
        print("{} downloaded".format(self.filename))
