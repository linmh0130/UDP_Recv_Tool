################################################################################
## Form generated from reading UI file 'network_tooleSsMrk.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
import socket
import threading
import time
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                          QRect, QSize, QUrl, Qt, QFile, QIODevice)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                         QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                         QRadialGradient)
from PyQt5.QtWidgets import *

MAX_DATA_LEN = 65536


class Ui_MainWindow(object):
    def __init__(self):
        self.isNetStartFlag = 0  # 标识是否开始调试
        self.num_received_bytes = 0
        self.num_sent_bytes = 0
        self.packet_count = 0

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(406, 220)
        MainWindow.setMinimumSize(QSize(406, 220))
        MainWindow.setMaximumSize(QSize(406, 220))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lb_outputFile = QLabel(self.centralwidget)
        self.lb_outputFile.setObjectName(u"lb_outputFile")
        self.lb_outputFile.setGeometry(QRect(10, 10, 111, 21))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(12)
        self.lb_outputFile.setFont(font)
        self.ledit_outputFile = QLineEdit(self.centralwidget)
        self.ledit_outputFile.setObjectName(u"ledit_outputFile")
        self.ledit_outputFile.setGeometry(QRect(120, 10, 201, 20))
        self.bt_open = QPushButton(self.centralwidget)
        self.bt_open.setObjectName(u"bt_open")
        self.bt_open.setGeometry(QRect(330, 10, 61, 20))
        self.bt_open.clicked.connect(self.onClick_bt_open)
        self.lb_sendText = QLabel(self.centralwidget)
        self.lb_sendText.setObjectName(u"lb_sendText")
        self.lb_sendText.setGeometry(QRect(180, 50, 111, 21))
        self.lb_sendText.setFont(font)
        self.lb_DstIP = QLabel(self.centralwidget)
        self.lb_DstIP.setObjectName(u"lb_DstIP")
        self.lb_DstIP.setGeometry(QRect(10, 50, 51, 21))
        self.lb_DstIP.setFont(font)
        self.ledit_DstIP = QLineEdit(self.centralwidget)
        self.ledit_DstIP.setObjectName(u"ledit_DstIP")
        self.ledit_DstIP.setGeometry(QRect(70, 50, 91, 20))
        self.ledit_DstIP.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.ledit_DstPort = QLineEdit(self.centralwidget)
        self.ledit_DstPort.setObjectName(u"ledit_DstPort")
        self.ledit_DstPort.setGeometry(QRect(110, 80, 51, 20))
        self.ledit_DstPort.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lb_DstPort = QLabel(self.centralwidget)
        self.lb_DstPort.setObjectName(u"lb_DstPort")
        self.lb_DstPort.setGeometry(QRect(10, 80, 61, 16))
        self.lb_DstPort.setFont(font)
        self.ledit_LocalIP = QLineEdit(self.centralwidget)
        self.ledit_LocalIP.setObjectName(u"ledit_LocalIP")
        self.ledit_LocalIP.setGeometry(QRect(70, 110, 91, 20))
        self.ledit_LocalIP.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lb_LocalIP = QLabel(self.centralwidget)
        self.lb_LocalIP.setObjectName(u"lb_LocalIP")
        self.lb_LocalIP.setGeometry(QRect(10, 110, 61, 21))
        self.lb_LocalIP.setFont(font)
        self.ledit_LocalPort = QLineEdit(self.centralwidget)
        self.ledit_LocalPort.setObjectName(u"ledit_LocalPort")
        self.ledit_LocalPort.setGeometry(QRect(110, 140, 51, 20))
        self.ledit_LocalPort.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lb_LocalPort = QLabel(self.centralwidget)
        self.lb_LocalPort.setObjectName(u"lb_LocalPort")
        self.lb_LocalPort.setGeometry(QRect(10, 140, 81, 16))
        self.lb_LocalPort.setFont(font)
        self.bt_start_stop = QPushButton(self.centralwidget)
        self.bt_start_stop.setObjectName(u"bt_start_stop")
        self.bt_start_stop.setGeometry(QRect(180, 140, 61, 20))
        self.bt_start_stop.clicked.connect(self.onClick_bt_start_stop)
        self.tedit_sendText = QTextEdit(self.centralwidget)
        self.tedit_sendText.setObjectName(u"tedit_sendText")
        self.tedit_sendText.setGeometry(QRect(180, 80, 221, 51))
        self.bt_Send = QPushButton(self.centralwidget)
        self.bt_Send.setObjectName(u"bt_Send")
        self.bt_Send.setGeometry(QRect(340, 140, 61, 20))
        self.bt_Send.clicked.connect(self.onClick_bt_Send)

        self.lb_T = QLabel(self.centralwidget)
        self.lb_T.setObjectName(u"lb_T")
        self.lb_T.setGeometry(QRect(180, 170, 21, 21))
        self.lb_T.setFont(font)
        self.lb_T_Num = QLabel(self.centralwidget)
        self.lb_T_Num.setObjectName(u"lb_T_Num")
        self.lb_T_Num.setGeometry(QRect(200, 170, 81, 21))
        self.lb_T_Num.setFont(font)
        self.lb_T_Num.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lb_R = QLabel(self.centralwidget)
        self.lb_R.setObjectName(u"lb_R")
        self.lb_R.setGeometry(QRect(10, 170, 21, 21))
        self.lb_R.setFont(font)
        self.lb_R.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lb_R_Num = QLabel(self.centralwidget)
        self.lb_R_Num.setObjectName(u"lb_R_Num")
        self.lb_R_Num.setGeometry(QRect(30, 170, 81, 21))
        self.lb_R_Num.setFont(font)
        self.lb_R_Num.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 406, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"UDP Receive Tool", None))
        self.lb_outputFile.setText(QCoreApplication.translate("MainWindow", u"Saving Location:", None))
        self.bt_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.lb_sendText.setText(QCoreApplication.translate("MainWindow", u"Send Text:", None))
        self.lb_DstIP.setText(QCoreApplication.translate("MainWindow", u"Dst IP:", None))
        self.ledit_DstIP.setText(QCoreApplication.translate("MainWindow", u"127.0.0.1", None))
        self.ledit_LocalPort.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        self.lb_LocalPort.setText(QCoreApplication.translate("MainWindow", u"Local Port:", None))
        self.ledit_DstPort.setText(QCoreApplication.translate("MainWindow", u"8000", None))
        self.lb_DstPort.setText(QCoreApplication.translate("MainWindow", u"Dst Port:", None))
        self.bt_start_stop.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.bt_Send.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.lb_T.setText(QCoreApplication.translate("MainWindow", u"T:", None))
        self.lb_T_Num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lb_R.setText(QCoreApplication.translate("MainWindow", u"R:", None))
        self.lb_R_Num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ledit_LocalIP.setText(QCoreApplication.translate("MainWindow", u"127.0.0.1", None))
        self.lb_LocalIP.setText(QCoreApplication.translate("MainWindow", u"Local IP:", None))

    # retranslateUi

    def onClick_bt_Send(self):
        dst_ip_addr = self.ledit_DstIP.text()
        dst_port = int(self.ledit_DstPort.text())
        if (self.isNetStartFlag == 1):
            try:
                send_data = self.tedit_sendText.toPlainText().encode()
                self.sock_UDP.sendto(send_data, (dst_ip_addr, dst_port))
                self.num_sent_bytes = self.num_sent_bytes + len(send_data)
                self.lb_T_Num.setText(str(self.num_sent_bytes))
            except:
                pass

    def onClick_bt_open(self):
        if (self.isNetStartFlag == 0):
            file_dialog = QFileDialog()
            if file_dialog.exec_():
                str_filename_list = file_dialog.selectedFiles()
                self.ledit_outputFile.setText(str_filename_list[0])

    def onClick_bt_start_stop(self):
        if (self.isNetStartFlag == 0):  # 还没开始

            str_outputFileName = self.ledit_outputFile.text()
            self.fp_outputFile = QFile(str_outputFileName)
            self.fp_outputFile.open(QIODevice.WriteOnly)
            if (self.fp_outputFile.isWritable()):
                self.sock_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                hostname = socket.gethostname()
                local_ip_addr = self.ledit_LocalIP.displayText()
                local_port = self.ledit_LocalPort.displayText()
                try:
                    self.sock_UDP.bind((local_ip_addr, int(local_port)))
                except:
                    print("Cannot open the network! Please check IPs and ports")
                    return -1

                self.isNetStartFlag = 1
                self.bt_start_stop.setText('Stop')
                self.ledit_LocalPort.setEnabled(False)
                self.ledit_DstPort.setEnabled(False)
                self.ledit_DstIP.setEnabled(False)
                self.ledit_LocalIP.setEnabled(False)
                self.ledit_outputFile.setEnabled(False)
                self.bt_open.setEnabled(False)

                self.udp_recv_thread = threading.Thread(target=self.thread_udp_receiver)
                self.udp_recv_thread.start()
            else:
                print("Cannot write to file")

        else:
            self.isNetStartFlag = 0
            self.bt_start_stop.setText('Start')
            self.ledit_LocalPort.setEnabled(True)
            self.ledit_DstPort.setEnabled(True)
            self.ledit_DstIP.setEnabled(True)
            self.ledit_LocalIP.setEnabled(True)
            self.ledit_outputFile.setEnabled(True)
            self.bt_open.setEnabled(True)
            self.sock_UDP.close()
            self.fp_outputFile.close()

    def thread_udp_receiver(self):
        while self.isNetStartFlag == 1:
            try:
                data, client_address = self.sock_UDP.recvfrom(MAX_DATA_LEN)
                data_len = len(data)
                self.packet_count = self.packet_count + 1
                print(self.packet_count, ":", "Received", data_len, "byte(s) from", client_address)
                self.num_received_bytes = self.num_received_bytes + data_len
                self.lb_R_Num.setText(str(self.num_received_bytes))
                if self.fp_outputFile.isOpen():
                    self.fp_outputFile.write(data)  # luckily data's type is bytes
                    self.fp_outputFile.flush()
            except Exception as e:
                print(e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
