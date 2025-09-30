# Firefox-Libportable

基于 libportable 的浏览器便携版自动化打包项目，支持 Zen 浏览器和 Firefox 浏览器

## 项目简介

本项目使用 [**libportable**](https://github.com/adonais/libportable)工具实现浏览器便携版的自动化打包。通过 GitHub Actions 工作流，自动检测新版本并生成便携版安装包。

## 支持的浏览器

- [**Zen 浏览器**](https://github.com/Piracola/Zen-Libportable)：基于 Firefox 的增强浏览器
- **Firefox 浏览器**：开源网页浏览器

## 核心功能

- **自动版本检测**：定时检查浏览器最新版本
- **多触发构建**：支持手动、代码提交和定时触发
- **便携化处理**：使用 libportable 进行 DLL 注入和便携化
- **自动发布**：构建完成后自动上传到 GitHub Release

## 使用方式

### 自动触发构建
- **代码提交**：推送到 main 或 master 分支时自动构建
- **定时构建**：每天 UTC 时间 0 点（北京时间 8 点）自动检查更新

**注意**：每次触发都会同时检查 Zen 浏览器和 Firefox 浏览器的更新，如果检测到新版本，则会自动构建对应的便携版。构建产物将自动发布到 GitHub Release。

## 许可证

MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。
