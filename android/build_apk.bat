@echo off
chcp 65001 > nul
title 超市计算器 - Android APK 编译

set JAVA_HOME=C:\Program Files\JetBrains\PyCharm Community Edition 2024.3.1.1\jbr
set ANDROID_HOME=%LOCALAPPDATA%\Android\Sdk
set GRADLE=%USERPROFILE%\.gradle\wrapper\dists\gradle-8.2.1-all\d8pvvlun5bx6sdtwqhf8y9z4b\gradle-8.2.1\bin\gradle.bat

echo [1/2] 正在编译 Android APK，请稍候（首次约需 3-5 分钟下载依赖）...
cd /d "%~dp0"
call "%GRADLE%" assembleRelease --stacktrace

if exist "app\build\outputs\apk\release\app-release.apk" (
    copy /Y "app\build\outputs\apk\release\app-release.apk" "..\超市计算器.apk" > nul
    echo.
    echo ✓ 编译成功！
    echo   APK 路径：%~dp0..\超市计算器.apk
) else (
    echo.
    echo ✗ 编译失败，请查看上方错误信息。
)
pause
