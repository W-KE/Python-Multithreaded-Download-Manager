import threading

import requests

from handler import Handler


def handler(start, end, url, filename):
    h = Handler(start, end, url, filename)
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
        fp = open(self.filename, "wb")
        fp.write(b"\x00" * self.filename)
        fp.close()

    def run(self):
        part = self.size // self.threads
        for i in range(self.threads):
            start = part * i
            end = start + part
            t = threading.Thread(target=handler,
                                 kwargs={"start": start, "end": end, "url": self.url, "filename": self.filename})
            t.setDaemon(True)
            t.start()
        main_thread = threading.current_thread()
        for t in threading.enumerate():
            if t is main_thread:
                continue
            t.join()
        print("{} downloaded".format(self.filename))
