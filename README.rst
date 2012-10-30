================
Loud
================

This nose plugin lets you play sound when running your test. Current version
only plays audio files on two instances, when you pass the test, or not (no
option to play sound at individual error/failure).

Loud will use these media players to play audio files:

- Linux/BSD: mpg123
- Mac OS: afplay
- Windows: wmplayer

Use option --perfect and/or --fail::

   $ nosetests --perfect ~/godlike.wav
   $ nosetests --fail ~/combo_breaker.wav
   $ nosetests --perfect ~/guilestheme.mp3 --fail ~/yaketysax.mp3


