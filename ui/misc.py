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

"""Misc widgets for akai MPK plus."""
from PyQt6 import QtWidgets
from PyQt6.QtCore import QT_TRANSLATE_NOOP
from PyQt6.QtWidgets import QLineEdit, QVBoxLayout

from ui.widgets import QCustomGroupBox


class Joystick(QCustomGroupBox):    # pylint: disable=too-few-public-methods
    """Create a group box containing joystick widgets."""

    def __init__(self, *args, **kwargs):
        """Create the layout and add the widgets."""
        super().__init__('joystick', 'VBox', *args, **kwargs)
        self.axes = []
        for axis in ('x', 'y'):
            js_axis = Axis(axis)
            self.layout.addWidget(js_axis)
            self.axes.append(js_axis)
        self.setLayout(self.layout)

    def retranslate(self):
        """Retranslate the widget."""
        self.setTitle(self._translate('joystick', 'Joystick'))
        for axis in self.axes:
            axis.retranslate()

    def fill(self, config):
        """Fill widgets with config values."""
        for axis in self.axes:
            axis.fill(config)

    def values(self):
        """Return a dict of values from the widget."""
        axes = []
        for axis in self.axes:
            axes.append(axis.values())
        return dict(axes[0], **axes[1])


class Axis(QCustomGroupBox):    # pylint: disable=too-few-public-methods
    """Create a group box containing axis widgets."""

    def __init__(self, axis, *args, **kwargs):
        """Create the layout and add the widgets."""
        super().__init__(f'joystick_{axis}_axis', 'VBox', *args, **kwargs)
        self.axis = axis
        self._axis_combo_box = self._add_combo_box(f'joystick_{axis}_axis', [''] * 3)
        self._axis_cc1_spin_box = self._add_spin_box(f'joystick_{axis}_axis_cc1', 0, 127, 14)
        self._axis_cc2_spin_box = self._add_spin_box(f'joystick_{axis}_axis_cc2', 0, 127, 14)

    def retranslate(self):
        """Retranslate the widget."""
        self.setTitle(self._translate('joystick', f'{self.axis} Axis'))
        modes = [
            QT_TRANSLATE_NOOP('joystick', 'Pitchbend'),
            QT_TRANSLATE_NOOP('joystick', 'Single CC'),
            QT_TRANSLATE_NOOP('joystick', 'Dual CC')
        ]
        self._axis_combo_box[0].setText(self._translate('joystick', 'Mode'))
        self._axis_combo_box[1].setToolTip(self._translate('joystick', 'Joystick CC mode'))
        for i, mode in enumerate(modes):
            self._axis_combo_box[1].setItemText(i, self._translate('joystick', mode))

        self._axis_cc1_spin_box[0].setText(self._translate('joystick', 'CC1'))
        self._axis_cc2_spin_box[0].setText(self._translate('joystick', 'CC2'))

    def fill(self, config):
        """Fill widgets with config values."""
        self._axis_combo_box[1].setCurrentIndex(config[f'joystick_{self.axis}_mode'])
        self._axis_cc1_spin_box[1].setValue(config[f'joystick_{self.axis}_cc1'])
        self._axis_cc2_spin_box[1].setValue(config[f'joystick_{self.axis}_cc2'])

    def values(self):
        """Return a dict of values from the widget."""
        return {
            f'joystick_{self.axis}_mode': self._axis_combo_box[1].currentIndex(),
            f'joystick_{self.axis}_cc1': self._axis_cc1_spin_box[1].value(),
            f'joystick_{self.axis}_cc2': self._axis_cc2_spin_box[1].value()
        }


