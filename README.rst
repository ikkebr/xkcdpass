===============================
PyXKCDPass
===============================

This script provides a simple way to generate secure and human readable passwords, based on XKCD #936

* Free software: BSD license

Usage
--------

Just call pyxckdpass and supply it with a dictionary:

  **pyxkcdpass -d /usr/share/dict/words**
  
or provide a dictionary and a password length

  **pyxkcdpass -d /usr/share/dict/words -l 10**

or use the included dictionary

  **pyxkcdpass**

