'''
Created on Jan 22, 2012

@author: ashique
'''

from numpy import *
from pylab import *
from experiments.utils import utils

def dataload(dir, paramfile):
    params = loadtxt(dir+"/"+paramfile)
    data = loadtxt(dir+"/"+"run0.txt")
    data[isnan(data)] = 10**4 
    data[data>10**4] = 10**4
    
    return params, data

def main():
    loaddir = "../../../data/"
    probdir = "prob.s2u.1.0.a.0.9998.s2v.1.0.s2o1.100.0.s2o1.0.0.m.20.o1s.5.N.50000" 
    utils.setsizes()
    
    params, data = dataload(dir=loaddir+"lms/"+probdir, paramfile="stepsizes.txt")
    ymax = 1
    plot(params, data/ymax, label="LMS")

#    params, data = dataload(dir=loaddir+"bmp/"+probdir, paramfile="metastepsizes.txt")
#    plot(params, data/ymax, label="BMP")

    params, data = dataload(dir=loaddir+"idbd/"+probdir, paramfile="metastepsizes.txt")
    plot(params, data/ymax, label="IDBD")
    params, data = dataload(dir=loaddir+"autostep/"+probdir, paramfile="metastepsizes.txt")
    plot(params, data/ymax, label="Autostep")

    params, data = dataload(dir=loaddir+"rls/"+probdir, paramfile="one_minus_gammas.txt")
    plot(params, data/ymax, label="RLS")

    legend(loc='lower left')
    xlim([10**-11, 1])
    ylim([0, 140])
    xscale("log")
    xlabel("tunable parameter", fontsize=utils.getxlabelsize(), labelpad=utils.getxlabelpadsize())
    ylabel("RMSE", fontsize=utils.getxlabelsize(), labelpad=utils.getxlabelpadsize())

if __name__ == '__main__':
    main()
    show()
    
