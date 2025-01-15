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

"""Menubar widget."""
from functools import partial

from PyQt6.QtCore import QCoreApplication, QRect
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenu, QMenuBar


class MenuBar(QMenuBar):    # pylint: disable=too-few-public-methods
    """Create a menu bar widget."""

    def _add_file_menu(self, file_actions):
        menu_file = QMenu(self)
        menu_file.setObjectName('menu_file')

        action_open = QAction()
        action_open.setObjectName('action_open')
        action_open.triggered.connect(file_actions[0])
        menu_file.addAction(action_open)

        action_save_as = QAction()
        action_save_as.setObjectName('action_save_as')
        action_save_as.triggered.connect(file_actions[1])
        menu_file.addAction(action_save_as)

        self.addAction(menu_file.menuAction())

        return (menu_file, action_open, action_save_as)

    def _add_edit_menu(self, edit_actions):
        menu_edit = QMenu(self)
        menu_edit.setObjectName('menu_edit')

        menu_copy_to = QMenu()
        menu_copy_to.setObjectName('menu_copy_to')
        menu_edit.addAction(menu_copy_to.menuAction())

        copy_actions = []
        for p_i in range(1, 9):
            action_copy_prog = QAction()
            action_copy_prog.setObjectName(f'action_copy_prog_{p_i}')
            action_copy_prog.triggered.connect(partial(edit_actions[0], p_i))
            menu_copy_to.addAction(action_copy_prog)
            copy_actions.append(action_copy_prog)

        action_show_auto_fill = QAction()
        action_show_auto_fill.setObjectName('action_show_auto_fill')
        action_show_auto_fill.triggered.connect(edit_actions[1])
        menu_edit.addAction(action_show_auto_fill)

        self.addAction(menu_edit.menuAction())
        return (menu_edit, menu_copy_to, copy_actions, action_show_auto_fill)

    def __init__(self, file_actions, edit_actions, *args, **kwargs):
        """Create the layout and add the widgets."""
        super().__init__(*args, **kwargs)
        self.setObjectName('menubar')
        self.setGeometry(QRect(0, 0, 1032, 18))
        self._translate = QCoreApplication.translate
        self._file_menu = self._add_file_menu(file_actions)
        self._edit_menu = self._add_edit_menu(edit_actions)

    def retranslate(self):
        """Retranslate the widget."""
        self._file_menu[0].setTitle(self._translate('menu', 'File'))
        self._file_menu[1].setText(self._translate('menu', 'Open'))
        self._file_menu[2].setText(self._translate('menu', 'Save as...'))
        self._edit_menu[0].setTitle(self._translate('menu', 'Edit'))
        self._edit_menu[1].setTitle(self._translate('menu', 'Copy to...'))
        for i, action in enumerate(self._edit_menu[2]):
            action.setText(self._translate('menu', f'PROG {i+1}'))
        self._edit_menu[3].setText(self._translate('menu', 'Auto fill...'))
