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

"""Knobs widget for akai MPK plus."""
from PyQt6.QtCore import QT_TRANSLATE_NOOP

from ui.widgets import QCustomGroupBox


class Knob(QCustomGroupBox):    # pylint: disable=too-few-public-methods
    """Create a group box containing knob widgets."""

    def __init__(self, index, *args, **kwargs):
        """Create the layout and add the widgets."""
        super().__init__(f'knob_{index}', 'VBox', *args, **kwargs)
        self.index = index
        self._knob_name_line_edit = self._add_line_edit(f'knob_{index}_name', 16)
        self._knob_cc_spin_box = self._add_spin_box(f'knob_{index}_cc', 0, 127, 16)
        self._knob_min_spin_box = self._add_spin_box(f'knob_{index}_min', 0, 127, 16)
        self._knob_max_spin_box = self._add_spin_box(f'knob_{index}_max', 0, 127, 16)
        self._knob_type_combo_box = self._add_combo_box(f'knob_{index}_type', [''] * 2)

    def retranslate(self):
        """Retranslate the widget."""
        self.setTitle(self._translate('knob', f'Knob {self.index+1}'))
        self._knob_name_line_edit[0].setText(self._translate('knob', 'Name'))
        self._knob_cc_spin_box[0].setText(self._translate('knob', 'CC'))
        self._knob_min_spin_box[0].setText(self._translate('knob', 'Min'))
        self._knob_max_spin_box[0].setText(self._translate('knob', 'Max'))

        knob_types = [QT_TRANSLATE_NOOP('knob', 'Absolute'), QT_TRANSLATE_NOOP('knob', 'Relative')]
        self._knob_type_combo_box[0].setText(self._translate('knob', 'Mode'))
        self._knob_type_combo_box[1].setToolTip(self._translate('knob', 'Knob mode'))
        for i, knob_type in enumerate(knob_types):
            self._knob_type_combo_box[1].setItemText(i, self._translate('knob', knob_type))

    def fill(self, config):
        """Fill widgets with config values."""
        self._knob_cc_spin_box[1].setValue(config[0])
        self._knob_min_spin_box[1].setValue(config[1])
        self._knob_max_spin_box[1].setValue(config[2])
        self._knob_type_combo_box[1].setCurrentIndex(config[3])
        name = [i for i in config[4:] if i != 0]
        name = ''.join([chr(x) for x in name])
        self._knob_name_line_edit[1].setText(name)

    def values(self):
        """Return a list of values from the widget."""
        name = self._knob_name_line_edit[1].text()
        if len(name) < 16:
            name = list(map(ord, name)) + [0] * (16 - (len(name)))
        elif len(name) >= 16:
            name = list(map(ord, name[0:16]))
        return [
            self._knob_cc_spin_box[1].value(), self._knob_min_spin_box[1].value(),
            self._knob_max_spin_box[1].value(), self._knob_type_combo_box[1].currentIndex(), *name
        ]


class Knobs(QCustomGroupBox):    # pylint: disable=too-few-public-methods
    """Create a group box containing knob widgets."""

    def __init__(self, *args, **kwargs):
        """Create the layout and add the widgets."""
        super().__init__('knobs', 'Grid', *args, **kwargs)
        self.knobs = []
        for knob_i in range(8):
            knob = Knob(knob_i)
            self.layout.addWidget(knob, knob_i // 4, knob_i % 4, 1, 1)
            self.knobs.append(knob)
        self.setLayout(self.layout)

    def retranslate(self):
        """Retranslate the widget."""
        self.setTitle(self._translate('knobs', 'Knobs'))
        for knob in self.knobs:
            knob.retranslate()

    def fill(self, config):
        """Fill widgets with config values."""
        knob_configs = list(config.knobs.values())
        for knob, knob_config in zip(self.knobs, knob_configs):
            knob.fill(knob_config)

    def values(self):
        """Return a dict of values from the widget."""
        knobs = {}
        for i, knob in enumerate(self.knobs):
            knobs[i + 1] = knob.values()
        return {'knobs': knobs}
