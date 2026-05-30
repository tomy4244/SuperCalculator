# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\tomy\\Desktop\\超市计算器_app\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\tomy\\Desktop\\超市计算器_app\\c.html', '.')],
    hiddenimports=['webview.platforms.edgechromium', 'webview.platforms.mshtml'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='超市计算器',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='C:\\Users\\tomy\\Desktop\\超市计算器_app\\app_icon.ico',
)
