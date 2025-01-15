#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# MPK-Mini-Plus-editor
# Copyright (C) 2025  Jesse G
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

"""UI for autofilling knobs and pads."""

from functools import partial

from core.config import Config
from PyQt6 import QtCore
from PyQt6.QtCore import QT_TRANSLATE_NOOP, Qt
from PyQt6.QtWidgets import (QCheckBox, QComboBox, QDialog, QGroupBox,
                             QHBoxLayout, QLabel, QPushButton, QSpinBox,
                             QVBoxLayout, QWidget)

from ui.widgets import QColorComboBox


class Pads(QGroupBox):    # pylint: disable=too-few-public-methods,too-many-instance-attributes
    """Box to contain the pad widgets."""

    def _add_h_box(self, name):
        """Add hbox layout."""
        h_box = QHBoxLayout()
        h_box.setObjectName(name)
        return h_box

    def _add_v_box(self, name):
        """Add vbox layout."""
        v_box = QVBoxLayout()
        v_box.setObjectName(name)
        return v_box

    def _add_note_start(self):
        """Add note start layout."""
        h_box = self._add_h_box('note_start_h_box')

        note_start_check_box = QCheckBox(self)
        note_start_check_box.setObjectName('note_start_check_box')
        h_box.addWidget(note_start_check_box)

        v_box = self._add_v_box('note_start_v_box')
        row_1 = self._add_h_box('note_start_row_1')
        direction_combo_box = QComboBox()
        direction_combo_box.setObjectName('note_direction_combo_box')
        direction_combo_box.addItems([''] * 2)
        row_1.addWidget(direction_combo_box)

        scale_combo_box = QComboBox(self)
        scale_combo_box.setObjectName('note_scale_combo_box')
        scale_combo_box.addItems([''] * 9)
        row_1.addWidget(scale_combo_box)
        v_box.addLayout(row_1)

        row_2 = self._add_h_box('note_start_row_2')

        note_spin_box = QSpinBox(self)
        note_spin_box.setMinimum(0)
        note_spin_box.setMaximum(127)
        note_spin_box.setProperty('value', 50)
        note_spin_box.setObjectName('note_spin_box')
        row_2.addWidget(note_spin_box)
        v_box.addLayout(row_2)
        h_box.addLayout(v_box)
        return (h_box, note_start_check_box, direction_combo_box, scale_combo_box, note_spin_box)

    def _add_pc_cc_start(self, name):
        """Add the pc and cc widgets."""
        h_box = self._add_h_box(f'{name}_h_box')
        start_check_box = QCheckBox(self)
        start_check_box.setObjectName(f'{name}_check_box')
        h_box.addWidget(start_check_box)

        start_spin_box = QSpinBox(self)
        start_spin_box.setMaximum(127)
        start_spin_box.setObjectName(f'{name}_spin_box')
        h_box.addWidget(start_spin_box)

        direction_combo_box = QComboBox(self)
        direction_combo_box.setObjectName(f'{name}_combo_box')
        direction_combo_box.addItems([''] * 2)
        h_box.addWidget(direction_combo_box)

        return (h_box, start_check_box, start_spin_box, direction_combo_box)

    def _add_cc_type_toggle(self, name):
        """Add cc type layout."""
        h_box = self._add_h_box(f'{name}_h_box')
        type_check_box = QCheckBox(self)
        type_check_box.setObjectName(f'{name}_check_box')
        h_box.addWidget(type_check_box)
        type_combo_box = QComboBox(self)
        type_combo_box.setObjectName(f'{name}_combo_box')
        type_combo_box.addItems([''] * 3)
        h_box.addWidget(type_combo_box)
        return (h_box, type_check_box, type_combo_box)

    def _add_on_off_color(self, name):
        """Add cc type layout."""
        h_box = self._add_h_box(f'{name}_h_box')
        type_check_box = QCheckBox(self)
        type_check_box.setObjectName(f'{name}_check_box')
        h_box.addWidget(type_check_box)

        color_combo_box = QColorComboBox(self)
        color_combo_box.setObjectName(f'{name}_combo_box')
        colors = [
            '#010101', '#ff0101', '#ff0113', '#ff1d01', '#ff5101', '#d07101', '#ffff01', '#e04121',
            '#ff7171', '#41f031', '#01ff01', '#55a890', '#01c439', '#71d071', '#018c71', '#4180d0',
            '#7165b4', '#01ffff', '#0171e0', '#0101ff', '#2101f0', '#3901c4', '#5501a8', '#714180',
            '#c001f0', '#ff01ff', '#c40139', '#e0011d', '#f00b71', '#ff6ab4', '#8fb0e0', '#d0c0ff',
            '#ffffff'
        ]
        color_combo_box.add_colors(colors)
        h_box.addWidget(color_combo_box)
        return (h_box, type_check_box, color_combo_box)

    def _add_apply_button(self, apply_autofill_programme):
        """Add apply layout layout."""
        h_box = self._add_h_box('pads_apply_h_box')
        apply_label = QLabel(self)
        apply_label.setObjectName('pads_apply_label')
        h_box.addWidget(apply_label)

        apply_a_button = QPushButton(self)
        apply_a_button.setObjectName('pads_apply_a_button')
        apply_a_button.setStyleSheet('background-color: green')
        apply_a_button.clicked.connect(partial(apply_autofill_programme, 'A'))
        h_box.addWidget(apply_a_button)

        apply_b_button = QPushButton(self)
        apply_b_button.setObjectName('pads_apply_b_button')
        apply_b_button.setStyleSheet('background-color: red')
        apply_b_button.clicked.connect(partial(apply_autofill_programme, 'B'))
        h_box.addWidget(apply_b_button)

        return (h_box, apply_label, apply_a_button, apply_b_button)

    def __init__(self, apply_autofill_programme, *args, **kwargs):
        """Init the pad widget."""
        super().__init__(*args, **kwargs)
        self.setObjectName('pads_group_box')

        self.layout = self._add_v_box('pads')
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.setStretch(1, 1)

        self.note_start = self._add_note_start()
        self.layout.addLayout(self.note_start[0])

        self.pc = self._add_pc_cc_start('pc')
        self.layout.addLayout(self.pc[0])

        self.cc = self._add_pc_cc_start('cc')
        self.layout.addLayout(self.cc[0])

        self.cc_type = self._add_cc_type_toggle('cc_type')
        self.layout.addLayout(self.cc_type[0])

        self.cc_toggle = self._add_cc_type_toggle('cc_toggle')
        self.layout.addLayout(self.cc_toggle[0])

        self.off_color = self._add_on_off_color('off_color')
        self.layout.addLayout(self.off_color[0])

        self.on_color = self._add_on_off_color('on_color')
        self.layout.addLayout(self.on_color[0])

        self.apply_button = self._add_apply_button(apply_autofill_programme)
        self.layout.addLayout(self.apply_button[0])
        self.setLayout(self.layout)

    def retranslate(self):
        """Retranslate the widget."""
        _translate = QtCore.QCoreApplication.translate
        self.setTitle(_translate('autoFill', 'Pads'))

        self.note_start[1].setText(_translate('autoFill', 'Note start'))
        directions = [QT_TRANSLATE_NOOP('auto_fill', 'Up'), QT_TRANSLATE_NOOP('auto_fill', 'Down')]
        for i, direction in enumerate(directions):
            self.note_start[2].setItemText(i, _translate('auto_fill', direction))

        scale_types = [
            QT_TRANSLATE_NOOP('scale', 'CHROMATIC'),
            QT_TRANSLATE_NOOP('scale', 'MAJOR'),
            QT_TRANSLATE_NOOP('scale', 'MELODIC MINOR'),
            QT_TRANSLATE_NOOP('scale', 'HARMONIC MINOR'),
            QT_TRANSLATE_NOOP('scale', 'DORIAN'),
            QT_TRANSLATE_NOOP('scale', 'PHRYGIAN'),
            QT_TRANSLATE_NOOP('scale', 'LYDIAN'),
            QT_TRANSLATE_NOOP('scale', 'MIXOLYDIAN'),
            QT_TRANSLATE_NOOP('scale', 'LOCRIAN')
        ]
        for i, scale in enumerate(scale_types):
            self.note_start[3].setItemText(i, _translate('auto_fill', scale))

        self.apply_button[1].setText(_translate('autoFill', '  Apply to...'))
        banks = [QT_TRANSLATE_NOOP('auto_fill', 'A'), QT_TRANSLATE_NOOP('auto_fill', 'B')]
        for i, bank in enumerate(banks):
            self.apply_button[i + 2].setText(_translate('auto_fill', bank))

        self.pc[1].setText(_translate('auto_fill', 'PC start'))
        for i, direction in enumerate(directions):
            self.pc[3].setItemText(i, _translate('auto_fill', direction))

        self.cc[1].setText(_translate('auto_fill', 'CC start'))
        for i, direction in enumerate(directions):
            self.cc[3].setItemText(i, _translate('auto_fill', direction))

        self.cc_type[1].setText(_translate('auto_fill', 'CC Type'))
        cc_types = [
            QT_TRANSLATE_NOOP('auto_fill', 'Note'),
            QT_TRANSLATE_NOOP('auto_fill', 'Program'),
            QT_TRANSLATE_NOOP('auto_fill', 'CC')
        ]
        for i, cc_type in enumerate(cc_types):
            self.cc_type[2].setItemText(i, _translate('auto_fill', cc_type))

        self.cc_toggle[1].setText(_translate('auto_fill', 'CC Toggle'))
        cc_toggles = [
            QT_TRANSLATE_NOOP('auto_fill', 'Momentary'),
            QT_TRANSLATE_NOOP('auto_fill', 'Toggle')
        ]
        for i, cc_toggle in enumerate(cc_toggles):
            self.cc_toggle[2].setItemText(i, _translate('auto_fill', cc_toggle))

        self.on_color[1].setText(_translate('auto_fill', 'On Color'))
        self.off_color[1].setText(_translate('auto_fill', 'Off Color'))


