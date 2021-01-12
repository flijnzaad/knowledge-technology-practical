# Knowledge Technology Practical
*Pharmacy Help expert system*

By Martin Cupic, Flip Lijnzaad and Gilles Lijnzaad.

## Dependencies
* [Python](https://www.python.org/downloads/) version >=3.8.5
* [pip](https://pip.pypa.io/en/stable/installing/) version >=20

## Install
* [Tkinter](https://docs.python.org/3/library/tkinter.html) version >=8.6:
  * Tkinter should have been included in your Python 3.x install.
  * [Windows](https://www.activestate.com/resources/quick-reads/how-to-install-tkinter-in-windows/)
* [SWI-Prolog](https://www.swi-prolog.org/download/stable) version >=8.2.2
* [pyswip](https://pypi.org/project/pyswip/) version >=0.2.10
  * `pip install pyswip`

## Running the system
Make sure you're in the folder that contains `finalsystem.py`.
The system can be started by running

    python3 finalsystem.py
    
This should open up a new window in which the system runs. 
The system can be quit at any time by closing the window.
    
## Uninstall
When you're done using the system, you may want to uninstall the software.
* SWI-Prolog
  * Linux: `sudo apt-get remove swi-prolog`
  * [Windows](http://www.uninstallapp.com/article/How-to-uninstall-SWI-Prolog-5.11.26-Development-/-5.10.5-Stable.html)
* [pyswip](https://pip.pypa.io/en/stable/reference/pip_uninstall/)
  * `pip uninstall pyswip`