# pylint: disable=too-few-public-methods,too-many-instance-attributes
class Arpegiator(QCustomGroupBox):
    """Create a group box containing arpegiator widgets."""

    def __init__(self, *args, **kwargs):
        """Create the layout and add the widgets."""
        super().__init__('arp', 'VBox', *args, **kwargs)
        self._arp_enable_check_box = self._add_check_box('arp_enable', 'padding-right:20px')
        self._arp_tempo_spin_box = self._add_spin_box('arp_tempo', 30, 240, 120)
        self._arp_time_div_combo_box = self._add_combo_box('arp_time_div', [''] * 8)
        self._arp_swing_spin_box = self._add_spin_box('arp_swing', 50, 75, 50)
        self._arp_octave_spin_box = self._add_spin_box('arp_octave', 1, 4, 0)
        self._arp_mode_combo_box = self._add_combo_box('arp_mode', [''] * 6)
        self._arp_tempo_taps_spin_box = self._add_spin_box('arp_tempo_taps', 2, 4, 2)
        self._arp_clock_combo_box = self._add_combo_box('arp_clock', [''] * 3)
        self._arp_latch_check_box = self._add_check_box('arp_latch', 'padding-right:20px')
        self._arp_gate_spin_box = self._add_spin_box('arp_gate', 10, 99, 50)
        self.setLayout(self.layout)

    def retranslate(self):
        """Retranslate the widget."""
        self.setTitle(self._translate('arpegiator', 'Arpegiator'))
        self._arp_enable_check_box[1].setText(self._translate('arpegiator', 'ON/OFF'))
        self._arp_enable_check_box[1].setToolTip(
            self._translate('arpegiator', 'Enable the arpegiator'))

        self._arp_tempo_spin_box[0].setText(self._translate('arpegiator', 'Tempo'))

        time_divs = [
            QT_TRANSLATE_NOOP('arpegiator', '1/4'),
            QT_TRANSLATE_NOOP('arpegiator', '1/4T'),
            QT_TRANSLATE_NOOP('arpegiator', '1/8'),
            QT_TRANSLATE_NOOP('arpegiator', '1/8T'),
            QT_TRANSLATE_NOOP('arpegiator', '1/16'),
            QT_TRANSLATE_NOOP('arpegiator', '1/16T'),
            QT_TRANSLATE_NOOP('arpegiator', '1/32'),
            QT_TRANSLATE_NOOP('arpegiator', '1/32T')
        ]
        self._arp_time_div_combo_box[0].setText(self._translate('arpegiator', 'Time Div'))
        self._arp_time_div_combo_box[1].setToolTip(
            self._translate('arpegiator', 'Arpegiator time division'))
        for i, time_div in enumerate(time_divs):
            self._arp_time_div_combo_box[1].setItemText(i, self._translate('arpegiator', time_div))

        self._arp_swing_spin_box[0].setText(self._translate('arpegiator', 'Swing'))
        self._arp_octave_spin_box[0].setText(self._translate('arpegiator', 'Octave'))

        arp_modes = [
            QT_TRANSLATE_NOOP('arpegiator', 'UP'),
            QT_TRANSLATE_NOOP('arpegiator', 'DOWN'),
            QT_TRANSLATE_NOOP('arpegiator', 'EXCLUSIVE'),
            QT_TRANSLATE_NOOP('arpegiator', 'INCLUSIVE'),
            QT_TRANSLATE_NOOP('arpegiator', 'ORDER'), 'RANDOM'
        ]
        self._arp_mode_combo_box[0].setText(self._translate('arpegiator', 'Mode'))
        self._arp_mode_combo_box[1].setToolTip(self._translate('arpegiator', 'Arpegiator mode'))
        for i, arp_mode in enumerate(arp_modes):
            self._arp_mode_combo_box[1].setItemText(i, self._translate('arpegiator', arp_mode))

        self._arp_tempo_taps_spin_box[0].setText(self._translate('arpegiator', 'Tempo Taps'))

        arp_clocks = [
            QT_TRANSLATE_NOOP('arpegiator', 'INTERNAL'),
            QT_TRANSLATE_NOOP('arpegiator', 'EXTERNAL'),
            QT_TRANSLATE_NOOP('arpegiator', 'CV TRIGGER')
        ]
        self._arp_clock_combo_box[0].setText(self._translate('arpegiator', 'Clock'))
        self._arp_clock_combo_box[1].setToolTip(
            self._translate('arpegiator', 'Arpegiator clock sync mode'))
        for i, arp_clock in enumerate(arp_clocks):
            self._arp_clock_combo_box[1].setItemText(i, self._translate('arpegiator', arp_clock))

        self._arp_latch_check_box[1].setText(self._translate('arpegiator', 'Latch'))
        self._arp_latch_check_box[1].setToolTip(
            self._translate('arpegiator', 'Latch the arpegiator on'))

        self._arp_gate_spin_box[0].setText(self._translate('arpegiator', 'Gate'))

    def fill(self, config):
        """Fill widgets with config values."""
        self._arp_enable_check_box[1].setChecked(bool(config.arp_on))
        self._arp_tempo_spin_box[1].setValue(config.arp_tempo[-1] + 128
                                             if config.arp_tempo[0] else config.arp_tempo[-1])
        self._arp_time_div_combo_box[1].setCurrentIndex(config.arp_time_div)
        self._arp_swing_spin_box[1].setValue(config.arp_swing + 50)
        self._arp_octave_spin_box[1].setValue(config.arp_octave + 1)
        self._arp_mode_combo_box[1].setCurrentIndex(config.arp_mode)
        self._arp_tempo_taps_spin_box[1].setValue(config.arp_tempo_taps)
        self._arp_clock_combo_box[1].setCurrentIndex(config.arp_clock)
        self._arp_latch_check_box[1].setChecked(bool(config.arp_latch))
        self._arp_gate_spin_box[1].setValue(config.arp_gate)

    def values(self):
        """Return a dict of values from the widget."""
        return {
            'arp_on':
            self._arp_enable_check_box[1].isChecked(),
            'arp_tempo': [1, self._arp_tempo_spin_box[1].value() - 128]
            if self._arp_tempo_spin_box[1].value() > 128 else [
                0, self._arp_tempo_spin_box[1].value()
            ],
            'arp_time_div':
            self._arp_time_div_combo_box[1].currentIndex(),
            'arp_swing':
            self._arp_swing_spin_box[1].value() - 50,
            'arp_octave':
            self._arp_octave_spin_box[1].value() - 1,
            'arp_mode':
            self._arp_mode_combo_box[1].currentIndex(),
            'arp_tempo_taps':
            self._arp_tempo_taps_spin_box[1].value(),
            'arp_clock':
            self._arp_clock_combo_box[1].currentIndex(),
            'arp_latch':
            self._arp_latch_check_box[1].isChecked(),
            'arp_gate':
            self._arp_gate_spin_box[1].value()
        }


