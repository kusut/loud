import platform, os
from nose.plugins import Plugin
from subprocess import call

class Loud(Plugin):
    name = 'loud'
    enabled = True

    def options(self, parser, env=os.environ):
        parser.add_option('--perfect',action='store',
                          dest='perfect',
                          metavar='AUDIO_FILE',
                          help='Play AUDIO_FILE on successful test')
        parser.add_option('--fail', action='store',
                          dest='fail',
                          metavar='AUDIO_FILE',
                          help='Play AUDIO_FILE on failed test')

    def configure(self, options, conf):
        super(Loud, self).configure(options, conf)
        if  hasattr(options, 'perfect'):
            self.perfect = options.perfect
        if  hasattr(options, 'fail'):
            self.fail = options.fail
        
    def finalize(self, result):
        param = (getattr(self, 'fail', None), 
                 getattr(self, 'perfect', None))[result.wasSuccessful()]
        if param is not None:
            if platform.system() == 'Windows':
                call(['sox', param, '-q', '-d'])
            else:
                call(['play', param, '-q'])
