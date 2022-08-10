# Change Log

## [Unrelease]
### Added

### Fixed

### Changed

### Removed

## [1.0.0] - 2022/08/10
### Added
- Add the python code `generatePkgConfig.py` to generate `.pc` file for the command `pkg-config`.
- Add makefile to install and uninstall libtorch.

### Fixed
- Fixed the bug that the makefile cannot copy libtorch to `/opt`.
- Fixed the bug that compiling code would fail using makefile because compiler need some flags in `.pc` file.
