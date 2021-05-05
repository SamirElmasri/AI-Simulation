#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 22:35:23 2021

@author: user
"""
def mesh(L,Element_number):
    
    nodes = np.arange(0,L+1,L/Element_number)
    
    return nodes

import numpy as np
import pandas as pd

class stifness_m:
    def __init__(self, nodes, Element, L_element):
      Matrix = np.zeros((len(nodes)*2,len(nodes)*2))
      Matrix[Element*2][Element*2] = 12
      Matrix[Element*2][Element*2+1] = 6*L_element
      Matrix[Element*2][Element*2+2] = -12
      Matrix[Element*2][Element*2+3] = 6*L_element
      Matrix[Element*2+1][Element*2] = 6*L_element
      Matrix[Element*2+1][Element*2+1] = 4*L_element**2
      Matrix[Element*2+1][Element*2+2] = -6*L_element
      Matrix[Element*2+1][Element*2+3] = 2*L_element**2
      Matrix[Element*2+2][Element*2] = -12
      Matrix[Element*2+2][Element*2+1] = -6*L_element
      Matrix[Element*2+2][Element*2+2] = 12
      Matrix[Element*2+2][Element*2+3] = -6*L_element
      Matrix[Element*2+3][Element*2] = 6*L_element
      Matrix[Element*2+3][Element*2+1] = 2*L_element**2
      Matrix[Element*2+3][Element*2+2] = -6*L_element
      Matrix[Element*2+3][Element*2+3] = 4*L_element**2

      
      self.Matrix = Matrix
      
#create the stifness matrix
def stifness_matrix(nodes, Element_number,L_element):
    
    indv_stifness_matrix = []
    global_matrix = np.zeros((len(nodes)*2,len(nodes)*2))
    for Element in range(Element_number):
        class_element = stifness_m(nodes,Element,L_element)
        indv_stifness_matrix.append(class_element)
        global_matrix = global_matrix + class_element.Matrix
        
    return indv_stifness_matrix , global_matrix

class f_class:
    def __init__(self, nodes, Element, L_element, W):
        f_indv = np.zeros(len(nodes)*2)
        f_indv[Element*2] = -W*L_element/2
        f_indv[Element*2+1] = -W*(L_element**2)/12
        f_indv[Element*2+2] = -W*L_element/2
        f_indv[Element*2+3] = W*(L_element**2)/12
        
        self.f_indv = f_indv

#create f0
def f0(nodes,Element_number, L_element ,W):
    
    F_list = np.zeros(len(nodes)*2)
    F_class_list = []
    for Element in range(Element_number):
        findv = f_class(nodes, Element, L_element, W)
        F_class_list.append(findv)
        F_list = F_list + findv.f_indv
        
    return F_class_list, F_list

def solver(F_list, global_matrix, L_element, E, I):
    
    global_matrix = global_matrix[2:,2:]
    global_matrix = E*I*global_matrix/(L_element**3)
    F_list = F_list[2:]
    Solution = np.linalg.solve(global_matrix, F_list)
    
    return Solution

def main():
    
    E = 30000000
    Element_number = 10
    
    L_list = np.arange(100,10100,100)
    W_list = np.arange(20,1000,10)
    I_list = np.arange(100,10100,100)

    Solution_list = []
    
    for L in range(len(L_list)):
        for W in range(len(W_list)):
            for I in range(len(I_list)):
                L_element = L_list[L]/Element_number
                inputs = np.array([L_list[L],W_list[W],I_list[I]])
                nodes = mesh(L_element,Element_number)
                indv_stifness_matrix , global_matrix = stifness_matrix(nodes, Element_number,L_element)
                F_class_list, F_list = f0(nodes,Element_number, L_element ,W_list[W])
                Solution = solver(F_list, global_matrix, L_element, E, I_list[I])
                S = np.array([])
                for i in range(Element_number):
                    S = np.append(S,Solution[i*2])
                S = np.concatenate(([0],S), axis = None)
                Solution_list.append(np.concatenate((inputs,S), axis = None))
    
    DF = pd.DataFrame(Solution_list)
    DF.to_csv("cantiliver.csv", header = None)
    