
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:


# A sample image

# Penguins.jpg
image = plt.imread('demo.jpg')

fig, ax = plt.subplots()
ax.imshow(image)
# ax.axis('off')  # clear x-axis and y-axis

plt.show()
print("image.shape = ",image.shape)


# In[3]:


# A sample image

# Penguins.jpg
image2 = plt.imread('Penguins.jpg')

fig, ax = plt.subplots()
ax.imshow(image2)
# ax.axis('off')  # clear x-axis and y-axis

plt.show()
print("image.shape = ",image2.shape)


# In[4]:


# A sample image

# Penguins.jpg
image1 = plt.imread('peo.jpg')

fig, ax = plt.subplots()
ax.imshow(image1)
# ax.axis('off')  # clear x-axis and y-axis

plt.show()
print("image.shape = ",image1.shape)
print(image1[0][0])


# In[5]:


plt.imshow(image1)
image1


# ### Kmeans算法
# > input: K, data #簇数，数据 
# <br>output：dataClass # [0,k-1 ]
# 1. 随机初始化K个中心点，计算 E^
# 2. 按照最近邻，分类。
# 3. 算出下一个中心。计算 E
# 4. 如果E - E^ > 迭代值。
# >>4.1 是，则回到2 <br>
# 4.2 否，退出

# ## 计算上一个中心的价值函数E ，和下一个中心resCenter

# In[12]:


def cost(data, centerList, k, log=False):
    shape = data.shape
    res = np.zeros(shape, dtype=np.uint8)
    resCenter = np.zeros((k, shape[2]+1))
    costE=0.0
    
    color = 255.0 / k    
    for i in range(shape[0]):
        for j in range(shape[1]):
            minD = 1e9
            minId = 0
            for center in range(k):               
                
#                                是的，与物理距离无关。新的中心也是RGB的三个值
                minue = centerList[center] -  data[i][j]
                dist = np.sum(np.dot(minue, minue))  # 此处距离还有问题。只考虑颜色，不考虑 x,y吗
#                 print("data[i][j] = ",data[i][j])
#                 print("centerList[center] = ", centerList[center])
#                 print("dist = ", dist)
    
                if(dist < minD):
                    minD = dist
                    minId = center
            #归为了某一类
            res[i][j] = centerList[minId]
            costE += minD
            #统计
            resCenter[minId] += np.concatenate((data[i, j], [1]))
       
    if(log):
        print("before 除法，中心点: \n",resCenter)
        
    for cen in range(k):
        if(resCenter[cen][3] != 0):
            resCenter[cen] /= resCenter[cen][3]
        
    if(log):    
        print("after: 除法，中心点：\n",resCenter)
    resCenter = np.delete(resCenter, 3, axis = 1)#删除 resCenter的第四列
    resCenter = resCenter.astype(int)#变为整数
    
    
    if(log):
        print("去掉计数列，中心点：\n",resCenter)
        print("E = ", costE)
        # https://blog.csdn.net/u013608424/article/details/80117178 imshow颜色问题。
        # 原来是数据类型的关系，，dtype要是 uint8才行。。。。
    plt.imshow(res, cmap=plt.get_cmap('hot'))
    plt.show()
    return costE, resCenter              


# ## Test Cost函数的正确性

# In[7]:


#传入 白色、灰色两个点，作为初始点，计算cost、类别
a, b = cost(image1, [[255,255,255 ], [93, 93, 93 ]], 2, True)

print(type(a))
print(type(b))


# ### 一些不常用的 库函数，
# 1. dot点乘
# 2. concatenate数组拼接
# 
# 

# In[16]:


one = np.ones([16, 3])
white = [255, 255, 255]
for i in range(16):
    one[i] *= white
two = one.reshape(4,4,3)

plt.imshow(two, cmap=plt.get_cmap('hot'))  
plt.show()


# In[8]:


minD = 1e9
a= np.array([1,2,3])
b= np.array([2,2,2])
print(np.dot(a, b) )
print(minD )
print(np.concatenate((b, a)) )

one = np.ones([16, 3], dtype=np.uint8)
yellow = np.array([225, 182, 62], dtype=np.uint8)
white = [255, 255, 255]
for i in range(16):
    one[i] *= yellow
two = one.reshape(4,4,3)

plt.imshow(255-two, cmap=plt.get_cmap('hot'))  
plt.show()

plt.imshow(two)
plt.show()
one


# # Kmeans算法主函数

# In[9]:


def My_Kmeans(data1, K, echos=20, minDiff=1000, log=False, rand = False):
    shape = data1.shape
    if(rand == False):
        np.random.seed(1)

    
    center = np.random.randint(255, size=[K, shape[2]])
    
#     x = np.random.randint(shape[0], size=[K, 1])
#     y = np.random.randint(shape[1], size=[K, 1])
#     center = np.concatenate( (x,y) , axis=1)
    
    if(log):
        print("center :", center)
    costNow, centerNow = cost(data1, center , K, log)
    
    center = centerNow
    costP = costNow
    for echo in range(echos):
        
        costNow, centerNow = cost(data1, center, K, log)
        print("聚类第%d次"% echo)
        
        diff = costP - costNow
        print("diff = ", diff)
        if( diff < minDiff):
            break
        else:
            if(log):
                print("center :", costNow)
                print("costP - costNow :", costP - costNow)
            center = centerNow
            costP = costNow
            


# # 对卡通企鹅 图像进行聚类

# In[10]:


My_Kmeans(image1, 3, log=True, rand=False)


# # 对 企鹅 图像进行聚类

# In[13]:


My_Kmeans(image2, 6, log=False, rand=True)


# # 对沙漠图像进行聚类

# In[14]:


My_Kmeans(image, 3, log=False, rand=True)


# In[15]:


My_Kmeans(image, 5, log=False, rand=True)

