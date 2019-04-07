# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 13:30:48 2019

@author: 30523
"""

import numpy as np 
import random
from pheromone_update_local import pheromone_update_local

def route_produce(ant_number,citys_number,distance_between_city,tau_Matrix_ACS,alpha_ACS,beta_ACS,Eta,q0,rho_local_ACS,tao_set):
    ##############为每个蚂蚁赋值初始的城市
    route_all_ants = np.zeros([ant_number,citys_number],dtype=int)#加入int的原因是默认np.zeros的生成的是[0.,0.,0.]
    city1_all_ant = np.zeros([ant_number,1],dtype=int)
    citys_random = random.sample(range(0,citys_number),citys_number)
    for i in range(ant_number):
        city1_all_ant[i] = random.sample(range(0,citys_number),1)
    for j in range(ant_number):
        route_all_ants[j,0]=city1_all_ant[j]

################开始进行路径构建
    for z in range(ant_number):#每个蚂蚁的循环
        tabu=[]
        tabu.append(route_all_ants[z,0])         
        for j in range(citys_number-1):#每个城市的循环
            ALLOW_citys = [city for city in citys_random if city not in tabu]
            P=[]
            for k in range(len(ALLOW_citys)):
                p=1/(distance_between_city[(tabu[len(tabu)-1]),(ALLOW_citys[k])])
                P.append(p)
            if random.random()<q0:
                #print(P)
                MAXindex = P.index(max(P))# 最近城市的引索
                tabu.append(ALLOW_citys[MAXindex])
            
            else:
                p_sum = sum(P)
                p_ = sorted(P) #p_为从小到大排列,里面数据为概率，数据类型为list 
#                pp= np.array(P)#将p_转化为一个数列，进行操作
#                p_index = np.argsort(pp)#输出从小打到排的引索,数据类型为array
#                p_index_list = p_index.tolist()  # 将p_index的类型转换为p_index_list
                p_a=[]
                p_leijia=[]#斐波那契数列
                ######下面为实现累加的过程,即轮盘赌过程。
                for i in range(len(P)):
                    if i ==0:
                        p_leijia.append(p_[i])
                    else:
                        p_leijia.append(p_leijia[i-1]+p_[i])
                for i in range(len(p_leijia)):
                    p_a.append(p_leijia[i]/p_sum)
                 
                p_a_array =  np.array(p_a)
                index = np.where(p_a_array>random.random())#where返回的是符合条件的引索，如果想找符合条件的数可以，a[a>3]这样       
                index_list = list(index)
                if  index_list:
                    city_next = index_list[0][0]
                    #print(city_next)
                    tabu.append(ALLOW_citys[city_next])
                else:
                    MAXindex = P.index(max(P))# 最近城市的引索
                    tabu.append(ALLOW_citys[MAXindex])
        route_all_ants[z] = tabu
    ########局部信息素更新
        tau_Matrix_ACS = pheromone_update_local(route_all_ants,tau_Matrix_ACS,rho_local_ACS,z,citys_number,tao_set)
    return route_all_ants,tau_Matrix_ACS