# Firefox-Libportable

[![Build Status](https://img.shields.io/github/actions/workflow/status/Piracola/Firefox-Libportable/Firefox-Portable-Package.yml?style=flat-square&label=构建状态)](https://github.com/Piracola/Firefox-Libportable/actions/workflows/Firefox-Portable-Package.yml)
[![Latest Release](https://img.shields.io/github/v/release/Piracola/Firefox-Libportable?style=flat-square&label=最新版本&color=blue)](https://github.com/Piracola/Firefox-Libportable/releases/latest)
[![License](https://img.shields.io/github/license/Piracola/Firefox-Libportable?style=flat-square&label=许可证)](LICENSE)

**开箱即用的 Firefox 浏览器便携版**

本项目基于 libportable，对 Firefox 浏览器进行自动化便携版打包。

## 🚀 快速开始

1. **下载**: [📥 下载最新版本](https://github.com/Piracola/Firefox-Libportable/releases/latest)
2. **解压**: 将压缩包解压到任意目录（如 `D:\Browser\Firefox`）。
3. **运行**: 双击 `开始.bat`，脚本将自动创建快捷方式。

## 🔄 更新指南

仅需替换浏览器本体目录即可完成升级：

1. 将旧版 `Firefox` 目录重命名为 `Firefoxold`（备份）。
2. 将新版 `Firefox` 目录复制到同级位置。
3. 启动浏览器验证，确认无误后可删除备份。

## ⚙️ 高级配置

配置文件位于 `Firefox/portable.ini`：

```ini
[Portable]
DataPath=..\Profile
CachePath=..\Cache
```

## 🔗 相关项目

本仓库通过 GitHub Actions 检出并调用主构建仓库 [Browser-builder](https://github.com/Piracola/Browser-builder) 中的通用脚本。

| 项目 | 说明 | 地址 |
|------|------|------|
| Browser-builder | 通用构建脚本 | [Piracola/Browser-builder](https://github.com/Piracola/Browser-builder) |
| Firefox-Libportable | Firefox 便携版（当前项目） | [Piracola/Firefox-Libportable](https://github.com/Piracola/Firefox-Libportable) |
| Floorp_portable | Floorp 便携版 | [Piracola/Floorp_portable](https://github.com/Piracola/Floorp_portable) |
| Zen-Libportable | Zen 便携版 | [Piracola/Zen-Libportable](https://github.com/Piracola/Zen-Libportable) |

## 📄 许可证

本项目采用 **MIT 许可证**。详见 [LICENSE](LICENSE) 文件。

<p>
  Made with ❤️ by <a href="https://github.com/Piracola">Piracola</a>
</p>
