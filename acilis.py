from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot,QDate
from PyQt5.QtWidgets import QApplication, QDialog
from ana_sayfa import Ui_OutputDialog
import sys
import threading

class Ui_Dialog(QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        loadUi("./acilis.ui", self)
        now = QDate.currentDate()
        current_date = now.toString('dd MMMM yyyy dddd')
        self.Date_Label.setText(current_date)
        self.baslaButon.clicked.connect(self.runSlot)
        self._new_window = None
        self.Videocapture_ = None

    def refreshAll(self):
        self.Videocapture_ = "0"

    @pyqtSlot()
    def runSlot(self):
        print("Başlatıldı")
        self.refreshAll()
        print(self.Videocapture_)
        ui.hide()
        self.outputWindow_()

    def outputWindow_(self):
        self._new_window = Ui_OutputDialog()
        self._new_window.egit()
        self._new_window.show()
        self._new_window.startVideo(self.Videocapture_)
        print("Kamera Görüntü Almaya Başladı")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
