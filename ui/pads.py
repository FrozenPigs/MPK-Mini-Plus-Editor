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

"""Main pads group box widget."""
from PyQt5.QtCore import QT_TRANSLATE_NOOP

from ui.widgets import QCustomGroupBox


class Pad(QCustomGroupBox):    # pylint: disable=too-few-public-methods,too-many-instance-attributes
    """Create a group box containing pad widgets."""

    def __init__(self, index, *args, **kwargs):
        """Create the layout and add the widgets."""
        super().__init__(f'pad_{index}', 'VBox', *args, **kwargs)
        self.index = index
        self.colors = [
            '#010101', '#ff0101', '#ff0113', '#ff1d01', '#ff5101', '#d07101', '#ffff01', '#e04121',
            '#ff7171', '#41f031', '#01ff01', '#55a890', '#01c439', '#71d071', '#018c71', '#4180d0',
            '#7165b4', '#01ffff', '#0171e0', '#0101ff', '#2101f0', '#3901c4', '#5501a8', '#714180',
            '#c001f0', '#ff01ff', '#c40139', '#e0011d', '#f00b71', '#ff6ab4', '#8fb0e0', '#d0c0ff',
            '#ffffff'
        ]

        self._pad_note_spin_box = self._add_spin_box(f'pad_{index}_note', 0, 127, 50)
        self._pad_cc_spin_box = self._add_spin_box(f'pad_{index}_cc', 0, 127, 50)
        self._pad_pc_spin_box = self._add_spin_box(f'pad_{index}_pc', 0, 127, 50)
        self._pad_type_combo_box = self._add_combo_box(f'pad_{index}_type', [''] * 3)
        self._pad_toggle_combo_box = self._add_combo_box(f'pad_{index}_toggle', [''] * 2)
        self._pad_off_color_combo_box = self._add_color_combo_box(f'pad_{index}_off_color',
                                                                  self.colors)
        self._pad_on_color_combo_box = self._add_color_combo_box(f'pad_{index}_on_color',
                                                                 self.colors)

    def retranslate(self):
        """Retranslate the widget."""
        self.setTitle(self._translate('pad', f'Pad  {self.index+1}'))
        self._pad_note_spin_box[0].setText(self._translate('pad', 'Note'))
        self._pad_cc_spin_box[0].setText(self._translate('pad', 'CC'))
        self._pad_pc_spin_box[0].setText(self._translate('pad', 'PC'))

        pad_types = [
            QT_TRANSLATE_NOOP('pad', 'Note'),
            QT_TRANSLATE_NOOP('pad', 'Program'),
            QT_TRANSLATE_NOOP('pad', 'CC')
        ]
        self._pad_type_combo_box[0].setText(self._translate('pad', 'Type'))
        self._pad_type_combo_box[1].setToolTip(self._translate('pad', 'Type of Pad'))
        for i, pad_type in enumerate(pad_types):
            self._pad_type_combo_box[1].setItemText(i, self._translate('pad', pad_type))

        pad_toggles = [QT_TRANSLATE_NOOP('pad', 'Momentary'), QT_TRANSLATE_NOOP('pad', 'Toggle')]
        self._pad_toggle_combo_box[0].setText(self._translate('pad', 'Toggle'))
        self._pad_toggle_combo_box[1].setToolTip(self._translate('pad', 'Toggle or momentary pad'))
        for i, pad_toggle in enumerate(pad_toggles):
            self._pad_toggle_combo_box[1].setItemText(i, self._translate('pad', pad_toggle))

        self._pad_off_color_combo_box[0].setText(self._translate('pad', 'Off Color'))
        self._pad_off_color_combo_box[1].setToolTip(self._translate('pad', 'Pads off color'))
        self._pad_on_color_combo_box[0].setText(self._translate('pad', 'On Color'))
        self._pad_on_color_combo_box[1].setToolTip(self._translate('pad', 'Pads on color'))

    def fill(self, config):
        """Fill widgets with config values."""
        self._pad_note_spin_box[1].setValue(config[0])
        self._pad_cc_spin_box[1].setValue(config[1])
        self._pad_pc_spin_box[1].setValue(config[2])
        self._pad_type_combo_box[1].setCurrentIndex(config[3])
        self._pad_toggle_combo_box[1].setCurrentIndex(config[4])
        self._pad_off_color_combo_box[1].setCurrentIndex(config[6])
        self._pad_on_color_combo_box[1].setCurrentIndex(config[5])

    def values(self):
        """Return a list of values from the widget."""
        return [
            self._pad_note_spin_box[1].value(), self._pad_cc_spin_box[1].value(
            ), self._pad_pc_spin_box[1].value(), self._pad_type_combo_box[1].currentIndex(), self.
            _pad_toggle_combo_box[1].currentIndex(), self._pad_on_color_combo_box[1].currentIndex(
            ), self._pad_off_color_combo_box[1].currentIndex()
        ]


class Bank(QCustomGroupBox):    # pylint: disable=too-few-public-methods
    """Create a group box containing pad widgets."""

    def __init__(self, index, *args, **kwargs):
        """Create the layout and add the widgets."""
        super().__init__(f'bank_{index}', 'Grid', *args, **kwargs)
        self.index = index
        self.setStyleSheet(f"""
                #bank_{index}_group_box{{
                border: 2px solid {'red' if index else 'green'};
                }}""")

        self.pads = []
        for pad_i in range(8):
            pad = Pad(pad_i)
            self.layout.addWidget(pad, 1 - (pad_i // 4), pad_i % 4, 1, 1)
            self.pads.append(pad)
        self.setLayout(self.layout)

    def retranslate(self):
        """Retranslate the widget."""
        self.setTitle(self._translate('pad', f'Pad  {"B" if self.index else "A"}'))
        for pad in self.pads:
            pad.retranslate()

    def fill(self, config):
        """Fill widgets with config values."""
        for pad, pad_config in zip(self.pads, config):
            pad.fill(pad_config)

    def values(self):
        """Return a dict of values from the widget."""
        pads = []
        for pad in self.pads:
            pads.append(pad.values())
        return pads


class Pads(QCustomGroupBox):    # pylint: disable=too-few-public-methods
    """Create a group box containing pad widgets."""

    def __init__(self, *args, **kwargs):
        """Create the layout and add the widgets."""
        super().__init__('pads', 'VBox', *args, **kwargs)

        self.banks = []
        for bank_i in range(2):
            bank = Bank(bank_i)
            self.layout.addWidget(bank)
            self.banks.append(bank)
        self.setLayout(self.layout)

    def retranslate(self):
        """Retranslate the widget."""
        self.setTitle(self._translate('pads', 'Pads'))
        for bank in self.banks:
            bank.retranslate()

    def fill(self, config):
        """Fill widgets with config values."""
        vals = list(config.pads.values())
        bank_a, bank_b = vals[0:8], vals[8:]
        for bank, bank_config in zip(self.banks, [bank_a, bank_b]):
            bank.fill(bank_config)

    def values(self):
        """Return a dict of values from the widget."""
        banks = []
        for bank in self.banks:
            banks += bank.values()

        pads = {}
        for i, pad in enumerate(banks):
            pads[i + 1] = pad
        return {'pads': pads}
