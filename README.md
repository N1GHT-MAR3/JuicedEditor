# Juiced Editor
An all-in-one editor for the 2005 racing game. Still a work-in-progress.

There are pre-release versions available in [Releases](https://github.com/N1GHT-MAR3/JuicedEditor/releases), but bear in mind that these are not properly tested. I offer no guarantees that these will work.

# Features
* Restore online functionality courtesy of [OpenSpy](http://beta.openspy.net/en/)
* Enable in-game cheat codes locked by the developers
* Change when cars are unlocked in Career mode

Many more features are planned in the future!

# Compatibility
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
| Xbox     | Acclaim (08-30)          | The executable of the August 30, 2004 Xbox beta. | No        | ?         |
| PS2      | Retail (SLUS_208.72)     | The executable of the American PS2 version.      | No        | ?         |
| PS2      | Retail (SLES_530.44)     | The executable of the European PS2 version.      | No        | ?         |
| PS2      | Retail (SLES_531.51)     | The executable of the Italian PS2 version.       | No        | ?         |
| PS2      | Retail (SLPM_662.77)     | The executable of the Japanese PS2 version.      | No        | ?         |
| PS2      | Retail (SLKA_252.83)     | The executable of the Korean PS2 version.        | No        | ?         |
| PS2      | Acclaim (06-11)          | The executable of the June 11, 2004 PS2 beta.    | No        | ?         |
| PS2      | Acclaim (07-28)          | The executable of the July 28, 2004 PS2 beta.    | No        | ?         |


If any executables are missing from this table, please let me know.

# Modules used
* [PyQt6](https://www.riverbankcomputing.com/software/pyqt/)
* [PyInstaller](https://pyinstaller.org/)
* [Auto PY to EXE](https://github.com/brentvollebregt/auto-py-to-exe)

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
* More game patches
  * Disable respect penalty for declining pink slips
  * Unlock all upgrades without CARS cheat
  * Edit starting cash and fallback cash (when you run out of money/cars)
  * Edit spectator bet scaling and thresholds (thanks to SxnnyB)
* Engine sound editor
  * Compile your own engine sounds
* Mod manager
