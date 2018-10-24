import requests


class Handler:
    def __init__(self, start, end, url, filename):
        self.start = start
        self.end = end
        self.url = url
        self.filename = filename

    def run(self):
        print("{} - {}".format(self.start, self.end))
        headers = {"Range": "bytes={}-{}".format(self.start, self.end)}
        r = requests.get(self.url, headers=headers, stream=True)
        with open(self.filename, "r+b") as fp:
            fp.seek(self.start)
            fp.write(r.content)
