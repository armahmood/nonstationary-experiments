'''
Created on Jan 21, 2012

@author: ashique
'''

import sys
sys.path.append("../../")

from numpy import *
from numpy.random import *
#from matplotlib.pyplot import *
from environments.stationaryprob import *
from algorithms.autostep import *
from algorithms.bmp import *
from algorithms.lms import *
from algorithms.rls import *
from algorithms.idbd import *
import os
from time import *

display = True

def main():
    M = 20
    N = 25000
    to = N/2
    nofu1s = M/4
    nruns = 50
    sigma2_u2 = 1.0
    sigma2_v = 1.0
    if len(sys.argv)>1:
        sigma2_u1 = double(sys.argv[1])
    else:
        sigma2_u1 = 100.0
    mus = array([10**-12, 10**-7, 10**-4, 10**-3, 2*10**-3, 5*10**-3, 10**-2, 2*10**-2, 5*10**-2, 10**-1, 2*10**-1, 5*10**-1, 1.0])
    mses = zeros((len(mus), nruns))
    savedir = "../../../data/autostep/"
    dirname = "prob.inputs.sigma2_u1."+str(sigma2_u1)+".sigma2_u2."+str(sigma2_u2)+".sigma2_v."+str(sigma2_v)+".m."+str(M)+".nofu1s."+str(nofu1s)+".N."+str(N)
    if not os.path.exists(savedir + dirname):
        os.makedirs(savedir + dirname)
    savetxt(savedir + dirname + "/metastepsizes.txt", mus)
    for run in range(nruns):
        seed(run)
        for mu in mus:
            t = clock()
            prob = StationaryProb(sigma2_u1=sigma2_u1, sigma2_u2=sigma2_u2, sigma2_v=sigma2_v, n=M, nofu1s=nofu1s)
            autostep = Autostep(w0=zeros(M), lmbda=10**-4, mu=mu, alpha=1.0/(M*sigma2_u1))
            w = zeros((M, N))
            mse = 0
            dev = 0
            for n in range(N):
                ret = prob.step()
                d = ret["d"]
                u = ret["u"]
                ret = autostep.step(yt = d, xt = u)
                pred = ret["pred"]
                w[:, n] = ret["w"]
                error = d - pred
                if (n>=to):
                    mse = mse + 1.0*(error**2 - mse)/(n+1-to)
                    
            mses[mu==mus, run==array(range(nruns))] = mse
            print "run" + str(run) + ": " + str(clock() - t) + "sec"
        savetxt(savedir + dirname+"/run"+str(run)+".txt", sqrt(mses[:,run]))
    print sqrt(mean(mses, 1))
    savetxt(savedir + dirname+"/avg_rmse.txt", sqrt(mean(mses, 1)))
    if display==True:
        plot(mus, sqrt(mean(mses, 1)))       
        title("autostep") 
        xscale("log")        
        ylim([0, 20])
        
if __name__ == '__main__':
    main()
    if display==True:
        show()