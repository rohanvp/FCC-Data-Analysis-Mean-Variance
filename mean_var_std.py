import numpy as np

def calculate(list):

  try:
  
    flattend_list=np.copy(list)
    list=np.reshape(list,(3,3))
    meana1=np.mean(list,axis=0)
    meana2=np.mean(list,axis=1)
    meanf=np.mean(flattend_list)
  
    vara1=np.var(list,axis=0)
    vara2=np.var(list,axis=1)
    varaf=np.var(flattend_list)
  
    stda1=np.std(list,axis=0)
    stda2=np.std(list,axis=1)
    stdf=np.std(list)
  
    maxa1=np.max(list,axis=0)
    maxa2=np.max(list,axis=1)
    maxf=np.max(flattend_list)
  
    mina1=np.min(list,axis=0)
    mina2=np.min(list,axis=1)
    minf=np.min(flattend_list)
  
    suma1=np.sum(list,axis=0)
    suma2=np.sum(list,axis=1)
    sumf=np.sum(flattend_list)
    
    
    calculations={}
  
    meanlist=[meana1.tolist(),meana2.tolist(),meanf]
    varlist=[vara1.tolist(),vara2.tolist(),varaf]
    stdlist=[stda1.tolist(),stda2.tolist(),stdf]
    maxlist=[maxa1.tolist(),maxa2.tolist(),maxf]
    minlist=[mina1.tolist(),mina2.tolist(),minf]
    sumlist=[suma1.tolist(),suma2.tolist(),sumf]
  
    calculations["mean"]=meanlist
    calculations["variance"]=varlist
    calculations["standard deviation"]=stdlist
    calculations["max"]=maxlist
    calculations["min"]=minlist
    calculations["sum"]=sumlist
    # print(calculations)
    

  except:
    raise ValueError("List must contain nine numbers.")
  

  return calculations