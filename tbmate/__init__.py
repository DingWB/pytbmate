#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 14:52:41 2020

@author: DingWB
"""

__all__=['tbmate']
__version__='1.0'
from .tbmate import pack_list,to_tbk,Read,Header,Query
from .tbmate import read_one_site,read_multi_samples,ReadBulk
