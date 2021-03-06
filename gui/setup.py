from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', base=base, targetName = 'GeniusBar.exe')
]

setup(name='GeniusBar',
      version = '1.0',
      description = 'geeng',
      options = dict(build_exe = buildOptions),
      executables = executables)
