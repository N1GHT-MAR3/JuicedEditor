# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'JEMain.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_JEMainWindow(object):
    def setupUi(self, JEMainWindow):
        if not JEMainWindow.objectName():
            JEMainWindow.setObjectName(u"JEMainWindow")
        JEMainWindow.resize(500, 460)
        JEMainWindow.setMinimumSize(QSize(500, 460))
        JEMainWindow.setMaximumSize(QSize(500, 500))
        icon = QIcon()
        icon.addFile(u"Juiced_32px.png", QSize(), QIcon.Normal, QIcon.Off)
        JEMainWindow.setWindowIcon(icon)
        JEMainWindow.setIconSize(QSize(24, 24))
        JEMainWindow.setDocumentMode(False)
        JEMainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionOpen = QAction(JEMainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(JEMainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave.setEnabled(False)
        self.actionSaveAs = QAction(JEMainWindow)
        self.actionSaveAs.setObjectName(u"actionSaveAs")
        self.actionSaveAs.setEnabled(False)
        self.actionAbout = QAction(JEMainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionCheckVersion = QAction(JEMainWindow)
        self.actionCheckVersion.setObjectName(u"actionCheckVersion")
        self.centralwidget = QWidget(JEMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.Info = QGroupBox(self.centralwidget)
        self.Info.setObjectName(u"Info")
        self.Info.setGeometry(QRect(0, 0, 500, 100))
        self.Info.setFlat(True)
        self.InfoHeader = QLabel(self.Info)
        self.InfoHeader.setObjectName(u"InfoHeader")
        self.InfoHeader.setGeometry(QRect(10, 10, 50, 20))
        self.InfoExeType = QLabel(self.Info)
        self.InfoExeType.setObjectName(u"InfoExeType")
        self.InfoExeType.setGeometry(QRect(10, 30, 240, 20))
        self.InfoExePath = QLineEdit(self.Info)
        self.InfoExePath.setObjectName(u"InfoExePath")
        self.InfoExePath.setEnabled(False)
        self.InfoExePath.setGeometry(QRect(10, 50, 240, 20))
        self.InfoExePath.setReadOnly(True)
        self.InfoExeSize = QLabel(self.Info)
        self.InfoExeSize.setObjectName(u"InfoExeSize")
        self.InfoExeSize.setGeometry(QRect(10, 70, 240, 20))
        self.InfoDecrypt = QLabel(self.Info)
        self.InfoDecrypt.setObjectName(u"InfoDecrypt")
        self.InfoDecrypt.setGeometry(QRect(270, 30, 81, 20))
        self.InfoServerPatch = QLabel(self.Info)
        self.InfoServerPatch.setObjectName(u"InfoServerPatch")
        self.InfoServerPatch.setGeometry(QRect(270, 70, 100, 20))
        self.InfoServerPatchButton = QPushButton(self.Info)
        self.InfoServerPatchButton.setObjectName(u"InfoServerPatchButton")
        self.InfoServerPatchButton.setEnabled(False)
        self.InfoServerPatchButton.setGeometry(QRect(400, 70, 90, 20))
        self.InfoDecryptStatus = QLabel(self.Info)
        self.InfoDecryptStatus.setObjectName(u"InfoDecryptStatus")
        self.InfoDecryptStatus.setGeometry(QRect(370, 30, 20, 20))
        self.InfoDecryptStatus.setStyleSheet(u"color: blue;")
        self.InfoServerPatchStatus = QLabel(self.Info)
        self.InfoServerPatchStatus.setObjectName(u"InfoServerPatchStatus")
        self.InfoServerPatchStatus.setGeometry(QRect(370, 70, 20, 20))
        self.InfoServerPatchStatus.setStyleSheet(u"color: red;")
        self.actionGitHub = QPushButton(self.Info)
        self.actionGitHub.setObjectName(u"actionGitHub")
        self.actionGitHub.setGeometry(QRect(480, 0, 20, 20))
        icon1 = QIcon()
        icon1.addFile(u"../../../Pictures/Icons/GitHub_16px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionGitHub.setIcon(icon1)
        self.actionGitHub.setFlat(True)
        self.actionDiscord = QPushButton(self.Info)
        self.actionDiscord.setObjectName(u"actionDiscord")
        self.actionDiscord.setGeometry(QRect(460, 0, 20, 20))
        icon2 = QIcon()
        icon2.addFile(u"../../../Pictures/Icons/Discord_16px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDiscord.setIcon(icon2)
        self.actionDiscord.setFlat(True)
        self.InfoVersion = QLabel(self.Info)
        self.InfoVersion.setObjectName(u"InfoVersion")
        self.InfoVersion.setGeometry(QRect(270, 50, 100, 20))
        self.InfoVersionStatus = QLabel(self.Info)
        self.InfoVersionStatus.setObjectName(u"InfoVersionStatus")
        self.InfoVersionStatus.setGeometry(QRect(370, 50, 121, 20))
        self.InfoVersionStatus.setStyleSheet(u"")
        self.expert = QGroupBox(self.centralwidget)
        self.expert.setObjectName(u"expert")
        self.expert.setGeometry(QRect(0, 360, 500, 60))
        self.expert.setFlat(True)
        self.expert.setCheckable(False)
        self.expertHeader = QLabel(self.expert)
        self.expertHeader.setObjectName(u"expertHeader")
        self.expertHeader.setGeometry(QRect(10, 10, 110, 20))
        self.expertDummy = QLabel(self.expert)
        self.expertDummy.setObjectName(u"expertDummy")
        self.expertDummy.setGeometry(QRect(10, 30, 100, 20))
        self.expertDummyCheckbox = QCheckBox(self.expert)
        self.expertDummyCheckbox.setObjectName(u"expertDummyCheckbox")
        self.expertDummyCheckbox.setEnabled(False)
        self.expertDummyCheckbox.setGeometry(QRect(110, 30, 20, 20))
        self.cheat = QGroupBox(self.centralwidget)
        self.cheat.setObjectName(u"cheat")
        self.cheat.setGeometry(QRect(0, 100, 500, 190))
        self.cheat.setFlat(True)
        self.cheatHeader = QLabel(self.cheat)
        self.cheatHeader.setObjectName(u"cheatHeader")
        self.cheatHeader.setGeometry(QRect(10, 10, 40, 20))
        self.cheatPINT = QLabel(self.cheat)
        self.cheatPINT.setObjectName(u"cheatPINT")
        self.cheatPINT.setGeometry(QRect(10, 30, 155, 20))
        self.cheatDOSH = QLabel(self.cheat)
        self.cheatDOSH.setObjectName(u"cheatDOSH")
        self.cheatDOSH.setGeometry(QRect(10, 50, 155, 20))
        self.cheatRESP = QLabel(self.cheat)
        self.cheatRESP.setObjectName(u"cheatRESP")
        self.cheatRESP.setGeometry(QRect(10, 70, 155, 20))
        self.cheatCARS = QLabel(self.cheat)
        self.cheatCARS.setObjectName(u"cheatCARS")
        self.cheatCARS.setGeometry(QRect(10, 90, 155, 20))
        self.cheatCREW = QLabel(self.cheat)
        self.cheatCREW.setObjectName(u"cheatCREW")
        self.cheatCREW.setGeometry(QRect(10, 110, 155, 20))
        self.cheatWIN = QLabel(self.cheat)
        self.cheatWIN.setObjectName(u"cheatWIN")
        self.cheatWIN.setGeometry(QRect(10, 150, 155, 20))
        self.cheatALL = QLabel(self.cheat)
        self.cheatALL.setObjectName(u"cheatALL")
        self.cheatALL.setGeometry(QRect(10, 170, 155, 20))
        self.cheatPINTCheckbox = QCheckBox(self.cheat)
        self.cheatPINTCheckbox.setObjectName(u"cheatPINTCheckbox")
        self.cheatPINTCheckbox.setEnabled(False)
        self.cheatPINTCheckbox.setGeometry(QRect(420, 30, 70, 20))
        self.cheatPINTCheckbox.setCheckable(True)
        self.cheatDOSHCheckbox = QCheckBox(self.cheat)
        self.cheatDOSHCheckbox.setObjectName(u"cheatDOSHCheckbox")
        self.cheatDOSHCheckbox.setEnabled(False)
        self.cheatDOSHCheckbox.setGeometry(QRect(420, 50, 70, 20))
        self.cheatDOSHCheckbox.setCheckable(True)
        self.cheatRESPCheckbox = QCheckBox(self.cheat)
        self.cheatRESPCheckbox.setObjectName(u"cheatRESPCheckbox")
        self.cheatRESPCheckbox.setEnabled(False)
        self.cheatRESPCheckbox.setGeometry(QRect(420, 70, 70, 20))
        self.cheatRESPCheckbox.setCheckable(True)
        self.cheatCARSCheckbox = QCheckBox(self.cheat)
        self.cheatCARSCheckbox.setObjectName(u"cheatCARSCheckbox")
        self.cheatCARSCheckbox.setEnabled(False)
        self.cheatCARSCheckbox.setGeometry(QRect(420, 90, 70, 20))
        self.cheatCARSCheckbox.setCheckable(True)
        self.cheatCREWCheckbox = QCheckBox(self.cheat)
        self.cheatCREWCheckbox.setObjectName(u"cheatCREWCheckbox")
        self.cheatCREWCheckbox.setEnabled(False)
        self.cheatCREWCheckbox.setGeometry(QRect(420, 110, 70, 20))
        self.cheatCREWCheckbox.setCheckable(True)
        self.cheatWINCheckbox = QCheckBox(self.cheat)
        self.cheatWINCheckbox.setObjectName(u"cheatWINCheckbox")
        self.cheatWINCheckbox.setEnabled(False)
        self.cheatWINCheckbox.setGeometry(QRect(420, 150, 70, 20))
        self.cheatWINCheckbox.setCheckable(True)
        self.cheatALLCheckbox = QCheckBox(self.cheat)
        self.cheatALLCheckbox.setObjectName(u"cheatALLCheckbox")
        self.cheatALLCheckbox.setEnabled(False)
        self.cheatALLCheckbox.setGeometry(QRect(420, 170, 70, 20))
        self.cheatALLCheckbox.setCheckable(True)
        self.cheatDOSHValue = QSpinBox(self.cheat)
        self.cheatDOSHValue.setObjectName(u"cheatDOSHValue")
        self.cheatDOSHValue.setEnabled(False)
        self.cheatDOSHValue.setGeometry(QRect(290, 50, 120, 20))
        font = QFont()
        font.setFamily(u"Courier New")
        self.cheatDOSHValue.setFont(font)
        self.cheatDOSHValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.cheatDOSHValue.setProperty("showGroupSeparator", True)
        self.cheatDOSHValue.setMaximum(2147483647)
        self.cheatDOSHValue.setSingleStep(1)
        self.cheatDOSHValue.setStepType(QAbstractSpinBox.DefaultStepType)
        self.cheatDOSHValue.setValue(2147483647)
        self.cheatRESPValue = QSpinBox(self.cheat)
        self.cheatRESPValue.setObjectName(u"cheatRESPValue")
        self.cheatRESPValue.setEnabled(False)
        self.cheatRESPValue.setGeometry(QRect(290, 70, 120, 20))
        self.cheatRESPValue.setFont(font)
        self.cheatRESPValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.cheatRESPValue.setProperty("showGroupSeparator", True)
        self.cheatRESPValue.setMaximum(2147483647)
        self.cheatRESPValue.setSingleStep(1)
        self.cheatRESPValue.setStepType(QAbstractSpinBox.DefaultStepType)
        self.cheatRESPValue.setValue(2147483647)
        self.cheatCHAR = QLabel(self.cheat)
        self.cheatCHAR.setObjectName(u"cheatCHAR")
        self.cheatCHAR.setGeometry(QRect(10, 130, 155, 20))
        self.cheatCHARCheckbox = QCheckBox(self.cheat)
        self.cheatCHARCheckbox.setObjectName(u"cheatCHARCheckbox")
        self.cheatCHARCheckbox.setEnabled(False)
        self.cheatCHARCheckbox.setGeometry(QRect(420, 130, 70, 20))
        self.cheatCHARCheckbox.setCheckable(True)
        self.cheatPINTCode = QLineEdit(self.cheat)
        self.cheatPINTCode.setObjectName(u"cheatPINTCode")
        self.cheatPINTCode.setEnabled(False)
        self.cheatPINTCode.setGeometry(QRect(160, 30, 120, 20))
        font1 = QFont()
        font1.setFamily(u"Courier")
        self.cheatPINTCode.setFont(font1)
        self.cheatPINTCode.setMaxLength(4)
        self.cheatPINTCode.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.cheatDOSHCode = QLineEdit(self.cheat)
        self.cheatDOSHCode.setObjectName(u"cheatDOSHCode")
        self.cheatDOSHCode.setEnabled(False)
        self.cheatDOSHCode.setGeometry(QRect(160, 50, 120, 20))
        self.cheatDOSHCode.setFont(font1)
        self.cheatDOSHCode.setMaxLength(4)
        self.cheatDOSHCode.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.cheatRESPCode = QLineEdit(self.cheat)
        self.cheatRESPCode.setObjectName(u"cheatRESPCode")
        self.cheatRESPCode.setEnabled(False)
        self.cheatRESPCode.setGeometry(QRect(160, 70, 120, 20))
        self.cheatRESPCode.setFont(font1)
        self.cheatRESPCode.setMaxLength(4)
        self.cheatRESPCode.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.cheatCARSCode = QLineEdit(self.cheat)
        self.cheatCARSCode.setObjectName(u"cheatCARSCode")
        self.cheatCARSCode.setEnabled(False)
        self.cheatCARSCode.setGeometry(QRect(160, 90, 120, 20))
        self.cheatCARSCode.setFont(font1)
        self.cheatCARSCode.setMaxLength(4)
        self.cheatCARSCode.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.cheatCREWCode = QLineEdit(self.cheat)
        self.cheatCREWCode.setObjectName(u"cheatCREWCode")
        self.cheatCREWCode.setEnabled(False)
        self.cheatCREWCode.setGeometry(QRect(160, 110, 120, 20))
        self.cheatCREWCode.setFont(font1)
        self.cheatCREWCode.setMaxLength(4)
        self.cheatCREWCode.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.cheatCHARCode = QLineEdit(self.cheat)
        self.cheatCHARCode.setObjectName(u"cheatCHARCode")
        self.cheatCHARCode.setEnabled(False)
        self.cheatCHARCode.setGeometry(QRect(160, 130, 120, 20))
        self.cheatCHARCode.setFont(font1)
        self.cheatCHARCode.setMaxLength(4)
        self.cheatCHARCode.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.cheatWINCode = QLineEdit(self.cheat)
        self.cheatWINCode.setObjectName(u"cheatWINCode")
        self.cheatWINCode.setEnabled(False)
        self.cheatWINCode.setGeometry(QRect(160, 150, 120, 20))
        self.cheatWINCode.setFont(font1)
        self.cheatWINCode.setMaxLength(4)
        self.cheatWINCode.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.cheatALLCode = QLineEdit(self.cheat)
        self.cheatALLCode.setObjectName(u"cheatALLCode")
        self.cheatALLCode.setEnabled(False)
        self.cheatALLCode.setGeometry(QRect(160, 170, 120, 20))
        self.cheatALLCode.setFont(font1)
        self.cheatALLCode.setMaxLength(4)
        self.cheatALLCode.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.mods = QGroupBox(self.centralwidget)
        self.mods.setObjectName(u"mods")
        self.mods.setGeometry(QRect(0, 300, 500, 60))
        self.mods.setFlat(True)
        self.mods.setCheckable(False)
        self.modsHeader = QLabel(self.mods)
        self.modsHeader.setObjectName(u"modsHeader")
        self.modsHeader.setGeometry(QRect(10, 10, 110, 20))
        self.modsCarUnlockButton = QToolButton(self.mods)
        self.modsCarUnlockButton.setObjectName(u"modsCarUnlockButton")
        self.modsCarUnlockButton.setEnabled(False)
        self.modsCarUnlockButton.setGeometry(QRect(10, 30, 80, 20))
        JEMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(JEMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 500, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        JEMainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(JEMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(False)
        self.statusbar.setStyleSheet(u"")
        self.statusbar.setSizeGripEnabled(False)
        JEMainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.InfoExePath, self.InfoServerPatchButton)
        QWidget.setTabOrder(self.InfoServerPatchButton, self.cheatDOSHValue)
        QWidget.setTabOrder(self.cheatDOSHValue, self.cheatRESPValue)
        QWidget.setTabOrder(self.cheatRESPValue, self.cheatPINTCheckbox)
        QWidget.setTabOrder(self.cheatPINTCheckbox, self.cheatDOSHCheckbox)
        QWidget.setTabOrder(self.cheatDOSHCheckbox, self.cheatRESPCheckbox)
        QWidget.setTabOrder(self.cheatRESPCheckbox, self.cheatCARSCheckbox)
        QWidget.setTabOrder(self.cheatCARSCheckbox, self.cheatCREWCheckbox)
        QWidget.setTabOrder(self.cheatCREWCheckbox, self.cheatCHARCheckbox)
        QWidget.setTabOrder(self.cheatCHARCheckbox, self.cheatWINCheckbox)
        QWidget.setTabOrder(self.cheatWINCheckbox, self.cheatALLCheckbox)
        QWidget.setTabOrder(self.cheatALLCheckbox, self.modsCarUnlockButton)
        QWidget.setTabOrder(self.modsCarUnlockButton, self.actionDiscord)
        QWidget.setTabOrder(self.actionDiscord, self.actionGitHub)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionCheckVersion)

        self.retranslateUi(JEMainWindow)

        QMetaObject.connectSlotsByName(JEMainWindow)
    # setupUi

    def retranslateUi(self, JEMainWindow):
        JEMainWindow.setWindowTitle(QCoreApplication.translate("JEMainWindow", u"Juiced Editor", None))
        self.actionOpen.setText(QCoreApplication.translate("JEMainWindow", u"Open...", None))
        self.actionSave.setText(QCoreApplication.translate("JEMainWindow", u"Save", None))
        self.actionSaveAs.setText(QCoreApplication.translate("JEMainWindow", u"Save As...", None))
        self.actionAbout.setText(QCoreApplication.translate("JEMainWindow", u"About...", None))
        self.actionCheckVersion.setText(QCoreApplication.translate("JEMainWindow", u"Check for updates", None))
        self.Info.setTitle("")
        self.InfoHeader.setText(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Info</span></p></body></html>", None))
        self.InfoExeType.setText(QCoreApplication.translate("JEMainWindow", u"Juiced.exe (unpatched)", None))
        self.InfoExePath.setText(QCoreApplication.translate("JEMainWindow", u"C:\\Program Files (x86)\\THQ\\Juiced", None))
        self.InfoExeSize.setText(QCoreApplication.translate("JEMainWindow", u"12,560,384 bytes", None))
#if QT_CONFIG(tooltip)
        self.InfoDecrypt.setToolTip(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Whether or not the game's code is decrypted. Some options are only available with decrypted executables.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.InfoDecrypt.setText(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Decrypted:<span style=\" font-size:11pt; font-weight:700; color:#0055ff; vertical-align:super;\">[?]</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.InfoServerPatch.setToolTip(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Whether or not the OpenSpy servers have been patched in. This allows for online functionality to be restored.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.InfoServerPatch.setText(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Servers patched:<span style=\" font-size:11pt; font-weight:700; color:#0055ff; vertical-align:super;\">[?]</span></p></body></html>", None))
        self.InfoServerPatchButton.setText(QCoreApplication.translate("JEMainWindow", u"Patch Servers", None))
        self.InfoDecryptStatus.setText(QCoreApplication.translate("JEMainWindow", u"Yes", None))
        self.InfoServerPatchStatus.setText(QCoreApplication.translate("JEMainWindow", u"No", None))
        self.actionGitHub.setText("")
        self.actionDiscord.setText("")
#if QT_CONFIG(tooltip)
        self.InfoVersion.setToolTip(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Which version of the game this .exe is.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.InfoVersion.setText(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Version:<span style=\" font-size:11pt; font-weight:696; color:#0055ff; vertical-align:super;\">[?]</span></p></body></html>", None))
        self.InfoVersionStatus.setText(QCoreApplication.translate("JEMainWindow", u"Unknown", None))
        self.expert.setTitle("")
        self.expertHeader.setText(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">ONLY FOR EXPERTS</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.expertDummy.setToolTip(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Changes the reference to carmodels.dat in the executable to dummyfile.dat, allowing the game to run with carmodels.dat unpacked.</p><p>If you don't know what this does, do not apply this patch.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.expertDummy.setText(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>dummyfile.dat:<span style=\" font-size:11pt; font-weight:700; color:#0055ff; vertical-align:super;\">[?]</span></p></body></html>", None))
        self.expertDummyCheckbox.setText("")
        self.cheat.setTitle("")
        self.cheatHeader.setText(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Cheats</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.cheatPINT.setToolTip(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Unlocks all Arcade races, and all cars/tracks in Custom Race, except for prototype cars.</p><p>Default code is PINT (or PING in certain versions.)</p><p>Enabled by default.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cheatPINT.setText(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>All arcade/custom unlocks<span style=\" font-size:11pt; font-weight:700; color:#0055ff; vertical-align:super;\">[?]</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.cheatDOSH.setToolTip(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Sets your cash in Career mode to a specified amount ($10,000,000 by default).</p><p>Default code is DOSH.</p><p>Disabled by default.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cheatDOSH.setText(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Money<span style=\" font-size:11pt; font-weight:700; color:#0055ff; vertical-align:super;\">[?]</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.cheatRESP.setToolTip(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Sets your respect with all crew members to the specified amount (2,000 by default), and unlocks all corresponding privileges.</p><p>Default code is RESP.</p><p>Disabled by default.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cheatRESP.setText(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Respect<span style=\" font-size:11pt; font-weight:700; color:#0055ff; vertical-align:super;\">[?]</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.cheatCARS.setToolTip(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Unlocks all cars in the dealership at the turn of the month, all upgrades, and adds one of every car to your garage.</p><p>Default code is CARS.</p><p>Disabled by default.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cheatCARS.setText(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Unlock all cars/upgrades<span style=\" font-size:11pt; font-weight:700; color:#0055ff; vertical-align:super;\">[?]</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.cheatCREW.setToolTip(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Adds Vito, Amber, and Chief to your crew.</p><p>Default code is CREW.</p><p>Disabled by default.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cheatCREW.setText(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Unlock all crew members<span style=\" font-size:11pt; font-weight:700; color:#0055ff; vertical-align:super;\">[?]</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.cheatWIN.setToolTip(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>You are scored as the winner of all races, regardless of race results, until the game is restarted.</p><p>Does not work online.</p><p>Default code is WIN.</p><p>Disabled by default.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cheatWIN.setText(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Win all (most) races<span style=\" font-size:11pt; font-weight:700; color:#0055ff; vertical-align:super;\">[?]</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.cheatALL.setToolTip(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Activates PINT, DOSH, RESP, CARS, and CREW.</p><p>Does not activate CHAR or WIN.</p><p>Default code is ALL.</p><p>Disabled by default.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cheatALL.setText(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Activate all (most) cheats<span style=\" font-size:11pt; font-weight:700; color:#0055ff; vertical-align:super;\">[?]</span></p></body></html>", None))
        self.cheatPINTCheckbox.setText(QCoreApplication.translate("JEMainWindow", u"Enabled", None))
        self.cheatDOSHCheckbox.setText(QCoreApplication.translate("JEMainWindow", u"Enabled", None))
        self.cheatRESPCheckbox.setText(QCoreApplication.translate("JEMainWindow", u"Enabled", None))
        self.cheatCARSCheckbox.setText(QCoreApplication.translate("JEMainWindow", u"Enabled", None))
        self.cheatCREWCheckbox.setText(QCoreApplication.translate("JEMainWindow", u"Enabled", None))
        self.cheatWINCheckbox.setText(QCoreApplication.translate("JEMainWindow", u"Enabled", None))
        self.cheatALLCheckbox.setText(QCoreApplication.translate("JEMainWindow", u"Enabled", None))
        self.cheatDOSHValue.setPrefix(QCoreApplication.translate("JEMainWindow", u"$", None))
        self.cheatRESPValue.setPrefix("")
#if QT_CONFIG(tooltip)
        self.cheatCHAR.setToolTip(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Activates a debug test menu whenever entering any talking head scene (e.x. betting against another driver). This allows you to preview all of their lines.</p><p>There is no way to exit this screen once entered. You must close the game afterwards.</p><p>Default code is CHAR.</p><p>Disabled by default.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cheatCHAR.setText(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Character test<span style=\" font-size:11pt; font-weight:700; color:#0055ff; vertical-align:super;\">[?]</span></p></body></html>", None))
        self.cheatCHARCheckbox.setText(QCoreApplication.translate("JEMainWindow", u"Enabled", None))
        self.cheatPINTCode.setText(QCoreApplication.translate("JEMainWindow", u"PINT", None))
        self.cheatDOSHCode.setText(QCoreApplication.translate("JEMainWindow", u"DOSH", None))
        self.cheatRESPCode.setText(QCoreApplication.translate("JEMainWindow", u"RESP", None))
        self.cheatCARSCode.setText(QCoreApplication.translate("JEMainWindow", u"CARS", None))
        self.cheatCREWCode.setText(QCoreApplication.translate("JEMainWindow", u"CREW", None))
        self.cheatCHARCode.setText(QCoreApplication.translate("JEMainWindow", u"CHAR", None))
        self.cheatWINCode.setText(QCoreApplication.translate("JEMainWindow", u"WIN.", None))
        self.cheatALLCode.setText(QCoreApplication.translate("JEMainWindow", u"ALL.", None))
        self.mods.setTitle("")
        self.modsHeader.setText(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Modifications</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.modsCarUnlockButton.setToolTip(QCoreApplication.translate("JEMainWindow", u"<html><head/><body><p>Allows you to change when cars are unlocked in Career mode.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.modsCarUnlockButton.setText(QCoreApplication.translate("JEMainWindow", u"Car Unlocks...", None))
        self.menuFile.setTitle(QCoreApplication.translate("JEMainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("JEMainWindow", u"Help", None))
    # retranslateUi

