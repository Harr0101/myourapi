from PyQt5.QtWidgets import QMainWindow
from Ui_MainWindow import Ui_MainWindow
from HttpServer import HttpServer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Our api')

        self.httpd = HttpServer()
        self.httpd.request_text_change.connect(self.add_to_request)
        self.httpd.client_text_change.connect(self.add_to_client)
        self.httpd.response_text_change.connect(self.add_to_response)
        self.httpd.start()

    def add_to_request(self, request_text):
        request_type, request_string = request_text.split(',')
        self.ui.requestText.setText(request_string)

    def add_to_client(self, client_text):
        self.ui.clientText.setText(client_text)

    def add_to_response(self, response_text):
        self.ui.responseText.setText(response_text)