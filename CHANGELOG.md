# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4] - 2021-06-10
### Fixed
- More accurately calculates expected size of plots.
- Archival requires only minimal extra space on target drive.
  The required space is based on the size of the actual plot to be transferred.
  Previously a 20% (~20GB) margin was required relative to a rough approximation of plot size.
- Identify more cases of chia plotting processes such as on NixOS.
- Avoid some more `NoSuchProcess` and `AccessDenied` errors when identifying plotting processes.
- Avoid crashing when parsing plotting process logs fails to decode due to `UnicodeDecodeError`.
- Avoid crashing when a tmp file is removed while we are checking a job's tmp usage.
- Windows is not yet supported, but plot and archive processes are now launched to be independent of the plotman process on Windows as it already was on Linux.
### Added
- Configuration file is versioned.
  The config for previous plotman versions has been retroactively defined to be version 0
  The new version is 1.
  An error will be raised when you launch plotman with a configuration file whose version does not match the expected configuration version.
  That error will include a link to the wiki to help understand the needed changes.
  See [the wiki configuration page](https://github.com/ericaltendorf/plotman/wiki/Configuration#1-v04).
- Archiving configuration has been reworked offering both a simple builtin local archiving setup as well as arbitrary configuration of the disk space check and transfer operations.
  See [the wiki archiving page](https://github.com/ericaltendorf/plotman/wiki/Archiving)
- The `directories:` `dst:` section is optional.
  If not specified then generally the tmp drive for the plot will be used as dst.
  If tmp2 is specified then it will be used as dst.
- Along with plot logs, there are now archive transfer logs and an overall plotman log.
  This helps with diagnosing issues with both the archival disk space check and the archival transfers.
  The paths are configurable under `logging:` via `plots:` (directory), `transfers:` (directory), and `application:` (file).
- Added support for `-c`/`--pool_contract_address`.
  Configurable as `plotting:` `pool_contract_address:`.
- Interactive can be launched with plotting and archiving inactive.
  This is available via the configuration file in `commands:` `interactive:` `autostart_plotting:` and `autostart_archiving:`.
  They are also available on the command line as `--[no-]autostart-plotting` and `--[no-]autostart-archiving`. 
- Uses `i` to differentiate between gigabytes vs. gibibytes, for example.
  `Gi` vs. `G`.

## [0.3.1] - 2021-05-13
Changes not documented.
Bug fixes for v0.3.1.

## [0.3] - 2021-05-12
Changes not documented.

## [0.2] - 2021-04-20
Changes not documented.

## [0.1.1] - 2021-02-07
### Fixed
- Find jobs more reliably by inspecting cmdline instead of "process name"
- checked-in config.yaml now conforms to code's expectations!
### Added
- Job progress histogram view in `interactive` mode
- Ability to disable archival (by commenting out the config section)
- Minor improvements to messages, titles, tables in interactive mode

## [0.1.0] - 2021-01-31
### Fixed
- Fixed issue with prioritization of tmp dirs

## [0.0.1] - 2021-01-30
### Added
- `.gitignore` and `CHANGELOG.md`
