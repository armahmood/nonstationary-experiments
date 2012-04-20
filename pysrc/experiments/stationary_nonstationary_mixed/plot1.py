'''
Created on Jan 22, 2012

@author: ashique
'''

from numpy import *
from pylab import *
from experiments.utils import utils

def jointdataload(dir1, dir2, paramfile):
    params = loadtxt(dir1+"/"+paramfile)
    data1 = loadtxt(dir1+"/"+"avg_rmse.txt")
    data1[isnan(data1)] = 10**4 
    data1[data1>10**4] = 10**4

    data2 = loadtxt(dir2+"/"+"avg_rmse.txt")
    data2[isnan(data2)] = 10**4 
    data2[data2>10**4] = 10**4
    
    
    return params, data1, data2

def main():
    utils.setsizes()
    mpl.rcParams['lines.markeredgewidth'] = utils.geterrorbarlinewidth()
    loaddir = "../../../data/"
    probdir1 = "prob.s2u.1.0.a.0.9998.s2v.1.0.s2o1.0.1.s2o1.0.0.m.20.o1s.5.N.50000"
    probdir2 = "prob.s2u.1.0.a.0.9998.s2v.1.0.s2o1.100.0.s2o1.0.0.m.20.o1s.5.N.50000" 
    
    params, data1, data2 = jointdataload(dir1=loaddir+"lms/"+probdir1, dir2=loaddir+"lms/"+probdir2, paramfile="stepsizes.txt")
    ymax1 = data1[params==0.05]
    ymax2 = data2[params==0.05]
    #plot(params, (data1/ymax1 + data2/ymax2)/2.0)

    params, data1, data2 = jointdataload(dir1=loaddir+"lms/"+probdir1, dir2=loaddir+"lms/"+probdir2, paramfile="stepsizes.txt")
    plot(params, (data1/ymax1 + data2/ymax2)/2.0, label="LMS")

    params, data1, data2 = jointdataload(dir1=loaddir+"idbd/"+probdir1, dir2=loaddir+"idbd/"+probdir2, paramfile="metastepsizes.txt")
    plot(params, (data1/ymax1 + data2/ymax2)/2.0, label="IDBD")

    params, data1, data2 = jointdataload(dir1=loaddir+"autostep/"+probdir1, dir2=loaddir+"autostep/"+probdir2, paramfile="metastepsizes.txt")
    plot(params, (data1/ymax1 + data2/ymax2)/2.0, label="Autostep")

    #params, data1, data2 = jointdataload(dir1=loaddir+"bmp/"+probdir1, dir2=loaddir+"bmp/"+probdir2, paramfile="metastepsizes.txt")
    #plot(params, (data1/ymax1 + data2/ymax2)/2.0, label="K-Y")

    params, data1, data2 = jointdataload(dir1=loaddir+"rls/"+probdir1, dir2=loaddir+"rls/"+probdir2, paramfile="one_minus_gammas.txt")
    plot(params, (data1/ymax1 + data2/ymax2)/2.0, label="RLS")

    legend(loc='lower left')
    xlim([10**-11, 1])
    ylim([0, 1.2])
    xscale("log")
    xlabel("tunable parameter", fontsize=utils.getxlabelsize())
    ylabel("$S$ (RMSE relative to best LMS)", fontsize=utils.getxlabelsize(), labelpad=utils.getxlabelpadsize())

if __name__ == '__main__':
    main()
    show()
    
