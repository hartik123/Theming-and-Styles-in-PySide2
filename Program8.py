import PySide2
from PySide2.QtWidgets import *
from PySide2.QtCore import Slot,Qt
from PySide2.QtGui import QPalette, QColor

app = QApplication([])

app.setStyle('Fusion')

default_palette = QPalette()
dark_palette = QPalette()
dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
dark_palette.setColor(QPalette.WindowText, Qt.white)
dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
dark_palette.setColor(QPalette.ToolTipText, Qt.white)
dark_palette.setColor(QPalette.Text, Qt.white)
dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ButtonText, Qt.white)
dark_palette.setColor(QPalette.BrightText, Qt.red)
dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
dark_palette.setColor(QPalette.HighlightedText, Qt.black)
dark_palette.setColor(QPalette.Window, QColor(53,53,53))
dark_palette.setColor(QPalette.WindowText, Qt.white)
dark_palette.setColor(QPalette.Base, QColor(25,25,25))
dark_palette.setColor(QPalette.Text, Qt.white)
dark_palette.setColor(QPalette.Button, QColor(53,53,53))
dark_palette.setColor(QPalette.ButtonText, Qt.white)

window= QWidget()
layout = QGridLayout()

for i in range(0,4):
    Dial = QDial()
    Button = QPushButton('Button'+str(i))
    Dial.setNotchesVisible(True)
    layout.addWidget(Button, 0,i)
    layout.addWidget(Dial,1,i)

@Slot()
def toggleDarkTheme():
    if not togglePushButton.isChecked():
        app.setPalette(dark_palette)
    else:
        app.setPalette(default_palette)

togglePushButton = QPushButton("Dark Mode")
togglePushButton.setCheckable(True)
togglePushButton.setChecked(True)
togglePushButton.clicked.connect(toggleDarkTheme)
layout.addWidget(togglePushButton,2,3)


window.setLayout(layout)
window.show()
app.exec_()