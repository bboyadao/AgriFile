# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules
contrib = collect_submodules('django.contrib')
whitenoise = collect_submodules('whitenoise')
filter = collect_submodules('django-filter')
crispy = collect_submodules('django-crispy-forms')

all_hidden_imports = contrib + whitenoise + filter + crispy
block_cipher = None

a = Analysis(
    ['manage.py'],
    pathex=[],
    binaries=[],
    datas=[
             ("templates", "templates"),
             ("staticfiles", "staticfiles"),
             ("static", "static"),
             ("storage", "storage"),
             ("venv/Lib/site-packages/crispy_forms", "crispy_forms"),
             ("venv/Lib/site-packages/django_filters", "django_filters"),
         ],
    hiddenimports=all_hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='AgriFile',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='AgriFile',
)
