'''
Created on May 3, 2010

@author: rupam
'''

from numpy import *
from predictorfactory import PredictorFactory

class Autostep(object):
    '''
    classdocs
    '''

    def __init__(self, w0, p, lmbda, mu, alpha=None):
        '''
        w0 and alphainit should be column vectors 
        '''
        self.__w = array(w0)
        if alpha==None:
            self.__alpha = 0.1*ones(shape(self.__w))
        else:
            self.__alpha = alpha
        self.__mu = mu
        self.__v = zeros(shape(self.__w))
        self.__h = zeros(shape(self.__w))
        self.__lambda = lmbda
        self.__p = p
        
    def params(self):
        return self.__w, self.__v, self.__h
        
    def step(self, yt, xt):
        pred = dot(self.__w, xt)
        delta = yt - pred
        dxh = delta*multiply(xt, self.__h)
        x2 = multiply(xt, xt)
        self.__v = maximum(abs(dxh)**self.__p, self.__v + self.__lambda*self.__alpha*x2*(abs(dxh)**self.__p - self.__v))
        v = self.__v
        bnum = multiply(self.__mu*dxh, v>0)
        v[v==0.0] = 1
        alphaprime = self.__alpha*exp(bnum/(v**(1.0/self.__p)))
        ## but, should be interpreted with beta
        self.__alpha = maximum(alphaprime/maximum(1, 0.5*dot(alphaprime, x2)), 10**-20)
        adx = multiply(self.__alpha, xt) * delta
        self.__w = self.__w + adx
        ax2 = multiply(self.__alpha, x2)
        self.__h = multiply(self.__h, 1-ax2) + adx
        
        return {'pred':pred, 'w':self.__w, 'alpha':self.__alpha, 'h':self.__h, 'dxh':dxh, 'm':self.__v, 'ax2': ax2, 'metastep':self.__mu/(v**(1/self.__p))}
    
    class Factory(PredictorFactory):
        
        def __init__(self, w0, p, lmbda):
            self.__w0 = w0
            self.__lambda = lmbda
            self.__p = p

        def create(self, param1):
            return Autostep(w0=self.__w0, p=self.__p, lmbda=self.__lambda, mu=param1)

    class FactoryInitStepsize(PredictorFactory):
        
        def __init__(self, w0, p, lmbda, mu):
            self.__w0 = w0
            self.__lambda = lmbda
            self.__p = p
            self.__mu = mu

        def create(self, param1):
            return Autostep(w0=self.__w0, p=self.__p, lmbda=self.__lambda, mu=self.__mu, alpha=param1*ones(shape(self.__w0)))

#b_i(t) &=& \delta(t) x_i(t) h_i(t)\\
#m_i(t+1) &=& \max \left| b_i(t)\right|, m_i(t) + 0.1 \alpha_i(t) x_i^2(t) \left( \left| b_i(t)\right| - m_i(t) \right)\\
#\beta_i(t+1) &=& \beta_i(t) + \mu \frac{b_i(t)}{m_i(t+1)}\\
#s(t) &=& \sum_j e^{\beta_j(t+1)} x_j^2(t)\\
#M(t+1) &=& \max s(t), M(t)+(1-\lambda)(s(t) - M(t))\\
#\alpha_i(t+1) &=& \frac{e^{\beta_i(t+1)}}{M(t+1)}\\
#w_i(t+1) &=& w_i(t) + \alpha_i(t+1) \delta(t) x_i(t)\\
#h_i(t+1) &=& h_i(t)\left(1 - \alpha(t+1)x_i^2(t)\right)+\alpha_i(t+1)\delta(t)x_i(t)\\