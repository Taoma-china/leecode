 * 有一叠扑克牌，每张牌介于1和10之间
 * 有四种出牌方法：
 * 单出一张
 * 出两张相同的牌(对子)
 * 出五张顺子(如12345)
 * 出三连对子(如112233)
 * 给10个数，表示1-10每种牌有几张，问最少要多少次能出完

def double_list(arr,time):


    for i in range(8):
        judge=True
        for j in range(i,i+3):
            if arr[j]<2:
                judge = False
                
        if judge== True:
            time = time +1
            print('a')
            for w in range(i,i+3):
                arr[w]=arr[w]-2
            arr,time = double_list(arr,time)
    return arr, time


def five_list(arr,time):
    
    for i in range(6):
        judge = True
        for j in range(i,i+5):
            if arr[j]<1:
                judge = False
        if judge ==True:
            time= time+1
            for w in range(i,i+5):
                arr[w]=arr[w]-1
            
            arr,time=five_list(arr,time)
    return arr, time

def double(arr,time):
    for i in range(len(arr)):
        if arr[i]>=2:
            time = time+1
            arr[i]=arr[i]-2
            arr,time=double(arr,time)
    return arr,time

def single(arr,time):
    for i in range(len(arr)):
        if arr[i]!=0:
            time=time+1
            arr[i]=arr[i]-1
            arr,time=single(arr,time)
    return arr,time



arr_ = [4,4,1,4,4,1,4,4,1,4]
arr = list(arr_)
time = 0 
arr, time = double_list(arr,time)
arr, time = five_list(arr,time)
arr, time = double(arr,time)
arr, time = single(arr,time)
print(time)
