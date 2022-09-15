# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'JECarUnlocks.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFrame,
    QHeaderView, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_JECarUnlocksDialog(object):
    def setupUi(self, JECarUnlocksDialog):
        if not JECarUnlocksDialog.objectName():
            JECarUnlocksDialog.setObjectName(u"JECarUnlocksDialog")
        JECarUnlocksDialog.setWindowModality(Qt.ApplicationModal)
        JECarUnlocksDialog.resize(417, 670)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(JECarUnlocksDialog.sizePolicy().hasHeightForWidth())
        JECarUnlocksDialog.setSizePolicy(sizePolicy)
        JECarUnlocksDialog.setMinimumSize(QSize(417, 670))
        JECarUnlocksDialog.setMaximumSize(QSize(417, 670))
        icon = QIcon()
        icon.addFile(u"Juiced_32px.png", QSize(), QIcon.Normal, QIcon.Off)
        JECarUnlocksDialog.setWindowIcon(icon)
        JECarUnlocksDialog.setModal(True)
        self.carUnlocksTable = QTableWidget(JECarUnlocksDialog)
        if (self.carUnlocksTable.columnCount() < 2):
            self.carUnlocksTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.carUnlocksTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.carUnlocksTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.carUnlocksTable.rowCount() < 52):
            self.carUnlocksTable.setRowCount(52)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(8, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(9, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(10, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(11, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(12, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(13, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(14, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(15, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(16, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(17, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(18, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(19, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(20, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(21, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(22, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(23, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(24, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(25, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(26, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(27, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(28, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(29, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(30, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(31, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(32, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(33, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(34, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(35, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(36, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(37, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(38, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(39, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(40, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(41, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(42, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(43, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(44, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(45, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(46, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(47, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(48, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(49, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(50, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.carUnlocksTable.setVerticalHeaderItem(51, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.carUnlocksTable.setItem(0, 1, __qtablewidgetitem54)
        self.carUnlocksTable.setObjectName(u"carUnlocksTable")
        self.carUnlocksTable.setGeometry(QRect(10, 10, 397, 650))
        sizePolicy.setHeightForWidth(self.carUnlocksTable.sizePolicy().hasHeightForWidth())
        self.carUnlocksTable.setSizePolicy(sizePolicy)
        self.carUnlocksTable.setMinimumSize(QSize(397, 650))
        self.carUnlocksTable.setMaximumSize(QSize(397, 650))
        self.carUnlocksTable.setFrameShape(QFrame.StyledPanel)
        self.carUnlocksTable.setFrameShadow(QFrame.Plain)
        self.carUnlocksTable.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.carUnlocksTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.carUnlocksTable.setAutoScrollMargin(24)
        self.carUnlocksTable.setAlternatingRowColors(False)
        self.carUnlocksTable.setSelectionMode(QAbstractItemView.NoSelection)
        self.carUnlocksTable.horizontalHeader().setMinimumSectionSize(96)
        self.carUnlocksTable.horizontalHeader().setDefaultSectionSize(96)
        self.carUnlocksTable.horizontalHeader().setHighlightSections(False)
        self.carUnlocksTable.verticalHeader().setVisible(True)
        self.carUnlocksTable.verticalHeader().setDefaultSectionSize(24)
        self.carUnlocksTable.verticalHeader().setHighlightSections(False)

        self.retranslateUi(JECarUnlocksDialog)

        QMetaObject.connectSlotsByName(JECarUnlocksDialog)
    # setupUi

    def retranslateUi(self, JECarUnlocksDialog):
        JECarUnlocksDialog.setWindowTitle(QCoreApplication.translate("JECarUnlocksDialog", u"Car Unlocks", None))
        ___qtablewidgetitem = self.carUnlocksTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Tier", None));
        ___qtablewidgetitem1 = self.carUnlocksTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Unlock", None));
        ___qtablewidgetitem2 = self.carUnlocksTable.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Acura Integra Type R", None));
        ___qtablewidgetitem3 = self.carUnlocksTable.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Acura NSX", None));
        ___qtablewidgetitem4 = self.carUnlocksTable.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Acura RSX Type-S", None));
        ___qtablewidgetitem5 = self.carUnlocksTable.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Chevrolet Camaro", None));
        ___qtablewidgetitem6 = self.carUnlocksTable.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Chevrolet Camaro Z28", None));
        ___qtablewidgetitem7 = self.carUnlocksTable.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Chevrolet Corvette", None));
        ___qtablewidgetitem8 = self.carUnlocksTable.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Chevrolet Corvette Z06", None));
        ___qtablewidgetitem9 = self.carUnlocksTable.verticalHeaderItem(7)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Dodge 1969 Charger R/T", None));
        ___qtablewidgetitem10 = self.carUnlocksTable.verticalHeaderItem(8)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Dodge Neon R/T", None));
        ___qtablewidgetitem11 = self.carUnlocksTable.verticalHeaderItem(9)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Dodge SRT-4", None));
        ___qtablewidgetitem12 = self.carUnlocksTable.verticalHeaderItem(10)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Dodge Viper GTS", None));
        ___qtablewidgetitem13 = self.carUnlocksTable.verticalHeaderItem(11)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Fiat Punto 1.8 HGT", None));
        ___qtablewidgetitem14 = self.carUnlocksTable.verticalHeaderItem(12)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Ford 2003 Focus SVT", None));
        ___qtablewidgetitem15 = self.carUnlocksTable.verticalHeaderItem(13)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Ford 2004 Focus ZTS", None));
        ___qtablewidgetitem16 = self.carUnlocksTable.verticalHeaderItem(14)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Ford 67 Mustang", None));
        ___qtablewidgetitem17 = self.carUnlocksTable.verticalHeaderItem(15)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Ford Falcon XR8", None));
        ___qtablewidgetitem18 = self.carUnlocksTable.verticalHeaderItem(16)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Ford Mustang GT 99", None));
        ___qtablewidgetitem19 = self.carUnlocksTable.verticalHeaderItem(17)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Holden Monaro CV8", None));
        ___qtablewidgetitem20 = self.carUnlocksTable.verticalHeaderItem(18)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Honda Civic DX", None));
        ___qtablewidgetitem21 = self.carUnlocksTable.verticalHeaderItem(19)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Honda Civic Type R", None));
        ___qtablewidgetitem22 = self.carUnlocksTable.verticalHeaderItem(20)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Honda CR-X", None));
        ___qtablewidgetitem23 = self.carUnlocksTable.verticalHeaderItem(21)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Honda Integra Type R '99", None));
        ___qtablewidgetitem24 = self.carUnlocksTable.verticalHeaderItem(22)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Honda Integra Type R '02", None));
        ___qtablewidgetitem25 = self.carUnlocksTable.verticalHeaderItem(23)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Honda NSX", None));
        ___qtablewidgetitem26 = self.carUnlocksTable.verticalHeaderItem(24)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Honda Prelude VT", None));
        ___qtablewidgetitem27 = self.carUnlocksTable.verticalHeaderItem(25)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Honda S2000", None));
        ___qtablewidgetitem28 = self.carUnlocksTable.verticalHeaderItem(26)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Mazda MX-5", None));
        ___qtablewidgetitem29 = self.carUnlocksTable.verticalHeaderItem(27)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Mazda RX-7", None));
        ___qtablewidgetitem30 = self.carUnlocksTable.verticalHeaderItem(28)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Mazda RX-8", None));
        ___qtablewidgetitem31 = self.carUnlocksTable.verticalHeaderItem(29)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Mitsubishi 3000GT", None));
        ___qtablewidgetitem32 = self.carUnlocksTable.verticalHeaderItem(30)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Mitsubishi Eclipse GSX", None));
        ___qtablewidgetitem33 = self.carUnlocksTable.verticalHeaderItem(31)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Mitsubishi FTO", None));
        ___qtablewidgetitem34 = self.carUnlocksTable.verticalHeaderItem(32)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Mitsubishi Lancer Evolution VI", None));
        ___qtablewidgetitem35 = self.carUnlocksTable.verticalHeaderItem(33)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Mitsubishi Lancer Evolution VIII", None));
        ___qtablewidgetitem36 = self.carUnlocksTable.verticalHeaderItem(34)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Nissan 300Z", None));
        ___qtablewidgetitem37 = self.carUnlocksTable.verticalHeaderItem(35)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Nissan 350Z", None));
        ___qtablewidgetitem38 = self.carUnlocksTable.verticalHeaderItem(36)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Nissan Skyline GT-R", None));
        ___qtablewidgetitem39 = self.carUnlocksTable.verticalHeaderItem(37)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Peugeot 206 GTI", None));
        ___qtablewidgetitem40 = self.carUnlocksTable.verticalHeaderItem(38)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Pontiac Firebird", None));
        ___qtablewidgetitem41 = self.carUnlocksTable.verticalHeaderItem(39)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Renault Clio Sport 2.0 16V", None));
        ___qtablewidgetitem42 = self.carUnlocksTable.verticalHeaderItem(40)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Subaru Impreza 22B STi", None));
        ___qtablewidgetitem43 = self.carUnlocksTable.verticalHeaderItem(41)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Subaru Impreza WRX STi", None));
        ___qtablewidgetitem44 = self.carUnlocksTable.verticalHeaderItem(42)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Toyota Celica SS-I", None));
        ___qtablewidgetitem45 = self.carUnlocksTable.verticalHeaderItem(43)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Toyota Celica SS-II", None));
        ___qtablewidgetitem46 = self.carUnlocksTable.verticalHeaderItem(44)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Toyota Corolla 1.6", None));
        ___qtablewidgetitem47 = self.carUnlocksTable.verticalHeaderItem(45)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Toyota MR2", None));
        ___qtablewidgetitem48 = self.carUnlocksTable.verticalHeaderItem(46)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Toyota MR-S", None));
        ___qtablewidgetitem49 = self.carUnlocksTable.verticalHeaderItem(47)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Toyota Supra", None));
        ___qtablewidgetitem50 = self.carUnlocksTable.verticalHeaderItem(48)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Vauxhall Corsa Sri 1.8i 16V", None));
        ___qtablewidgetitem51 = self.carUnlocksTable.verticalHeaderItem(49)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Volkswagen Beetle GLS 1.8T", None));
        ___qtablewidgetitem52 = self.carUnlocksTable.verticalHeaderItem(50)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Volkswagen Corrado VR6", None));
        ___qtablewidgetitem53 = self.carUnlocksTable.verticalHeaderItem(51)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("JECarUnlocksDialog", u"Volkswagen Golf MkIV", None));

        __sortingEnabled = self.carUnlocksTable.isSortingEnabled()
        self.carUnlocksTable.setSortingEnabled(False)
        self.carUnlocksTable.setSortingEnabled(__sortingEnabled)

    # retranslateUi

