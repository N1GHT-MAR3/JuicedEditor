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

        # Runs openExe() when File -> Open... is clicked
        self.actionOpen.triggered.connect(self.openExe)
    
    # Opens Juiced.exe where specified.
    def openExe(self):
        # Opens a file dialog asking the user to locate Juiced.exe.
        exePath = QFileDialog.getOpenFileName(self, "Open...", getcwd(), "Executable files (*.exe)")[0]
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
            error = QtWidgets.QMessageBox.critical(self, "Error", "Load aborted. This does not appear to be a valid Juiced .exe.")
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
        # If the .exe type is unknown, display a warning message stating that results may vary.
        if exe_type == 0:
            notice = QtWidgets.QMessageBox.warning(self, "Warning", ".exe type could not be determined. You may run into problems.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JE = JEMainWindow()
    JE.show()
    sys.exit(app.exec())