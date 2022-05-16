# Imports PyQt6 modules used to display the GUI.
from logging import critical
from PyQt6 import QtCore, QtGui, QtWidgets
# Imports the main window UI files from JEMain.py.
from JEMain import Ui_JEMainWindow
# Imports the file dialog seen when opening a file.
from PyQt6.QtWidgets import QFileDialog
# Imports a function used to get a Windows directory.
from os import getcwd


# Sets up the main window UI.
class JEMainWindow(QtWidgets.QMainWindow, Ui_JEMainWindow):
    def __init__(self):
        super(JEMainWindow, self).__init__()
        self.setupUi(self)

        # Initializes startup text to make things easier for me in Qt Designer
        self.InfoExeType.setText("No .exe loaded")
        self.InfoExePath.setText("")
        self.InfoExeSize.setText("")
        self.InfoDecryptStatus.setText("")
        self.InfoDecryptStatus.setStyleSheet("color: black;")
        self.InfoServerPatchStatus.setText("")
        self.InfoServerPatchStatus.setStyleSheet("color: black;")

        # Runs openExe() when File -> Open... is clicked
        self.actionOpen.triggered.connect(self.openExe)

        # Runs patchServers() when Patch Servers is clicked
        self.InfoServerPatchButton.clicked.connect(self.patchServers)

        # Runs saveExe() when File -> Save is clicked
        self.actionSave.triggered.connect(self.saveExe)

        # Runs saveExeAs() when File -> Save As... is clicked
        self.actionSaveAs.triggered.connect(self.saveExeAs)
    
    # Opens Juiced.exe where specified.
    def openExe(self):
        global exe_bytes
        global decrypted
        global exePath
        # Opens a file dialog asking the user to locate Juiced.exe.
        exePath = QFileDialog.getOpenFileName(self, "Open...", getcwd(), "Executable files (*.exe)")[0]
        #exePath = QFileDialog.getOpenFileName(self, "Open...", "C:\\Users\\N1GHTMAR3\\Documents\\Programs\\Juiced Editor", "Executable files (*.exe)")[0]
        # Try to open the .exe at the path provided by the user in the file dialog.
        try:
            f = open(exePath, "rb")
        # If there is no .exe path (if the user cancels the file dialog), do nothing.
        except FileNotFoundError:
            return
        # Write all of the bytes in the .exe to an array so the editor can process them.
        exe_bytes = bytearray(f.read())
        # Closes the .exe so it's not being used. Doesn't need to be until the .exe is saved anyways.
        f.close()

        
        product_name_bytes = b"\x4A\x00\x75\x00\x69\x00\x63\x00\x65\x00\x64\x00\x20\x00\x50\x00\x43\x00\x20\x00\x47\x00\x61\x00\x6D\x00\x65"
        # If the product name "Juiced PC Game" (which can be seen in the .exe's Properties) cannot be found in the .exe, most likely, the .exe isn't a valid Juiced executable.
        if product_name_bytes not in exe_bytes:
            # If this is the case, create and display a generic error message.
            QtWidgets.QMessageBox.critical(self, "Error", "Load aborted. This does not appear to be a valid Juiced .exe.")
            # Stop loading the .exe.
            return

        '''
        Detects the type of Juiced .exe:
        0 = unknown                 ; if the .exe size does not match any known version
        1 = vanilla unpatched .exe  ; the one that comes on the disc
        2 = vanilla patched .exe    ; the updated .exe that comes with the online patcher
        3 = hlm-juic .exe           ; initial crack by Hoodlum - unpatched .exe
        4 = hlm-juif .exe           ; fixed crack by Hoodlum - unpatched .exe
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
        # Set the text of the .exe info label to the string.
        self.InfoExeType.setText(exeTypeStr)
        # Take the file path and cut it off before the last slash, and set that as the text of the .exe path label.
        self.InfoExePath.setText(exePath[:exePath.rindex('/')])
        # Get the length of the .exe, add comma separators to it, and set that as the text of the .exe size label.
        self.InfoExeSize.setText("{:,}".format(len(exe_bytes)) + " bytes")

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
        
        # Allow saving the .exe.
        self.actionSave.setEnabled(True)
        self.actionSaveAs.setEnabled(True)

        # If the .exe type is unknown, display a warning message stating that results may vary.
        if exe_type == 0:
            QtWidgets.QMessageBox.warning(self, "Warning", ".exe type could not be determined. You may run into problems.")
    
    def patchServers(self):
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
    
    def saveExe(self):
        try:
            f = open(exePath, "wb")
        except PermissionError:
            QtWidgets.QMessageBox.critical(self, "Error", ".exe could not be saved to " + exePath + ". Access was denied.\nTry running as administrator, and make sure the .exe isn't read-only.")
            return
        f.write(exe_bytes)
        f.close()

        QtWidgets.QMessageBox.information(self, "Success", ".exe saved to " + exePath + ".")
    
    def saveExeAs(self):
        exePath = QFileDialog.getSaveFileName(self, "Save as...", getcwd() + "/Juiced.exe", "Executable files (*.exe)")[0]
        try:
            f = open(exePath, "wb")
        except PermissionError:
            QtWidgets.QMessageBox.critical(self, "Error", ".exe could not be saved to " + exePath + ". Access was denied.\nTry running as administrator, and make sure the .exe isn't read-only.")
            return
        f.write(exe_bytes)
        f.close()

        QtWidgets.QMessageBox.information(self, "Success", ".exe saved to " + exePath + ".")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JE = JEMainWindow()
    JE.show()
    sys.exit(app.exec())