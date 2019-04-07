# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 13:25:11 2019

@author: 30523
"""

def pheromone_update_global(tau_Matrix_ACS,rho_global_ACS,citys_number,min_route,length_best_ACS):
    for i in range(citys_number-2):
        x=min_route[i]
        y=min_route[i+1]
        delta_tao = 1/length_best_ACS
        tau_Matrix_ACS[x,y] =(1-rho_global_ACS)* tau_Matrix_ACS[x,y] +rho_global_ACS*delta_tao
        tau_Matrix_ACS[y,x] =(1-rho_global_ACS)* tau_Matrix_ACS[y,x] +rho_global_ACS*delta_tao
    x = min_route[citys_number-1]
    y = min_route[0]
    delta_tao = 1/length_best_ACS 
    tau_Matrix_ACS[x,y] =(1-rho_global_ACS)* tau_Matrix_ACS[x,y] +rho_global_ACS*delta_tao
    tau_Matrix_ACS[y,x] =(1-rho_global_ACS)* tau_Matrix_ACS[y,x] +rho_global_ACS*delta_tao
    return tau_Matrix_ACS