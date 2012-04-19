'''
Created on Apr 24, 2010

@author: Ashique Rupam Mahmood
         ashique@ualberta.ca
'''

from numpy import *
from predictorfactory import PredictorFactory

class RLS(object):

    def __init__(self, w0, gama):
        '''
        w0 and alpha should be column vectors
        '''

        self.__w = w0
        self.__gama = gama
        #self.__B = (1-gamma)**-1*mat(eye(2))
        self.__B = mat(eye(w0.size))
        #self.__B = mat(eye(2))
                
    def step(self, yt, xt):
        pred = dot(self.__w, xt)
        delta = yt - pred
        mxt = mat(xt).T
        A = self.__B/(self.__gama + mxt.T*self.__B*mxt)
        self.__w = self.__w +  delta*array(A*mxt).T
        self.__B = self.__gama**-1 * (eye(self.__w.size) - A*mxt*mxt.T)*self.__B
        #self.__B = self.__gamma**-1 * (eye(2) - A*mxt*mxt.T)*self.__B
        
        return {'pred': pred, 'w':self.__w, "B":self.__B, "A":A}

    class Factory(PredictorFactory):
        
        def __init__(self, w0):
            self.__w0 = w0

        def create(self, param1):
            return RLS(w0=self.__w0, gama=1-param1)
    