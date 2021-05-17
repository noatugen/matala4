# -*- coding: utf-8 -*-
"""
Created on Wed May 12 22:44:41 2021

@author: HP
"""

import requests
import pprint
from sys import exit

def lat_lng(address_1):
    try:
        address=address_1
        api_key="AIzaSyBxdzxzHBqeNdfrZIx4ZFrpBct8Vgm2XxE"
        url="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (address,api_key)
        try:
            response = requests.get(url)
            if not response.status_code == 200:
                print("HTTP error",response.status_code)
            else:
                try:
                    response_data = response.json()
                except:
                    print("Response not in valid JSON format")
        except:
            print("Something went wrong with requests.get")
        # print(response_data)
        lat_lng=response_data['results'][0]['geometry']['location']
        lat=lat_lng['lat']
        lng=lat_lng['lng']
        return lat,lng
    except:
        print("There is a problem")
        exit()
def distance_time(address_1):
        try:
            address=address_1
            api_key="AIzaSyBxdzxzHBqeNdfrZIx4ZFrpBct8Vgm2XxE"
            # url="https://maps.googleapis.com/maps/api/distancematrix/json?origins=Vancouver+BC|Seattle&destinations=San+Francisco|Victoria+BC&mode=bicycling&language=fr-FR&key=YOUR_API_KEY"
            url="https://maps.googleapis.com/maps/api/distancematrix/json?key=%s&origins=tel+aviv&destinations=%s" % (api_key,address)
            try:
                response = requests.get(url)
                if not response.status_code == 200:
                    print("HTTP error",response.status_code)
                else:
                    try:
                        response_data = response.json()
                    except:
                        print("Response not in valid JSON format")
            except:
                print("Something went wrong with requests.get")
            distance = response_data['rows'][0]['elements'][0]['distance']['text']
            time = response_data['rows'][0]['elements'][0]['duration']['value']
            time_hr=int(time/(3600))
            time_min=round((time-3600*time_hr)/60)
            return distance,int(time_min),int(time_hr)
        except:
            print("There is a problem")
            exit()
            
        
    
def the_three_bigger(all_dictionary):
    max1=0
    list_1=[0,0,0]
    for i in range(3):
        max1=0
        for key in all_dictionary:
            lst=all_dictionary[key][0].split()
            lstt=lst[1]
            lstt=lstt.replace(",","")
            lstt=float(lstt)   
            if lstt>max1 :
                max1=lstt
                list_1[i]=key
        all_dictionary.pop(list_1[i])
    return list_1
   
lst1=[]
big=0
data_dic=dict()
file = open("dests.txt" , encoding='utf8')
for line in file:
    data_1=distance_time(line)
    data_2=lat_lng(line)
    line=line.rstrip()
    # all_data = {"distance": data_1[0] , "Time(mins)": data_1[1] , "Time(hours)": data_1[2] , "lat": data_2[1] , "lng": data_2[0]}
    all_data = ("distance: " + str(data_1[0]) , "Time: " +  str(data_1[2]) + ' hours ' + str(data_1[1]) + ' minutes '  ,  "longitude: " + str(data_2[1]),"latitude: " +  str(data_2[0]))
    data_dic[line]=all_data

pprint.pprint(data_dic)
data_dic_1=data_dic.copy()
print(the_three_bigger(data_dic_1))





