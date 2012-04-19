'''
Created on May 17, 2010

@author: Ashique Rupam Mahmood
         ashique@ualberta.ca
'''

from numpy import *
from predictorfactory import PredictorFactory

class ALAP(object):
    '''
    classdocs
    '''


    def __init__(self, w0, alphainit, gamma, theta):
        '''
        w0 and alphainit should be column vectors 
        '''
        
        self.__w = array(w0)
        self.__alpha = alphainit
        self.__theta = theta
        self.__gamma = gamma
        self.__v = zeros(shape(w0))
        self.__dxtm1 = zeros(shape(w0))
        
    def step(self, yt, xt):
        pred = dot(self.__w, xt)
        delta = yt - pred
        self.__v = self.__v + self.__gamma * (multiply(delta*xt, delta*xt) - self.__v) 
        v = self.__v
        anum = multiply(self.__theta*delta*multiply(xt, self.__dxtm1), v>0)
        v[v==0.0] = 1
        self.__alpha = multiply(self.__alpha, (1 + anum/v))
        self.__alpha = maximum(self.__alpha, 10.0**-10)
        adeltax = multiply(self.__alpha, xt) * delta
        self.__w = self.__w + adeltax
        self.__dxtm1 = delta*xt
        
        return {'pred':pred, 'w':self.__w, 'alpha':self.__alpha}
        
    class Factory(PredictorFactory):
        
        def __init__(self, w0, alphainit, gamma):
            self.__w0 = w0
            self.__alphainit = alphainit
            self.__gamma = gamma

        def create(self, param1):
            return ALAP(w0=self.__w0, alphainit=self.__alphainit, gamma=self.__gamma, theta=param1)

    class FactoryInitStepsize(PredictorFactory):
        
        def __init__(self, w0, gamma, theta):
            self.__w0 = w0
            self.__gamma = gamma
            self.__theta = theta

        def create(self, param1):
            return ALAP(w0=self.__w0, alphainit=param1*ones(shape(self.__w0)), gamma=self.__gamma, theta=self.__theta)
