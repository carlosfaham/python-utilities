import matplotlib

def font_size(font_size):
    font = {'family' : 'normal',
            'weight' : 'normal',
            'size'   : font_size}

    matplotlib.rc('font', **font)