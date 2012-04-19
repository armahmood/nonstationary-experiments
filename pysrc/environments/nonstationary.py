'''
Created on Jan 21, 2012

@author: ashique
'''

from numpy import *
from numpy.random import *

class Nonstationary(object):
    '''
    classdocs
    '''

    def __init__(self, sigma2_u, a, sigma2_v, sigma2_o1, sigma2_o2, n, o1s):
        # defaults are from 14.8
        '''
        Constructor
        '''

        self.sigma2_u = sigma2_u
        self.a = a
        self.sigma2_v = sigma2_v
        self.sigma2_o1 = sigma2_o1 
        self.sigma2_o2 = sigma2_o2
        self.n = n
        self.o1s = o1s
        self.w_o = zeros(n)
        for i in range(n):
            if i < self.o1s:
                self.w_o [i] = randn()*sqrt(self.sigma2_o1)
            else:
                self.w_o [i] = randn()*sqrt(self.sigma2_o2)

        
    def step(self):
        
        u = zeros(self.n)
        for i in range(self.n):
            u[i] = randn()*sqrt(self.sigma2_u)
            
        omega= zeros(self.n)
        for i in range(self.n):
            if i < self.o1s:
                omega[i] = randn()*sqrt(self.sigma2_o1)
            else:
                omega[i] = randn()*sqrt(self.sigma2_o2)
        
        d = dot(u, self.w_o) + randn()*sqrt(self.sigma2_v)
        
        self.w_o = self.w_o*self.a + omega
        
        return {"d":d, "u":u, "w_o":self.w_o }
        
        
        
        
        
        