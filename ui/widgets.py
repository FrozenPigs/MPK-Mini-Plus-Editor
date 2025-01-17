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

"""Custom default QT widgets to inherit from."""

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QCoreApplication, Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (QCheckBox, QComboBox, QGridLayout, QGroupBox,
                             QHBoxLayout, QLabel, QLineEdit, QSpinBox,
                             QVBoxLayout)


class ComboDelegate(QtWidgets.QStyledItemDelegate):    # pylint: disable=too-few-public-methods
    """Deal with drawing of color combo box items."""

    def paint(self, painter, option, index):
        """Paint the combo box items."""
        self.initStyleOption(option, index)
        painter.fillRect(option.rect, option.backgroundBrush)
        painter.save()
        if option.state & QtWidgets.QStyle.StateFlag.State_MouseOver:
            if option.backgroundBrush.color().lightness() in (0, 1):
                new_color = QtGui.QColor(255, 255, 255)
            elif option.backgroundBrush.color().lightness() <= 121 or (option.backgroundBrush.color(
            ).blue() == 255 and option.backgroundBrush.color().lightness() < 255):
                new_color = option.backgroundBrush.color().lighter(175)
            else:
                new_color = option.backgroundBrush.color().darker(175)
            painter.fillRect(option.rect, option.backgroundBrush)
            painter.setPen(new_color)
            painter.drawText(
                option.rect,
                QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignVCenter, 'S')

        painter.restore()


class QColorComboBox(QComboBox):
    """A drop down menu for selecting colors."""

    selectedColor = QtCore.pyqtSignal(QColor)

    def __init__(self, parent=None, enable_add_colors=False):
        """Init color Combo Box.

        Set enable_add_colors if no user definable colors.
        """
        super().__init__(parent)
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)

        self._add_colors_text = 'Custom'
        if enable_add_colors:
            self.addItem(self._add_colors_text)

        self._current_color = None
        self.setItemDelegate(ComboDelegate())

        self.activated.connect(self._color_selected)
        self._init = True

    def add_colors(self, colors):
        """Add colors to the QComboBox."""
        for a_color in colors:
            if not isinstance(a_color, QColor):
                a_color = QColor(a_color)
            if self.findData(a_color) == -1:
                self.addItem('', userData=a_color)
                self.setItemData(self.count() - 1, QColor(a_color),
                                 QtCore.Qt.ItemDataRole.BackgroundRole)
        if self._init:
            self._color_selected(0, emit_signal=False)
            self._init = False

    def add_color(self, color):
        """Add the color to the QComboBox."""
        self.add_colors([color])

    def set_color(self, color):
        """Add the color to the QComboBox and selects it."""
        self.add_color(color)
        self._color_selected(self.findData(color), False)

    def get_current_color(self):
        """Return the currently selected QColor.

        Return None if non has been selected yet.
        """
        return self._current_color

    def setCurrentIndex(self, index):    # pylint: disable=invalid-name
        """Reimplement setCurrentIndex to update selected color."""
        super().setCurrentIndex(index)
        self._color_selected(index, emit_signal=False)

    def _color_selected(self, index, emit_signal=True):
        """Process the selection of the QComboBox."""
        if self.itemText(index) in ('', 'S'):
            self._current_color = self.itemData(index)
            if emit_signal:
                self.selectedColor.emit(self._current_color)
        elif self.itemText(index) == self._add_colors_text:
            new_color = QtWidgets.QColorDialog.getColor(
                self._current_color if self._current_color else QtCore.Qt.white)
            if new_color.isValid():
                self.add_color(new_color)
                self._current_color = new_color
                if emit_signal:
                    self.selectedColor.emit(self._current_color)
        if self._current_color:
            self.lineEdit().setStyleSheet('background-color: ' + self._current_color.name())


class QCustomGroupBox(QGroupBox):    # pylint: disable=too-few-public-methods
    """Custom group box with VBox layout and  methods to add widgets."""

    def __init__(self, name, layout_type, *args, **kwargs):
        """Create the layout and add the widgets."""
        super().__init__(*args, **kwargs)
        self.setObjectName(f'{name}_group_box')
        self.setAlignment(4)
        if layout_type == 'VBox':
            self.layout = QVBoxLayout(self)
        if layout_type == 'Grid':
            self.layout = QGridLayout(self)
        self.layout.setObjectName(f'{name}_layout')
        self.layout.setContentsMargins(1, 1, 1, 1)
        self.layout.setSpacing(1)
        self._translate = QCoreApplication.translate

    def _add_boilerplate_layout(self, name, label=True):
        layout = QHBoxLayout()
        layout.setObjectName(f'{name}_layout')
        if label:
            label = QLabel(self)
            label.setObjectName(f'{name}_label')
            layout.addWidget(label)
        return (layout, label)

    def _add_spin_box(self, name, minimum, maximum, default):
        layout, label = self._add_boilerplate_layout(name)
        spin_box = QSpinBox(self)
        spin_box.setMaximum(maximum)
        spin_box.setMinimum(minimum)
        spin_box.setProperty('value', default)
        spin_box.setObjectName(f'{name}_spin_box')
        layout.addWidget(spin_box)
        self.layout.addLayout(layout)
        return (label, spin_box)

    def _add_combo_box(self, name, items):
        layout, label = self._add_boilerplate_layout(name)
        combo_box = QComboBox(self)
        combo_box.setObjectName(f'{name}_combo_box')
        combo_box.addItems(items)
        layout.addWidget(combo_box)
        self.layout.addLayout(layout)
        return (label, combo_box)

    def _add_check_box(self, name, style_sheet=None, state_change_action=None):
        layout, label = self._add_boilerplate_layout(name)
        check_box = QCheckBox(self)
        check_box.setObjectName(f'{name}_check_box')
        if style_sheet:
            check_box.setStyleSheet(style_sheet)
        if state_change_action:
            check_box.stateChanged.connect(state_change_action)
        layout.addWidget(check_box, 0, Qt.AlignmentFlag.AlignHCenter)
        self.layout.addLayout(layout)
        return (label, check_box)

    def _add_line_edit(self, name, max_length):
        layout, label = self._add_boilerplate_layout(name)
        line_edit = QLineEdit()
        line_edit.setObjectName(name)
        line_edit.setMaxLength(max_length)
        layout.addWidget(line_edit)
        self.layout.addLayout(layout)
        return (label, line_edit)

    def _add_color_combo_box(self, name, colors):
        layout, label = self._add_boilerplate_layout(name)
        color_combo_box = QColorComboBox()
        color_combo_box.setObjectName(name)
        color_combo_box.add_colors(colors)
        # color_combo_box._color_selected(0, emit_signal=False)
        layout.addWidget(color_combo_box)
        self.layout.addLayout(layout)
        return (label, color_combo_box)

    def _create_tooltip(self, text):
        """Create a UI tooltip element."""
        return '<html><head/><body><p>' + text.replace('\n', '</p><p>') + '</p></body></html>'
