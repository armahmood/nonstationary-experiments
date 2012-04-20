'''
Created on Jan 22, 2012

@author: ashique
'''

from numpy import *
from pylab import *
from experiments.utils import utils

def dataload(dir, paramfile):
    params = loadtxt(dir+"/"+paramfile)
    data = loadtxt(dir+"/"+"avg_rmse.txt")
    data[isnan(data)] = 10**4 
    data[data>10**4] = 10**4
    
    return params, data

def main():
    loaddir = "../../../data/"
    probdir = "prob_trans.corrinputs.sigma2_u1.1.0.sigma2_u2.1.0.sigma2_v.1.0.m.20.nofu1s.5.N.25000" 
    utils.setsizes()
    
    ymax = 1#data[params==0.001]
    params, data = dataload(dir=loaddir+"lms/"+probdir, paramfile="stepsizes.txt")
    plot(params, data/ymax, label="LMS")

    #params, data = dataload(dir=loaddir+"bmp/"+probdir, paramfile="metastepsizes.txt")
    #plot(params, data/ymax, label="K-Y")

    params, data = dataload(dir=loaddir+"idbd/"+probdir, paramfile="metastepsizes.txt")
    plot(params, data/ymax, label="IDBD")

    params, data = dataload(dir=loaddir+"autostep/"+probdir, paramfile="metastepsizes.txt")
    plot(params, data/ymax, label="Autostep")

    params, data = dataload(dir=loaddir+"rls/"+probdir, paramfile="one_minus_gammas.txt")
    plot(params, data/ymax, label="RLS")

    legend(loc='lower left')
    xlim([10**-4, 1])
    ylim([0, 2])
    xscale("log")
    xlabel("tunable parameter", fontsize=utils.getxlabelsize())
    ylabel("RMSE", fontsize=utils.getxlabelsize(), labelpad=utils.getxlabelpadsize())
    
if __name__ == '__main__':
    main()
    show()
    
