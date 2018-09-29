# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.backends.backend_pgf import FigureCanvasPgf
mpl.backend_bases.register_backend('pdf', FigureCanvasPgf)
pgf_with_latex = {
    "pgf.texsystem": "xelatex",         # use Xelatex which is TTF font aware
}

mpl.rcParams.update(pgf_with_latex)
plt.rc('text', usetex=True)
plt.rc('font', family='serif', serif = 'CMU Serif', size = 12)
plt.rcParams['text.latex.preamble'] = [
            r'\usepackage{amsmath}',
            r'\usepackage{amsfonts}',
            r'\usepackage{graphicx}',
            r'\usepackage[english,russian]{babel}',
            r'\usepackage[utf8]{inputenc}',
            r'\usepackage[T1]{fontenc}',
            ]
g = np.genfromtxt('veryharddiagram.csv',delimiter=';')
x = g[1:,0]
y = g[1:,1]
x2 = g[1:6,2]
y2 = g[1:6,5]
x3 = np.arange(0,min(x),2)
y3 = np.zeros(len(x3))
fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot(111)
ax.grid(which='both')
ax.scatter(x, y, label = r'устойчивое равновесие', color = '#FF7800')
ax.scatter(x3, y3, color = '#FF7800')
ax.scatter(x2, y2, label = r'неустойчивое равновесие', color = '#133CAC', marker='x')
ax.set_xlim(0,max(x)+0.2*max(x))
ax.set_ylim(0-2,max(y)+0.2*max(y))
ax.tick_params(axis='x', direction='inout')
ax.tick_params(axis='y', direction='inout')
ax.set_xlabel(r'М, усл. ед.')
ax.set_ylabel(r'Амплитуда, усл. ед.')
ax.legend(loc='upper left')
fig.savefig('veryharddiagram.pdf')
plt.show()