class ProgrammeName(QCustomGroupBox):    # pylint: disable=too-few-public-methods
    """Create a group box containing programme name widgets."""

    def __init__(self, *args, **kwargs):
        """Create the layout and add the widgets."""
        super().__init__('name', 'VBox', *args, **kwargs)
        self._name_line_edit = QLineEdit()
        self._name_line_edit.setObjectName('name_line_edit')
        self._name_line_edit.setMaxLength(16)
        self.layout.addWidget(self._name_line_edit)
        self.setLayout(self.layout)

    def retranslate(self):
        """Retranlate the widget."""
        self.setTitle(self._translate('name', 'Programme Name'))

    def fill(self, config):
        """Fill widgets with config values."""
        self._name_line_edit.setText(''.join([chr(x) for x in config.title]))

    def values(self):
        """Return a dict of values from the widget."""
        return {'title': list(map(ord, self._name_line_edit.text()))}


class Channels(QCustomGroupBox):    # pylint: disable=too-few-public-methods
    """Create a group box containing channels widgets."""

    def __init__(self, *args, **kwargs):
        """Create the layout and add the widgets."""
        super().__init__('channels', 'VBox', *args, **kwargs)
        self._channel_pad_spin_box = self._add_spin_box('channel_pad', 1, 16, 2)
        self._channel_pad_aftertouch_combo_box = self._add_combo_box('channel_pad_aftertouch', [
            ''
        ] * 3)
        self._channel_key_spin_box = self._add_spin_box('channel_key', 1, 16, 1)
        self.setLayout(self.layout)

    def retranslate(self):
        """Retranslate the widget."""
        self.setTitle(self._translate('channels', 'Pad'))
        self._channel_pad_spin_box[0].setText(self._translate('channels', 'Pad'))

        aftertouches = [
            QT_TRANSLATE_NOOP('channels', 'Off'),
            QT_TRANSLATE_NOOP('channels', 'Channel'),
            QT_TRANSLATE_NOOP('channels', 'Polly')
        ]
        self._channel_pad_aftertouch_combo_box[0].setText(
            self._translate('channels', 'Pad Aftertouch'))
        self._channel_pad_aftertouch_combo_box[1].setToolTip(
            self._translate('channels', 'Change pad aftertouch mode'))
        for i, aftertouch in enumerate(aftertouches):
            self._channel_pad_aftertouch_combo_box[1].setItemText(
                i, self._translate('channels', aftertouch))

        self._channel_key_spin_box[0].setText(self._translate('channels', 'Keys/CC'))

    def fill(self, config):
        """Fill widgets with config values."""
        self._channel_pad_spin_box[1].setValue(config.pad_channel + 1)
        self._channel_key_spin_box[1].setValue(config.key_channel + 1)
        self._channel_pad_aftertouch_combo_box[1].setCurrentIndex(config.pad_aftertouch)

    def values(self):
        """Return a dict of values from the widget."""
        return {
            'pad_channel': self._channel_pad_spin_box[1].value() - 1,
            'key_channel': self._channel_key_spin_box[1].value() - 1,
            'pad_aftertouch': self._channel_pad_aftertouch_combo_box[1].currentIndex()
        }