class Knobs(QGroupBox):    # pylint: disable=too-few-public-methods
    """Box to contain the pad widgets."""

    def _add_h_box(self, name):
        """Add hbox layout."""
        h_box = QHBoxLayout()
        h_box.setObjectName(name)
        return h_box

    def _add_min_max(self, name):
        """Add min/max widgets."""
        h_box = self._add_h_box(f'{name}_h_box')
        check_box = QCheckBox(self)
        check_box.setObjectName(f'{name}_check_box')
        h_box.addWidget(check_box)
        spin_box = QSpinBox(self)
        spin_box.setMaximum(127)
        spin_box.setObjectName(f'{name}_spin_box')
        h_box.addWidget(spin_box)
        self.layout.addLayout(h_box)
        return (check_box, spin_box)

    def _add_cc_start(self, name):
        """Add cc start widget."""
        h_box = self._add_h_box(f'{name}_h_box')
        check_box = QCheckBox(self)
        check_box.setObjectName(f'{name}_check_box')
        h_box.addWidget(check_box)

        spin_box = QSpinBox(self)
        spin_box.setMaximum(127)
        spin_box.setObjectName(f'{name}_spin_box')
        h_box.addWidget(spin_box)

        combo_box = QComboBox(self)
        combo_box.setObjectName(f'{name}_combo_box')
        combo_box.addItems([''] * 2)
        h_box.addWidget(combo_box)

        self.layout.addLayout(h_box)
        return (check_box, spin_box, combo_box)

    def __init__(self, apply_autofill_knobs, *args, **kwargs):
        """Init the pad widget."""
        super().__init__(*args, **kwargs)
        self.setObjectName('knobsGroupBox')
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.setObjectName('knobs_layout')

        self.cc_start = self._add_cc_start('cc_start')
        self.cc_min = self._add_min_max('cc_min')
        self.cc_max = self._add_min_max('cc_max')

        self.apply_button = QPushButton(self)
        self.apply_button.setObjectName('knobs_apply_push_button')
        self.apply_button.clicked.connect(apply_autofill_knobs)

        self.layout.addWidget(self.apply_button, 0, QtCore.Qt.AlignmentFlag.AlignRight)

    def retranslate(self):
        """Retranslate the widgets."""
        _translate = QtCore.QCoreApplication.translate
        self.setTitle(_translate('autoFill', 'Knobs'))
        self.cc_start[0].setText(_translate('autoFill', 'CC start'))
        self.cc_start[2].setItemText(0, _translate('autoFill', 'Up'))
        self.cc_start[2].setItemText(1, _translate('autoFill', 'Down'))
        self.apply_button.setText(_translate('autoFill', 'Apply to knobs'))
        self.cc_min[0].setText(_translate('autoFill', 'Set min'))
        self.cc_max[0].setText(_translate('autoFill', 'Set max'))


