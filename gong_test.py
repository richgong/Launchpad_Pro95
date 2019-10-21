import sys


def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)


for path in [
    '/Applications/Ableton Live 10 Standard.app/Contents/App-Resources/Python/lib',
    '/Applications/Ableton Live 10 Standard.app/Contents/App-Resources/Python/site-packages/raven-5.8.1-py2.7.egg',
    '/Applications/Ableton Live 10 Standard.app/Contents/App-Resources/Python/site-packages/setuptools-28.7.1-py2.7.egg',
    '/Applications/Ableton Live 10 Standard.app/Contents/App-Resources/Python/site-packages/decorator-3.3.2-py2.5.egg',
    '/Applications/Ableton Live 10 Standard.app/Contents/App-Resources/Python/site-packages/python',
    '/Applications/Ableton Live 10 Standard.app/Contents/App-Resources/Python/site-packages/abl.util-0.1.16-py2.7.egg',
    '/Applications/Ableton Live 10 Standard.app/Contents/App-Resources/Python/site-packages/abl.vpath-0.8.2-py2.7.egg',
    '/Applications/Ableton Live 10 Standard.app/Contents/App-Resources/Python/site-packages/multipledispatch-0.4.8-py2.7.egg',
    '/Applications/Ableton Live 10 Standard.app/Contents/App-Resources/Python/site-packages/pkg_resources',
    '/Applications/Ableton Live 10 Standard.app/Contents/App-Resources/Python/abl.live',
    '/Applications/Ableton Live 10 Standard.app/Contents/App-Resources/MIDI Remote Scripts/'
]:
    add_path(path)

import code
code.interact("HI")