class Keyboard(QCustomGroupBox):    # pylint: disable=too-few-public-methods
    """Create a group box containing channels widgets."""

    def __init__(self, *args, **kwargs):
        """Create the layout and add the widgets."""
        super().__init__('keyboard', 'VBox', *args, **kwargs)
        self._keyboard_transpose_spin_box = self._add_spin_box('keyboard_transpose', -12, 12, 0)
        self._keyboard_octave_spin_box = self._add_spin_box('keyboard_octave', -4, 4, 0)
        self._keyboard_transport_combo_box = self._add_combo_box('keyboard_transport', [''] * 2)
        self.setLayout(self.layout)

    def retranslate(self):
        """Retranslate the widget."""
        self.setTitle(self._translate('keyboard', 'Keyboard'))
        self._keyboard_transpose_spin_box[0].setText(self._translate('keyboard', 'Transpose'))
        self._keyboard_octave_spin_box[0].setText(self._translate('keyboard', 'Octave'))

        transports = [QT_TRANSLATE_NOOP('keyboard', 'On'), QT_TRANSLATE_NOOP('keyboard', 'On/Off')]
        self._keyboard_transport_combo_box[0].setText(self._translate('keyboard', 'Transport'))
        self._keyboard_transport_combo_box[1].setToolTip(
            self._translate('keyboard', 'Change transport control mode'))
        for i, transport in enumerate(transports):
            self._keyboard_transport_combo_box[1].setItemText(
                i, self._translate('keyboard', transport))

    def fill(self, config):
        """Fill widgets with config values."""
        self._keyboard_transpose_spin_box[1].setValue(config.key_transpose - 12)
        self._keyboard_octave_spin_box[1].setValue(config.key_octave - 4)
        self._keyboard_transport_combo_box[1].setCurrentIndex(config.transport)

    def values(self):
        """Return a dict of values from the widget."""
        return {
            'key_transpose': self._keyboard_transpose_spin_box[1].value() + 12,
            'key_octave': self._keyboard_octave_spin_box[1].value() + 4,
            'transport': self._keyboard_transport_combo_box[1].currentIndex()
        }


class NoteRepeat(QCustomGroupBox):    # pylint: disable=too-few-public-methods
    """Create a group box containing note repeat widgets."""

    def __init__(self, *args, **kwargs):
        """Create the layout and add the widgets."""
        super().__init__('note_repeat', 'VBox', *args, **kwargs)
        self._note_repeat_enable_check_box = self._add_check_box('note_repeat_enable')
        self._note_repeat_time_div_combo_box = self._add_combo_box('note_repeat_time_div', [''] * 8)
        self.setLayout(self.layout)

    def retranslate(self):
        """Retranslate the widget."""
        self.setTitle(self._translate('note_repeat', 'Note Repeat'))
        self._note_repeat_enable_check_box[1].setText(self._translate('note_repeat', 'ON/OFF'))
        self._note_repeat_enable_check_box[1].setToolTip(
            self._translate('note_repeat', 'Activate note repeat'))

        time_divs = [
            QT_TRANSLATE_NOOP('note_repeat', '1/4'),
            QT_TRANSLATE_NOOP('note_repeat', '1/4T'),
            QT_TRANSLATE_NOOP('note_repeat', '1/8'),
            QT_TRANSLATE_NOOP('note_repeat', '1/8T'),
            QT_TRANSLATE_NOOP('note_repeat', '1/16'),
            QT_TRANSLATE_NOOP('note_repeat', '1/16T'),
            QT_TRANSLATE_NOOP('note_repeat', '1/32'),
            QT_TRANSLATE_NOOP('note_repeat', '1/32T')
        ]
        self._note_repeat_time_div_combo_box[0].setText(self._translate('note_repeat', 'Time Div'))
        self._note_repeat_time_div_combo_box[1].setToolTip(
            self._translate('note_repeat', 'Change note repeat time division'))
        for i, time_div in enumerate(time_divs):
            self._note_repeat_time_div_combo_box[1].setItemText(
                i, self._translate('note_repeat', time_div))

    def fill(self, config):
        """Fill widgets with config values."""
        self._note_repeat_enable_check_box[1].setChecked(bool(config.note_repeat_on))
        self._note_repeat_time_div_combo_box[1].setCurrentIndex(config.note_repeat_time_div)

    def values(self):
        """Return a dict of values from the widget."""
        return {
            'note_repeat_on': self._note_repeat_enable_check_box[1].isChecked(),
            'note_repeat_time_div': self._note_repeat_time_div_combo_box[1].currentIndex()
        }


