"""Install the program."""
from setuptools import setup

setup(
    name='mpk-mini-plus-editor',
    version='1.0.0',
    description='An alternative to the official AKAI MPKMini MkII Editor',
    author='Jesse G',
    author_email='https://github.com/FrozenPigs/MPK-Mini-Plus-Editor',
    url='',
    packages=['ui', 'core'],
    install_requires=['python-rtmidi', 'pyqt5'],
    scripts=['mpk-mini-plus-editor'],
    include_package_data=True)
