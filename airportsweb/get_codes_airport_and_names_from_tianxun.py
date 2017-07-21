#当下py文件代码由廖汉腾老师提供并指导
# coding: utf-8

# ## 從這裡開始

# In[19]:

# 导入os和json两个模块，打开data目录下的airport_zh.json，然后输出到数据。
import os
import json
with open(os.path.join('data','airports_zh.json'), 'r', encoding='utf8') as fp:
    reload = json.load(fp)


# In[20]:
#重新加载一次之前运行过的模块
reload


# In[21]:
#把reload上的数据赋值到dict_c_n上
# 讀回到dict_c_n 就不用再抓網頁
dict_c_n = reload


# In[22]:
#导入csv模块，通过row函数等处理原airport-codes.csv得出新的数据
# 數據來源
# https://github.com/datasets/airport-codes
import csv
data = {}

with open(os.path.join('data','airport-codes.csv'), 'r', encoding='utf8') as fp:
    reader = csv.DictReader(fp, delimiter = ',')
    for row in reader: 
        if row['iso_country'] == 'CN' and row['iata_code']!='':
            data[row['iata_code']] = row['coordinates']


# In[23]:
#输出data内的数据
data


# In[24]:
#输出data数据中的值
data.keys()


# In[25]:
#输出dict_c_n数据中的值
dict_c_n.keys()


# In[26]:
#打印出dict_c_n和data中的数据总量
# 比較兩數據的大小
print (len(dict_c_n))
print (len(data))


# In[27]:
#取dict_c_n的值和data的值的交集生成一个集合
# 取交集
airports_available = set(dict_c_n.keys()).intersection(set(data.keys()))


# In[28]:
#通过生成特定格式的的字典的办法赋值到data_output下
data_output = { dict_c_n[c]:{'latitude':float(data[c].split(",")[0]),'longitude':float(data[c].split(",")[1]) }  for c in airports_available}
data_output


# In[29]:
#导入json和os.path模块再输出保存到Airports_zh_code_geo.json下
# 輸出
import json
import os.path
with open(os.path.join('data','Airports_zh_code_geo.json'), 'w', encoding='utf8') as fp:
    json.dump(data_output, fp)

