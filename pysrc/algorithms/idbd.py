'''
Created on Apr 28, 2010

@author: Ashique Rupam Mahmood
         ashique@ualberta.ca
'''

from numpy import *
from predictorfactory import PredictorFactory

class IDBD(object):
    '''
    classdocs
    '''


    def __init__(self, w0, alphainit, theta):
        '''
        w0 and alphainit should be column vectors 
        '''
        
        self.__w = array(w0)
        self.__beta = array(log(alphainit))
        self.__theta = theta
        self.__h = zeros(shape(self.__w))
        
    def step(self, yt, xt):
        pred = dot(self.__w, xt)
        delta = yt - pred
        dxh = delta*multiply(xt, self.__h)
        self.__beta = self.__beta + self.__theta*dxh
        alpha = exp(self.__beta)
        adeltax = multiply(alpha, xt) * delta
        self.__w = self.__w + adeltax
        ax2 = multiply(multiply(alpha, xt), xt)
        i_ax2 = (1 - ax2)
        i_ax2p = multiply(i_ax2, i_ax2>0)
        self.__h = multiply(i_ax2p, self.__h) + adeltax
        
        return {'pred':pred, 'w':self.__w, 'alpha':alpha, 'h':self.__h, 'dxh':dxh, 'beta':self.__beta, 'ax2':ax2}
        
    class Factory(PredictorFactory):
        
        def __init__(self, w0, alphainit):
            self.__w0 = w0
            self.__alphainit = alphainit

        def create(self, param1):
            return IDBD(w0=self.__w0, alphainit=self.__alphainit, theta=param1)

    class FactoryInitStepsize(PredictorFactory):
        
        def __init__(self, w0, theta):
            self.__w0 = w0
            self.__theta = theta

        def create(self, param1):
            return IDBD(w0=self.__w0, alphainit=param1*ones(shape(self.__w0)), theta=self.__theta)