class Chords(QCustomGroupBox):    # pylint: disable=too-few-public-methods
    """Create a group box containing chord widgets."""

    def __init__(self, *args, **kwargs):
        """Create the layout and add the widgets."""
        super().__init__('chord', 'VBox', *args, **kwargs)
        self._chord_enable_check_box = self._add_check_box('chord_enable')
        self._chord_type_combo_box = self._add_combo_box('chord_type', [''] * 6)
        self._chord_inversion_combo_box = self._add_combo_box('chord_inversion', [''] * 4)
        self.setLayout(self.layout)

    def retranslate(self):
        """Retranslate the widget."""
        self.setTitle(self._translate('chord', 'Chords'))
        self._chord_enable_check_box[1].setText(self._translate('chord', 'ON/OFF'))
        self._chord_enable_check_box[1].setToolTip(self._translate('chord', 'Activate chord mode'))

        chord_types = [
            QT_TRANSLATE_NOOP('chord', '1-3-5'),
            QT_TRANSLATE_NOOP('chord', '+7'),
            QT_TRANSLATE_NOOP('chord', '+7 +9'),
            QT_TRANSLATE_NOOP('chord', 'Maj7'),
            QT_TRANSLATE_NOOP('chord', 'Min7'),
            QT_TRANSLATE_NOOP('chord', 'Dom7')
        ]
        self._chord_type_combo_box[0].setText(self._translate('chord', 'Chord Type'))
        self._chord_type_combo_box[1].setToolTip(self._translate('chord', 'Change chord type'))
        for i, chord_type in enumerate(chord_types):
            self._chord_type_combo_box[1].setItemText(i, self._translate('chord', chord_type))

        chord_inversions = [
            QT_TRANSLATE_NOOP('chord', 'NONE'),
            QT_TRANSLATE_NOOP('chord', '1ST'),
            QT_TRANSLATE_NOOP('chord', '2ND'),
            QT_TRANSLATE_NOOP('chord', '3RD')
        ]
        self._chord_inversion_combo_box[0].setText(self._translate('chord', 'Chord inversion'))
        self._chord_inversion_combo_box[1].setToolTip(
            self._translate('chord', 'Type of chord inversion to play'))
        for i, chord_inversion in enumerate(chord_inversions):
            self._chord_inversion_combo_box[1].setItemText(
                i, self._translate('chord', chord_inversion))

    def fill(self, config):
        """Fill widgets with config values."""
        self._chord_enable_check_box[1].setChecked(bool(config.chord_on))
        self._chord_type_combo_box[1].setCurrentIndex(config.chord_type)
        self._chord_inversion_combo_box[1].setCurrentIndex(config.chord_inversion)

    def values(self):
        """Return a dict of values from the widget."""
        return {
            'chord_on': self._chord_enable_check_box[1].isChecked(),
            'chord_type': self._chord_type_combo_box[1].currentIndex(),
            'chord_inversion': self._chord_inversion_combo_box[1].currentIndex()
        }


class Scales(QCustomGroupBox):    # pylint: disable=too-few-public-methods
    """Create a group box containing scale widgets."""

    def __init__(self, *args, **kwargs):
        """Create the layout and add the widgets."""
        super().__init__('scale', 'VBox', *args, **kwargs)
        self._scale_enable_check_box = self._add_check_box('scale_enable')
        self._scale_key_combo_box = self._add_combo_box('scale_key', [''] * 12)
        self._scale_type_combo_box = self._add_combo_box('scale_type', [''] * 16)
        self._scale_non_s_note_combo_box = self._add_combo_box('scale_non_s_note', [''] * 2)
        self.setLayout(self.layout)

    def retranslate(self):
        """Retranslate the widget."""
        self.setTitle(self._translate('scale', 'Scales'))
        self._scale_enable_check_box[1].setText(self._translate('scale', 'ON/OFF'))
        self._scale_enable_check_box[1].setToolTip(self._translate('scale', 'Activate scale mode'))

        scale_keys = [
            QT_TRANSLATE_NOOP('scale', 'C'),
            QT_TRANSLATE_NOOP('scale', 'C#'),
            QT_TRANSLATE_NOOP('scale', 'D'),
            QT_TRANSLATE_NOOP('scale', 'D#'),
            QT_TRANSLATE_NOOP('scale', 'E'),
            QT_TRANSLATE_NOOP('scale', 'F'),
            QT_TRANSLATE_NOOP('scale', 'F#'),
            QT_TRANSLATE_NOOP('scale', 'G'),
            QT_TRANSLATE_NOOP('scale', 'G#'),
            QT_TRANSLATE_NOOP('scale', 'A'),
            QT_TRANSLATE_NOOP('scale', 'A#'),
            QT_TRANSLATE_NOOP('scale', 'B')
        ]
        self._scale_key_combo_box[0].setText(self._translate('scale', 'Scale Key'))
        self._scale_key_combo_box[1].setToolTip(self._translate('scale', 'Key to play in'))
        for i, scale_key in enumerate(scale_keys):
            self._scale_key_combo_box[1].setItemText(i, self._translate('scale', scale_key))

        scale_types = [
            QT_TRANSLATE_NOOP('scale', 'CHROMATIC'),
            QT_TRANSLATE_NOOP('scale', 'MAJOR'),
            QT_TRANSLATE_NOOP('scale', 'MELODIC MINOR'),
            QT_TRANSLATE_NOOP('scale', 'HARMONIC MINOR'),
            QT_TRANSLATE_NOOP('scale', 'MAJOR PENTATONIC'),
            QT_TRANSLATE_NOOP('scale', 'MINOR PENTATONIC'),
            QT_TRANSLATE_NOOP('scale', 'DORIAN'),
            QT_TRANSLATE_NOOP('scale', 'PHRYGIAN'),
            QT_TRANSLATE_NOOP('scale', 'LYDIAN'),
            QT_TRANSLATE_NOOP('scale', 'MIXOLYDIAN'),
            QT_TRANSLATE_NOOP('scale', 'AEOLIAN'),
            QT_TRANSLATE_NOOP('scale', 'LOCRIAN'),
            QT_TRANSLATE_NOOP('scale', 'BLUES'),
            QT_TRANSLATE_NOOP('scale', 'FLAMENCO'),
            QT_TRANSLATE_NOOP('scale', 'HUNGARIAN'),
            QT_TRANSLATE_NOOP('scale', 'WHOLE TONE')
        ]
        self._scale_type_combo_box[0].setText(self._translate('scale', 'Scale Type'))
        self._scale_type_combo_box[1].setToolTip(self._translate('scale', 'Type of scale to play'))
        for i, scale_type in enumerate(scale_types):
            self._scale_type_combo_box[1].setItemText(i, self._translate('scale', scale_type))

        s_note_types = [
            QT_TRANSLATE_NOOP('scale', 'TRANSPOSED'),
            QT_TRANSLATE_NOOP('scale', 'IGNORED')
        ]
        self._scale_non_s_note_combo_box[0].setText(self._translate('scale', 'Non-S Note'))
        self._scale_non_s_note_combo_box[1].setToolTip(
            self._translate('scale', 'Type of non-s mode'))
        for i, s_note_type in enumerate(s_note_types):
            self._scale_non_s_note_combo_box[1].setItemText(i, self._translate(
                'scale', s_note_type))

    def fill(self, config):
        """Fill widgets with config values."""
        self._scale_enable_check_box[1].setChecked(bool(config.scale_on))
        self._scale_key_combo_box[1].setCurrentIndex(config.scale_key)
        self._scale_type_combo_box[1].setCurrentIndex(config.scale_type)
        self._scale_non_s_note_combo_box[1].setCurrentIndex(config.scale_non_s_note)

    def values(self):
        """Return a dict of values from the widget."""
        return {
            'scale_on': self._scale_enable_check_box[1].isChecked(),
            'scale_key': self._scale_key_combo_box[1].currentIndex(),
            'scale_type': self._scale_type_combo_box[1].currentIndex(),
            'scale_non_s_note': self._scale_non_s_note_combo_box[1].currentIndex()
        }


