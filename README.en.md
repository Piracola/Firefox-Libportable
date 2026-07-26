# Firefox-Libportable

[![Build](https://img.shields.io/github/actions/workflow/status/Piracola/Firefox-Libportable/Firefox-Portable-Package.yml?style=flat-square&label=Build)](https://github.com/Piracola/Firefox-Libportable/actions/workflows/Firefox-Portable-Package.yml)
[![Release](https://img.shields.io/github/v/release/Piracola/Firefox-Libportable?style=flat-square&label=Release&color=blue)](https://github.com/Piracola/Firefox-Libportable/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/Piracola/Firefox-Libportable/total?style=flat-square&label=Downloads)](https://github.com/Piracola/Firefox-Libportable/releases)
[![License](https://img.shields.io/github/license/Piracola/Firefox-Libportable?style=flat-square&label=License)](LICENSE)

[简体中文](README.md) | **English**

A ready-to-run **portable build of Firefox**, rebuilt daily to keep up with official releases.

The browser itself comes straight from Mozilla's official installer and is made portable with [libportable](https://github.com/adonais/libportable): all data stays inside the folder you extracted, nothing is written to the registry, nothing pollutes the system, and you can carry the whole thing around on a USB stick.

## Quick start

1. Open the [latest release](https://github.com/Piracola/Firefox-Libportable/releases/latest).
2. Download `Firefox_<version>.7z`.
3. Extract it anywhere you like, for example `D:\Browser\Firefox`.
4. Double-click `开始.bat`; it creates a shortcut in the same folder.
5. Use that shortcut to start the browser from then on.

> **Do not download `Source code.zip` / `Source code.tar.gz`.** Those are the repository sources and contain no browser at all.

## Verifying your download

Every release ships a `.sha256` checksum file, and the hash is also written into the release notes. If security matters to you, it is worth checking:

```powershell
Get-FileHash .\Firefox_153.0.7z -Algorithm SHA256
```

The hash it prints should match the one in the release notes exactly.

## Directory layout

This is what you get after extracting; `Profiles/` and `Cache/` are created automatically on first run:

```text
Extracted folder/
├── Firefox/                      The browser itself
│   ├── firefox.exe
│   ├── portable.ini              Portable build configuration
│   ├── portable64.dll            Portable runtime
│   ├── README                    libportable documentation
│   └── LICENSE-libportable.txt   libportable license
├── Profiles/                     User data: bookmarks, extensions, sign-ins, passwords
├── Cache/                        Cache
├── 开始.bat                      Script that creates the shortcut
└── Firefox.lnk                   The shortcut created by running 开始.bat
```

**`Profiles/` is the one that matters.** As long as that directory survives, so does your browser data.

## Updating to a new version

When updating, replace only the browser itself and keep `Profiles/`:

1. Close Firefox completely.
2. Rename the old `Firefox` directory to `Firefox_old` as a backup.
3. Extract the `Firefox` directory from the new archive into the same place.
4. Start the browser and confirm that your bookmarks, extensions, and sign-ins are all intact.
5. Once you are satisfied, delete `Firefox_old`.

> Do not delete the whole extracted folder and start over from the new archive; that takes everything in `Profiles/` with it.

## Configuration

The configuration file lives at `Firefox/portable.ini`, and normally you do not need to touch it. The settings people actually use:

| Setting | Default | Description |
|--------|--------|------|
| `Portable` | `1` | Portable mode switch; set it to `0` to fall back to the behavior of a normal installation |
| `PortableDataPath` | `../Profiles` | User data directory, resolved relative to `Firefox/` |
| `TmpDataPath` | `../Cache` | Cache directory |
| `DisableScan` | `0` | Set to `1` to stop the browser from scanning the registry for third-party extensions and plugins |
| `Update` | `0` | libportable's own third-party update channel; leave it off |
| `Bosskey` | empty | Boss key, configure it however you like |

Changes take effect only after restarting the browser. See `Firefox/README` for the full list of settings.

## How portability is guaranteed

"The build succeeded" is not the same as "it is genuinely portable", so every package has to pass two checks before it is published:

1. **Static check**: read the PE import table of `mozglue.dll` and confirm that the portable runtime really was injected.
2. **Runtime check**: launch the browser once headless and confirm that user data really lands in `Profiles/` rather than in the system's `%APPDATA%`.

If either check fails, the build fails and nothing is published. That is what catches injection silently going dead — for example when a major Firefox release stops the portable patching hooks from taking effect.

The installer itself is also compared byte for byte against the `SHA512SUMS` published by Mozilla right after download, and any mismatch aborts the build immediately.

## Automated builds

This repository stores no browser files; the packages are built automatically by GitHub Actions every day. The repository contains only three things:

| File | Purpose |
|------|------|
| `libportable/portable.ini` | The portable patching configuration specific to Firefox |
| `开始.bat` | The launcher script that creates the shortcut |
| `.github/workflows/` | The workflow that calls the shared builder |

All the download, verification, extraction, injection, and packaging logic lives in the shared builder, [Browser-builder](https://github.com/Piracola/Browser-builder), which all three browser repositories run through.

## Building locally

Regular users can skip this section. For maintainers who want to reproduce a build locally:

```powershell
# Prerequisites: Python 3.10+ and 7-Zip
git clone https://github.com/Piracola/Browser-builder.git builder
pip install -r builder/requirements.txt

# Build the latest version
python builder/build.py --browser firefox --auto-version `
  --libportable libportable --launcher 开始.bat

# For the Simplified Chinese Firefox
python builder/build.py --browser firefox --auto-version --lang zh-CN `
  --libportable libportable --launcher 开始.bat
```

The result is `Firefox_<version>.7z` in the current directory.

## FAQ

### Which file should I download?

`Firefox_<version>.7z`. `Source code` is the repository source and is of no use as a browser.

### Can I keep it on a USB stick?

Yes, that is exactly what a portable build is for. Prefer a simple path such as `U:\Firefox` so you do not run into overly long paths or special characters.

### Where is my data stored?

In `Profiles/`, inside the folder you extracted. To back up or migrate, just keep that directory.

### The shortcut was not created. What now?

First check that `Firefox\firefox.exe` exists. If it does, you can double-click it directly and the browser will start fine; `开始.bat` only exists to generate a convenient shortcut for you.

### My antivirus flags it. Is that normal?

Portable patching has to modify the browser's module import table, and security software often flags that kind of change as a false positive. Download only from this project's release page, verify the package against the SHA-256 checksum described above, and then decide for yourself whether to trust it.

### The interface is in English. Can I switch it to Chinese?

Yes. Open `Settings → General → Language` in the browser and add the Chinese language pack. You can also build a Chinese installer yourself with `--lang zh-CN`.

## Related projects

| Project | Description |
|------|------|
| [Browser-builder](https://github.com/Piracola/Browser-builder) | The shared builder |
| [Floorp_portable](https://github.com/Piracola/Floorp_portable) | Portable Floorp |
| [Zen-Libportable](https://github.com/Piracola/Zen-Libportable) | Portable Zen |
| [libportable](https://github.com/adonais/libportable) | The upstream portable runtime |

## License

This repository is released under the MIT License; see [LICENSE](LICENSE) for details.

Firefox is a trademark of the Mozilla Foundation, and the browser itself remains copyright Mozilla. The libportable component used for portable patching is covered by its own license and is distributed together with the package.
