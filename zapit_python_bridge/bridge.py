import matlab.engine

class bridge:

    ## Attributes (remove from here, perhaps, when it all works)
    def __init__(self):
        """
        Connect to the MATLAB engine
        """

        print('CONNECTING TO MATLAB')
        # TODO - What happens if there is more than one session called zapit?
        # maybe can find if this is the case with matlab.engine.find_matlab()
        self.eng = matlab.engine.connect_matlab('zapit')

        print('CONNECTED')
        # TODO -- check variables exist
        self.hZP = self.eng.workspace['hZP']
        self.hZPview = self.eng.workspace['hZPview']


    def __del__(self):
        print('Disconnecting from MATLAB')
        self.eng.quit() # Otherwise it locks up if we try to reconnect

    def send_samples(self, conditionNum=-1, laserOn=True, hardwareTriggered=True, logging=True, verbose=False):
        condition_num, laser_on  = self.eng.sendSamples(self.hZP, 'conditionNum', -1,
                                            'laserOn', True,
                                            'hardwareTriggered', True,
                                            'logging', True,
                                            'verbose', False,
                                            nargout=2)

    def stop_opto_stim(self):
        self.eng.stopOptoStim(self.hZP,  nargout=0)
