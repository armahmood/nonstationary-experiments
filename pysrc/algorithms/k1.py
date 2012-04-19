'''
Created on Apr 28, 2010

@author: Ashique Rupam Mahmood
         ashique@ualberta.ca
'''

from numpy import *
from predictorfactory import PredictorFactory

class K1(object):
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
        
    def params(self):
        return self.__w, self.__beta, self.__theta, self.__h
        
    def step(self, yt, xt):
        pred = dot(self.__w, xt)
        delta = yt - pred
        dxh = delta*multiply(xt, self.__h)
        self.__beta = self.__beta + self.__theta*dxh
        alpha = exp(self.__beta)/(1+dot(multiply(exp(self.__beta), xt), xt))
        adeltax = multiply(alpha, xt) * delta
        self.__w = self.__w + adeltax
        ax2 = multiply(multiply(alpha, xt), xt)
        i_ax2 = (1 - ax2)
        self.__h = multiply(self.__h + adeltax, i_ax2)
        
        return {'pred':pred, 'w':self.__w, 'alpha':alpha, 'beta':self.__beta, 'h':self.__h, 'dxh':dxh, 'ax2':ax2}
        
    class Factory(PredictorFactory):
        
        def __init__(self, w0, alphainit):
            self.__w0 = w0
            self.__alphainit = alphainit

        def create(self, param1):
            return K1(w0=self.__w0, alphainit=self.__alphainit, theta=param1)
    
    class FactoryInitStepsize(PredictorFactory):
        
        def __init__(self, w0, theta):
            self.__w0 = w0
            self.__theta = theta

        def create(self, param1):
            return K1(w0=self.__w0, theta=self.__theta, alphainit=param1)
    
    