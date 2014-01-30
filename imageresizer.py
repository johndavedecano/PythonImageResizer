# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imageresizer.ui'
#
# Created: Thu Jan 30 10:39:03 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys,os,signal,glob
from PIL import Image

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    files_count = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(421, 248)
        MainWindow.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.dir = os.getcwd()
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 403, 227))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setText(self.dir)
        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))

        self.file_model = QFileSystemModel()
        self.file_model.setFilter(QDir.NoDotAndDotDot | QDir.Files)
        filters = ["*.jpg","*.png","*.png"]
        self.file_model.setNameFilters(filters)
        self.file_model.setNameFilterDisables(False)
        root = self.file_model.setRootPath(self.dir)

        self.listView = QtGui.QListView(self.widget)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.listView.setModel(self.file_model)
        self.listView.setRootIndex(root)

        self.horizontalLayout_2.addWidget(self.listView)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_2 = QtGui.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit_3 = QtGui.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        #self.lineEdit_4 = QtGui.QLineEdit(self.widget)
        #self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        #self.verticalLayout_3.addWidget(self.lineEdit_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        # STATUS BAR
        self.statusBar = QtGui.QStatusBar()
        self.statusBar.showMessage("Total Items")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # REGISTER EVENTS
        self.pushButton.clicked.connect(self.selectFolder)
        self.pushButton_2.clicked.connect(self.resizeImages)
        #

    def selectFolder(self):
        directory = QtGui.QFileDialog.getExistingDirectory(None,'Select Images Folder','C:/',QtGui.QFileDialog.ShowDirsOnly)
        self.lineEdit.setText(directory)
        self.dir = directory
        root = self.file_model.setRootPath(self.lineEdit.text())
        self.listView.setRootIndex(root)
        self.countFiles()

    def countFiles(self):
        extensions = ["*.jpg","*.png","*.gif"]
        self.files_count = 0
        for i in extensions:
            images_path = str(self.dir) + "/" + i
            self.files_count += len(glob.glob(images_path))
        self.label_3.setText("Total Images: " + str(self.files_count))

    def resizeImages(self):

        extensions = ["*.jpg","*.png","*.gif"]
        files_count = 0
        output_dir = str(self.dir) + "/output"
        width = self.lineEdit_2.text()
        height = self.lineEdit_3.text()
        self.countFiles()

        if self.files_count == 0:
            QtGui.QMessageBox.warning(None, 'Error','You have to select a valid folder with images in it.')
        else:
            if width == "" or height == "":
                QtGui.QMessageBox.warning(None, 'Error','You must specify both height and width')
            else:
                for i in extensions:
                    images_path = str(self.dir) + "/" + i
                    for x in glob.glob(images_path):
                        image = Image.open(x)
                        output = image.resize((int(width),int(height)))
                        if not os.path.exists(output_dir):
                            os.makedirs(output_dir)
                        filename = os.path.join(output_dir,os.path.basename(x))
                        output.save(filename)
                #SUCCESS AFTER ITERATION
                QtGui.QMessageBox.information(None, 'Success','All images has been resized.')

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Resizer", None))
        self.pushButton.setText(_translate("MainWindow", "Select Directory", None))
        self.label.setText(_translate("MainWindow", "Width", None))
        self.label_2.setText(_translate("MainWindow", "Height", None))
        self.label_3.setText(_translate("MainWindow", "Total Images: 0", None))
        self.pushButton_2.setText(_translate("MainWindow", "Resize Images", None))

class MainWindow (QMainWindow,Ui_MainWindow):

    #Create settings for the software
    settings = QSettings('Your Name','Name of the software')
    settings.setFallbacksEnabled(False)
    version = '1.0'

    def __init__ (self, parent = None):
        QMainWindow.__init__( self,parent)
        #Load the ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )
        #Set the MainWindow Title
        self.setWindowTitle('Image Resizer Pro - ' + self.version)
        #When the software are closed on console the software are closed
        #signal.signal(signal.SIGINT, signal.SIG_DFL)
        #Show the form
        self.show()
        self.setFixedSize(self.size())

def main():
    #Start the software
    app = QApplication(sys.argv)
    MainWindow_ = QMainWindow()
    ui = MainWindow()
    ui.setupUi(MainWindow_)
    #Add the close feature at the program with the X
    sys.exit(app.exec_())
#Execute the software
main()

