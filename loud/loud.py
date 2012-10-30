import os
import platform
from nose.plugins import Plugin
from subprocess import call


class Loud(Plugin):
    name = 'loud'
    enabled = True

    def options(self, parser, env=os.environ):
        parser.add_option(
            '--perfect',
            action='store',
            dest='perfect',
            metavar='AUDIO_FILE',
            help='Play AUDIO_FILE on successful test'
        )
        parser.add_option(
            '--fail',
            action='store',
            dest='fail',
            metavar='AUDIO_FILE',
            help='Play AUDIO_FILE on failed test'
        )

    def configure(self, options, conf):
        super(Loud, self).configure(options, conf)
        self.perfect = getattr(options, 'perfect', None)
        self.fail = getattr(options, 'fail', None)

    def finalize(self, result):
        param = (self.fail, self.perfect)[result.wasSuccessful()]
        if param is not None:
            machine = platform.system()
            if machine == 'Windows':
                call(['wmplayer', param])
            elif machine == 'Darwin':
                call(['afplay', param])
            else:
                call(['mpg123', '-q', param])
