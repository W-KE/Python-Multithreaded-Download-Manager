from manager import Manager

if __name__ == '__main__':
    manager = Manager("http://dl.eagleget.com/latest/eagleget_setup.exe", 1024)
    manager.prepare()
    manager.run()
