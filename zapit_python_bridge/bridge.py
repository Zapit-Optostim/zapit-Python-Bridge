import matlab.engine


class bridge:

    # Attributes (remove from here, perhaps, when it all works)
    def __init__(self):
        """
        Connect to the MATLAB engine
        """

        names = matlab.engine.find_matlab()
        if "zapit" in names:
            print("CONNECTING TO MATLAB")
            self.eng = matlab.engine.connect_matlab("zapit")

            print("CONNECTED")
            # TODO -- check variables exist
            self.hZP = self.eng.workspace["hZP"]
            self.hZPview = self.eng.workspace["hZPview"]
        else:
            print('FAILED TO FIND MATLAB SESSION "zapit"')

    def __del__(self):
        print("Disconnecting from MATLAB")
        self.eng.quit()  # Otherwise it locks up if we try to reconnect

    def send_samples(
        self,
        conditionNum=-1,
        laserOn=True,
        hardwareTriggered=True,
        logging=True,
        verbose=False,
    ):
        condition_num, laser_on = self.eng.sendSamples(
            self.hZP,
            "conditionNum",
            -1,
            "laserOn",
            True,
            "hardwareTriggered",
            True,
            "logging",
            True,
            "verbose",
            False,
            nargout=2,
        )

    def stop_opto_stim(self):
        """
        Stops the optostim
        """
        self.eng.stopOptoStim(self.hZP, nargout=0)

    def num_stim_cond(self):
        """
        TODO
        """
        return 0

    def set_experiment_dir(self):
        """
        TODO
        """
        return 0

    def unset_experiment_dir(self):
        # TODO (this also does not exist in MATLAB)
        return 0
