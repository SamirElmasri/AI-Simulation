#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 20:49:51 2021

@author: user
"""

import numpy as np

def mesh(L,Element_number,F):
    
    if F[1] == 'distributed':
#add an  if statement if the remaineder of L/element_number is not 0
        nodes = np.arange(0,L+1,L/Element_number)
    
    return nodes

#create the stifnees matrix
class stifness_m:
    def __init__(self, nodes, Element, L):
      Matrix = np.zeros((len(nodes)*2,len(nodes)*2))
      Matrix[Element*2][Element*2] = 12
      Matrix[Element*2][Element*2+1] = 6*L
      Matrix[Element*2][Element*2+2] = -12
      Matrix[Element*2][Element*2+3] = 6*L
      Matrix[Element*2+1][Element*2] = 6*L
      Matrix[Element*2+1][Element*2+1] = 4*L**2
      Matrix[Element*2+1][Element*2+2] = -6*L
      Matrix[Element*2+1][Element*2+3] = 2*L**2
      Matrix[Element*2+2][Element*2] = -12
      Matrix[Element*2+2][Element*2+1] = -6*L
      Matrix[Element*2+2][Element*2+2] = 12
      Matrix[Element*2+2][Element*2+3] = -6*L
      Matrix[Element*2+3][Element*2] = 6*L
      Matrix[Element*2+3][Element*2+1] = 2*L**2
      Matrix[Element*2+3][Element*2+2] = -6*L
      Matrix[Element*2+3][Element*2+3] = 4*L**2
      
      self.Matrix = Matrix
                 
def stifness_matrix(nodes, Element_number,L):
    
    indv_stifness_matrix = []
    global_matrix = np.zeros((len(nodes)*2,len(nodes)*2))
    for Element in range(Element_number):
        class_element = stifness_m(nodes,Element,L)
        indv_stifness_matrix.append(class_element)
        global_matrix = global_matrix + class_element.Matrix
        
    return indv_stifness_matrix , global_matrix
        
def boundary_conditions(nodes,Element_number, L , F, B):
    
    if F[1] == 'distributed':
        if F[2][1] == L:
            M = 'M' + str(nodes[0])
            F_at_node = F[0]/L
            F_nodes = np.array([nodes [0] , F_at_node , M])
            for i in range(1 , len(nodes)):
                moment = 'M' + str(i)
                F_nodes = np.row_stack((F_nodes, [i , F_at_node , moment]))
    
    d = 'd' + str(nodes[0])
    r = 'r' + str(nodes[0])
    Deformation_nodes = np.array([nodes[0], d[0], r[0]])
    
    for i in range(1, len(nodes)):
        d = 'd' + str(i)
        r = 'r' + str(i)
        Deformation_nodes = np.row_stack((Deformation_nodes , [i , d ,r] ))
                
    for b in B:
       if b[0] in nodes:
           index = np.where(nodes == b[0])
           if b[1] == 'roller':
               Deformation_nodes[index[0][0]][1] = 0
               F_nodes[index[0][0]][2] = 0

           if b[1] ==   'pin':
               Deformation_nodes[index[0][0]][1] = 0
               F_nodes[index[0][0]][2] = 0
    
    return F_nodes , Deformation_nodes

def main():
    
    E = 21000
    L = 4

# boundary conditions
    B = [[0 , 'roller'], [L, 'pin']]

# force
    
    F = [2000 , 'distributed' , [0,L]]

# number of element
    
    Element_number = 4
    
    nodes = mesh(L, Element_number,F)
    indv_stifness_matrix , global_matrix = stifness_matrix(nodes, Element_number , L)
    
    
