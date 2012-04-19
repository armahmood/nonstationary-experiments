'''
Created on Jan 21, 2012

@author: ashique
'''

import sys
sys.path.append("../../../")

from numpy import *
from numpy.random import *
#from matplotlib.pyplot import *
from environments.nonstationary import *
from algorithms.autostep import *
from algorithms.bmp import *
from algorithms.lms import *
from algorithms.rls import *
from algorithms.idbd import *
import os
from time import *

display = True

def main():
    N = 50000
    M = 20
    o1s = M/4
    nruns = 50
    to = N/2
    sigma2_u = 1.0
    a = 0.9998
    sigma2_v = 1.0
    if len(sys.argv)>1:
        sigma2_o1 = double(sys.argv[1])
    else:
        sigma2_o1 = 100.0
    if len(sys.argv)>2:
        sigma2_o2 = double(sys.argv[2])
    else:
        sigma2_o2 = 0.0
    gamas = array([5*10**-3, 10**-2, 2*10**-2, 5*10**-2, 10**-1, 2*10**-1, 5*10**-1, 9*10**-1])
    mses = zeros((len(gamas), nruns))
    savedir = "../../../data/rls/"
    dirname = "prob.nonstat.s2u."+str(sigma2_u)+".a."+str(a)+".s2v."+str(sigma2_v)+".s2o1."+str(sigma2_o1)+".s2o1."+str(sigma2_o2)+".m."+str(M)+".o1s."+str(o1s)+".N."+str(N)
    if not os.path.exists(savedir + dirname):
        os.makedirs(savedir + dirname)
    savetxt(savedir + dirname + "/one_minus_gammas.txt", gamas)
    for run in range(nruns):
        for gama in gamas:
            t = clock()
            seed(1)
            prob = Nonstationary(sigma2_u=sigma2_u, a=a, sigma2_v=sigma2_v, sigma2_o1=sigma2_o1, sigma2_o2=sigma2_o2, n=M, o1s=o1s)
            rls = RLS(w0=zeros(M), gama=1-gama)
            w = zeros((M, N))
            mse = 0
            dev = 0
            seed(run)
            for n in range(N):
                ret = prob.step()
                d = ret["d"]
                u = ret["u"]
                ret = rls.step(yt = d, xt = u)
                pred = ret["pred"]
                w[:, n] = ret["w"]
                error = d - pred
                if (n>=to):
                    mse = mse + 1.0*(error**2 - mse)/(n+1-to)
                    
            mses[gama==gamas, run==array(range(nruns))] = mse
            print "run" + str(run) + ": " + str(clock() - t) + "sec"
        savetxt(savedir + dirname+"/run"+str(run)+".txt", sqrt(mses[:,run]))
    print sqrt(mean(mses, 1))
    savetxt(savedir + dirname+"/avg_rmse.txt", sqrt(mean(mses, 1)))
    if display==True:
        plot(gamas, sqrt(mean(mses, 1)))  
        title("rls")      
        xscale("log")        
        ylim([0, 20])
        
if __name__ == '__main__':
    main()
    if display==True:
        show()