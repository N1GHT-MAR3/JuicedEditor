'''
Juiced Editor
by N1GHTMAR3

Version 1
released 2022-10-01

https://github.com/N1GHT-MAR3/JuicedEditor
'''

# Allows images to properly display while running as an .exe.
# Credit to max on StackOverflow for this. (https://stackoverflow.com/a/13790741)
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = path.abspath(".")

    return path.join(base_path, relative_path)

# The version number of this build of Juiced Editor.
version = 8

# Imports PySide2 modules used to display the GUI.
from PySide2 import QtCore, QtGui, QtWidgets
# Imports the main window UI files from JEMain.py.
from JEMain import Ui_JEMainWindow
# Imports the car unlock window UI files from JECarUnlocks.py.
from JECarUnlocks import Ui_JECarUnlocksWindow
# Imports the about dialog UI files from JEAbout.py.
from JEAbout import Ui_JEAboutDialog
# Imports the file dialog seen when opening a file.
from PySide2.QtWidgets import QFileDialog
# Imports a function used to get a Windows directory.
from os import getcwd, path
# Imports functions required to convert bytes to and from floats.
import struct
# Imports functions allowing the editor to open links.
import webbrowser
# Imports functions allowing the editor to read from web links.
import urllib.request


# Sets up the main window UI.
class JEMainWindow(QtWidgets.QMainWindow, Ui_JEMainWindow):
    def __init__(self):
        super(JEMainWindow, self).__init__()
        self.setupUi(self)

        # Check for a new version on startup.
        self.checkVersion()

        # Initialize the variable for the last used path.
        self.lastPath = ""

        # Sets up the Juiced icon.
        global juicedIcon
        juicedIcon = QtGui.QIcon()
        juicedIcon.addPixmap(QtGui.QPixmap(resource_path("./Juiced_32px.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(juicedIcon)
        # Sets up the Discord icon.
        discordIcon = QtGui.QIcon()
        discordIcon.addPixmap(QtGui.QPixmap(resource_path("./Discord_16px.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionDiscord.setIcon(discordIcon)
        # Sets up the GitHub icon.
        gitHubIcon = QtGui.QIcon()
        gitHubIcon.addPixmap(QtGui.QPixmap(resource_path("./GitHub_16px.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionGitHub.setIcon(gitHubIcon)
        # Move the Discord and GitHub buttons to the menu bar here, since you can't do that in Qt Designer for some reason.
        self.actionDiscord.setParent(self.menubar)
        self.actionDiscord.move(460, 1)
        self.actionGitHub.setParent(self.menubar)
        self.actionGitHub.move(480, 1)

        # Initializes startup text to make things easier for me in Qt Designer
        self.InfoExeType.setText("No .exe loaded")
        self.InfoExePath.setText("")
        self.InfoExeSize.setText("")
        self.InfoDecryptStatus.setText("")
        self.InfoDecryptStatus.setStyleSheet("color: black;")
        self.InfoVersionStatus.setText("")
        self.InfoServerPatchStatus.setText("")
        self.InfoServerPatchStatus.setStyleSheet("color: black;")
        self.cheatDOSHValue.setValue(10000000)
        self.cheatRESPValue.setValue(2000)

        # Runs openExe() when File -> Open... is clicked
        self.actionOpen.triggered.connect(self.openExe)

        # Runs openAbout() when Help -> About... is clicked
        self.actionAbout.triggered.connect(self.openAbout)

        # Runs checkVersion() when About -> Check for updates is clicked
        self.actionCheckVersion.triggered.connect(self.checkVersion)

        # Runs openDiscord() when the Discord button is clicked
        self.actionDiscord.clicked.connect(self.openDiscord)

        # Runs openGitHub() when the GitHub button is clicked
        self.actionGitHub.clicked.connect(self.openGitHub)

        # Runs patchServers() when Patch Servers is clicked
        self.InfoServerPatchButton.clicked.connect(self.patchServers)
        
        # Runs toggle<cheat>() when the respective checkbox is clicked
        self.cheatPINTCheckbox.stateChanged.connect(self.togglePINT)
        self.cheatDOSHCheckbox.stateChanged.connect(self.toggleDOSH)
        self.cheatRESPCheckbox.stateChanged.connect(self.toggleRESP)
        self.cheatCARSCheckbox.stateChanged.connect(self.toggleCARS)
        self.cheatCREWCheckbox.stateChanged.connect(self.toggleCREW)
        self.cheatCHARCheckbox.stateChanged.connect(self.toggleCHAR)
        self.cheatWINCheckbox.stateChanged.connect(self.toggleWIN)
        self.cheatALLCheckbox.stateChanged.connect(self.toggleALL)

        # Runs showCarUnlocks() when "Car Unlocks..." is clicked
        self.modsCarUnlockButton.clicked.connect(self.showCarUnlocks)

        # Runs saveExe() when File -> Save is clicked
        self.actionSave.triggered.connect(self.saveExe)

        # Runs saveExeAs() when File -> Save As... is clicked
        self.actionSaveAs.triggered.connect(self.saveExeAs)
    
    # Checks against version.txt on GitHub to see if the script is running the latest version.
    def checkVersion(self):
        try:
            cur = int(urllib.request.urlopen("https://raw.githubusercontent.com/N1GHT-MAR3/JuicedEditor/main/version.txt").read())
            if version < cur:
                # If not, ask the user if they want to update.
                update = QtWidgets.QMessageBox.question(self, "Update", "A new version of Juiced Editor is available. Would you like to update?", QtWidgets.QMessageBox.StandardButton.Yes|QtWidgets.QMessageBox.StandardButton.No)
                # If they do, take the user to the releases page of the repo.
                if update == 16384:
                    webbrowser.open("https://github.com/N1GHT-MAR3/JuicedEditor/releases")
                # If they don't, then this will do nothing and continue to Juiced Editor as normal.
            # If checkVersion() was triggered by something (the check for updates button), display a message if Juiced Editor is up to date.
            elif self.sender() != None:
                QtWidgets.QMessageBox.information(self, "Up to date", "You're running the most recent version of Juiced Editor.")
            # If not, silently continue to Juiced Editor.
        # If the current version number cannot be determined...
        except urllib.error.URLError:
            # Show the user an error message if they clicked "Check for updates".
            if self.sender() != None:
                QtWidgets.QMessageBox.critical(self, "Error", "Could not determine the most recent version. Check your internet connection.")
            # If not, silently continue to Juiced Editor.
    
    def openAbout(self):
        JEA.show()

    # Links to the Juiced Modding Discord server.
    def openDiscord(self):
        webbrowser.open("https://discord.gg/pu2jdxR")
    
    # Links to the Juiced Editor GitHub page.
    def openGitHub(self):
        webbrowser.open("https://github.com/N1GHT-MAR3/JuicedEditor")

    # Opens Juiced.exe where specified.
    def openExe(self):
        global exe_bytes
        global decrypted
        global exePath
        global exe_type
        global exeVer
        global locCheats
        global locDOSH
        global locRESP
        global locCarUnlocks
        global carUnlocks
        global locModels
        global indexDict

        # Check if a path has already been logged.
        if self.lastPath != "":
            # If there is, open a file dialog asking the user to locate the Juiced executable, using the last used path as a starting point.
            exeTempPath = QFileDialog.getOpenFileName(self, "Open...", self.lastPath, "Executable files (*.exe)")[0]
        # If not, open a file dialog asking the user to locate Juiced.exe, using the current working directory as a starting point.
        else:
            exeTempPath = QFileDialog.getOpenFileName(self, "Open...", getcwd(), "Executable files (*.exe)")[0]
        # Try to open the .exe at the path provided by the user in the file dialog.
        product_name_bytes = b"\x4A\x00\x75\x00\x69\x00\x63\x00\x65\x00\x64\x00\x20\x00\x50\x00\x43\x00\x20\x00\x47\x00\x61\x00\x6D\x00\x65"
        
        try:
            f = open(exeTempPath, "rb")
            exe = f.read()
            # If the product name "Juiced PC Game" (which can be seen in the .exe's Properties) cannot be found in the .exe, most likely, the .exe isn't a valid Juiced executable.
            if product_name_bytes not in exe:
                # If this is the case, create and display a generic error message.
                QtWidgets.QMessageBox.critical(self, "Error", "Load aborted. This does not appear to be a valid Juiced .exe.")
                # Stop loading the .exe.
                return
        # If there is no .exe path (if the user cancels the file dialog), do nothing.
        except FileNotFoundError:
            return
        exePath = exeTempPath
        # Write all of the bytes in the .exe to an array so the editor can process them.
        exe_bytes = bytearray(exe)
        # Closes the .exe so it's not being used. Doesn't need to be until the .exe is saved anyways.
        f.close()
        # Record the file path used to lastPath.
        self.lastPath = exePath[:exePath.rfind("/")]

        '''
        Detects the type of Juiced .exe:
        0 = unknown                 ; if the .exe size does not match any known version
        1 = vanilla unpatched .exe  ; the one that comes on the disc
        2 = vanilla patched .exe    ; the updated .exe that comes with the online patcher
        3 = hlm-juic .exe           ; initial crack by Hoodlum - unpatched .exe
        4 = hlm-juif .exe           ; fixed crack by Hoodlum - unpatched .exe
        5 = Z3r0n3 v1 .exe          ; initial crack by Z3r0n3 - patched .exe
        6 = Z3r0n3 v2 .exe          ; latest crack by Z3r0n3 - patched .exe
        '''
        # If the .exe is 12,560,384 bytes, it's probably an hlm-juif .exe.
        if len(exe_bytes) == 12560384:
            exe_type = 4
        # If the .exe is 6,852,608 bytes, it's probably a patched .exe.
        elif len(exe_bytes) == 6852608:
            exe_type = 2
        # Both the unpatched and hlm-juic .exes are 12,533,760 bytes long, so we need a secondary check to tell between the two.
        elif len(exe_bytes) == 12533760:
            # The first different byte should be at 0xDB8 (3512 dec.); if that byte is 0x20 (32 dec.), it's probably an unpatched .exe.
            if exe_bytes[3512] == 32:
                exe_type = 1
            # If it's 0x56 (86 dec.), it's probably an hlm-juic .exe.
            elif exe_bytes[3512] == 86:
                exe_type = 3
            # If it isn't either of these, something's probably gone wrong - flag it as an unknown .exe.
            else:
                exe_type = 0
        # If the .exe is 30,097,408 bytes, it's probably a Z3r0n3 v1 .exe.
        elif len(exe_bytes) == 30097408:
            exe_type = 5
        # If the .exe is 13,760,830 bytes, it's probably a Z3r0n3 v2 .exe.
        elif len(exe_bytes) == 13760830:
            exe_type = 6
        # If the file size doesn't match any known .exe, flag it as an unknown.
        else:
            exe_type = 0

        # Set the first half of the .exe type string as the .exe name by taking the file path from earlier and starting it after the last slash.
        exeTypeStr = exePath[exePath.rindex('/') + 1:] + " "
        # Append the detected .exe type to the string.
        if exe_type == 0:
            exeTypeStr += "(unknown)"
        elif exe_type == 1:
            exeTypeStr += "(unpatched)"
        elif exe_type == 2:
            exeTypeStr += "(patched)"
        elif exe_type == 3:
            exeTypeStr += "(hlm-juic)"
        elif exe_type == 4:
            exeTypeStr += "(hlm-juif)"
        elif exe_type == 5:
            exeTypeStr += "(Z3r0n3 v1)"
        elif exe_type == 6:
            exeTypeStr += "(Z3r0n3 v2)"
        # Set the text of the .exe info label to the string.
        self.InfoExeType.setText(exeTypeStr)
        # Take the file path and cut it off before the last slash, and set that as the text of the .exe path label.
        self.InfoExePath.setEnabled(True)
        self.InfoExePath.setText(exePath[:exePath.rindex('/')])
        # Get the length of the .exe, add comma separators to it, and set that as the text of the .exe size label.
        self.InfoExeSize.setText("{:,}".format(len(exe_bytes)) + " bytes")

        # Set the version of the .exe depending on which type is loaded.
        if exe_type == 1 or exe_type == 3 or exe_type == 4:
            exeVer = 1
        elif exe_type == 2 or exe_type == 5 or exe_type == 6:
            exeVer = 2
        elif exe_type == 0:
            exeVer = 0
        # Update the version label accordingly.
        if exeVer == 1:
            self.InfoVersionStatus.setText("v1.0")
        elif exeVer == 2:
            self.InfoVersionStatus.setText("v1.1")
        elif exeVer == 0:
            self.InfoVersionStatus.setText("Unknown")

        # Checks for a certain string of bytes that only appears in decrypted .exes.
        if b"\x2C\xC2\x04\x00\xC7\x47\x0C" in exe_bytes:
            decrypted = True
        else:
            decrypted = False
        
        # Updates the GUI with the decryption status.
        if decrypted:
            self.InfoDecryptStatus.setText("Yes")
            self.InfoDecryptStatus.setStyleSheet("color: blue;")
        else:
            self.InfoDecryptStatus.setText("No")
            self.InfoDecryptStatus.setStyleSheet("color: red;")
        
        # Checks to see if the .exe has been patched with all 9 openspy.net references.
        # This used to check for any gamespy.com references, but has been reworked in the event that an .exe was already patched with a different domain.
        # if b"gamespy.com" in exe_bytes:
        openspy_bytes = b"openspy.net"
        if exe_bytes.count(openspy_bytes) == 9:
            # If all 9 are found, the servers must already be patched, so let them know that
            self.InfoServerPatchStatus.setStyleSheet("color: blue;")
            self.InfoServerPatchStatus.setText("Yes")
            # No reason to enable the patch button since it shouldn't do anything
            self.InfoServerPatchButton.setEnabled(False)
        else:
            # If there's one missing, let the user know the servers aren't patched...
            self.InfoServerPatchStatus.setStyleSheet("color: red;")
            self.InfoServerPatchStatus.setText("No")
            # ...and let them patch the servers
            self.InfoServerPatchButton.setEnabled(True)
        
        locCheats = exe_bytes.index(b"\xc8\x00\x00\x00\xC8\x00\x00\x00") + 8

        # Allows the code bytes to be easily converted to numbers JE can understand.
        def convCode(offset):
            # Start at the cheat location defined from earlier and add whatever offset is given (pertaining to which character in which code is being read).
            # . is an outlier character compared to the letters, being much earlier in the ASCII table. If the read character is a period, just set it to the corresponding combo box index (which is 26).
            if exe_bytes[locCheats + offset] == 136:
                return 26
            else:
                '''
                To convert a Juiced code letter, subtract 90 (dec) to get its (dec) value in the ASCII table.
                (ex. A in the ASCII table is 65 dec, 41 hex. In Juiced's cheat format, it is 155 dec, 9B hex.)
                To convert to the indices of the combo boxes JE uses, subtract 65 (dec) more.
                (ex. Since A in ASCII is 65 (dec), subtracting 65 will give you its index in the combo boxes (0).
                Adding those two together (90 + 65), take whatever byte is read, and subtract 155 from it to get the correct index needed.
                '''
                return int(exe_bytes[locCheats + offset] - 155)
        
        if decrypted:
            locDOSH = exe_bytes.index(b"\x2C\xC2\x04\x00\xC7\x47\x0C") + 7
            locRESP = exe_bytes.index(b"\x01\x00\x8B\x13\x68") + 5
        
        # Allow all 8 of the codes to be toggled on or off by the user.
        self.cheatPINTCheckbox.setEnabled(True)
        self.cheatDOSHCheckbox.setEnabled(True)
        self.cheatRESPCheckbox.setEnabled(True)
        self.cheatCARSCheckbox.setEnabled(True)
        self.cheatCREWCheckbox.setEnabled(True)
        self.cheatCHARCheckbox.setEnabled(True)
        self.cheatWINCheckbox.setEnabled(True)
        self.cheatALLCheckbox.setEnabled(True)

        # Since disabling a cheat is done by setting the first letter to 1 (139 dec, 8B hex), an inaccessible character, use that to determine whether or not the cheat is disabled
        # If it's not disabled, set the corresponding letter boxes to the corret values
        if exe_bytes[locCheats] != 139:
            self.cheatPINT1.setCurrentIndex(convCode(0))
            self.cheatPINT2.setCurrentIndex(convCode(1))
            self.cheatPINT3.setCurrentIndex(convCode(2))
            self.cheatPINT4.setCurrentIndex(convCode(3))
            self.cheatPINT1.setEnabled(True)
            self.cheatPINT2.setEnabled(True)
            self.cheatPINT3.setEnabled(True)
            self.cheatPINT4.setEnabled(True)
            self.cheatPINTCheckbox.setChecked(True)
        else:
            # If the cheat is disabled, deny access to the combo boxes unless the cheat is enabled by the user
            self.cheatPINT1.setEnabled(False)
            self.cheatPINT2.setEnabled(False)
            self.cheatPINT3.setEnabled(False)
            self.cheatPINT4.setEnabled(False)
            self.cheatPINTCheckbox.setChecked(False)
        
        if exe_bytes[locCheats + 4] != 139:
            self.cheatDOSH1.setCurrentIndex(convCode(4))
            self.cheatDOSH2.setCurrentIndex(convCode(5))
            self.cheatDOSH3.setCurrentIndex(convCode(6))
            self.cheatDOSH4.setCurrentIndex(convCode(7))
            self.cheatDOSH1.setEnabled(True)
            self.cheatDOSH2.setEnabled(True)
            self.cheatDOSH3.setEnabled(True)
            self.cheatDOSH4.setEnabled(True)
            self.cheatDOSHCheckbox.setChecked(True)
        else:
            self.cheatDOSH1.setEnabled(False)
            self.cheatDOSH2.setEnabled(False)
            self.cheatDOSH3.setEnabled(False)
            self.cheatDOSH4.setEnabled(False)
            self.cheatDOSHCheckbox.setChecked(False)
        if exe_bytes[locCheats + 4] != 139 and decrypted:
            self.cheatDOSHValue.setValue(int.from_bytes(exe_bytes[locDOSH:locDOSH + 4], "little"))
            self.cheatDOSHValue.setEnabled(True)
        else:
            self.cheatDOSHValue.setEnabled(False)
        
        if exe_bytes[locCheats + 8] != 139:
            self.cheatRESP1.setCurrentIndex(convCode(8))
            self.cheatRESP2.setCurrentIndex(convCode(9))
            self.cheatRESP3.setCurrentIndex(convCode(10))
            self.cheatRESP4.setCurrentIndex(convCode(11))
            self.cheatRESP1.setEnabled(True)
            self.cheatRESP2.setEnabled(True)
            self.cheatRESP3.setEnabled(True)
            self.cheatRESP4.setEnabled(True)
            self.cheatRESPCheckbox.setChecked(True)
        else:
            # If the cheat is disabled, deny access to the combo boxes unless the cheat is enabled by the user
            self.cheatRESP1.setEnabled(False)
            self.cheatRESP2.setEnabled(False)
            self.cheatRESP3.setEnabled(False)
            self.cheatRESP4.setEnabled(False)
            self.cheatRESPCheckbox.setChecked(False)
        if exe_bytes[locCheats + 8] != 139 and decrypted:
            self.cheatRESPValue.setValue(int(struct.unpack('f', exe_bytes[locRESP:locRESP + 4])[0]))
            self.cheatRESPValue.setEnabled(True)
        else:
            self.cheatRESPValue.setEnabled(False)
        
        if exe_bytes[locCheats + 12] != 139:
            self.cheatCARS1.setCurrentIndex(convCode(12))
            self.cheatCARS2.setCurrentIndex(convCode(13))
            self.cheatCARS3.setCurrentIndex(convCode(14))
            self.cheatCARS4.setCurrentIndex(convCode(15))
            self.cheatCARS1.setEnabled(True)
            self.cheatCARS2.setEnabled(True)
            self.cheatCARS3.setEnabled(True)
            self.cheatCARS4.setEnabled(True)
            self.cheatCARSCheckbox.setChecked(True)
        else:
            # If the cheat is disabled, deny access to the combo boxes unless the cheat is enabled by the user
            self.cheatCARS1.setEnabled(False)
            self.cheatCARS2.setEnabled(False)
            self.cheatCARS3.setEnabled(False)
            self.cheatCARS4.setEnabled(False)
            self.cheatCARSCheckbox.setChecked(False)
        
        if exe_bytes[locCheats + 16] != 139:
            self.cheatCREW1.setCurrentIndex(convCode(16))
            self.cheatCREW2.setCurrentIndex(convCode(17))
            self.cheatCREW3.setCurrentIndex(convCode(18))
            self.cheatCREW4.setCurrentIndex(convCode(19))
            self.cheatCREW1.setEnabled(True)
            self.cheatCREW2.setEnabled(True)
            self.cheatCREW3.setEnabled(True)
            self.cheatCREW4.setEnabled(True)
            self.cheatCREWCheckbox.setChecked(True)
        else:
            # If the cheat is disabled, deny access to the combo boxes unless the cheat is enabled by the user
            self.cheatCREW1.setEnabled(False)
            self.cheatCREW2.setEnabled(False)
            self.cheatCREW3.setEnabled(False)
            self.cheatCREW4.setEnabled(False)
            self.cheatCREWCheckbox.setChecked(False)
        
        if exe_bytes[locCheats + 20] != 139:
            self.cheatCHAR1.setCurrentIndex(convCode(20))
            self.cheatCHAR2.setCurrentIndex(convCode(21))
            self.cheatCHAR3.setCurrentIndex(convCode(22))
            self.cheatCHAR4.setCurrentIndex(convCode(23))
            self.cheatCHAR1.setEnabled(True)
            self.cheatCHAR2.setEnabled(True)
            self.cheatCHAR3.setEnabled(True)
            self.cheatCHAR4.setEnabled(True)
            self.cheatCHARCheckbox.setChecked(True)
        else:
            # If the cheat is disabled, deny access to the combo boxes unless the cheat is enabled by the user
            self.cheatCHAR1.setEnabled(False)
            self.cheatCHAR2.setEnabled(False)
            self.cheatCHAR3.setEnabled(False)
            self.cheatCHAR4.setEnabled(False)
            self.cheatCHARCheckbox.setChecked(False)
        
        if exe_bytes[locCheats + 24] != 139:
            self.cheatWIN1.setCurrentIndex(convCode(24))
            self.cheatWIN2.setCurrentIndex(convCode(25))
            self.cheatWIN3.setCurrentIndex(convCode(26))
            self.cheatWIN4.setCurrentIndex(convCode(27))
            self.cheatWIN1.setEnabled(True)
            self.cheatWIN2.setEnabled(True)
            self.cheatWIN3.setEnabled(True)
            self.cheatWIN4.setEnabled(True)
            self.cheatWINCheckbox.setChecked(True)
        else:
            # If the cheat is disabled, deny access to the combo boxes unless the cheat is enabled by the user
            self.cheatWIN1.setEnabled(False)
            self.cheatWIN2.setEnabled(False)
            self.cheatWIN3.setEnabled(False)
            self.cheatWIN4.setEnabled(False)
            self.cheatWINCheckbox.setChecked(False)
        
        if exe_bytes[locCheats + 28] != 139:
            self.cheatALL1.setCurrentIndex(convCode(28))
            self.cheatALL2.setCurrentIndex(convCode(29))
            self.cheatALL3.setCurrentIndex(convCode(30))
            self.cheatALL4.setCurrentIndex(convCode(31))
            self.cheatALL1.setEnabled(True)
            self.cheatALL2.setEnabled(True)
            self.cheatALL3.setEnabled(True)
            self.cheatALL4.setEnabled(True)
            self.cheatALLCheckbox.setChecked(True)
        else:
            # If the cheat is disabled, deny access to the combo boxes unless the cheat is enabled by the user
            self.cheatALL1.setEnabled(False)
            self.cheatALL2.setEnabled(False)
            self.cheatALL3.setEnabled(False)
            self.cheatALL4.setEnabled(False)
            self.cheatALLCheckbox.setChecked(False)
        
        try:
            locCarUnlocks = exe_bytes.index(b"\x48\x3C\x6F\x00\x00\x00\x00\x00\x00\x00\x00\x00") + 12
        # Patched .exe has a different instruction preceding the car unlock data.
        except ValueError:
            locCarUnlocks = exe_bytes.index(b"\x80\x6C\x6F\x00\x00\x00\x00\x00\x00\x00\x00\x00") + 12
        self.modsCarUnlockButton.setEnabled(True)

        indexDict = {
            0  : 47, # Acura Integra Type R             ; index 47
            1  : 48, # Acura NSX                        ; index 48
            2  : 46, # Acura RSX Type-S                 ; index 46
            3  : 38, # Chevrolet Camaro                 ; index 38
            4  : 44, # Chevrolet Camaro Z28             ; index 44
            5  : 42, # Chevrolet Corvette               ; index 42
            6  : 12, # Chevrolet Corvete Z06            ; index 12
            7  : 39, # Dodge 1969 Charger R/T           ; index 39
            8  : 25, # Dodge Neon R/T                   ; index 25
            9  : 41, # Dodge SRT-4                      ; index 41
            10 : 13, # Dodge Viper GTS                  ; index 13
            11 : 15, # Fiat Punto 1.8 HGT               ; index 15
            12 : 4,  # Ford 2003 Focus SVT              ; index 4
            13 : 51, # Ford 2004 Focus ZTS              ; index 51
            14 : 24, # Ford 67 Mustang                  ; index 24
            15 : 45, # Ford Falcon XR8                  ; index 45
            16 : 37, # Ford Mustang 99 GT               ; index 37
            17 : 26, # Holden Monaro CV8                ; index 26
            18 : 23, # Honda Civic DX                   ; index 23
            19 : 1,  # Honda Civic Type R               ; index 1
            20 : 3,  # Honda CR-X                       ; index 3
            21 : 21, # Honda Integra Type R '99         ; index 21
            22 : 36, # Honda Integra Type R '02         ; index 36
            23 : 8,  # Honda NSX                        ; index 8
            24 : 32, # Honda Prelude VT                 ; index 32
            25 : 19, # Honda S2000                      ; index 19
            26 : 22, # Mazda MX-5                       ; index 22
            27 : 10, # Mazda RX-7                       ; index 10
            28 : 49, # Mazda RX8                        ; index 49
            29 : 35, # Mitsubishi 3000GT                ; index 35
            30 : 18, # Mitsubishi Eclipse GSX           ; index 18
            31 : 28, # Mitsubishi FTO                   ; index 28
            32 : 31, # Mitsubishi Lancer Evolution VI   ; index 31
            33 : 5,  # Mitsubishi Lancer Evolution VIII ; index 5
            34 : 33, # Nissan 300Z                      ; index 33
            35 : 34, # Nissan 350Z                      ; index 34
            36 : 6,  # Nissan Skyline GT-R              ; index 6
            37 : 9,  # Peugeot 206 GTI                  ; index 9
            38 : 11, # Pontiac Firebird                 ; index 11
            39 : 2,  # Renault Clio Sport 2.0 16V       ; index 2
            40 : 7,  # Subaru Impreza 22B STi           ; index 7
            41 : 27, # Subaru Impreza WRX STi           ; index 27
            42 : 0,  # Toyota Celica SS-I               ; index 0
            43 : 29, # Toyota Celica SS-II              ; index 29
            44 : 40, # Toyota Corolla 1.6               ; index 40
            45 : 30, # Toyota MR2                       ; index 30
            46 : 43, # Toyota MR-S                      ; index 43
            47 : 20, # Toyota Supra                     ; index 20
            48 : 17, # Vauxhall Corsa Sri 1.8i 16V      ; index 17
            49 : 50, # Volkswagen Beetle GLS 1.8T       ; index 50
            50 : 14, # Volkswagen Corrado VR6           ; index 14
            51 : 16  # Volkswagen Golf MkIV             ; index 16
        }
        carUnlocks = []
        for i in range(52):
            carUnlocks.append(int.from_bytes(exe_bytes[locCarUnlocks + (4 * i):locCarUnlocks + (4 * i) + 4], "little"))
        for i in range(52):
            JECU.carUnlocksTable.cellWidget(i, 0).setValue(carUnlocks[indexDict[i]])
            if JECU.carUnlocksTable.cellWidget(i, 0).value() == 0:
                JECU.carUnlocksTable.cellWidget(i, 1).setText("Start")
            else:
                JECU.carUnlocksTable.cellWidget(i, 1).setText(str(JECU.carUnlocksTable.cellWidget(i, 0).value() * 3) + " races")
        
        
        # Find the location in the .exe where carmodels.dat would be defined using a consistent byte string that comes before it in all 4 .exes.
        locModels = exe_bytes.index(b"\x69\x00\x00\x4A\x00\x75\x00\x69\x00\x63\x00\x65\x00\x64\x00\x00\x00\x00\x00") + 19

        # Check to see if dummyfile.dat has been patched in, and update the checkbox accordingly.
        if exe_bytes[locModels:locModels + 13] != b"dummyfile.dat":
            self.expertDummyCheckbox.setChecked(False)
        else:
            self.expertDummyCheckbox.setChecked(True)
        
        # Allow the user to toggle the dummyfile.dat patch.
        self.expertDummyCheckbox.setEnabled(True)
        
        # Allow saving the .exe.
        self.actionSave.setEnabled(True)
        self.actionSaveAs.setEnabled(True)

        # If the .exe type is unknown, display a warning message stating that results may vary.
        if exe_type == 0:
            QtWidgets.QMessageBox.warning(self, "Warning", ".exe type could not be determined. You may run into problems.")
        
        # If the .exe is encrypted, display a warning message stating that certain features will be unavailable.
        if not decrypted:
            QtWidgets.QMessageBox.warning(self, "Warning", "This .exe is encrypted. Some options will be unavailable.")
    
    # Redirect all of the online domains to openspy.net to restore online functionality.
    def patchServers(self):
        # Keep track of how many domains are replaced with openspy.net for the notification message later on.
        domainsReplaced = 0
        gamestats_index = exe_bytes.find(b"gamestats.")
        # If the domain found isn't already openspy.net, change it
        if exe_bytes[gamestats_index + 10:gamestats_index + 21] != b"openspy.net":
            domainsReplaced += 1
            exe_bytes[gamestats_index + 10:gamestats_index + 21] = b"openspy.net"

        available_index = exe_bytes.find(b"%s.available.")
        if exe_bytes[available_index + 13:available_index + 24] != b"openspy.net":
            domainsReplaced += 1
            exe_bytes[available_index + 13:available_index + 24] = b"openspy.net"

        master_index = exe_bytes.find(b"%s.master.")
        if exe_bytes[master_index + 10:master_index + 21] != b"openspy.net":
            domainsReplaced += 1
            exe_bytes[master_index + 10:master_index + 21] = b"openspy.net"

        natneg2_index = exe_bytes.find(b"natneg2.")
        if exe_bytes[natneg2_index + 8:natneg2_index + 19] != b"openspy.net":
            domainsReplaced += 1
            exe_bytes[natneg2_index + 8:natneg2_index + 19] = b"openspy.net"

        natneg1_index = exe_bytes.find(b"natneg1.")
        if exe_bytes[natneg1_index + 8:natneg1_index + 19] != b"openspy.net":
            domainsReplaced += 1
            exe_bytes[natneg1_index + 8:natneg1_index + 19] = b"openspy.net"

        ms_index = exe_bytes.find(b"%s.ms%d.")
        if exe_bytes[ms_index + 8:ms_index + 19] != b"openspy.net":
            domainsReplaced += 1
            exe_bytes[ms_index + 8:ms_index + 19] = b"openspy.net"
        
        second_gamestats_index = exe_bytes[gamestats_index + 1:].find(b"gamestats.") + gamestats_index + 1
        if exe_bytes[second_gamestats_index + 10:second_gamestats_index + 21] != b"openspy.net":
            domainsReplaced += 1
            exe_bytes[second_gamestats_index + 10:second_gamestats_index + 21] = b"openspy.net"

        gpsp_index = exe_bytes.find(b"gpsp.")
        if exe_bytes[gpsp_index + 5:gpsp_index + 16] != b"openspy.net":
            domainsReplaced += 1
            exe_bytes[gpsp_index + 5:gpsp_index + 16] = b"openspy.net"

        gpcm_index = exe_bytes.find(b"gpcm.")
        if exe_bytes[gpcm_index + 5:gpcm_index + 16] != b"openspy.net":
            domainsReplaced += 1
            exe_bytes[gpcm_index + 5:gpcm_index + 16] = b"openspy.net"

        # Once that's done, change the status to let the user know the operation is done...
        self.InfoServerPatchStatus.setStyleSheet("color: blue;")
        self.InfoServerPatchStatus.setText("Yes")
        # ...and disable the button to prevent performing a redundant operation
        self.InfoServerPatchButton.setEnabled(False)
        if domainsReplaced == 1:
            QtWidgets.QMessageBox.information(self, "Success", str(domainsReplaced) + " domain was replaced with openspy.net.\nRemember to save your changes.")
        else:
            QtWidgets.QMessageBox.information(self, "Success", str(domainsReplaced) + " domains were replaced with openspy.net.\nRemember to save your changes.")
    
    # Enables or disables the letter combo boxes depending on whether or not the corresponding check box is checked.
    def togglePINT(self):
        if self.cheatPINTCheckbox.isChecked():
            self.cheatPINT1.setEnabled(True)
            self.cheatPINT2.setEnabled(True)
            self.cheatPINT3.setEnabled(True)
            self.cheatPINT4.setEnabled(True)
        else:
            self.cheatPINT1.setEnabled(False)
            self.cheatPINT2.setEnabled(False)
            self.cheatPINT3.setEnabled(False)
            self.cheatPINT4.setEnabled(False)
    
    def toggleDOSH(self):
        if self.cheatDOSHCheckbox.isChecked():
            self.cheatDOSH1.setEnabled(True)
            self.cheatDOSH2.setEnabled(True)
            self.cheatDOSH3.setEnabled(True)
            self.cheatDOSH4.setEnabled(True)
            if decrypted:
                self.cheatDOSHValue.setEnabled(True)
        else:
            self.cheatDOSH1.setEnabled(False)
            self.cheatDOSH2.setEnabled(False)
            self.cheatDOSH3.setEnabled(False)
            self.cheatDOSH4.setEnabled(False)
            self.cheatDOSHValue.setEnabled(False)
    
    def toggleRESP(self):
        if self.cheatRESPCheckbox.isChecked():
            self.cheatRESP1.setEnabled(True)
            self.cheatRESP2.setEnabled(True)
            self.cheatRESP3.setEnabled(True)
            self.cheatRESP4.setEnabled(True)
            if decrypted:
                self.cheatRESPValue.setEnabled(True)
        else:
            self.cheatRESP1.setEnabled(False)
            self.cheatRESP2.setEnabled(False)
            self.cheatRESP3.setEnabled(False)
            self.cheatRESP4.setEnabled(False)
            self.cheatRESPValue.setEnabled(False)
    
    def toggleCARS(self):
        if self.cheatCARSCheckbox.isChecked():
            self.cheatCARS1.setEnabled(True)
            self.cheatCARS2.setEnabled(True)
            self.cheatCARS3.setEnabled(True)
            self.cheatCARS4.setEnabled(True)
        else:
            self.cheatCARS1.setEnabled(False)
            self.cheatCARS2.setEnabled(False)
            self.cheatCARS3.setEnabled(False)
            self.cheatCARS4.setEnabled(False)
    
    def toggleCREW(self):
        if self.cheatCREWCheckbox.isChecked():
            self.cheatCREW1.setEnabled(True)
            self.cheatCREW2.setEnabled(True)
            self.cheatCREW3.setEnabled(True)
            self.cheatCREW4.setEnabled(True)
        else:
            self.cheatCREW1.setEnabled(False)
            self.cheatCREW2.setEnabled(False)
            self.cheatCREW3.setEnabled(False)
            self.cheatCREW4.setEnabled(False)
    
    def toggleCHAR(self):
        if self.cheatCHARCheckbox.isChecked():
            self.cheatCHAR1.setEnabled(True)
            self.cheatCHAR2.setEnabled(True)
            self.cheatCHAR3.setEnabled(True)
            self.cheatCHAR4.setEnabled(True)
        else:
            self.cheatCHAR1.setEnabled(False)
            self.cheatCHAR2.setEnabled(False)
            self.cheatCHAR3.setEnabled(False)
            self.cheatCHAR4.setEnabled(False)
    
    def toggleWIN(self):
        if self.cheatWINCheckbox.isChecked():
            self.cheatWIN1.setEnabled(True)
            self.cheatWIN2.setEnabled(True)
            self.cheatWIN3.setEnabled(True)
            self.cheatWIN4.setEnabled(True)
        else:
            self.cheatWIN1.setEnabled(False)
            self.cheatWIN2.setEnabled(False)
            self.cheatWIN3.setEnabled(False)
            self.cheatWIN4.setEnabled(False)
    
    def toggleALL(self):
        if self.cheatALLCheckbox.isChecked():
            self.cheatALL1.setEnabled(True)
            self.cheatALL2.setEnabled(True)
            self.cheatALL3.setEnabled(True)
            self.cheatALL4.setEnabled(True)
        else:
            self.cheatALL1.setEnabled(False)
            self.cheatALL2.setEnabled(False)
            self.cheatALL3.setEnabled(False)
            self.cheatALL4.setEnabled(False)
    
    def showCarUnlocks(self):
        JECU.show()
    
    # Reverses the operation done in convCode.
    def convCodeBack(self, index):
        if index == 26:
            return 136
        else:
            return index + 155
    
    # Check if any cheats use duplicate codes.
    def checkCheats(self):
        # Initialize a list of the cheat codes to patch in.
        newCheats = []
        # Check each cheat to see if it's enabled. If it is, pack its code into a tuple and add it to the list.
        if self.cheatPINTCheckbox.isChecked():
            newCheats.append((self.cheatPINT1.currentIndex(), self.cheatPINT2.currentIndex(), self.cheatPINT3.currentIndex(), self.cheatPINT4.currentIndex()))
        if self.cheatDOSHCheckbox.isChecked():
            newCheats.append((self.cheatDOSH1.currentIndex(), self.cheatDOSH2.currentIndex(), self.cheatDOSH3.currentIndex(), self.cheatDOSH4.currentIndex()))
        if self.cheatRESPCheckbox.isChecked():
            newCheats.append((self.cheatRESP1.currentIndex(), self.cheatRESP2.currentIndex(), self.cheatRESP3.currentIndex(), self.cheatRESP4.currentIndex()))
        if self.cheatCARSCheckbox.isChecked():
            newCheats.append((self.cheatCARS1.currentIndex(), self.cheatCARS2.currentIndex(), self.cheatCARS3.currentIndex(), self.cheatCARS4.currentIndex()))
        if self.cheatCREWCheckbox.isChecked():
            newCheats.append((self.cheatCREW1.currentIndex(), self.cheatCREW2.currentIndex(), self.cheatCREW3.currentIndex(), self.cheatCREW4.currentIndex()))
        if self.cheatCHARCheckbox.isChecked():
            newCheats.append((self.cheatCHAR1.currentIndex(), self.cheatCHAR2.currentIndex(), self.cheatCHAR3.currentIndex(), self.cheatCHAR4.currentIndex()))
        if self.cheatWINCheckbox.isChecked():
            newCheats.append((self.cheatWIN1.currentIndex(), self.cheatWIN2.currentIndex(), self.cheatWIN3.currentIndex(), self.cheatWIN4.currentIndex()))
        if self.cheatALLCheckbox.isChecked():
            newCheats.append((self.cheatALL1.currentIndex(), self.cheatALL2.currentIndex(), self.cheatALL3.currentIndex(), self.cheatALL4.currentIndex()))
        
        # If there's more than one cheat enabled...
        if len(newCheats) > 1:
            # Run one less check than there are cheats...
            for i in range(len(newCheats) - 1):
                # ...to see if there are any tuples (codes) that occur more than once in the list.
                if newCheats.count(newCheats[i]) > 1:
                    # If there are any, show the user a warning message about the duplicate codes and ask them if they want to save anyways.
                    question = QtWidgets.QMessageBox.warning(self, "Warning", "You have multiple cheats with the same code. Only the first cheat using a given code will be triggered in-game. Do you wish to continue?", QtWidgets.QMessageBox.StandardButton.Yes|QtWidgets.QMessageBox.StandardButton.No)
                    # If they select yes (represented by int 16384), break the loop (since they've indicated they're okay with dupe codes) and return True to indicate that the check is good.
                    if question == 16384:
                        return True
                    # If they select no (represented by int 16384), break the loop and return False to indicate that the check did not pass.
                    elif question == 65536:
                        return False
        # If the check completes fully without any issues, return True.
        return True
                    


    # Save the .exe to the same place it was opened from.
    def saveExe(self):
        # If the cheat check did not clear, do not save the .exe.
        if self.checkCheats() == False:
            return
        # Check to see that the PINT cheat is enabled.
        if self.cheatPINTCheckbox.isChecked():
            # If it is, convert each of the letters to their corresponding number that Juiced's codes use
            exe_bytes[locCheats] = self.convCodeBack(self.cheatPINT1.currentIndex())
            exe_bytes[locCheats + 1] = self.convCodeBack(self.cheatPINT2.currentIndex())
            exe_bytes[locCheats + 2] = self.convCodeBack(self.cheatPINT3.currentIndex())
            exe_bytes[locCheats + 3] = self.convCodeBack(self.cheatPINT4.currentIndex())
        else:
            # If it's set to be disabled, just do what Juiced does and set the first letter to 1, which is normally impossible to input
            exe_bytes[locCheats] = 139
        
        if self.cheatDOSHCheckbox.isChecked():
            # If it is, convert each of the letters to their corresponding number that Juiced's codes use
            exe_bytes[locCheats + 4] = self.convCodeBack(self.cheatDOSH1.currentIndex())
            exe_bytes[locCheats + 5] = self.convCodeBack(self.cheatDOSH2.currentIndex())
            exe_bytes[locCheats + 6] = self.convCodeBack(self.cheatDOSH3.currentIndex())
            exe_bytes[locCheats + 7] = self.convCodeBack(self.cheatDOSH4.currentIndex())
            if decrypted:
                exe_bytes[locDOSH:locDOSH + 4] = int.to_bytes(self.cheatDOSHValue.value(), 4, "little")
        else:
            # If it's set to be disabled, just do what Juiced does and set the first letter to 1, which is normally impossible to input
            exe_bytes[locCheats + 4] = 139
        
        if self.cheatRESPCheckbox.isChecked():
            # If it is, convert each of the letters to their corresponding number that Juiced's codes use
            exe_bytes[locCheats + 8] = self.convCodeBack(self.cheatRESP1.currentIndex())
            exe_bytes[locCheats + 9] = self.convCodeBack(self.cheatRESP2.currentIndex())
            exe_bytes[locCheats + 10] = self.convCodeBack(self.cheatRESP3.currentIndex())
            exe_bytes[locCheats + 11] = self.convCodeBack(self.cheatRESP4.currentIndex())
            if decrypted:
                exe_bytes[locRESP:locRESP + 4] = struct.pack('f', float(self.cheatRESPValue.value()))
        else:
            # If it's set to be disabled, just do what Juiced does and set the first letter to 1, which is normally impossible to input
            exe_bytes[locCheats + 8] = 139
        
        if self.cheatCARSCheckbox.isChecked():
            # If it is, convert each of the letters to their corresponding number that Juiced's codes use
            exe_bytes[locCheats + 12] = self.convCodeBack(self.cheatCARS1.currentIndex())
            exe_bytes[locCheats + 13] = self.convCodeBack(self.cheatCARS2.currentIndex())
            exe_bytes[locCheats + 14] = self.convCodeBack(self.cheatCARS3.currentIndex())
            exe_bytes[locCheats + 15] = self.convCodeBack(self.cheatCARS4.currentIndex())
        else:
            # If it's set to be disabled, just do what Juiced does and set the first letter to 1, which is normally impossible to input
            exe_bytes[locCheats + 12] = 139
        
        if self.cheatCREWCheckbox.isChecked():
            # If it is, convert each of the letters to their corresponding number that Juiced's codes use
            exe_bytes[locCheats + 16] = self.convCodeBack(self.cheatCREW1.currentIndex())
            exe_bytes[locCheats + 17] = self.convCodeBack(self.cheatCREW2.currentIndex())
            exe_bytes[locCheats + 18] = self.convCodeBack(self.cheatCREW3.currentIndex())
            exe_bytes[locCheats + 19] = self.convCodeBack(self.cheatCREW4.currentIndex())
        else:
            # If it's set to be disabled, just do what Juiced does and set the first letter to 1, which is normally impossible to input
            exe_bytes[locCheats + 16] = 139
        
        if self.cheatCHARCheckbox.isChecked():
            # If it is, convert each of the letters to their corresponding number that Juiced's codes use
            exe_bytes[locCheats + 20] = self.convCodeBack(self.cheatCHAR1.currentIndex())
            exe_bytes[locCheats + 21] = self.convCodeBack(self.cheatCHAR2.currentIndex())
            exe_bytes[locCheats + 22] = self.convCodeBack(self.cheatCHAR3.currentIndex())
            exe_bytes[locCheats + 23] = self.convCodeBack(self.cheatCHAR4.currentIndex())
        else:
            # If it's set to be disabled, just do what Juiced does and set the first letter to 1, which is normally impossible to input
            exe_bytes[locCheats + 20] = 139
        
        if self.cheatWINCheckbox.isChecked():
            # If it is, convert each of the letters to their corresponding number that Juiced's codes use
            exe_bytes[locCheats + 24] = self.convCodeBack(self.cheatWIN1.currentIndex())
            exe_bytes[locCheats + 25] = self.convCodeBack(self.cheatWIN2.currentIndex())
            exe_bytes[locCheats + 26] = self.convCodeBack(self.cheatWIN3.currentIndex())
            exe_bytes[locCheats + 27] = self.convCodeBack(self.cheatWIN4.currentIndex())
        else:
            # If it's set to be disabled, just do what Juiced does and set the first letter to 1, which is normally impossible to input
            exe_bytes[locCheats + 24] = 139
        
        if self.cheatALLCheckbox.isChecked():
            # If it is, convert each of the letters to their corresponding number that Juiced's codes use
            exe_bytes[locCheats + 28] = self.convCodeBack(self.cheatALL1.currentIndex())
            exe_bytes[locCheats + 29] = self.convCodeBack(self.cheatALL2.currentIndex())
            exe_bytes[locCheats + 30] = self.convCodeBack(self.cheatALL3.currentIndex())
            exe_bytes[locCheats + 31] = self.convCodeBack(self.cheatALL4.currentIndex())
        else:
            # If it's set to be disabled, just do what Juiced does and set the first letter to 1, which is normally impossible to input
            exe_bytes[locCheats + 28] = 139
        
        # Rewrite the car unlocks based on what's set in the respective menu.
        for i in range(52):
            exe_bytes[locCarUnlocks + (indexDict[i] * 4):locCarUnlocks + (indexDict[i] * 4) + 4] = int.to_bytes(JECU.carUnlocksTable.cellWidget(i, 0).value(), 4, "little")
        
        if self.expertDummyCheckbox.isChecked():
            exe_bytes[locModels:locModels + 13] = b"dummyfile.dat"
        else:
            exe_bytes[locModels:locModels + 13] = b"carmodels.dat"

        try:
            f = open(exePath, "wb")
        # Throw an error message if the file is read-only or the user lacks permissions to save in the directory (ex. Program Files).
        except PermissionError:
            QtWidgets.QMessageBox.critical(self, "Error", ".exe could not be saved to " + exePath + ". Access was denied.\nTry running as administrator, and make sure the .exe isn't read-only.")
            return
        # Write the .exe bytes in memory to the .exe.
        f.write(exe_bytes)
        # Close the file.
        f.close()

        # Updates the three .exe info lines after saving.
        # Set the first half of the .exe type string as the .exe name by taking the file path from earlier and starting it after the last slash.
        exeTypeStr = exePath[exePath.rindex('/') + 1:] + " "
        # Append the detected .exe type to the string.
        if exe_type == 0:
            exeTypeStr += "(unknown)"
        elif exe_type == 1:
            exeTypeStr += "(unpatched)"
        elif exe_type == 2:
            exeTypeStr += "(patched)"
        elif exe_type == 3:
            exeTypeStr += "(hlm-juic)"
        elif exe_type == 4:
            exeTypeStr += "(hlm-juif)"
        elif exe_type == 5:
            exeTypeStr += "(Z3r0n3 v1)"
        elif exe_type == 6:
            exeTypeStr += "(Z3r0n3 v2)"
        # Set the text of the .exe info label to the string.
        self.InfoExeType.setText(exeTypeStr)
        # Take the file path and cut it off before the last slash, and set that as the text of the .exe path label.
        self.InfoExePath.setEnabled(True)
        self.InfoExePath.setText(exePath[:exePath.rindex('/')])
        # Get the length of the .exe, add comma separators to it, and set that as the text of the .exe size label.
        self.InfoExeSize.setText("{:,}".format(len(exe_bytes)) + " bytes")

        # Display a success message.
        QtWidgets.QMessageBox.information(self, "Success", ".exe saved to " + exePath + ".")

    # Saves the .exe in memory to a location specified by the user.
    def saveExeAs(self):
        global exePath
        exeTempPath = QFileDialog.getSaveFileName(self, "Save as...", self.lastPath + "/Juiced.exe", "Executable files (*.exe)")[0]
        if exeTempPath == "":
            return
        else:
            exePath = exeTempPath
        self.saveExe()

class JECarUnlocksWindow(QtWidgets.QMainWindow, Ui_JECarUnlocksWindow):
    def __init__(self):
        super(JECarUnlocksWindow, self).__init__()
        self.setupUi(self)

        self.setWindowIcon(juicedIcon)

        # Runs fixTabOrder() whenever switching to a different cell in the table.
        self.carUnlocksTable.currentCellChanged.connect(self.fixTabOrder)

        for i in range(self.carUnlocksTable.rowCount()):
            # Make each first item in a row a spin box to determine what unlock tier a car is in.
            self.carUnlocksTable.setCellWidget(i, 0, QtWidgets.QSpinBox())
            # Prevent tiers from going into the negatives.
            self.carUnlocksTable.cellWidget(i, 0).setMinimum(0)
            # 715,827,882 * 3 = 2,147,483,646 races; the highest %3 value you can reach in a signed 4-byte int.
            # Theoretically the tiers can go all the way up to 2,147,483,647 (or higher depending on if it's actually signed) - but that could cause an overflow when calculating the races required.
            # Nobody's gonna want to go this high anyways.
            self.carUnlocksTable.cellWidget(i, 0).setMaximum(715827882)
            # Set the second item in a row to a read-only line edit as a user-friendly way of determining # of races required.
            # To be honest, I don't remember why I'm setting them to QLineEdits instead of just editing the fields directly, but fuck it. It works.
            self.carUnlocksTable.setCellWidget(i, 1, QtWidgets.QLineEdit())
            self.carUnlocksTable.cellWidget(i, 1).setReadOnly(True)
        
        # Prevents rows and columns from being resized
        self.carUnlocksTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Fixed)
        self.carUnlocksTable.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Fixed)
        
        # Monitor each spin box to update the # races line edit whenever the spin box is changed.
        # Yes, this is terribly inefficient. No, I could not figure out a better way of doing this. Should note for the future though - there HAS to be a better way.
        self.carUnlocksTable.cellWidget(0, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(1, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(2, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(3, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(4, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(5, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(6, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(7, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(8, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(9, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(10, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(11, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(12, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(13, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(14, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(15, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(16, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(17, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(18, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(19, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(20, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(21, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(22, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(23, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(24, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(25, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(26, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(27, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(28, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(29, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(30, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(31, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(32, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(33, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(34, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(35, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(36, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(37, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(38, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(39, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(40, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(41, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(42, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(43, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(44, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(45, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(46, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(47, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(48, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(49, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(50, 0).valueChanged.connect(self.updateRaces)
        self.carUnlocksTable.cellWidget(51, 0).valueChanged.connect(self.updateRaces)

        self.actionDefault.triggered.connect(self.setDefaultOrder)

    # Refresh text to determine how many races an unlock tier requires.
    def updateRaces(self):
        # Since children in a table widget don't know their index in said table, use this workaround to find that out.
        # Credit to ekhumoro on StackOverflow. (https://stackoverflow.com/questions/39814304/pyqt5-get-index-of-cell-widgets-and-their-chosen-values)
        line = self.carUnlocksTable.cellWidget(self.carUnlocksTable.indexAt(self.sender().pos()).row(), 1)
        # If unlock tier == 0, the car will be available at the start.
        if self.sender().value() == 0:
            line.setText("Start")
        # Otherwise, # races required is just the tier times three.
        else:
            line.setText(str(self.sender().value() * 3) + " races")
    
    # Keeps the table from tabbing into the read-only unlocks column.
    def fixTabOrder(self):
        if self.sender().currentColumn() == 1:
            self.carUnlocksTable.setCurrentCell(self.sender().currentRow() + 1, 0)
    
    def setDefaultOrder(self):
        defaultOrder = [6, 10, 6, 11, 11, 6, 12, 8, 3, 7, 12, 1, 2, 1, 4, 9, 6, 9, 3, 5, 0, 6, 6, 10, 4, 3, 1, 8, 8, 9, 2, 7, 7, 11, 7, 5, 10, 0, 12, 5, 4, 8, 4, 4, 2, 5, 5, 10, 3, 0, 6, 2]
        for i in range(52):
            self.carUnlocksTable.cellWidget(i, 0).setValue(defaultOrder[i])

class JEAboutDialog(QtWidgets.QDialog, Ui_JEAboutDialog):
    def __init__(self):
        super(JEAboutDialog, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(juicedIcon)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JE = JEMainWindow()
    JECU = JECarUnlocksWindow()
    JEA = JEAboutDialog()
    JE.show()
    sys.exit(app.exec_())