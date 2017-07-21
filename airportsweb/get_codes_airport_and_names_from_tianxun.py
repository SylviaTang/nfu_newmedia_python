
# coding: utf-8

# ## 從這裡開始

# In[19]:

# 輸入
import os
import json
with open(os.path.join('data','airports_zh.json'), 'r', encoding='utf8') as fp:
    reload = json.load(fp)


# In[20]:

reload


# In[21]:

# 讀回到dict_c_n 就不用再抓網頁
dict_c_n = reload


# In[22]:

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

data


# In[24]:

data.keys()


# In[25]:

dict_c_n.keys()


# In[26]:

# 比較兩數據的大小
print (len(dict_c_n))
print (len(data))


# In[27]:

# 取交集
airports_available = set(dict_c_n.keys()).intersection(set(data.keys()))


# In[28]:

data_output = { dict_c_n[c]:{'latitude':float(data[c].split(",")[0]),'longitude':float(data[c].split(",")[1]) }  for c in airports_available}
data_output


# In[29]:

# 輸出
import json
import os.path
with open(os.path.join('data','Airports_zh_code_geo.json'), 'w', encoding='utf8') as fp:
    json.dump(data_output, fp)

