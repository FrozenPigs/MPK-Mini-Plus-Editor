MPK-Mini-Plus-Editor
=============
Alternative to the official AKAI MPKMini Plus Editor

Special shout outs to Damien Picard(PiOverFour) whos project this was initally based on, though most code has been rewritten, and Joonas from [joonas.fi](https://joonas.fi) for his artical on reversing his MPK3.

![Edit or window](docs/editor_screenshot.png?raw=true "The editor")

## Overview
This program is a replacement for the official Akai MPK Mini Plus Editor. Although less fancy, it is just as usable.

## Requirements
The program is written in Python3 and relies on PyQt5 and python-rtmidi. It was tested on GNU/Linux.

## Installation
A good way would be to use pip for the dependencies.
### Debian-based distributions
```
  # Replace libjack-dev by libjack-jackd2-dev if using jackd2
  apt-get install build-essential python3-dev python3-pip libasound2-dev libjack-dev
  pip3 install -r requirements.txt
```

### Mac OS X
***UNTESTED***
You can install Python and pip using homebrew. You may need a recent version of Mac OS X.
```
  brew install python3
  pip3 install -r requirements.txt
```

### Windows
***UNTESTED***
* Download and install `python3` from [the python website](https://www.python.org/downloads/windows/). Make sure you install `pip` as well in the installer wizard
* Download and install [Visual C++ build tools 2015](http://landinghub.visualstudio.com/visual-cpp-build-tools)
* In a command prompt, type:
```
  pip3 install -r requirements.txt
```

## Usage
Connect your controller, then start the editor with ```./mpk-m2-editor```
If you're familiar with the official editor, you should find it's similar, except that programs are grouped in tabs at the top of the window. You can send an individual program or all of them at once. Some fields have tooltips, don't hesitate to hover them.

You can use the scrollwheel to modify any value. If you use it with `CTRL`, the values will change by increments of 10.

The Send RAM button allows you to send the current controller configuration, without overriding any program.

### Joystick
The joystick options work this way:
* First, select the basic behaviour: **Pitchbend**, **CC1** or **CC2**.
* **Pitchbend**: you're done.
* **CC1**: The joystick sends a CC message on the channel specified in **CC1** for the both Axes.
* **CC2**: The joystick sends a CC message on the canals specified in **CC1** OR **CC2** for the both Axes.

### Auto Fill
Click the menu Edit -> Auto fill... This dialog allows you to fill several fields at once. First tick the check boxes for the options you would like to have filled (eg. PC start). Fill the corresponding fields, and press the button corresponding to the options you'd like to fill (eg. A for Bank A). This will fill the options for the *selected program* tab only.

![Auto fill window](docs/autofill_screenshot.png?raw=true "The auto fill window")

## Feedback and pull requests welcome!
This is a good starting point. If you would like to contribute, please do so!

## License

> Copyright (C) 2025 Jesse G derived from work of
> Copyright (C) 2017-2020 Damien Picard dam.pic AT free.fr and
> contributors
>
> This program is free software: you can redistribute it and/or modify
> it under the terms of the GNU General Public License as published by
> the Free Software Foundation, either version 3 of the License, or
> (at your option) any later version.
>
> This program is distributed in the hope that it will be useful,
> but WITHOUT ANY WARRANTY; without even the implied warranty of
> MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
> GNU General Public License for more details.
>
> You should have received a copy of the GNU General Public License
> along with this program. If not, see <http://www.gnu.org/licenses/>.
