# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'JEAbout.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QWidget)

class Ui_JEAboutDialog(object):
    def setupUi(self, JEAboutDialog):
        if not JEAboutDialog.objectName():
            JEAboutDialog.setObjectName(u"JEAboutDialog")
        JEAboutDialog.resize(400, 400)
        self.aboutText = QLabel(JEAboutDialog)
        self.aboutText.setObjectName(u"aboutText")
        self.aboutText.setGeometry(QRect(0, 0, 400, 400))
        self.aboutText.setOpenExternalLinks(True)

        self.retranslateUi(JEAboutDialog)

        QMetaObject.connectSlotsByName(JEAboutDialog)
    # setupUi

    def retranslateUi(self, JEAboutDialog):
        JEAboutDialog.setWindowTitle(QCoreApplication.translate("JEAboutDialog", u"About", None))
        self.aboutText.setText(QCoreApplication.translate("JEAboutDialog", u"<html><head/><body><p align=\"center\"><a href=\"https://github.com/N1GHT-MAR3/JuicedEditor\"><span style=\" font-weight:700; text-decoration: underline; color:#0000ff;\">Juiced Editor</span></a><span style=\" font-style:italic;\"> (Pre-release 6)<br/>by </span>N1GHTMAR3</p><p align=\"center\">Courtesy of the <a href=\"https://discord.gg/pu2jdxR\"><span style=\" text-decoration: underline; color:#0000ff;\">Juiced Modding Discord<br/></span></a>(if you need any help, come ask here!)</p><p align=\"center\"><span style=\" font-weight:700; text-decoration: underline;\">Modules used</span><span style=\" text-decoration: underline;\"><br/></span><a href=\"https://wiki.qt.io/Qt_for_Python\"><span style=\" text-decoration: underline; color:#0000ff;\">PySide6</span></a><br/><a href=\"https://pyinstaller.org/\"><span style=\" text-decoration: underline; color:#0000ff;\">PyInstaller</span></a><br/><a href=\"https://github.com/brentvollebregt/auto-py-to-exe\"><span style=\" text-decoration: underline; color:#0000ff;\">Aut"
                        "o PY to EXE</span></a></p><p align=\"center\"><span style=\" font-weight:700; text-decoration: underline;\">Special thanks</span><span style=\" text-decoration: underline;\"><br/></span><span style=\" font-weight:700;\">Bomb Bloke</span>: for unswizzling console textures with your DDT converter<span style=\" text-decoration: underline;\"><br/></span><span style=\" font-weight:700;\">Ekey</span>: for opening the floodgates with your <a href=\"https://github.com/Ekey/JCED.DAT.Tool/\"><span style=\" text-decoration: underline; color:#0000ff;\">unpacker</span></a><br/><span style=\" font-weight:700;\">GrimMaple</span>: for making the game playable with <a href=\"https://github.com/GrimMaple/JuicedFixes\"><span style=\" text-decoration: underline; color:#0000ff;\">JuicedFixes</span></a><br/><span style=\" font-weight:700;\">mariokart64n</span>: for JATool, your 3ds Max knowledge, and everything else<br/><span style=\" font-weight:700;\">Martin_SW</span>: for laying the groundwork of the modding scene<br/>The <span "
                        "style=\" font-weight:700;\">OpenSpy</span> team: for <a href=\"http://beta.openspy.net/en/\"><span style=\" text-decoration: underline; color:#0000ff;\">making online play possible</span></a><br/><span style=\" font-weight:700;\">RedCarDriver</span>: for your gameplay overhauls and overall knowledge<br/><span style=\" font-weight:700;\">SxnnyB</span>: for your overarching knowledge, research, and consultation<br/><span style=\" font-weight:700;\">4ernobill</span>, <span style=\" font-weight:700;\">Eagle</span>, <span style=\" font-weight:700;\">LotusEliseBoy</span>, <span style=\" font-weight:700;\">TFP</span>, <span style=\" font-weight:700;\">ZA-7</span>:<br/>for all your contributions to the scene</p><p align=\"center\">...and everyone else that's helped keep this game alive!</p></body></html>", None))
    # retranslateUi

