# HitBtc API Class
# Developed by jmarcolan in Python 3.5.4 64 bit
# https://github.com/jmarcolan/pyQtGuiHitBitc
# if you like
# donate ETH: 0xb641e28C20574E968EB18dadd5060c33083a6b45
# donate BTC: 17tzJPnyJMsW2TRSi4TCTQ4YSawB6JkZU7


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
#import Gui class generate from Qt Designe
from ui_mining import Ui_Dialog

# https://github.com/jmarcolan/pyQtGuiHitBitc
from HitBtc import public_api
import datetime

# Class to construct Logic from Gui generate from Qt Design
class HitBtcMonitoringGui(Ui_Dialog):
    # python constructor
    def __init__(self):
        super(HitBtcMonitoringGui , self).__init__()
        self.Dialog = QtWidgets.QDialog()
        self.setupUi(self.Dialog)
        self.Dialog.show()
        self.hit = public_api()
        #connect signal and slot
        self.pbStartMonitoring.clicked.connect(self.startTimer)
        self.pbStopMonitoring.clicked.connect(self.stopTimer)


    # Slot function call when
    # When start button are clicked  the time start and gui logic refresh
    def startTimer(self):
        self.pbStartMonitoring.setEnabled(False)
        self.teCurrency.setEnabled(False)
        self.pbStopMonitoring.setEnabled(True)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.leticker)
        #4000 ms = 4seg
        self.timer.start(4000)

    # Slot function call when stop button are clicked
    # When button are click stop timer and gui refresh
    def stopTimer(self):
        self.timer.stop()
        self.pbStartMonitoring.setEnabled(True)
        self.teCurrency.setEnabled(True)
        self.pbStopMonitoring.setEnabled(False)



    # Slot function call when timer timeout happens
    # Every time timeout happens tick pair and gui refresh
    def leticker(self):
        self.tick = self.hit.ticker(self.teCurrency.text())
        #print(self.tick['last'])
        self.lblCurrentPrice.setText('The ether price are ' + self.tick['last'])
        self.lblSpread.setText('The spread are '+ str((float(self.tick['ask']) - float(self.tick['bid']))))
        self.lblBuying.setText('Last price get on ' +datetime.datetime.fromtimestamp(round(self.tick['timestamp']/1000)).strftime('%Y-%m-%d %H:%M:%S'))



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    teste = HitBtcMonitoringGui()
    sys.exit(app.exec_())
