# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 13:29:52 2019

@author: 30523
"""

def pheromone_update_local(route_all_ants,tau_Matrix_ACS,rho_local_ACS,i,citys_number,tao_set):
    for j in range(citys_number-1):
        x = route_all_ants[i,j]
        y = route_all_ants[i,j+1]
        tau_Matrix_ACS[x,y] =  (1-rho_local_ACS)*tau_Matrix_ACS[x,y] +rho_local_ACS*tao_set
        tau_Matrix_ACS[y,x] =  (1-rho_local_ACS)*tau_Matrix_ACS[y,x] +rho_local_ACS*tao_set
    
    x = route_all_ants[i,citys_number-1]
    y = route_all_ants[i,0]
    tau_Matrix_ACS[x,y] =  (1-rho_local_ACS)*tau_Matrix_ACS[x,y] +rho_local_ACS*tao_set
    tau_Matrix_ACS[y,x] =  (1-rho_local_ACS)*tau_Matrix_ACS[y,x] +rho_local_ACS*tao_set
    return tau_Matrix_ACS