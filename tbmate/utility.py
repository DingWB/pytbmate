# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 19:52:20 2020

@author: DingWB
"""

import os,sys
import struct

version=1.0

dtype_fmt={
        'float':'f',
        'int':'i',
        'string':'s',
        'chr':'c',
        'double':'d'
        }

dtype_map={
        'int':1,
        'float':4,
        'double':5,
        'string':7,
        'chr':6
        }

dtype_map_rev={
        1:'int',
        2:'int',
        3:'int',
        4:'float',
        5:'double',
        6:'chr',
        7:'string'
        }

dtype_func={
        'float':float,
        'int':int,
        'string':str,
        'chr':str,
        'double':float
        }

def pack_header(idx,outfile,dtype):
    print(f"Packing and writing to {outfile}")
    idx_len=len(idx)
    fo=open(outfile,'wb')
    fo.write(struct.pack('3s',b'tbk')) #'tbk',byte=3*1=3
    fo.write(struct.pack('f',version)) #version:1; byte=4
    fo.write(struct.pack('q',dtype_map[dtype])) #dtype, bytes=8
#    fo.write(struct.pack('i',idx_len)) #idx_len, byte=4
    fo.write(struct.pack('q',-1)) #max data, byte=8

    if idx_len > 8169:
        idx=idx[:8169]

    fo.write(struct.pack(f'{idx_len}s',bytes(idx,'utf-8'))) #idx file, byte=idx_len

    if idx_len < 8169:
        for i in range(8169-idx_len):
            fo.write(struct.pack('x')) #fill to 500.
    #Total used bytes = 3+4+8+8+8169=8192
    return fo