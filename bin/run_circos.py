#!/usr/bin/env python
# -- coding:utf-8 --
# Last-modified: 10 Nov 2017 04:46:43 PM
#
#         Module/Scripts Description
# 
# Copyright (c) 2016 Yunfei Wang <yfwang0405@gmail.com>
# 
# This code is free software; you can redistribute it and/or modify it
# under the terms of the BSD License (see the file COPYING included with
# the distribution).
# 
# @status:  experimental
# @version: 1.0.0
# @author:  Yunfei Wang
# @contact: yfwang0405@gmail.com

# ------------------------------------
# python modules
# ------------------------------------

import os
import sys
import pandas
import pycircos

# ------------------------------------
# constants
# ------------------------------------

# ------------------------------------
# Misc functions
# ------------------------------------

# ------------------------------------
# Classes
# ------------------------------------

# ------------------------------------
# Main
# ------------------------------------

if __name__=="__main__":
    if len(sys.argv)==1:
        sys.exit("Example:"+sys.argv[0]+" infile1 infile2 [infile3 ...]\n{0} ".format(DESCRIPTION))

    CNV = pandas.read_table("scores.gistic")
    CNV['chrom'] = 'chr' + CNV.Chromosome.astype(str)
    CNV = CNV.sort_values(['Chromosome','Start'])
    
    AMP = CNV.loc[CNV.Type=='Amp',:]
    DEL = CNV.loc[CNV.Type=='Del',:]
    DEL.loc[:,'frequency'] *= -1
    
    chromsizes = pandas.read_table("hg19.fa.sizes",index_col=0,header=None,names=['start','length','chrom'])
    cg = Circos(chromsizes, gap=2)
    # draw cytoband
    cg.draw_cytobands(8.1,0.3,"cytoBand.txt.gz")
    
    # draw chrom region
    cg.draw_scaffold(8.1,0.3)
    cg.draw_ticks(8.1,0.2,inside=True)
    cg.draw_scaffold_ids(9.2,inside=False,fontsize=15)
    
    # CNV
    cg.draw_scaffold(5.5,0.01)
    cg.fill_between(5.5,AMP.iloc[:100,:],start='Start',end='End',score='frequency',scale=2.0,facecolor='red',alpha=0.5)
    cg.fill_between(5.5,DEL.iloc[:100,:],start='Start',end='End',score='frequency',scale=2.0,facecolor='blue',alpha=0.5)
    
    # draw links
    cg.draw_link(4.5,['chr1','chr4'],[10000000,10000000],[110000000,110000000],color='purple',alpha=0.5)
    cg.draw_link(4.5,['chr3','chr8'],[10000000,10000000],[110000000,110000000],color='lightblue',alpha=0.5)
    
    plt.savefig('Circos.pdf')