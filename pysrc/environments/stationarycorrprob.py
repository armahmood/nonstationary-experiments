'''
Created on Jan 21, 2012

@author: ashique
'''

from numpy import *
from numpy.random import *

class StationaryCorrProb(object):
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
            
        # generate cor matrix
        
        a = reshape(randn(n*n), (n, n))
        b = mat(a.T)*mat(a)
        c = sqrt(diag(b))
        corrm = mat(diag(1/c))*b*mat(diag(1/c))
        g = ones(n)*sqrt(sigma2_u2)
        g[:nofu1s] = sqrt(sigma2_u1)
        self.covm = multiply(g*g.T, corrm)
        
    def step(self):
        u = multivariate_normal(zeros(self.n), self.covm)            
        d = dot(u, self.w_o) + randn()*sqrt(self.sigma2_v)
        
        return {"d":d, "u":u}
        
    def getcovm(self):
        return self.covm
        
        
        
        