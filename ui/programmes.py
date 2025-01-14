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

"""Main programmes tab widget."""

from PyQt5.QtWidgets import QGridLayout, QTabWidget, QWidget

from ui.knobs import Knobs
from ui.misc import Misc
from ui.pads import Pads


class Programme(QWidget):    # pylint: disable=too-few-public-methods
    """Create a menu bar widget."""

    def __init__(self, name, *args, **kwargs):
        """Create the layout and add the widgets."""
        super().__init__(*args, **kwargs)
        self.setObjectName(name)

        prog_grid_layout = QGridLayout(self)
        prog_grid_layout.setContentsMargins(0, 0, 0, 0)
        prog_grid_layout.setObjectName('prog_grid_layout')
        knobs = Knobs(self)
        prog_grid_layout.addWidget(knobs, 0, 1, 1, 1)
        # Pads
        banks = Pads(self)
        prog_grid_layout.addWidget(banks, 0, 0, 2, 1)
        # # Misc
        misc_layout = Misc(self)
        prog_grid_layout.addLayout(misc_layout, 1, 1, 1, 1)


class Programmes(QTabWidget):    # pylint: disable=too-few-public-methods
    """Create a menu bar widget."""

    def __init__(self, *args, **kwargs):
        """Create the layout and add the widgets."""
        super().__init__(*args, **kwargs)
        self.setEnabled(True)
        self.setTabShape(QTabWidget.Rounded)
        self.setObjectName('programmes')

        # Programmes
        self.progs = []
        for prog_i in range(1, 9):
            prog = Programme(f'prog_{prog_i}')

            self.addTab(prog, '')
            self.progs.append(prog)
