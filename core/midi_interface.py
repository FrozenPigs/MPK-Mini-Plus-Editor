#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# MPK-Mini-Plus-editor
# Copyright (C) 2025  Jesse G
# Original work derived from
# MPK M2-editor
# Copyright (C) 2017  Damien Picard dam.pic AT free.fr
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Interface with Akai MPK Plus."""
import time

import rtmidi

from core.config import Config


class AkaiMPKPlus():
    """Midi interface for Akai MPK mini plus."""

    GET_CONFIG = [240, 126, 6, 1, 127, 240, 71, 127, 84, 102, 0, 1, 1, 247]

    def __init__(self):
        """Init config and midi connection."""
        self.midi_config = Config()
        self.connected = self.midi_setup()

    # pylint: disable=no-member
    def midi_setup(self):
        """Create the midi connection."""
        self.mo = rtmidi.MidiOut()
        self.mi = rtmidi.MidiIn()

        is_out_open, is_in_open = False, False
        for i, p in enumerate(self.mo.get_ports()):
            if any(mpk in p for mpk in ('MPKmini', 'MPK mini')):
                if not self.mo.is_port_open():
                    self.mo.open_port(i)
                is_out_open = True
        for i, p in enumerate(self.mi.get_ports()):
            if any(mpk in p for mpk in ('MPKmini', 'MPK mini')):
                if not self.mi.is_port_open():
                    self.mi.open_port(i)
                    self.mi.ignore_types(sysex=False)
                is_in_open = True

        if not is_out_open and not is_in_open:
            return False
        return True

    def send_midi_message(self, out_message):
        """Send out_message to the midi controler."""
        # print('out:', out_message)

        in_message = [[]]
        self.mo.send_message(out_message)
        time.sleep(0.1)
        in_message = self.mi.get_message()
        while in_message and len(in_message[0]) < 2902:
            in_message = self.mi.get_message()

        # print('in:', in_message)
        if in_message is not None:
            in_message = in_message[0]    # strip midi time
        return in_message

    def get_programme(self, p_i):
        """Get programme p_i from the midi controller.

        Returns a config dataclass of parsed response.
        """
        out_message = self.GET_CONFIG[:]
        out_message[12] = p_i
        # print('out', out_message)
        in_message = self.send_midi_message(out_message)
        # print('in', in_message)
        config = Config()
        try:
            config.parse_config(in_message)
        except TypeError:
            self.midi_setup()
        return config
