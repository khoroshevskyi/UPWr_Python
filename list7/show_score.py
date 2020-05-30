# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo

class Ui_Form(object):
    """
    Class for showing all scores in all the setAlignment
    The scores are writen in mongoDB
    """
    def setupUi(self, Form):
        self.Form = Form
        self.Form.setObjectName("Form")
        self.Form.resize(330, 400)
        self.Form.setMinimumSize(QtCore.QSize(330, 143))
        self.Form.setAutoFillBackground(False)
        self.gridLayout = QtWidgets.QGridLayout(self.Form)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 310, 380))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setReadOnly(True)

        data_to_show = self.find_data()
        self.plainTextEdit.insertPlainText(data_to_show)

        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(self.Form)
        QtCore.QMetaObject.connectSlotsByName(self.Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.Form.setWindowTitle(_translate("Form", "Form"))

    # finding and preparing data to show
    def find_data(self):
        text = ("The list of best scores that users made:\n" +
                "Player       ||     Score\n "+ "-"* 30 + "\n")
        data = self.open_read_db()
        data = sorted(data, key = lambda i: i['player_score'],reverse=True)

        for item in data:
            text = (text + item["player_name"] + " "*(20-len(item["player_name"]))  + "||" + " "*10  + str(item['player_score']) + "\n")
        return(text)

    # reading data from mongoDB
    def open_read_db(self):
        try:
            self.client = pymongo.MongoClient('localhost')
            self.db = self.client.lotto_alex
        except pymongo.errors.ConnectionFailure as e:
            print("Could not connect to server: %s" % e)

        try:
            data = []
            for x in self.db.scores.find():
                data.append(x)

        except pymongo.errors.BulkWriteError as err:
            print(err)
        else:
            self.client.close()
            print("Server connection has been closed.")
            return(data)

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
'''
