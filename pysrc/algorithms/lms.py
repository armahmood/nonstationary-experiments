'''
Created on Apr 24, 2010

@author: Ashique Rupam Mahmood
         ashique@ualberta.ca
'''

from numpy import *
from predictorfactory import PredictorFactory

class LMS(object):

    def __init__(self, w0, alpha):
        '''
        w0 and alpha should be column vectors 
        '''

        self.__w = array(w0)
        self.__alpha = alpha
                
    def step(self, yt, xt):
        pred = dot(self.__w, xt)
        delta = yt - pred
        self.__w = self.__w + multiply(self.__alpha, xt) * delta
        
        return {'pred': pred, 'w':self.__w}

    class Factory(PredictorFactory):
        
        def __init__(self, w0):
            self.__w0 = w0

        def create(self, param1):
            return LMS(w0=self.__w0, alpha=param1)
    