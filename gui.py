from PyQt5.QtWidgets import QWidget, QPushButton, QTableWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QDialog, \
    QFileDialog


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 600
        self.init_ui()
        self.tasks = []

    def init_ui(self):
        b1 = QPushButton("Add")
        b1.setToolTip('This is an example button')
        b1.clicked.connect(self.new_task)
        b2 = QPushButton("Start")
        b3 = QPushButton("Pause")
        b4 = QPushButton("Remove")
        b5 = QPushButton("Sort")
        b6 = QPushButton("Configuration")

        window = QVBoxLayout()
        menu = QHBoxLayout()
        menu.addWidget(b1)
        menu.addWidget(b2)
        menu.addWidget(b3)
        menu.addWidget(b4)
        menu.addWidget(b5)
        menu.addWidget(b6)
        tasks = QTableWidget()
        tasks.setColumnCount(5)
        tasks.setHorizontalHeaderLabels(["Filename", "Type", "Size", "Time", "Open"])
        window.addLayout(menu)
        window.addWidget(tasks)
        self.setLayout(window)

        self.setWindowTitle("PyQt")
        self.show()

    def new_task(self):
        d = QDialog()
        window = QVBoxLayout()

        # Download Url
        hbox = QHBoxLayout()
        label = QLabel("Url")
        # pixmap = QPixmap("link.png")
        # label.setPixmap(pixmap)
        hbox.addWidget(label)
        url = QLineEdit()
        url.returnPressed.connect(self.search_slot)
        hbox.addWidget(url)
        window.addLayout(hbox)

        # Download Filename
        hbox = QHBoxLayout()
        label = QLabel("Filename")
        # pixmap = QPixmap("link.png")
        # label.setPixmap(pixmap)
        hbox.addWidget(label)
        filename = QLineEdit()
        hbox.addWidget(filename)
        window.addLayout(hbox)

        # File size
        # label = QLabel("0 kb")
        # window.addWidget(label)

        # Save Directory
        hbox = QHBoxLayout()
        url = QLineEdit()
        hbox.addWidget(url)
        open = QPushButton("Open")
        hbox.addWidget(open)
        window.addLayout(hbox)

        # Number of Threads
        hbox = QHBoxLayout()
        label = QLabel("Number of Threads")
        hbox.addWidget(label)
        threads = QLineEdit()
        hbox.addWidget(threads)
        window.addLayout(hbox)

        # Buttons
        ok = QPushButton("OK")
        window.addWidget(ok)

        d.setWindowTitle("New Task")
        d.setLayout(window)
        d.exec_()

    def get_directory(self):
        return str(QFileDialog.getExistingDirectory(self, "Select Directory"))
