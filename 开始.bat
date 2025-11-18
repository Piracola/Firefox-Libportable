@echo off
setlocal enabledelayedexpansion

:: 设置目标文件路径
set "targetDir=Firefox"
set "targetExe=firefox.exe"
set "targetPath=%~dp0%targetDir%\%targetExe%"

:: 检查目标文件是否存在
if not exist "%targetPath%" (
    echo 错误: 未找到 %targetPath%
    pause
    exit /b 1
)

:: 设置快捷方式名称和路径
set "shortcutName=Firefox浏览器.lnk"
set "shortcutPath=%~dp0%shortcutName%"

:: 创建VBS脚本来生成快捷方式
set "vbsScript=%temp%\CreateShortcut.vbs"

echo Set oWS = WScript.CreateObject("WScript.Shell") > "%vbsScript%"
echo sLinkFile = "%shortcutPath%" >> "%vbsScript%"
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> "%vbsScript%"
echo oLink.TargetPath = "%targetPath%" >> "%vbsScript%"
echo oLink.WorkingDirectory = "%~dp0%targetDir%" >> "%vbsScript%"
echo oLink.Description = "Firefox便携版" >> "%vbsScript%"
echo oLink.Save >> "%vbsScript%"

:: 执行VBS脚本创建快捷方式
cscript //nologo "%vbsScript%"

:: 删除临时VBS脚本
del "%vbsScript%"

pause