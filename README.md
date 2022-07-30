# Juiced Editor
An all-in-one editor for the 2005 racing game. Still a work-in-progress.

There are pre-release versions available in [Releases](https://github.com/N1GHT-MAR3/JuicedEditor/releases), but bear in mind that these are not properly tested. I offer no guarantees that these will work.

# Features
* Restore online functionality courtesy of [OpenSpy](http://beta.openspy.net/en/)
* Enable in-game cheat codes locked by the developers
* Change when cars are unlocked in Career mode

Many more features are planned in the future!

# Compatibility
| Executable           | Description                                   | Supported | Decrypted |
| --------------       | ------------------------------------          | --------- | --------- |
| PC (unpatched)       | The default .exe that comes on disc.          | Yes       | No        |
| PC (patched)         | The 1.1 patched .exe.                         | Yes       | No        |
| PC (DRM-free)        | A 1.0 .exe with DRM bypassed.                 | Yes       | Yes       |
| PC (DRM-free, fixed) | A fixed 1.0 .exe with DRM bypassed.           | Yes       | Yes       |
| PS2 (SLUS_208.72)    | The American executable of the PS2 version.   | No        | ?         |
| PS2 (SLES_530.44)    | The European executable of the PS2 version.   | No        | ?         |
| PS2 (SLES_531.51)    | The Italian executable of the PS2 version.    | No        | ?         |
| PS2 (SLPM_662.77)    | The Japanese executable of the PS2 version.   | No        | ?         |
| PS2 (SLKA_252.83)    | The Korean executable of the PS2 version.     | No        | ?         |
| Xbox (default.xbe)   | The executable of the Xbox version.           | No        | ?         |

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
