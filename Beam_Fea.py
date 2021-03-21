#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 20:49:51 2021

@author: user
"""

import numpy as np

def mesh(L,Element_number,F)
    
    if F[1] == 'distributed':
#add an  if statement if the remaineder of L/element_number is not 0
    nodes = np.arange(0,L+1,L/Element_number)
    
    return nodes


class stifness_m:
    def __init__(self, nodes, Element, L):
      Matrix = np.empty((len(nodes)*2,len(nodes)*2))
      Matrix[Element][Element] = 12
      Matrix[Element][Element+1] = 6*L
      Matrix[Element][Element+2] = -12
      Matrix[Element][Element+3] = 6*L
      Matrix[Element+1][Element] = 6*L
      Matrix[Element+1][Element+1] = 4*L**2
      Matrix[Element+1][Element+2] = -6*L
      Matrix[Element+1][Element+3] = 2*L**2
      Matrix[Element+2][Element] = -12
      Matrix[Element+2][Element+1] = -6*L
      Matrix[Element+2][Element+2] = 12
      Matrix[Element+2][Element+3] = -6*L
      Matrix[Element+3][Element] = 6*L
      Matrix[Element+3][Element+1] = 2*L**2
      Matrix[Element+3][Element+2] = -6*L
      Matrix[Element+3][Element+3] = 4*L**2
                 
def stifness_matrix(nodes, Element_number,L):
    
    indv_stifness_matrix = []
    for Element in range(len(Element_number)):
        
        

def main():
    
    E = 21000
    L = 4

# boundary conditions
    B = [[0 , 'roller'], [L, 'fixed']]

# force
    
    F = [2000 , 'distributed' , [0,L]]

# number of element
    
    Element_number = 5
    
    nodes = mesh(L, Element_number,F)
    
    