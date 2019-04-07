# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 13:32:23 2019

@author: 30523
"""

import numpy as np
def length_get(length_best_ACS,ite,route_all_ants,ant_number,citys_number,distance_between_city,min_PL_ACS,min_route):
#############计算每一只蚂蚁的路径长度###############################################################
    length_all_ants=[]
    for i in range(ant_number):
        route_one_ant = route_all_ants[i]
        lenth_one_ant = 0
        for j in range(citys_number -2):
            lenth_one_ant = lenth_one_ant + distance_between_city[route_one_ant[j],route_one_ant[j+1]]
        lenth_one_ant = lenth_one_ant +  distance_between_city[route_one_ant[0],route_one_ant[citys_number -1]]#首尾相连
        length_all_ants.append(lenth_one_ant)

###########比较每一次迭代的最优解的长度#############################################################
    if ite ==0:
        length_best = min(length_all_ants)#最短的长度
        length_best_index = length_all_ants.index(min(length_all_ants))#最短的长度对应的蚂蚁
        min_route = route_all_ants[length_best_index]#最短长度对应的蚂蚁一次路径
        length_best_ACS = length_best 
    else:
        length_best_iter= min(length_all_ants)#长度
        length_best_iter_index = length_all_ants.index(min(length_all_ants))#引索
        length_best_ACS =min(length_best_iter,length_best_ACS)
        if length_best_iter ==length_best_ACS:#找到最优解
            min_route = route_all_ants[length_best_iter_index]
        else:
            min_route = min_route
    return length_best_ACS,min_route