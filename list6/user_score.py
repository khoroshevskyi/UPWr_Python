# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    """
    Class for showing Dialog window: user scored in this game
    """
    def setupUi(self, Dialog, rand_val, user_val, score):
        self.Dialog = Dialog
        self.rand_val = rand_val
        self.user_val = user_val
        self.score = str(score)

        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(404, 189)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Dialog.setFont(font)
        self.formLayout = QtWidgets.QFormLayout(self.Dialog)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.line = QtWidgets.QFrame(self.Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.line_2 = QtWidgets.QFrame(self.Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.line_2)
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.Dialog)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.close_window)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pushButton)

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Liczby ktore zostaly wylosowane:   "))
        self.label_3.setText(_translate("Dialog", "Liczby wybrales ty: "))
        self.label_5.setText(_translate("Dialog", "Twoj wynik:"))


        self.rand_val = ', '.join(self.rand_val)
        self.user_val = ', '.join(self.user_val)
        self.label_2.setText(_translate("Dialog", self.rand_val))
        self.label_4.setText(_translate("Dialog", self.user_val))
        self.label_6.setText(_translate("Dialog", self.score))
        self.pushButton.setText(_translate("Dialog", "Close"))

    def close_window(self):
        self.Dialog.close()

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog, "", "", "")
    Dialog.show()
    sys.exit(app.exec_())
'''
