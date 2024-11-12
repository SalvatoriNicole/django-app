# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 11:29:38 2023

@author: Salvatori
"""

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
#from django.views.decorators.csrf import csrf_exempt
from botrite.models import Botrite
from rest_framework.parsers import JSONParser
from botrite.serializers import BotriteListSerializer

import numpy as np
from celery import shared_task

@shared_task
#@csrf_exempt
@api_view(['GET', 'POST'])
def botrite_list(request, format=None):
    if request.method == 'GET':
        return HttpResponse("I want POST requests")
    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = BotriteListSerializer(data=request.data, many=True)

        if serializer.is_valid():
             #serializer.save()
            
             data = [i["data"] for i in serializer.data]
             state = [i["state"] for i in serializer.data]
            
             len_data=len(data)
             
             if bool(state[0])==True:
                 cumulateInfection_t0=float(state[0]['cumulateInfection'])
                 cumulateInfectionBerry_t0=float(state[0]['cumulateInfectionBerry'])
                 doy1=int(state[0]['doy'])
             else:
                 cumulateInfection_t0=0
                 cumulateInfectionBerry_t0=0
                 doy1=1
             
             for j in range(0,len(data)):
                                                      
                LotId = [i["LotId"] for i in data[j]]
                doy=[int(i["doy"]) for i in data[j]]
                year=[int(i["year"]) for i in data[j]]
                data_daily = [i["data_daily"] for i in data[j]]
                index=doy.index(doy1)
                
                df=[]
                #Missing_values=[]
    
                InfCum1=0
                InfCum2=0

                for days in range(index,len(data_daily)):
                    #LotId = [i["LotId"] for i in data_daily[days]]
                    ver=all("hod" in d for d in data_daily[days])
                    if ver==True:
                        hod=[int(i["hod"]) for i in data_daily[days]]
                    else:
                        hod=[0]*24 
                        Missing_values.append(doy[days])
                        #stop='Missing Value at day '+ str(days)
                        #return JsonResponse(Missing_values, safe=False, status=201)
                        df_new={'LotId':LotId[0],'year':year[0],'data':df}  
                        return JsonResponse(df_new, safe=False, status=201)
                    
                    ver=all("temperature" in d for d in data_daily[days])
                    if ver==True:
                        Temp_data=[float(i["temperature"]) for i in data_daily[days]]
                    else:
                        #Temp_data=[15]*24
                        #Missing_values.append(doy[days])
                        df_new={'LotId':LotId[0],'year':year[0],'data':df}  
                        return JsonResponse(df_new, safe=False, status=201)
                    
                    ver=all("humidity" in d for d in data_daily[days])
                    if ver==True:
                        RH_data=[float(i["humidity"]) for i in data_daily[days]]
                    else:
                        #RH_data=[50]*24
                        #Missing_values.append(doy[days])
                        df_new={'LotId':LotId[0],'year':year[0],'data':df}  
                        return JsonResponse(df_new, safe=False, status=201)
                    
                    ver=all("leafwetness" in d for d in data_daily[days])
                    if ver==True:
                        bagnatura_data=[int(i["leafwetness"]) for i in data_daily[days]]
                    else:
                        #bagnatura_data=[0]*24
                        #Missing_values.append(doy[days])
                        df_new={'LotId':LotId[0],'year':year[0],'data':df}  
                        return JsonResponse(df_new, safe=False, status=201)
                    ver=all("rain" in d for d in data_daily[days])
                    if ver==True:
                        Rain_data=[float(i["rain"]) for i in data_daily[days]]
                    else:
                        #Rain_data=[0]*24
                        #Missing_values.append(doy[days])
                        df_new={'LotId':LotId[0],'year':year[0],'data':df}  
                        return JsonResponse(df_new, safe=False, status=201)
                    ver=all("GS" in d for d in data_daily[days])
                    if ver==True:
                        GS=[int(i["GS"]) for i in data_daily[days]]
                    else:
                        #GS=[30]*24
                        #Missing_values.append(doy[days])
                        df_new={'LotId':LotId[0],'year':year[0],'data':df}  
                        return JsonResponse(df_new, safe=False, status=201)
                    ver=all("treatment" in d for d in data_daily[days])
                    if ver==True:
                        treatment=[int(i["treatment"]) for i in data_daily[days]]
                    else:
                        #treatment=[False]*24
                        #Missing_values.append(doy[days])
                        df_new={'LotId':LotId[0],'year':year[0],'data':df}  
                        return JsonResponse(df_new, safe=False, status=201)
                    
                    len_data_daily=len(treatment)
                    
                    Rain_data = [0 if i is None else i for i in Rain_data] #substitute None with 0
                    bagnatura_data = [0 if i is None else i for i in bagnatura_data]
                    RH_data = [0 if i is None else i for i in RH_data]
                
                    Mf= [0] * len(Temp_data)
                    i=1
                    hours=1
                    start=0
                    while i<=len(Temp_data)-1:
                        if (Rain_data[i]>=0.2 or bagnatura_data[i]==1 or RH_data[i]>=90):
                            if start==1:
                                Mf[i]=Mf[i-1]+1 
                            elif start==0:
                                Mf[i]=1
                                start=1
                        else:
                            if start==1:
                                Mf[i]=Mf[i-1]
                            elif start==0:
                                Mf[i]=0
                        i+=1
                        hours+=1   
                        
                
                
                    Temp_data_daily=np.mean(Temp_data)
                    RH_data_daily=np.mean(RH_data)
                    bagnatura_data_daily=np.sum(bagnatura_data) #QUESTO CAMBIATO!!
                    Rain_data_daily=np.mean(Rain_data)
                    Mf_daily=np.mean(Mf)
                    T_min_data_daily=min(Temp_data)
                    T_max_data_daily=max(Temp_data)
                    GS=np.mean(GS)
                    treatment=np.mean(treatment)
                    
                    if T_max_data_daily==T_min_data_daily:
                        Teq=0
                    else:
                        Teq=(Temp_data_daily-T_min_data_daily)/(T_max_data_daily-T_min_data_daily)
                        
                    MYGR=np.power(3.78*np.power(Teq,0.9)*(1-Teq),0.475)*Mf_daily
                    SPOR=(3.7*Teq**0.9*(1-Teq))**10.49*(-3.595+0.097*RH_data_daily-0.0005*RH_data_daily**2)
                    CYSO=MYGR*SPOR
                    
                    #"""FIRST INFECTION TIME WINDOW"""
                    
                    Teq=(Temp_data_daily-0)/(35-0)
                    SUS1=-379.09*(GS/100)**3+671.25*(GS/100)**2-390.33*(GS/100)+75.209
                    INF1=((3.56*Teq**0.99*(1-Teq))**0.71)/(1+np.exp(1.85-0.19*bagnatura_data_daily))*SUS1
                    RIS1=CYSO*INF1 
                    "relative infection severity"
                    
                    #"""SECOND INFECTION TIME WINDOW (stage 79 to 89)"""
                    SUS2=5*10**-17*np.exp(0.4219*GS)
                    INF2=(6.416*Teq**1.292*(1-Teq))**0.469*np.exp(-2.3*np.exp(-0.048*bagnatura_data_daily))*SUS2
                    RIS2=CYSO*INF2
                    
                    #"""Infection rate for berry-to-berry infection during the second infection """
                    SUS3=0.0546*GS-3.87
                    if SUS3>1:
                        SUS3=1
                        
                    INF3=((7.75*(Teq**2.14)*(1-Teq))**0.469)/(1+np.exp(35.36-40.26*RH_data_daily/100))*SUS3
                    RIS3=CYSO*INF3
                    
                    if RIS1<0:
                        RIS1=0
                    if RIS2<0:
                        RIS2=0
                    if RIS3<0:
                        RIS3=0
                    
                    #RIS1 = Relative infection severity of the inflorescences and young clusters; 
                    #RIS2 = Relative infection severity for conidial infection on ripening berries; 
                    #RIS3 = Relative infection severity for berry-to-berry infection on ripening berries.
                                        
                    
                    if GS <53:
                        Infection=0
                        Infection_berry=0
                        cumulateInfection=0
                        cumulateInfectionBerry=0
                        
                    if GS >= 53 and GS <= 73:
                        Infection=RIS1
                        Infection_berry=0
                        cumulateInfection=cumulateInfection_t0+Infection
                        cumulateInfectionBerry=0
                        
                    if GS > 73 and GS < 79:
                        Infection=0
                        Infection_berry=0
                        cumulateInfection=cumulateInfection_t0
                        cumulateInfectionBerry=0
                    if GS >= 79 and GS < 89:
                        Infection=0 #RIS2
                        Infection_berry=RIS2+RIS3              
                        cumulateInfection=cumulateInfection_t0
                        cumulateInfectionBerry=cumulateInfectionBerry_t0+Infection_berry
                    if GS >= 89:
                        Infection=0
                        Infection_berry=0
                        cumulateInfection=cumulateInfection_t0
                        cumulateInfectionBerry=cumulateInfectionBerry_t0
                    
                                        
                    if treatment==True:
                        cumulateInfection=0
                        cumulateInfectionBerry=0
                    
                    cumulateInfectionBerry_t0=cumulateInfectionBerry
                    cumulateInfection_t0=cumulateInfection
                    
                    df_days={'doy':doy[days], 'Infection': Infection, 'InfectionBerry': Infection_berry, 'cumulateInfection':cumulateInfection, 'cumulateInfectionBerry':cumulateInfectionBerry}
                    df.append(df_days)
            
             df_new={'LotId':LotId[0],'year':year[0],'data':df}   
        
             return JsonResponse(df_new, safe=False, status=201)
        return JsonResponse(serializer.errors, safe=False, status=400)
        
    
#@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def botrite_detail(request, pk):
    try:
        botrite = Botrite.objects.get(pk=pk)
    except Botrite.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BotriteListSerializer(botrite)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BotriteListSerializer(botrite, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, safe=False, status=400)

    elif request.method == 'DELETE':
        botrite.delete()
        return HttpResponse(status=204)
            
