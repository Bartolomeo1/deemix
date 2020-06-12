"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

import os
from setuptools import setup

def tree(src):
    return [(root, map(lambda f: os.path.join(root, f), files))
        for (root, dirs, files) in os.walk(os.path.normpath(src))]

APP = ['deemix_gui.py']
DATA_FILES = ['webui/public', 'icon.icns']
OPTIONS = {
    'argv_emulation': False,
    'strip': True,
    'iconfile': 'icon.icns',
    'includes': ['WebKit', 'Foundation', 'webview', 'flask', 'flask-socketio', 'deemix']
    }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
