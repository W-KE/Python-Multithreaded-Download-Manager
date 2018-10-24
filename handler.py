from time import sleep

import requests

from lock import LOCK


class Handler:
    def __init__(self, start, end, url, file):
        self.start = start
        self.end = end
        self.url = url
        self.file = file

    def write(self, data):
        LOCK.acquire()
        print("Writing: {} - {}".format(self.start, self.end))
        # fp = open(self.filename, "r+b")
        self.file.seek(self.start)
        self.file.write(data)
        # fp.close()
        LOCK.release()

    def run(self):
        print("Downloading: {} - {}".format(self.start, self.end))
        headers = {"Range": "bytes={}-{}".format(self.start, self.end)}
        r = requests.get(self.url, headers=headers, stream=True)
        self.write(r.content)
