import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math

def Entropy_compute(img,dim):
    num = dict()
    count = 0
    entro = 0
    val = [0,0]
    for i in range(0,len(img),2):
        for j in range(0,len(img[0]),2):
            val[0] = img[i,j,0]
            val[1] = img[i,j+1,0]
            num[str(val)] = num.get(str(val),0) + 1
            count = count + 1
    for k  in num.keys():
        num[k] = float(num[k]/count)
        entro = entro - num[k] * (math.log(num[k])/math.log(2.0))
        print(k+' '+str(num[k])+' '+str(entro))
    return entro
if __name__ ==  '__main__':
    img1 = np.array(Image.open('lena.jpg'))
    print(Entropy_compute(img1,2))#经计算，二维平均符号熵为11.503102119935228比特