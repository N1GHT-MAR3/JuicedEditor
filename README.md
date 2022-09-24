# Juiced Editor
An all-in-one editor for the 2005 racing game. Still a work-in-progress.

There are pre-release versions available in [Releases](https://github.com/N1GHT-MAR3/JuicedEditor/releases), but bear in mind that these are not properly tested. I offer no guarantees that these will work.

# Features
* Restore online functionality courtesy of [OpenSpy](http://beta.openspy.net/en/)
* Enable in-game cheat codes locked by the developers
* Change when cars are unlocked in Career mode

Many more features are planned in the future!

# Compatibility

Juiced Editor only works on Windows 10 and later, due to being built on Python 3.9 and Qt6. Earlier versions of Windows will not work until a legacy version can be developed.

| Platform | Version                  | Description                                      | Supported | Decrypted |
| -------- | ------------------------ | ------------------------------------------------ | --------- | --------- |
| PC       | Retail (unpatched)       | The default .exe that comes on disc.             | Yes       | No        |
| PC       | Retail (patched)         | The 1.1 patched .exe.                            | Yes       | No        |
| PC       | Retail (DRM-free)        | A 1.0 .exe with DRM bypassed.                    | Yes       | Yes       |
| PC       | Retail (DRM-free, fixed) | A fixed 1.0 .exe with DRM bypassed.              | Yes       | Yes       |
| PC       | Demo (unpatched)         | The default .exe that comes with the demo.       | No        | ?         |
| PC       | Demo (patched)           | The patched .exe that comes with the demo.       | No        | ?         |
| PC       | Acclaim Demo (05-27)     | The .exe on the May 27, 2004 Acclaim demo.       | No        | ?         |
| PC       | Acclaim Demo (07-02)     | The .exe on the July 2, 2004 Acclaim demo.       | No        | ?         |
| Xbox     | Retail                   | The executable of the Xbox version.              | No        | ?         |
| Xbox     | Acclaim (05-05)          | The executable of the May 5, 2004 Xbox beta.     | No        | ?         |
| Xbox     | Acclaim (05-13)          | The executable of the May 13, 2004 Xbox beta.    | No        | ?         |
| Xbox     | Acclaim (07-13)          | The executable of the July 13, 2004 Xbox beta.   | No        | ?         |
| Xbox     | Acclaim (08-04)          | The executable of the August 4, 2004 Xbox beta.  | No        | ?         |
| PS2      | Retail (SLUS_208.72)     | The executable of the American PS2 version.      | No        | ?         |
| PS2      | Retail (SLES_530.44)     | The executable of the European PS2 version.      | No        | ?         |
| PS2      | Retail (SLES_531.51)     | The executable of the Italian PS2 version.       | No        | ?         |
| PS2      | Retail (SLPM_662.77)     | The executable of the Japanese PS2 version.      | No        | ?         |
| PS2      | Retail (SLKA_252.83)     | The executable of the Korean PS2 version.        | No        | ?         |
| PS2      | Acclaim (06-11)          | The executable of the June 11, 2004 PS2 beta.    | No        | ?         |
| PS2      | Acclaim (07-28)          | The executable of the July 28, 2004 PS2 beta.    | No        | ?         |


If any executables are missing from this table, please let me know.

# To-do
### Version 1
* Test and release
### Version 2: Registry
* Modify display settings without restriction:
  * Resolution
  * Widescreen
  * Windowed mode
  * Anti-aliasing (up to level 8)
### Version 3: Soundtrack
* Replace the in-game soundtrack with up to 128 of your own songs
### Unknown
* Console support (PS2 and Xbox)
* Legacy OS support (at least as far back as Windows XP)
* More game patches
  * Disable respect penalty for declining pink slips
  * Unlock all upgrades without CARS cheat
  * Edit starting cash and fallback cash (when you run out of money/cars)
  * Edit spectator bet scaling and thresholds (thanks to SxnnyB)
* Engine sound editor
  * Compile your own engine sounds
* Mod manager


# Licenses
If any of the below information is incorrect, please contact me and I will fix it.

**[PySide6](https://wiki.qt.io/Qt_for_Python)** is licensed under the **GNU Lesser General Public License**, version 3.

GNU LESSER GENERAL PUBLIC LICENSE

Version 3, 29 June 2007 

Copyright © 2007 Free Software Foundation, Inc. <https://fsf.org/>

Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed. 
This version of the GNU Lesser General Public License incorporates the terms and conditions of version 3 of the GNU General Public License, supplemented by the additional permissions listed below. 
0. Additional Definitions.
As used herein, “this License” refers to version 3 of the GNU Lesser General Public License, and the “GNU GPL” refers to version 3 of the GNU General Public License. 
“The Library” refers to a covered work governed by this License, other than an Application or a Combined Work as defined below. 
An “Application” is any work that makes use of an interface provided by the Library, but which is not otherwise based on the Library. Defining a subclass of a class defined by the Library is deemed a mode of using an interface provided by the Library. 
A “Combined Work” is a work produced by combining or linking an Application with the Library. The particular version of the Library with which the Combined Work was made is also called the “Linked Version”. 
The “Minimal Corresponding Source” for a Combined Work means the Corresponding Source for the Combined Work, excluding any source code for portions of the Combined Work that, considered in isolation, are based on the Application, and not on the Linked Version. 
The “Corresponding Application Code” for a Combined Work means the object code and/or source code for the Application, including any data and utility programs needed for reproducing the Combined Work from the Application, but excluding the System Libraries of the Combined Work. 
1. Exception to Section 3 of the GNU GPL.
You may convey a covered work under sections 3 and 4 of this License without being bound by section 3 of the GNU GPL. 
2. Conveying Modified Versions.
If you modify a copy of the Library, and, in your modifications, a facility refers to a function or data to be supplied by an Application that uses the facility (other than as an argument passed when the facility is invoked), then you may convey a copy of the modified version: 
a) under this License, provided that you make a good faith effort to ensure that, in the event an Application does not supply the function or data, the facility still operates, and performs whatever part of its purpose remains meaningful, or 
b) under the GNU GPL, with none of the additional permissions of this License applicable to that copy. 
3. Object Code Incorporating Material from Library Header Files.
The object code form of an Application may incorporate material from a header file that is part of the Library. You may convey such object code under terms of your choice, provided that, if the incorporated material is not limited to numerical parameters, data structure layouts and accessors, or small macros, inline functions and templates (ten or fewer lines in length), you do both of the following: 
a) Give prominent notice with each copy of the object code that the Library is used in it and that the Library and its use are covered by this License. 
b) Accompany the object code with a copy of the GNU GPL and this license document. 
4. Combined Works.
You may convey a Combined Work under terms of your choice that, taken together, effectively do not restrict modification of the portions of the Library contained in the Combined Work and reverse engineering for debugging such modifications, if you also do each of the following: 
a) Give prominent notice with each copy of the Combined Work that the Library is used in it and that the Library and its use are covered by this License. 
b) Accompany the Combined Work with a copy of the GNU GPL and this license document. 
c) For a Combined Work that displays copyright notices during execution, include the copyright notice for the Library among these notices, as well as a reference directing the user to the copies of the GNU GPL and this license document. 
d) Do one of the following: 
0) Convey the Minimal Corresponding Source under the terms of this License, and the Corresponding Application Code in a form suitable for, and under terms that permit, the user to recombine or relink the Application with a modified version of the Linked Version to produce a modified Combined Work, in the manner specified by section 6 of the GNU GPL for conveying Corresponding Source. 
1) Use a suitable shared library mechanism for linking with the Library. A suitable mechanism is one that (a) uses at run time a copy of the Library already present on the user's computer system, and (b) will operate properly with a modified version of the Library that is interface-compatible with the Linked Version. 
e) Provide Installation Information, but only if you would otherwise be required to provide such information under section 6 of the GNU GPL, and only to the extent that such information is necessary to install and execute a modified version of the Combined Work produced by recombining or relinking the Application with a modified version of the Linked Version. (If you use option 4d0, the Installation Information must accompany the Minimal Corresponding Source and Corresponding Application Code. If you use option 4d1, you must provide the Installation Information in the manner specified by section 6 of the GNU GPL for conveying Corresponding Source.) 
5. Combined Libraries.
You may place library facilities that are a work based on the Library side by side in a single library together with other library facilities that are not Applications and are not covered by this License, and convey such a combined library under terms of your choice, if you do both of the following: 
a) Accompany the combined library with a copy of the same work based on the Library, uncombined with any other library facilities, conveyed under the terms of this License. 
b) Give prominent notice with the combined library that part of it is a work based on the Library, and explaining where to find the accompanying uncombined form of the same work. 
6. Revised Versions of the GNU Lesser General Public License.
The Free Software Foundation may publish revised and/or new versions of the GNU Lesser General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns. 
Each version is given a distinguishing version number. If the Library as you received it specifies that a certain numbered version of the GNU Lesser General Public License “or any later version” applies to it, you have the option of following the terms and conditions either of that published version or of any later version published by the Free Software Foundation. If the Library as you received it does not specify a version number of the GNU Lesser General Public License, you may choose any version of the GNU Lesser General Public License ever published by the Free Software Foundation. 
If the Library as you received it specifies that a proxy can decide whether future versions of the GNU Lesser General Public License shall apply, that proxy's public statement of acceptance of any version is permanent authorization for you to choose that version for the Library. 


**[PyInstaller](https://pyinstaller.org/en/stable/)** is licensed under the **GNU General Public License**, version 2. Juiced Editor falls under the following Bootloader Exception:

Bootloader Exception

In addition to the permissions in the GNU General Public License, the
authors give you unlimited permission to link or embed compiled bootloader
and related files into combinations with other programs, and to distribute
those combinations without any restriction coming from the use of those
files. (The General Public License restrictions do apply in other respects;
for example, they cover modification of the files, and distribution when
not linked into a combined executable.)


**[Auto PY to EXE](https://github.com/brentvollebregt/auto-py-to-exe)** is licensed under the **MIT License**.

MIT License

Copyright (c) 2018 Brent Vollebregt

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
