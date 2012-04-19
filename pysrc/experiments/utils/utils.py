'''
Created on Jul 2, 2010

@author: rupam
'''

from numpy import *
from pylab import *
from matplotlib import cm

def setsizes():

    mpl.rcParams['axes.linewidth'] = 1.0
    mpl.rcParams['lines.markeredgewidth'] = 0.0
    mpl.rcParams['lines.markersize'] = 10.0
    
    mpl.rcParams['xtick.labelsize'] = 17.0
    mpl.rcParams['ytick.labelsize'] = 17.0
    #mpl.rcParams['xtick.major.size'] = 10.0
    #mpl.rcParams['ytick.major.size'] = 10.0
    mpl.rcParams['xtick.direction'] = "in"
    mpl.rcParams['ytick.direction'] = "in"
    mpl.rcParams['lines.linewidth'] = 3.0
    #mpl.rcParams['axes.labelsize'] = 2.0
    mpl.rcParams['ytick.minor.pad'] = 50.0

def figtype():
    return ".pdf"

def putlegend(ax, loc=1, legendsize=18, opacity=0.6):
    leg = ax.legend(loc=loc,fancybox=True, shadow=True)
    for t in leg.get_texts():
        t.set_fontsize(legendsize)
    leg.get_frame().set_alpha(opacity)
    
def geterrorbarlinewidth():
    return 1.0

def getxlabelsize():
    return 20.0

def getylabelsize():
    return 25.0

def getlegendsize():
    return 18

def getxlabelpadsize():
    return 20

def getylabelpadsize():
    return 20

def getfigpath():
    return "../../../figures/"

def toyprob1targetstd():
    return 254.847966763

def robotaccelztargetstd():
    return 175.428848452

def robotlight2targetstd():
    return 31.8888755645

def robotirdistance0targetstd():
    return 59.6289001142

def robotmotor0currenttargetstd():
    return 7.57543969475

def robotmotor0speedtargetstd():
    return 12.9950478888

def robotrotationveltargetstd():
    return 157.264319282


def toyprob1targetrange():
    return 254.847966763

def robotaccelztargetrange():
    return 2047.0+1770.0

def robotlight2targetrange():
    return 870.0-16.0

def robotirdistance0targetrange():
    return 255.0-1.0

def robotmotor0currenttargetrange():
    return 107.0-0.0

def robotmotor0speedtargetrange():
    return 107.0+49.0

def robotrotationveltargetrange():
    return 503.0+454.0
