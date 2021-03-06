import json
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2): # 经度1，纬度1，经度2，纬度2 （十进制度数）  
    """ 
    Calculate the great circle distance between two points  
    on the earth (specified in decimal degrees) 
    """  
    # 将十进制度数转化为弧度  
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])  
  
    # haversine公式  
    dlon = lon2 - lon1   
    dlat = lat2 - lat1   
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2  
    c = 2 * asin(sqrt(a))   
    r = 6371 # 地球平均半径，单位为公里  
    return c * r 

def get_latlon(airport):
    lat_lon = []
    with open('data\Airports_zh_code_geo.json', 'r', encoding='utf8') as infile:
        dd = json.load (infile)
        for k,v in dd.items():
            if k == airport:
                for v in v.values():
                    lat_lon.append(v)
        return lat_lon

def get_distance(airport1,airport2):
    a1 = get_latlon(airport1)
    a2 = get_latlon(airport2)
    distance = haversine(a1[1],a1[0],a2[1],a2[0])
    return str("%.2f" %distance) + ' km'
    
test = get_distance('1','1')
print(test)
