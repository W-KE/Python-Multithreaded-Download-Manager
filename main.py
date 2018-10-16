from random import shuffle
from threading import Thread

from downloader import Downloader
from manager import Manager

if __name__ == '__main__':
    manager = Manager("https://cdncontribute.geeksforgeeks.org/wp-content/uploads/vertical-Technical-Scripter-min.png",
                      1, "test.png")
    ranges = manager.get_range()
    # shuffle(ranges)
    for i in ranges:
        downloader = Downloader(manager, i[0], i[1])
        Thread(target=downloader.run, args=()).start()
