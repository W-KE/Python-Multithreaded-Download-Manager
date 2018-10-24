from manager import Manager

if __name__ == '__main__':
    manager = Manager("https://cdncontribute.geeksforgeeks.org/wp-content/uploads/vertical-Technical-Scripter-min.png",
                      16, "test.png")
    # ranges = manager.get_range()
    # shuffle(ranges)
    manager.run()
