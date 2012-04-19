'''
Created on May 17, 2010

@author: Ashique Rupam Mahmood
         ashique@ualberta.ca
'''

from numpy import *
from predictorfactory import PredictorFactory

class SMD(object):
    '''
    classdocs
    '''


    def __init__(self, w0, alphainit, theta):
        '''
        w0 and alphainit should be column vectors 
        '''
        
        self.__w = array(w0)
        self.__alpha = alphainit
        self.__theta = theta
        self.__h = zeros(shape(self.__w))
        
    def step(self, yt, xt):
        pred = dot(self.__w, xt)
        delta = yt - pred
        self.__alpha = multiply(self.__alpha, maximum(0.5, 1 + self.__theta*delta*multiply(xt, self.__h)))
        adeltax = multiply(self.__alpha, xt) * delta
        self.__w = self.__w + adeltax
        hdotx = dot(self.__h, xt)
        self.__h = self.__h - multiply(self.__alpha, xt)*hdotx + adeltax
        
        return {'pred':pred, 'w':self.__w, 'alpha':self.__alpha, 'h':self.__h}
        
    class Factory(PredictorFactory):
        
        def __init__(self, w0, alphainit):
            self.__w0 = w0
            self.__alphainit = alphainit

        def create(self, param1):
            return SMD(w0=self.__w0, alphainit=self.__alphainit, theta=param1)

    class FactoryInitStepsize(PredictorFactory):
        
        def __init__(self, w0, theta):
            self.__w0 = w0
            self.__theta = theta

        def create(self, param1):
            return SMD(w0=self.__w0, alphainit=param1*ones(shape(self.__w0)), theta=self.__theta)
