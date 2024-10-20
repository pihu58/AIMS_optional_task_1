import pandas as pd
class ordinal_encoder():
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
      for j in data[i]:
        for k in self.all_items[a]:
          if j == k:
            data[i].replace(j,self.all_items[a].index(k),inplace=True)
      a+=1
    return data
  def fit_transform(self,data):
    self.fit(data)
    self.transform(data)
    return data
