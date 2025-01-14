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

"""Config for MPK mini plus."""
from dataclasses import Field, dataclass, field, fields


@dataclass(order=True)
class Config():    # pylint: disable=too-many-instance-attributes
    """Dataclass reperestation of MPK mini Plus config."""

    start_sysex: list[int] = field(default_factory=list)
    programme: int = 1
    title: list[int] = field(default_factory=list)
    pad_channel: int = 1
    pad_aftertouch: int = 0
    key_channel: int = 0
    key_octave: int = 4
    key_transpose: int = 12
    transport: int = 0
    arp_on: int = 0
    arp_mode: int = 0
    arp_time_div: int = 2
    arp_clock: int = 1
    arp_latch: int = 0
    arp_swing: int = 0
    arp_tempo_taps: int = 3
    arp_tempo: list[int] = field(default_factory=list)
    arp_octave: int = 0
    arp_gate: int = 50
    note_repeat_time_div: int = 4
    note_repeat_on: int = 0
    cv_trigger_source: int = 0
    cv_note_priority: int = 0
    cv_gate_mode: int = 0
    cv_mod_source: int = 0
    cv_bend_range: int = 2
    cv_clock_in_div: int = 2
    cv_clock_out_div: int = 6
    scale_on: int = 0
    scale_key: int = 0
    scale_type: int = 1
    scale_non_s_note: int = 0
    chord_on: int = 0
    chord_type: int = 0
    chord_inversion: int = 0
    joystick_x_mode: int = 2
    joystick_x_cc1: int = 14
    joystick_x_cc2: int = 14
    joystick_y_mode: int = 2
    joystick_y_cc1: int = 15
    joystick_y_cc2: int = 15
    pads: dict[int:list[int]] = field(default_factory=dict)
    knobs: dict[int:list[int]] = field(default_factory=dict)
    sysex_end: list[int] = field(default_factory=list)
    sysex_pad: list[int] = field(default_factory=list)
    sysex_final: int = 247

    def add_values(self, values):
        """Add values from dict."""
        for key, value in values.items():
            if isinstance(value, bool):
                value = 1 if value else 0
            object.__setattr__(self, key, value)

    def __init__(self):
        """Initiate lists and dicts."""
        self.start_sysex = [240, 71, 127, 84, 100, 22, 78]
        self.title = [82, 80, 82, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.arp_tempo = [0, 120]
        # note, cc, pg, mode, toggle, on_color, off_color
        self.pads = {
            1: [36, 1, 0, 2, 1, 6, 24],
            2: [37, 2, 1, 2, 1, 6, 24],
            3: [38, 3, 2, 2, 1, 6, 24],
            4: [39, 4, 3, 2, 1, 6, 24],
            5: [40, 5, 4, 2, 1, 6, 24],
            6: [41, 6, 5, 2, 1, 6, 24],
            7: [42, 7, 6, 2, 1, 6, 24],
            8: [43, 8, 7, 2, 1, 6, 24],
            9: [44, 9, 8, 2, 1, 1, 28],
            10: [45, 10, 9, 2, 1, 1, 28],
            11: [46, 11, 10, 2, 1, 1, 28],
            12: [47, 12, 11, 2, 1, 1, 28],
            13: [48, 13, 12, 2, 1, 1, 28],
            14: [49, 14, 13, 2, 1, 1, 28],
            15: [50, 15, 14, 2, 1, 1, 28],
            16: [51, 16, 15, 2, 1, 1, 28]
        }
        # cc, min, max, mode, name
        self.knobs = {
            1: [16, 0, 127, 1, 81, 76, 73, 78, 75, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [17, 0, 127, 1, 81, 76, 73, 78, 75, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [18, 0, 127, 1, 81, 76, 73, 78, 75, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            4: [19, 0, 127, 1, 81, 76, 73, 78, 75, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            5: [20, 0, 127, 1, 81, 76, 73, 78, 75, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            6: [21, 0, 127, 1, 81, 76, 73, 78, 75, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            7: [22, 0, 127, 1, 81, 76, 73, 78, 75, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            8: [23, 0, 127, 1, 81, 76, 73, 78, 75, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        }
        self.sysex_end = [16, 0, 2, 9]
        self.sysex_pad = [0] * 2562

    def __getitem__(self, key):
        """Implement __getitem__."""
        return super().__getattribute__(key)

    def serialize(self):
        """Serialize the config into a list of ints."""
        conf_fields: tuple[Field, ...] = fields(self.__class__)
        output: list[int] = []
        for value in conf_fields:
            if value.name in ('start_sysex', 'title', 'arp_tempo', 'pads', 'knobs', 'sysex_end',
                              'sysex_pad'):
                value = getattr(self, value.name)
                if isinstance(value, list):
                    for i in value:
                        output.append(i)
                else:
                    for i in value.values():
                        for x in i:
                            output.append(x)
            else:
                output.append(getattr(self, value.name))
        return output

    def parse_config(self, config):    # pylint: disable=too-many-statements
        """Parse a config from a list of ints."""
        # sysex 0:8
        self.start_sysex = config[0:7]
        self.programme = config[7]
        # title 8:24 done
        self.title = config[8:24]
        # misc 24:30 done
        self.pad_channel = config[24] + 1
        self.pad_aftertouch = config[25]
        self.key_channel = config[26] + 1
        self.key_octave = config[27]
        self.key_transpose = config[28]
        self.transport = config[29]
        # arp 30:41 doneo
        self.arp_on = config[30]
        self.arp_mode = config[31]
        self.arp_time_div = config[32]
        self.arp_clock = config[33]
        self.arp_latch = config[34]
        self.arp_swing = config[35]
        self.arp_tempo_taps = config[36]
        self.arp_tempo = config[37:39]
        self.arp_octave = config[39]
        self.arp_gate = config[40]
        # repeat 41:43 done
        self.note_repeat_time_div = config[41]
        self.note_repeat_on = config[42]
        # cv 43:50 done
        self.cv_trigger_source = config[43]
        self.cv_note_priority = config[44]
        self.cv_gate_mode = config[45]
        self.cv_mod_source = config[46]
        self.cv_bend_range = config[47]
        self.cv_clock_in_div = config[48]
        self.cv_clock_out_div = config[49]
        # scale 50:54 done
        self.scale_on = config[50]
        self.scale_key = config[51]
        self.scale_type = config[52]
        self.scale_non_s_note = config[53]
        # chord 54:57 done
        self.chord_on = config[54]
        self.chord_type = config[55]
        self.chord_inversion = config[56]
        # joystick 57:63 done
        self.joystick_x_mode = config[57]
        self.joystick_x_cc1 = config[58]
        self.joystick_x_cc2 = config[59]
        self.joystick_y_mode = config[60]
        self.joystick_y_cc1 = config[61]
        self.joystick_y_cc2 = config[62]
        # pads 63:175
        pads = config[63:175]
        new_pads = {}
        bot, top = 0, 7
        for i in range(0, 16):
            new_pads[i] = pads[bot:top]
            bot, top = top, top + 7
        self.pads = new_pads

        # knobs 175:335
        knobs = config[175:335]
        new_knobs = {}
        bot, top = 0, 20
        for i in range(0, 8):
            new_knobs[i + 1] = knobs[bot:top]
            bot, top = top, top + 20
        self.knobs = new_knobs

        # end 335:
        self.sysex_end = config[335:339]
        self.sysex_pad = config[339:-1]
        self.sysex_final = config[-1]
