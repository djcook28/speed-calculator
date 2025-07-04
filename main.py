from PyQt6.QtWidgets import (QGridLayout, QLineEdit, QLabel, QApplication, QPushButton, QWidget,
                             QComboBox)
import sys

class SpeedCalculator(QWidget):
    def __init__(self):
        # instantiate the QWidget class
        super().__init__()

        # initiate widgets
        distance_label = QLabel("Distance: ")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time (hours): ")
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton("Convert")
        calculate_button.clicked.connect(self.calculate)

        self.metric_combo = QComboBox()
        self.metric_combo.addItems(["Metric (km)", "Imperial (mi)"])

        self.output_label = QLabel("")

        grid = QGridLayout()
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.metric_combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        # first 2 numbers set the row and column position, second 2 set
        # width and height in numbers of rows and columns
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        # set grid to add record widget
        self.setLayout(grid)

    def calculate(self):
        distance = self.distance_line_edit.text()
        time = self.time_line_edit.text()
        try:
            distance = float(distance)
            time = float(time)
            avg_speed = distance/time
            if(self.metric_combo.currentText().startswith("Metric")):
               self.output_label.setText(f"Your average speed was {avg_speed} km/hr")
            else:
                self.output_label.setText(f"Your average speed was {avg_speed} mi/hr")
        except:
            self.output_label.setText("Entries must be numbers")

app = QApplication(sys.argv)
speed_conv_widget = SpeedCalculator()
speed_conv_widget.show()
sys.exit(app.exec())