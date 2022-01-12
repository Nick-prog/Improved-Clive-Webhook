from cx_Freeze import setup, Executable
import Webhook

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', base=base, target_name = 'Webhook', icon = 'C:/Users/KUNRR004/Documents/VSCode/New Webhook/images/TAMUK Logo 3.ico')
]

setup(name='Webhook',
      version = Webhook.__version__,
      description = Webhook.__description__,
      options = {'build_exe': build_options},
      executables = executables)