class CV(QCustomGroupBox):    # pylint: disable=too-few-public-methods
    """Create a group box containing scale widgets."""

    def __init__(self, *args, **kwargs):
        """Create the layout and add the widgets."""
        super().__init__('cv', 'VBox', *args, **kwargs)
        self._cv_trigger_source_combo_box = self._add_combo_box('cv_trigger_source', [''] * 20)
        self._cv_note_priority_combo_box = self._add_combo_box('cv_note_priority', [''] * 3)
        self._cv_gate_mode_combo_box = self._add_combo_box('cv_gate_mode', [''] * 2)
        self._cv_mod_source_combo_box = self._add_combo_box('cv_mod_source', [''] * 2)
        self._cv_bend_range_combo_box = self._add_combo_box('cv_bend_range', [''] * 12)
        self._cv_clock_in_combo_box = self._add_combo_box('cv_clock_in_div', [''] * 12)
        self._cv_clock_out_combo_box = self._add_combo_box('cv_clock_out_div', [''] * 12)
        self.setLayout(self.layout)

    def retranslate(self):    # pylint: disable=too-many-locals
        """Retranslate the widget."""
        self.setTitle(self._translate('cv', 'CV'))
        trigger_sources = [
            QT_TRANSLATE_NOOP('cv', 'KEYBOARD'),
            QT_TRANSLATE_NOOP('cv', 'KEYBOARD TRIGGER'),
            QT_TRANSLATE_NOOP('cv', 'MIDI CH. 1'),
            QT_TRANSLATE_NOOP('cv', 'MIDI CH. 2'),
            QT_TRANSLATE_NOOP('cv', 'MIDI CH. 3'),
            QT_TRANSLATE_NOOP('cv', 'MIDI CH. 4'),
            QT_TRANSLATE_NOOP('cv', 'MIDI CH. 5'),
            QT_TRANSLATE_NOOP('cv', 'MIDI CH. 6'),
            QT_TRANSLATE_NOOP('cv', 'MIDI CH. 7'),
            QT_TRANSLATE_NOOP('cv', 'MIDI CH. 8'),
            QT_TRANSLATE_NOOP('cv', 'MIDI CH. 9'),
            QT_TRANSLATE_NOOP('cv', 'MIDI CH. 10'),
            QT_TRANSLATE_NOOP('cv', 'MIDI CH. 11'),
            QT_TRANSLATE_NOOP('cv', 'MIDI CH. 12'),
            QT_TRANSLATE_NOOP('cv', 'MIDI CH. 13'),
            QT_TRANSLATE_NOOP('cv', 'MIDI CH. 14'),
            QT_TRANSLATE_NOOP('cv', 'MIDI CH. 15'),
            QT_TRANSLATE_NOOP('cv', 'MIDI CH.16'),
            QT_TRANSLATE_NOOP('cv', 'PADS'),
            QT_TRANSLATE_NOOP('cv', 'DRUM SEQUENCER')
        ]
        self._cv_trigger_source_combo_box[0].setText(self._translate('cv', 'CV Trigger'))
        self._cv_trigger_source_combo_box[1].setToolTip(
            self._translate('cv', 'Source of CV Trigger'))
        for i, trigger_source in enumerate(trigger_sources):
            self._cv_trigger_source_combo_box[1].setItemText(i,
                                                             self._translate('cv', trigger_source))

        note_priorities = [
            QT_TRANSLATE_NOOP('cv', 'LAST'),
            QT_TRANSLATE_NOOP('cv', 'HIGH'),
            QT_TRANSLATE_NOOP('cv', 'LOW')
        ]
        self._cv_note_priority_combo_box[0].setText(self._translate('cv', 'Note Priority'))
        self._cv_note_priority_combo_box[1].setToolTip(self._translate('cv', 'CV note priority'))
        for i, note_priority in enumerate(note_priorities):
            self._cv_note_priority_combo_box[1].setItemText(i, self._translate(
                'cv', note_priority))

        gate_modes = [QT_TRANSLATE_NOOP('cv', 'NORMAL'), QT_TRANSLATE_NOOP('cv', 'LEGATO')]
        self._cv_gate_mode_combo_box[0].setText(self._translate('cv', 'Gate Mode'))
        self._cv_gate_mode_combo_box[1].setToolTip(self._translate('cv', 'CV gate mode priority'))
        for i, gate_mode in enumerate(gate_modes):
            self._cv_gate_mode_combo_box[1].setItemText(i, self._translate('cv', gate_mode))

        mod_sources = [QT_TRANSLATE_NOOP('cv', 'MOD WHEEL'), QT_TRANSLATE_NOOP('cv', 'VELOCITY')]
        self._cv_mod_source_combo_box[0].setText(self._translate('cv', 'Mod Source'))
        self._cv_mod_source_combo_box[1].setToolTip(self._translate('cv', 'CV mod source'))
        for i, mod_source in enumerate(mod_sources):
            self._cv_mod_source_combo_box[1].setItemText(i, self._translate('cv', mod_source))

        bend_ranges = [
            QT_TRANSLATE_NOOP('cv', '1'),
            QT_TRANSLATE_NOOP('cv', '2'),
            QT_TRANSLATE_NOOP('cv', '3'),
            QT_TRANSLATE_NOOP('cv', '4'),
            QT_TRANSLATE_NOOP('cv', '5'),
            QT_TRANSLATE_NOOP('cv', '6'),
            QT_TRANSLATE_NOOP('cv', '7'),
            QT_TRANSLATE_NOOP('cv', '8'),
            QT_TRANSLATE_NOOP('cv', '9'),
            QT_TRANSLATE_NOOP('cv', '10'),
            QT_TRANSLATE_NOOP('cv', '11'),
            QT_TRANSLATE_NOOP('cv', '12')
        ]
        self._cv_bend_range_combo_box[0].setText(self._translate('cv', 'Bend Range'))
        self._cv_bend_range_combo_box[1].setToolTip(self._translate('cv', 'CV bend range'))
        for i, bend_range in enumerate(bend_ranges):
            self._cv_bend_range_combo_box[1].setItemText(i, self._translate('cv', bend_range))

        clock_ins = [
            QT_TRANSLATE_NOOP('cv', 'X4'),
            QT_TRANSLATE_NOOP('cv', 'X2'),
            QT_TRANSLATE_NOOP('cv', '1'),
            QT_TRANSLATE_NOOP('cv', '/1.5'),
            QT_TRANSLATE_NOOP('cv', '/2'),
            QT_TRANSLATE_NOOP('cv', '/3'),
            QT_TRANSLATE_NOOP('cv', '/4'),
            QT_TRANSLATE_NOOP('cv', '/6'),
            QT_TRANSLATE_NOOP('cv', '/8'),
            QT_TRANSLATE_NOOP('cv', '/12'),
            QT_TRANSLATE_NOOP('cv', '/24'),
            QT_TRANSLATE_NOOP('cv', '/48')
        ]
        self._cv_clock_in_combo_box[0].setText(self._translate('cv', 'Clock In Div'))
        self._cv_clock_in_combo_box[1].setToolTip(self._translate('cv', 'CV clock in division'))
        for i, clock_in in enumerate(clock_ins):
            self._cv_clock_in_combo_box[1].setItemText(i, self._translate('cv', clock_in))

        clock_outs = [
            QT_TRANSLATE_NOOP('cv', '1'),
            QT_TRANSLATE_NOOP('cv', '1/2'),
            QT_TRANSLATE_NOOP('cv', '1/4'),
            QT_TRANSLATE_NOOP('cv', '1/4T'),
            QT_TRANSLATE_NOOP('cv', '1/8'),
            QT_TRANSLATE_NOOP('cv', '1/8T'),
            QT_TRANSLATE_NOOP('cv', '1/16'),
            QT_TRANSLATE_NOOP('cv', '1/16T'),
            QT_TRANSLATE_NOOP('cv', '1/32'),
            QT_TRANSLATE_NOOP('cv', '1/32T'),
            QT_TRANSLATE_NOOP('cv', '24p'),
            QT_TRANSLATE_NOOP('cv', '48p')
        ]
        self._cv_clock_out_combo_box[0].setText(self._translate('cv', 'Clock Out Div'))
        self._cv_clock_out_combo_box[1].setToolTip(self._translate('cv', 'CV clock out division'))
        for i, clock_out in enumerate(clock_outs):
            self._cv_clock_out_combo_box[1].setItemText(i, self._translate('cv', clock_out))

    def fill(self, config):
        """Fill widgets with config values."""
        self._cv_trigger_source_combo_box[1].setCurrentIndex(config.cv_trigger_source)
        self._cv_note_priority_combo_box[1].setCurrentIndex(config.cv_note_priority)
        self._cv_gate_mode_combo_box[1].setCurrentIndex(config.cv_gate_mode)
        self._cv_mod_source_combo_box[1].setCurrentIndex(config.cv_mod_source)
        self._cv_bend_range_combo_box[1].setCurrentIndex(config.cv_bend_range - 1)
        self._cv_clock_in_combo_box[1].setCurrentIndex(config.cv_clock_in_div)
        self._cv_clock_out_combo_box[1].setCurrentIndex(config.cv_clock_out_div)

    def values(self):
        """Return a dict of values from the widget."""
        return {
            'cv_trigger_source': self._cv_trigger_source_combo_box[1].currentIndex(),
            'cv_note_priority': self._cv_note_priority_combo_box[1].currentIndex(),
            'cv_gate_mode': self._cv_gate_mode_combo_box[1].currentIndex(),
            'cv_mod_source': self._cv_mod_source_combo_box[1].currentIndex(),
            'cv_bend_range': self._cv_bend_range_combo_box[1].currentIndex() + 1,
            'cv_clock_in_div': self._cv_clock_in_combo_box[1].currentIndex(),
            'cv_clock_out_div': self._cv_clock_out_combo_box[1].currentIndex()
        }


