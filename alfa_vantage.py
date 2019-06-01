'''
Created on Jul 27, 2018

@author: vmaaaaan
'''

import alpha_vantage.timeseries as avts


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
ts = avts.TimeSeries(key = 'UQV2D45VFXJGX00j')
print("Fetching Data... 1 of 5")
raw_data_0, meta_data_0 = ts.get_daily('HD', outputsize= 'full')

data_p1_0 = str(raw_data_0).split("': '")
data_p2_0 = []
for d in data_p1_0:
    for ds in d.split("', '"):
        data_p2_0.append(ds)
data_p2b_0 = []
for d in data_p2_0:
    for ds in d.split("'},"):
        data_p2b_0.append(ds)
data_rev_0 = []
new_seg_0 = []
for d in data_p2b_0:
    if is_number(d.strip()):
        new_seg_0.append(float(d.strip()))
    if len(new_seg_0) == 5:
        data_rev_0.append(new_seg_0)
        new_seg_0 = []
  
data_0 = []
for dx in range(len(data_rev_0)-1, -1, -1):
    data_0.append(data_rev_0[dx])
print("Data Fetched")
#print(raw_data)
#print(data_p1)
#print(data_p2)
print(data_p2b_0)
print(data_0)
print(len(data_0))


print("Fetching Data... 2 of 5")
raw_data_1, meta_data_1 = ts.get_daily('XOM', outputsize= 'full')
data_p1_1 = str(raw_data_1).split("': '")
data_p2_1 = []
for d in data_p1_1:
    for ds in d.split("', '"):
        data_p2_1.append(ds)
data_p2b_1 = []
for d in data_p2_1:
    for ds in d.split("'},"):
        data_p2b_1.append(ds)
data_rev_1 = []
new_seg_1 = []
for d in data_p2b_1:
    if is_number(d.strip()):
        new_seg_1.append(float(d.strip()))
    if len(new_seg_1) == 5:
        data_rev_1.append(new_seg_1)
        new_seg_1 = []
                
data_1 = []
for dx in range(len(data_rev_1)-1, -1, -1):
    data_1.append(data_rev_1[dx])
print("Data Fetched")
#print(raw_data)
#print(data_p1)
#print(data_p2)
print(data_p2b_1)
print(data_1)
print(len(data_1))


print("Fetching Data... 3 of 5")
raw_data_2, meta_data_2 = ts.get_daily('WBA', outputsize= 'full')
data_p1_2 = str(raw_data_2).split("': '")
data_p2_2 = []
for d in data_p1_2:
    for ds in d.split("', '"):
        data_p2_2.append(ds)
data_p2b_2 = []
for d in data_p2_2:
    for ds in d.split("'},"):
        data_p2b_2.append(ds)
data_rev_2 = []
new_seg_2 = []
for d in data_p2b_2:
    if is_number(d.strip()):
        new_seg_2.append(float(d.strip()))
    if len(new_seg_2) == 5:
        data_rev_2.append(new_seg_2)
        new_seg_2 = []
                
data_2 = []
for dx in range(len(data_rev_2)-1, -1, -1):
    data_2.append(data_rev_2[dx])
print("Data Fetched")
#print(raw_data)
#print(data_p1)
#print(data_p2)
print(data_p2b_2)
print(data_2)
print(len(data_2))


print("Fetching Data... 4 of 5")
raw_data_3, meta_data_3 = ts.get_daily('JPM', outputsize= 'full')
data_p1_3 = str(raw_data_3).split("': '")
data_p2_3 = []
for d in data_p1_3:
    for ds in d.split("', '"):
        data_p2_3.append(ds)
data_p2b_3 = []
for d in data_p2_3:
    for ds in d.split("'},"):
        data_p2b_3.append(ds)
data_rev_3 = []
new_seg_3 = []
for d in data_p2b_3:
    if is_number(d.strip()):
        new_seg_3.append(float(d.strip()))
    if len(new_seg_3) == 5:
        data_rev_3.append(new_seg_3)
        new_seg_3 = []
                
data_3 = []
for dx in range(len(data_rev_3)-1, -1, -1):
    data_3.append(data_rev_3[dx])
print("Data Fetched")
#print(raw_data)
#print(data_p1)
#print(data_p2)
print(data_p2b_3)
print(data_3)
print(len(data_3))


print("Fetching Data... 5 of 5")
raw_data_4, meta_data_4 = ts.get_daily('AXP', outputsize= 'full')
data_p1_4 = str(raw_data_4).split("': '")
data_p2_4 = []
for d in data_p1_4:
    for ds in d.split("', '"):
        data_p2_4.append(ds)
data_p2b_4 = []
for d in data_p2_4:
    for ds in d.split("'},"):
        data_p2b_4.append(ds)
data_rev_4 = []
new_seg_4 = []
for d in data_p2b_4:
    if is_number(d.strip()):
        new_seg_4.append(float(d.strip()))
    if len(new_seg_4) == 5:
        data_rev_4.append(new_seg_4)
        new_seg_4 = []
                
data_4 = []
for dx in range(len(data_rev_4)-1, -1, -1):
    data_4.append(data_rev_4[dx])
print("Data Fetched")
#print(raw_data)
#print(data_p1)
#print(data_p2)
print(data_p2b_4)
print(data_4)
print(len(data_4))
