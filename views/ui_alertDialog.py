# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_alertDialog(object):
    def setupUi(self, alertDialog):
        alertDialog.setObjectName("alertDialog")
        alertDialog.resize(372, 176)
        self.verticalLayout = QtWidgets.QVBoxLayout(alertDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(alertDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.iconLbl = QtWidgets.QLabel(self.widget)
        self.iconLbl.setStyleSheet("")
        self.iconLbl.setText("")
        self.iconLbl.setPixmap(QtGui.QPixmap(":/images/assets/images/state-warning.svg"))
        self.iconLbl.setObjectName("iconLbl")
        self.horizontalLayout.addWidget(self.iconLbl)
        self.titleLbl = QtWidgets.QLabel(self.widget)
        self.titleLbl.setObjectName("titleLbl")
        self.horizontalLayout.addWidget(self.titleLbl)
        self.verticalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignLeft)
        self.bodyLbl = QtWidgets.QLabel(self.frame)
        self.bodyLbl.setObjectName("bodyLbl")
        self.verticalLayout_2.addWidget(self.bodyLbl, 0, QtCore.Qt.AlignHCenter)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(alertDialog)
        QtCore.QMetaObject.connectSlotsByName(alertDialog)

    def retranslateUi(self, alertDialog):
        _translate = QtCore.QCoreApplication.translate
        alertDialog.setWindowTitle(_translate("alertDialog", "Dialog"))
        self.titleLbl.setText(_translate("alertDialog", "TextLabelf"))
        self.bodyLbl.setText(_translate("alertDialog", "TextLabel"))
from views import resource_rc
