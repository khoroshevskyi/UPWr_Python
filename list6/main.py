# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import random
import pymongo

class Ui_MainWindow(object):
    """
    Creating game lotto window
    """
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 504)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 401, 443))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.label_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_name.setFont(font)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_name)
        self.label_name_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_name_2.setMinimumSize(QtCore.QSize(187, 18))
        self.label_name_2.setObjectName("label_name_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_name_2)

        # lineEdit for typing name of the player
        self.lineEdit_name = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_name)

        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.line)

        # labels for showing which item to choose
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)

        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_5)

        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_6)

        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_7)

        # comboboxes: for choosing the values
        combo_items = self.values_will_be_used()
        self.comboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.addItems(combo_items)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox)

        self.comboBox_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_2.addItems(combo_items)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)

        self.comboBox_3 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_3.addItems(combo_items)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)

        self.comboBox_4 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_4.addItems(combo_items)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.comboBox_4)

        self.comboBox_5 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_5.addItems(combo_items)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.comboBox_5)

        self.comboBox_6 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_6.addItems(combo_items)
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.comboBox_6)

        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setMinimumSize(QtCore.QSize(174, 26))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.show_best_scores)
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.check_lotto)
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)

        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 421, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_name.setText(_translate("MainWindow", "Lotto u Alexa"))
        self.label_name_2.setText(_translate("MainWindow", "Twoje imie:"))
        self.label.setText(_translate("MainWindow", "Prosze wybrac 6 liczb ktore uwazasz wylosujemy za chwile\n"
" Liczby beda losowane z puli 1-49"))
        self.label_3.setText(_translate("MainWindow", "Liczba 2:"))
        self.label_4.setText(_translate("MainWindow", "Liczba 3:"))
        self.label_5.setText(_translate("MainWindow", "Liczba 4:"))
        self.label_6.setText(_translate("MainWindow", "Liczba 5:"))
        self.label_7.setText(_translate("MainWindow", "Liczba 6:"))
        self.pushButton_2.setText(_translate("MainWindow", "Sprawdz i zapisz podejscie"))
        self.pushButton.setText(_translate("MainWindow", "Sprawdz najlepsze wyniki"))
        self.label_2.setText(_translate("MainWindow", "Liczba 1:"))

    # making values for comboboxes
    def values_will_be_used(self):
        values = list(range(1,50))
        values = list(map(str, values))
        return values

    # checking
    def check_lotto(self):
        try:
            liczba1 = self.comboBox.currentText()
            liczba2 = self.comboBox_2.currentText()
            liczba3 = self.comboBox_3.currentText()
            liczba4 = self.comboBox_4.currentText()
            liczba5 = self.comboBox_5.currentText()
            liczba6 = self.comboBox_6.currentText()
            liczby = [liczba1, liczba2, liczba3, liczba4, liczba5, liczba6]

            if self.checkIfDuplicates(liczby):
                self.message("choose another value!", "Liczby sie powtarzaja")

            else:
                player_name = self.lineEdit_name.text()
                if player_name == "":
                    self.message("Print your name!", "You have to wrtie your name or nickname!")
                else:
                    randomized_values = self.randomize_6_values(self.values_will_be_used())
                    correct_values = []
                    for nb in liczby:
                        if nb in randomized_values:
                            correct_values.append(nb)
                    self.show_user_score(randomized_values, liczby, str(len(correct_values)))
        except Exception as err:
            print(err)

    # random 6 values
    def randomize_6_values(self, values):
        wylosowane_liczby = []
        for k in range(0,6):
            wylosowane_liczby.append(random.choice(values))
        if self.checkIfDuplicates(wylosowane_liczby):
            wylosowane_liczby = self.randomize_6_values(values)
        return(wylosowane_liczby)

    # checking if values that is randomized and user choose are duplicating
    def checkIfDuplicates(self, listOfElems):
        ''' Check if given list contains any duplicates '''
        if len(listOfElems) == len(set(listOfElems)):
            return False
        else:
            return True

    # showing and writing the user score
    # using for it class user_score.py
    def show_user_score(self, rand_val, user_val, score):
        import user_score
        Dialog = QtWidgets.QDialog()
        self.ui1 = user_score.Ui_Dialog()
        self.ui1.setupUi(Dialog, rand_val, user_val, score)
        Dialog.show()
        user_name = self.lineEdit_name.text()

        data = {"player_name": user_name,
                "player_score": int(score)
        }

        self.insert_to_mongo(data)

    # showing messages
    def message(self, msg, msg_text):
        self.NewUserMsg = QMessageBox()
        self.NewUserMsg.setIcon(QMessageBox.Information)
        self.NewUserMsg.setText(msg_text)
        self.NewUserMsg.setWindowTitle(msg)
        self.NewUserMsg.setStandardButtons(QMessageBox.Ok)
        returnValue = self.NewUserMsg.exec()

    # showing all scares by opeing class show_score.py
    def show_best_scores(self):
        import show_score as show
        Form = QtWidgets.QWidget()
        self.ui = show.Ui_Form()
        self.ui.setupUi(Form)
        Form.show()

    # inserting new data to mongoDB
    def insert_to_mongo(self, data):
        """
        The database looks like:
        {
            "_id": {
            "$oid": "_____"
            },
            "player_name": "name",
            "player_score": score
        }
        """
        try:
            self.client = pymongo.MongoClient('localhost')
            self.db = self.client.lotto_alex
        except pymongo.errors.ConnectionFailure as e:
            print("Could not connect to server: %s" % e)

        try:
            ref_insert = self.db.scores.insert_one(data)
            print("Data has been saved")

        except pymongo.errors.BulkWriteError as err:
            print(err)
        else:
            self.client.close()
            print("Server connection has been closed.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
