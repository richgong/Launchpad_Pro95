# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.7 (default, May  4 2020, 14:16:01) 
# [Clang 10.0.1 (clang-1001.0.46.4)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/MPK_mini/config.py
# Compiled at: 2020-01-09 05:21:34
from __future__ import absolute_import, print_function, unicode_literals
from .consts import *
TRANSPORT_CONTROLS = {b'STOP': -1, 
   b'PLAY': -1, 
   b'REC': -1, 
   b'LOOP': -1, 
   b'RWD': -1, 
   b'FFWD': -1}
DEVICE_CONTROLS = (
 GENERIC_ENC1,
 GENERIC_ENC2,
 GENERIC_ENC3,
 GENERIC_ENC4,
 GENERIC_ENC5,
 GENERIC_ENC6,
 GENERIC_ENC7,
 GENERIC_ENC8)
VOLUME_CONTROLS = (
 (-1, -1),
 (-1, -1),
 (-1, -1),
 (-1, -1),
 (-1, -1),
 (-1, -1),
 (-1, -1),
 (-1, -1))
TRACKARM_CONTROLS = (-1, -1, -1, -1, -1, -1, -1, -1)
BANK_CONTROLS = {b'TOGGLELOCK': -1, 
   b'BANKDIAL': -1, 
   b'NEXTBANK': -1, 
   b'PREVBANK': -1, 
   b'BANK1': -1, 
   b'BANK2': -1, 
   b'BANK3': -1, 
   b'BANK4': -1, 
   b'BANK5': -1, 
   b'BANK6': -1, 
   b'BANK7': -1, 
   b'BANK8': -1}
PAD_TRANSLATION = (
 (0, 0, 36, 0),
 (1, 0, 37, 0),
 (2, 0, 38, 0),
 (3, 0, 39, 0),
 (0, 1, 32, 0),
 (1, 1, 33, 0),
 (2, 1, 34, 0),
 (3, 1, 35, 0),
 (0, 2, 48, 0),
 (1, 2, 49, 0),
 (2, 2, 50, 0),
 (3, 2, 51, 0),
 (0, 3, 44, 0),
 (1, 3, 45, 0),
 (2, 3, 46, 0),
 (3, 3, 47, 0))
CONTROLLER_DESCRIPTION = {b'INPUTPORT': b'MPK mini', 
   b'OUTPUTPORT': b'MPK mini', 
   b'CHANNEL': -1, 
   b'PAD_TRANSLATION': PAD_TRANSLATION}
MIXER_OPTIONS = {b'NUMSENDS': 2, 
   b'SEND1': (-1, -1, -1, -1, -1, -1, -1, -1), 
   b'SEND2': (-1, -1, -1, -1, -1, -1, -1, -1), 
   b'MASTERVOLUME': -1}
# okay decompiling config.pyc
