@echo off
if exist "%~dp0firefox.exe" (echo.) && if exist "%~dp0mozglue.dll" (
echo 已找到需要注入的文件firefox.exe. 
goto platform
) else (
echo 没找到相关文件,请把程序放入浏览器的安装目录执行.
goto eof
)

:platform
if exist "%~dp0upcheck.exe" del /s/q "%~dp0upcheck.exe" 2>nul 1>nul
if exist "%~dp0upcheck32.exe" (
    upcheck32.exe -file 2>nul
) else (
    if exist "%~dp0upcheck64.exe" upcheck64.exe -file 2>nul
)
if "%errorlevel%"=="32" set bits=32&goto x86
if "%errorlevel%"=="64" set bits=64&goto x64
goto eof

:x86
@echo ***********************************************************************
@echo *                程序自动注入32位的Firefox浏览器                      *
@echo ***********************************************************************
echo+
@pause .
if exist "%~dp0upcheck32.exe" rename upcheck32.exe upcheck.exe 2>nul
goto runing

:x64
echo+
@echo ***********************************************************************
@echo *                程序自动注入64位的Firefox浏览器                      *
@echo ***********************************************************************
echo+
@pause .
if exist "%~dp0upcheck64.exe" rename upcheck64.exe upcheck.exe 2>nul

:runing
if exist "%~dp0upcheck.exe" upcheck.exe -dll 2>nul
if "%errorlevel%"=="0" echo 注入成功,请仔细阅读README和portable(example).ini文件!&goto eof
echo 程序注入失败, 请参考错误信息, 或许你之前注入过.

:eof
pause .
@del /s/q setdll*.exe 2>nul 1>nul
if "%bits%"=="32" del /s/q portable64.dll upcheck64.exe 2>nul 1>nul
if "%bits%"=="64" del /s/q portable32.dll upcheck32.exe 2>nul 1>nul
if not exist %~dp0portable.ini copy /y %~dp0portable(example).ini %~dp0portable.ini 2>nul 1>nul
@del /q %0 2>nul 1>nul
