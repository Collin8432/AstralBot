


from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QtGui


class button(QPushButton):
    def __init__(self, text, parent):
        super().__init__(text, parent)
        self.setFixedSize(100, 50)
        self.setStyleSheet("background-color: #4CAF50; color: white;")
        self.clicked.connect(self.button_clicked)

    def button_clicked(self):
        print("Button clicked")

    def set_text(self, text):
        self.setText(text)

    def get_text(self):
        return self.text()

    def set_color(self, color):
        self.setStyleSheet("background-color: " + color + "; color: white;")

    def get_color(self):
        return self.styleSheet()

    def set_font_size(self, size):
        self.setFont(QtGui.QFont("Arial", size))

    def get_font_size(self):
        return self.font().pointSize()

    def set_font_color(self, color):
        self.setStyleSheet("background-color: " + self.get_color() + "; color: " + color + ";")

    def get_font_color(self):
        return self.styleSheet()[-7:]

    def set_font_family(self, family):
        self.setFont(QFont(family))

    def get_font_family(self):
        return self.font().family()

    def set_font_style(self, style):
        self.setFont(QFont(self.get_font_family(), self.get_font_size(), style))

    def get_font_style(self):
        return self.font().style()

    def set_font_weight(self, weight):
        self.setFont(QFont(self.get_font_family(), self.get_font_size(), self.get_font_style(), weight))

    def get_font_weight(self):
        return self.font().weight()

    def set_font_italic(self, italic):
        self.setFont(Q