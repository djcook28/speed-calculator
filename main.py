from PyQt6.QtWidgets import (QGridLayout, QLineEdit, QLabel, QApplication, QPushButton, QWidget,
                             QListWidget)
import sys

class SpeedCalculator(QWidget):
    def __init__(self):
        # instantiate the QWidget class
        super().__init__()

        # initiate widgets
        distance_label = QLabel("Distance: ")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time: ")
        self.time_line_edit = QLineEdit()

        convert_button = QPushButton("Convert")
        convert_button.clicked.connect(self.convert)

        self.output_label = QLabel("")

        grid = QGridLayout()
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)

        self.setLayout(grid)

    def convert(self):
        distance = self.distance_line_edit.text()
        time = self.time_line_edit.text()
        try:
            distance = float(distance)
            time = float(time)
            speed = distance/time
            self.output_label.text(f"Your speed was {speed}")
        except:
            self.output_label.text("Entries must be numbers")

app = QApplication(sys.argv)
speed_conv_widget = SpeedCalculator()
speed_conv_widget.show()
sys.exit(app.exec())