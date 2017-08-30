# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mining.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(864, 176)
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 30, 141, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.teCurrency = QtWidgets.QLineEdit(self.groupBox_3)
        self.teCurrency.setGeometry(QtCore.QRect(10, 20, 113, 20))
        self.teCurrency.setObjectName("teCurrency")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(160, 20, 131, 101))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pbStartMonitoring = QtWidgets.QPushButton(self.groupBox_4)
        self.pbStartMonitoring.setObjectName("pbStartMonitoring")
        self.verticalLayout_2.addWidget(self.pbStartMonitoring)
        self.pbStopMonitoring = QtWidgets.QPushButton(self.groupBox_4)
        self.pbStopMonitoring.setEnabled(False)
        self.pbStopMonitoring.setObjectName("pbStopMonitoring")
        self.verticalLayout_2.addWidget(self.pbStopMonitoring)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblCurrentPrice = QtWidgets.QLabel(self.groupBox_2)
        self.lblCurrentPrice.setText("")
        self.lblCurrentPrice.setObjectName("lblCurrentPrice")
        self.verticalLayout.addWidget(self.lblCurrentPrice)
        self.lblSpread = QtWidgets.QLabel(self.groupBox_2)
        self.lblSpread.setText("")
        self.lblSpread.setObjectName("lblSpread")
        self.verticalLayout.addWidget(self.lblSpread)
        self.lblBuying = QtWidgets.QLabel(self.groupBox_2)
        self.lblBuying.setText("")
        self.lblBuying.setObjectName("lblBuying")
        self.verticalLayout.addWidget(self.lblBuying)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Pass 1 Controlers"))
        self.groupBox_3.setTitle(_translate("Dialog", "1.1 Set Pair"))
        self.teCurrency.setText(_translate("Dialog", "ETHUSD"))
        self.groupBox_4.setTitle(_translate("Dialog", "1.2 Use the controllers"))
        self.pbStartMonitoring.setText(_translate("Dialog", "Start"))
        self.pbStopMonitoring.setText(_translate("Dialog", "Stop"))
        self.groupBox_2.setTitle(_translate("Dialog", "Pass 2 Results"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

