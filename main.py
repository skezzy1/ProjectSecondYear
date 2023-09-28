from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDockWidget
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Main Window")

button = QPushButton()
button.setText("Press me")

window.addDockWidget()
window.show()
app.exec()
