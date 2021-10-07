import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math

def informationEntropy(img,block_size):#计算32*32分块内的信息熵
    num=dict()
    count=0
    entro=0
    for i in range(block_size[0]):
        for j in range(block_size[1]):
            val = img[i][j][0]
            num[val] = num.get(val,0) + 1
            count = count + 1
    #print(num)
    for k in num.keys():
        num[k] = float(num[k]/count)
        entro = entro - num[k] * (math.log(num[k])/math.log(2.0))
    return entro    
#print(informationEntropy(img1,img2.shape))
def min_Entropy_block(img,min_block_size):#遍历lena所有的32*32子块的像素矩阵  计算时间较长
    size = img.shape
    min_Entro = 999
    for i in range(img.shape[0]-min_block_size[0]):
        for j in range(img.shape[1]-min_block_size[1]):
            min_Entro = min(min_Entro,informationEntropy(img[i:i+min_block_size[0],j:j+min_block_size[1]],min_block_size))
            if informationEntropy(img[i:i+min_block_size[0],j:j+min_block_size[1]],min_block_size) == min_Entro :
                min_row,min_column = i,j
            print(min_row,min_column,min_Entro,i,j,informationEntropy(img[i:i+min_block_size[0],j:j+min_block_size[1]],min_block_size))
    return min_row,min_column,min_Entro

#print(min_Entropy_block(img1,img2.shape))
def replace(img1,img2,row,column,size):
    img1[row:row+size[0],column:column+size[1]]=img2
    return img1


if __name__=='__main__' :
    img1= np.array(Image.open('lena.jpg'))
    img2= np.array(Image.open('ji.jpg'))    
    row,column,entro=min_Entropy_block(img1,img2.shape)
    ans = replace(img1,img2,row,column,img2.shape)
    '''    
    因计算时间较长 为了方便查看 将结果放在下一行的注释指令中 经过最小信息熵计算后 
    在从第（0，133）个像素点到（31，164）个像素点的 32*32的子块 信息熵最小 且最小信息熵为1.1042037481427605
    于是进行替换 得到结果 如果运算时间过长 可直接执行下条指令
    '''
    #ans = replace(img1,img2,0,133,img2.shape) 
    im = Image.fromarray(ans)
    im.save('./result1.png')
    im.show()


#plt.ion()
'''
plt.figure('answer')
plt.imshow(replace(img1,img2,0,133,img2.shape))#由于计算时间过长
plt.axis('off')
#plt.ioff()
#plt.show()
plt.savefig('./result.png',)
'''

