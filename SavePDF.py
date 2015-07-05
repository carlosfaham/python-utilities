from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import pyplot as plt
import os

def save(filename,fig=plt.gcf()):
    if filename[-3:] != 'pdf':
        filename = filename + '.pdf'
    pp = PdfPages(filename)
    fig.savefig(pp, format='pdf')
    a = os.getcwd()
    print 'Saved file %s/%s' % (a,filename)
    pp.close()

def save_eps(filename,fig=plt.gcf()):
    if filename[-3:] != 'eps':
        filename = filename + '.eps'
    pp = PdfPages(filename)
    fig.savefig(pp, format='eps')
    a = os.getcwd()
    print 'Saved file %s/%s' % (a,filename)
    pp.close()