'''
Created on Jan 21, 2012

@author: ashique
'''

from numpy import *
from numpy.random import *

class StationaryProb(object):
    '''
    classdocs
    '''

    def __init__(self, sigma2_u1, sigma2_u2, sigma2_v, n, nofu1s):
        # defaults are from 14.8
        '''
        Constructor
        '''

        self.sigma2_u1 = sigma2_u1
        self.sigma2_u2 = sigma2_u2
        self.sigma2_v = sigma2_v
        self.nofu1s = nofu1s
        self.n = n
        self.w_o = zeros(n)
        for i in range(n):
            self.w_o[i] = randn()
        
    def step(self):
        
        u = zeros(self.n)
        for i in range(self.n):
            if i < self.nofu1s:
                u[i] = randn()*sqrt(self.sigma2_u1)
            else:
                u[i] = randn()*sqrt(self.sigma2_u2)
            
        d = dot(u, self.w_o) + randn()*sqrt(self.sigma2_v)
        
        return {"d":d, "u":u}
        
        
        
        
        
        