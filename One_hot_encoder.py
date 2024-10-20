import pandas as pd
class one_hot_encoder():
  def __init__(self):
    pass
  def fit(self,data):
    self.all_items=[]
    self.cat_list =[x for x in data.columns if data[x].dtype=="object"]
    for i in self.cat_list:
      self.all_items.append(data[i].unique().tolist())
  def transform(self,data):
    a = 0
    for i in self.cat_list:
      for k in self.all_items[a]: 
        b = []
        for j in data[i]:
          if j == k:
            b.append(1)
          else:
            b.append(0)
        data[k] = b
      data.drop(i,axis=1,inplace=True)       
      a+=1
    return data
  def fit_transform(self,data):
    self.fit(data)
    self.transform(data)
    return data
