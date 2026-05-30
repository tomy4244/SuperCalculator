@echo off
chcp 65001 > nul
set PY=%LOCALAPPDATA%\Programs\Python\Python312\python.exe
set PI=%LOCALAPPDATA%\Programs\Python\Python312\Scripts\pyinstaller.exe

echo [1/2] 安装依赖...
"%PY%" -m pip install pywebview pyinstaller --quiet

echo [2/2] 打包中，请稍候...
"%PI%" --onefile --windowed ^
  --add-data "c.html;." ^
  --hidden-import "webview.platforms.edgechromium" ^
  --hidden-import "webview.platforms.mshtml" ^
  --icon "app_icon.ico" ^
  --name "超市计算器" ^
  --distpath dist ^
  --workpath build ^
  --specpath . ^
  main.py

if exist "dist\超市计算器.exe" (
  copy /Y "dist\超市计算器.exe" "%USERPROFILE%\Desktop\超市计算器.exe" > nul
  echo.
  echo 打包成功！桌面已生成 超市计算器.exe
) else (
  echo.
  echo 打包失败，请查看上方错误信息。
)
pause