class Misc(QVBoxLayout):    # pylint: disable=too-few-public-methods
    """Create a menu bar widget."""

    def _add_top_layout(self, prog):
        top_section_layout = QtWidgets.QHBoxLayout()
        top_section_layout.setObjectName('top_section_layout')
        joystick = Joystick(prog)
        top_section_layout.addWidget(joystick)
        arp = Arpegiator(prog)
        top_section_layout.addWidget(arp)
        channel_keys_layout = QtWidgets.QVBoxLayout()
        channel_keys_layout.setObjectName('channel_keys_layout')
        name = ProgrammeName(prog)
        channel_keys_layout.addWidget(name)
        channel = Channels(prog)
        channel_keys_layout.addWidget(channel)
        keyboard = Keyboard(prog)
        channel_keys_layout.addWidget(keyboard)
        top_section_layout.addLayout(channel_keys_layout)
        self.addLayout(top_section_layout)
        return (joystick, arp, name, channel, keyboard)

    def _add_bottom_layout(self, prog):
        bottom_section_layout = QtWidgets.QHBoxLayout()
        bottom_section_layout.setObjectName('bottom_section_layout')
        cv = CV(prog)
        bottom_section_layout.addWidget(cv)
        scale = Scales(prog)
        bottom_section_layout.addWidget(scale)
        nr_chord_layout = QtWidgets.QVBoxLayout()
        nr_chord_layout.setObjectName('note_repeat_chord_layout')
        note_repeat = NoteRepeat(prog)
        nr_chord_layout.addWidget(note_repeat)
        chords = Chords(prog)
        nr_chord_layout.addWidget(chords)
        bottom_section_layout.addLayout(nr_chord_layout)
        self.addLayout(bottom_section_layout)
        return (cv, scale, note_repeat, chords)

    def __init__(self, prog, *args, **kwargs):
        """Create the layout and add the widgets."""
        super().__init__(*args, **kwargs)
        self.setObjectName('misc')
        self._top_layout = self._add_top_layout(prog)
        self._bottom_layout = self._add_bottom_layout(prog)

    def retranslate(self):
        """Retranslate the widget."""
        for widget in self._top_layout:
            widget.retranslate()
        for widget in self._bottom_layout:
            widget.retranslate()

    def fill(self, config):
        """Fill widgets with config values."""
        for widget in self._top_layout + self._bottom_layout:
            widget.fill(config)

    def values(self):
        """Return a dict of values from the widget."""
        config = {}
        for widget in self._top_layout + self._bottom_layout:
            config.update(widget.values())
        return config
