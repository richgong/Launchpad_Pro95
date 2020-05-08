# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.7 (default, May  4 2020, 14:16:01) 
# [Clang 10.0.1 (clang-1001.0.46.4)]
# Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/MPK_mini/__init__.py
# Compiled at: 2020-01-09 05:21:34
from __future__ import absolute_import, print_function, unicode_literals
from _Generic.GenericScript import GenericScript
import Live
from .config import *

def create_instance(c_instance):
    """ The generic script can be customised by using parameters (see config.py). """
    return GenericScript(c_instance, Live.MidiMap.MapMode.absolute, Live.MidiMap.MapMode.absolute, DEVICE_CONTROLS, TRANSPORT_CONTROLS, VOLUME_CONTROLS, TRACKARM_CONTROLS, BANK_CONTROLS, CONTROLLER_DESCRIPTION)


from _Framework.Capabilities import *

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=2536, product_ids=[124], model_name=b'MPK mini'), 
       PORTS_KEY: [
                 inport(props=[NOTES_CC, REMOTE, SCRIPT]), outport(props=[SCRIPT])]}
# okay decompiling __init__.pyc
