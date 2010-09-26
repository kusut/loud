================
Loud
================

This nose plugin lets you play sound when running your test. Current version
only play audio files on two instances, when you pass the test, or not (no
option to play sound at individual error/failure).


Requirement/Gotchas
-------------

This plugin uses sox (http://sox.sourceforge.net/) to play audio files. Make 
sure you have the libraries needed on your OSes for all audio formats you
want to play. 


Usage
--------------

Use option --perfect or --fail::

   $ nosetests --perfect ~/godlike.wav
   $ nosetests --fail ~/combobreaker.wav
   $ nosetests --perfect ~/godlike.wav --fail ~/combobreaker.wav
