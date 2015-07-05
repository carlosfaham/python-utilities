import time
class tictoc():
    '''
    This provides similar functionality to MATLAB's tic toc timing.
    Create an object t = tictoc()
    then t.tic() starts timer, t.toc() ends it and prints the delta time 
    It supports multiple t.toc() calls to time different stages.
    '''
    def __init__(self):
        self.time1 = None
    def tic(self):
        self.time1 = time.time()
    def toc(self):
        self.time2 = time.time()
        delta_seconds = float(self.time2 - self.time1)
        print 'Time elapsed: %3.2f sec' % delta_seconds