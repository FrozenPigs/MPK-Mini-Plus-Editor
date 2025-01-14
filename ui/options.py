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

"""Options widget for MPK plus."""
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout


class Options(QHBoxLayout):    # pylint: disable=too-few-public-methods
    """Create a group box containing options widgets."""

    def _add_push_button_set(self, name, get_function, push_function):
        layout = QVBoxLayout()
        get_push_button = QPushButton()
        get_push_button.setObjectName(f'get_{name}_push_button')
        get_push_button.clicked.connect(get_function)
        layout.addWidget(get_push_button)
        send_push_button = QPushButton()
        send_push_button.setObjectName(f'send_{name}_push_button')
        send_push_button.clicked.connect(push_function)
        layout.addWidget(send_push_button)
        self.addLayout(layout)
        return (layout, get_push_button, send_push_button)

    def __init__(self, button_functions, *args, **kwargs):
        """Create the layout and add the widgets."""
        super().__init__(*args, **kwargs)
        self.setObjectName('options')
        self._translate = QCoreApplication.translate
        self._buttons = {}
        for key, value in button_functions.items():
            self._buttons[key] = self._add_push_button_set(key, value[0], value[1])

    def retranslate(self):
        """Retranslate the widget."""
        self._buttons['current'][1].setText(self._translate('options', 'Get Current'))
        self._buttons['current'][1].setToolTip(self._translate('options', 'Get current programm'))
        self._buttons['current'][2].setText(self._translate('options', 'Send Current'))
        self._buttons['current'][2].setToolTip(
            self._translate('options', 'Send current programme'))

        self._buttons['all'][1].setText(self._translate('options', 'Get All'))
        self._buttons['all'][1].setToolTip(self._translate('options', 'Get all programmes'))
        self._buttons['all'][2].setText(self._translate('options', 'Send All'))
        self._buttons['all'][2].setToolTip(self._translate('options', 'Send all programmes'))

        self._buttons['ram'][1].setText(self._translate('options', 'Get RAM'))
        self._buttons['ram'][1].setToolTip(self._translate('options', 'Get programme from RAM'))
        self._buttons['ram'][2].setText(self._translate('options', 'Send RAM'))
        self._buttons['ram'][2].setToolTip(self._translate('options', 'Send programme to RAM'))
