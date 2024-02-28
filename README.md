# Skills-Bootcamp
For run program "pet_shopping_cart.py" you have to install Python library tabulate

Installation
To install the Python library and the command line utility, run:

pip install tabulate

The command line utility will be installed as tabulate to bin on Linux (e.g. /usr/bin); 
or as tabulate.exe to Scripts in your Python installation on Windows (e.g. C:\Python39\Scripts\tabulate.exe).

You may consider installing the library only for the current user:
pip install tabulate --user

In this case the command line utility will be installed to ~/.local/bin/tabulate on Linux and to %APPDATA%\Python\Scripts\tabulate.exe on Windows.

To install just the library on Unix-like operating systems:
TABULATE_INSTALL=lib-only pip install tabulate

On Windows:
set TABULATE_INSTALL=lib-only
pip install tabulate
