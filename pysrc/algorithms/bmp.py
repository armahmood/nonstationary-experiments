'''
Created on Apr 24, 2010

@author: Ashique Rupam Mahmood
         ashique@ualberta.ca
'''
# This is the KY algorithm, originally done by Benveniste et al.
from numpy import *
from predictorfactory import PredictorFactory

class BMP(object):

    def __init__(self, w0, initalpha, mu):
        '''
        w0 and alpha should be column vectors 
        '''

        self.__w = array(w0)
        self.__alpha = initalpha
        self.__mu = mu
        self.__h = zeros(size(w0))
                
    def step(self, yt, xt):
        pred = dot(self.__w, xt)
        delta = yt - pred
        self.__w = self.__w + self.__alpha * xt * delta
        self.__alpha = self.__alpha + self.__mu*delta*dot(xt, self.__h)
        self.__alpha = max(self.__alpha, 10**-10)
        self.__h = self.__h - self.__alpha*dot(xt, self.__h)*xt + delta * xt 
        
        return {'pred': pred, 'w':self.__w, 'alpha':self.__alpha}

    class Factory(PredictorFactory):
        
        def __init__(self, w0, initalpha):
            self.__w0 = w0
            self.__initalpha = initalpha

        def create(self, param1):
            return BMP(w0=self.__w0, initalpha=self.__initalpha, mu=param1)
    