class UiAutoFill(QWidget):
    """Autofill the knob and pad UIs."""

    SCALES = [
        [0, 1, 2, 3, 4, 5, 6, 7],    # chromatic
        [0, 2, 4, 5, 7, 9, 11, 12],    # major
        [0, 2, 3, 5, 7, 8, 10, 12],    # minor
        [0, 2, 4, 5, 7, 8, 11, 12],    # harmonic minor
        [0, 2, 3, 5, 7, 9, 10, 12],    # dorian
        [0, 1, 3, 5, 7, 8, 10, 12],    # phrygian
        [0, 2, 4, 6, 7, 9, 11, 12],    # lydian
        [0, 2, 4, 5, 7, 9, 10, 12],    # myxolidian
        [0, 1, 3, 5, 6, 8, 10, 12],    # locrian
    ]

    def __init__(self, main_window, *args, **kwargs):
        """Init the main window widgets."""
        super().__init__(*args, **kwargs)
        self.setObjectName('auto_fill_main_widget')
        self.setMinimumSize(500, 250)
        self.resize(500, 250)
        self.move(0, 0)
        self.setWindowFlags(QtCore.Qt.WindowType.Dialog)
        self.main_window = main_window

        layout = QHBoxLayout(self)
        layout.setObjectName('horizontalLayout')

        self.pads_group_box = Pads(self.apply_autofill_programme)
        layout.addWidget(self.pads_group_box)

        self.knobs_group_box = Knobs(self.apply_autofill_knobs)
        layout.addWidget(self.knobs_group_box)

        self.setLayout(layout)
        self.retranslate()

    def apply_autofill_knobs(self):
        """Apply the autofill settings to the current programme knobs."""
        mw = self.main_window
        p_from = mw.get_active_tab_index()
        config = Config()
        conf = mw.get_tab_programme(config, p_from)
        do_values = self.knobs_group_box.cc_start[0].checkState()
        do_min = self.knobs_group_box.cc_min[0].checkState()
        do_max = self.knobs_group_box.cc_max[0].checkState()
        if do_values:
            start_value = self.knobs_group_box.cc_start[1].value()
            direction = self.knobs_group_box.cc_start[2].currentIndex()
            direction = 1 if direction == 0 else -1
            for i in range(8):
                conf.knobs[i + 1][0] = start_value + i * direction
        if do_min:
            minimum = self.knobs_group_box.cc_min[1].value()
            for i in range(8):
                conf.knobs[i + 1][1] = minimum
        if do_max:
            maximum = self.knobs_group_box.cc_max[1].value()
            for i in range(8):
                conf.knobs[i + 1][2] = maximum
        mw.fill_tab(conf, p_from)

    def apply_autofill_programme(self, programme):
        """Apply the autofill settings to the current programme pads."""
        mw = self.main_window
        p_from = mw.get_active_tab_index()
        config = Config()
        conf = mw.get_tab_programme(config, p_from)
        programme = 0 if programme == 'A' else 8

        if self.pads_group_box.note_start[1].checkState():
            scale = self.pads_group_box.note_start[3].currentIndex()
            direction = self.pads_group_box.note_start[2].currentIndex()
            start_note = self.pads_group_box.note_start[4].value()
            values = self.SCALES[scale]
            if direction:
                values.reverse()
                values = [n - values[0] for n in values]
            values = [n + start_note for n in values]
            for i, val in enumerate(values):
                conf.pads[i + 1 + programme][0] = val

        conf_id = 1
        for i in [self.pads_group_box.cc, self.pads_group_box.pc]:
            conf = self._get_spin_box_conf(i, programme, conf, conf_id)
            conf_id += 1

        conf_id = 3
        for i in [
                self.pads_group_box.cc_type, self.pads_group_box.cc_toggle,
                self.pads_group_box.on_color, self.pads_group_box.off_color
        ]:
            conf = self._get_combo_box_conf(i, programme, conf, conf_id)
            conf_id += 1

        mw.fill_tab(conf, p_from)

    def _get_spin_box_conf(self, widget, programme, conf, conf_id):
        if widget[1].checkState():
            value = widget[2].value()
            pc_direction = widget[3].currentIndex()
            pc_direction = 1 if pc_direction == 0 else -1
            for i in range(8):
                conf.pads[i + 1 + programme][conf_id] = value + i * pc_direction
        return conf

    def _get_combo_box_conf(self, widget, programme, conf, conf_id):
        if widget[1].checkState():
            cc_type = widget[2].currentIndex()
            for i in range(8):
                conf.pads[i + 1 + programme][conf_id] = cc_type
        return conf

    def retranslate(self):
        """Retranslate the UI."""
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate('auto_fill', 'Auto Fill'))
        self.pads_group_box.retranslate()
        self.knobs_group_box.retranslate()
