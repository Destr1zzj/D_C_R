#冒泡start##
def maopao(arr):
    for i in range(len(arr)-1): #p1 遍历列表，最差情况需要遍历n-1 次，即最小的在最后一位
        for j in range(len(arr)-1): #p2 遍历列表
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


#插入排序##
def charu(arr):
    for i in range(len(arr)):
        idx = i - 1#idx 用来对比的
        num = arr[i]#用来移动的数字：
        while idx >= 0 and arr[idx] > num: #当还有用来对比的数，并且这个数大于当前排序数字时 进入  【1，3（idx），2（num），3，4，5】
            arr[idx + 1] = arr[idx] #进入后 将当前位置置为 上个用来对比的数【1，3（idx），3（num的位置，idx+1），3，4，5】
            idx -= 1#【1（idx），3，3（num的位置，idx+1），3，4，5】
        arr[idx+1] = num#不满足while条件跳出后赋值【1（idx），2（num的位置idx+1），3，3，4，5】
    return arr


#选择###
def chose(arr):
    for i in range(len(arr)): # 固定 i位置， 从后续列表中找一个最小的，和i换，然后重复这个过程
        idx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[idx]:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
    return arr


###归并### 递归 + merge
def mergeSort(arr):
    if len(arr) < 2:# 即=1
        return arr
    mid = len(arr) >> 1  ##分治的思想，左右分别递归
    left = arr[0:mid] #这里不包含mid
    right = arr[mid:]#这里包含mid
    return merge(mergeSort(left), mergeSort(right))  ###这里是递归 每次调用process 会将传入的arr根据中点 分成left 和right，并且分别再次调用process


def merge(left, right): # 调用双指针排序
    sortlist = []
    p1 = p2 = 0
    while p1 < len(left) and p2 < len(right):

        if left[p1] > right[p2]:
            sortlist.append(right[p2])
            p2 += 1
        else:
            sortlist.append(left[p1])
            p1 += 1
    while p1 == len(left) and p2 < len(right):
        sortlist += right[p2:]  ##python 这里可以直接list 相加
        return sortlist
    while p2 == len(right) and p1 < len(left):
        sortlist += left[p1:]
        return sortlist


######快排###
def quickSort(arr):
    return quickSorthelp(arr, 0, len(arr) - 1)# 这里是为了让用户只需要输入原始数据即可


def quickSorthelp(arr, first, last):  #这里进行递归
    if first < last: #如果列表> 1 进行分割，否则直接返回
        split = partition(arr, first, last)
        quickSorthelp(arr, first, split - 1)
        quickSorthelp(arr, split, last)
    return arr


def three4mid(arr, first, last):
    mid = (first + last) >> 1

    if arr[first] > arr[last]:
        arr[first], arr[last] = arr[last], arr[first]   ###如果首项大于末项，那么首和末交换位置   无论是否交换， 这时列表末项>首项
    if arr[mid] > arr[last]:
        arr[mid], arr[last] = arr[last], arr[mid]   ### 如果中项大于末项，那么交换位置 这时列表 末项>首项，末项>中项
    if arr[first] > arr[mid]:
        arr[mid], arr[first] = arr[first], arr[mid] ###这里保证 中项在最前
    #arr[mid], arr[first + 1] = arr[first + 1], arr[mid]
    #TODO 这里需要mid 和first+1 或last -1

def partition(arr, first, last):
    ####这里进行固定基准值的操作,先取基准值：  三值取中法 ，这里没有用到，这里将三个值按顺序排列了，无意义
    three4mid(arr, first, last)# TODO 这里要加回取中，之后研究
    piv = arr[first + 1]## 这里以最小的首项做为基准值 这里算法有问题。。。
    i = first - 1

    while first < last:###以first为基准， 双指针排序
        if arr[first] < piv:
            i += 1
            arr[first], arr[i] = arr[i], arr[first]
            first += 1
        elif arr[first] == piv:
            first += 1
        else:
            arr[first], arr[last] = arr[last], arr[first]
            last -= 1
    return first


#####堆排序##############
def duiSort(arr):
    res = [0] * len(arr)##这里可以优化掉这个res组
    size = len(arr)
    ###################
    for i, v in enumerate(arr):
        k = i
        res[k] = v
        while res[k] > res[abs((k-1))//2]: #当子节点比父节点大的时候，子节点与父节点交换位置。 这里由于python // 是整数运算，那么左右子节点的父节点，都可以用  (i-1)//2 表示注意，k=0时，需要变成蒸熟
            res[k], res[abs((k-1))//2] = res[abs((k-1))//2], res[k]
            k = abs((k-1))//2  ###往上遍历，父子谁大
        #print(arr[k], res[k], "-------here---------")
    #########################
    # print(res ,"--------------big root-------------- ")
    while size > 0:
        res[0], res[size-1] = res[size-1], res[0]  #将最大值，放到列表最后，并且排序时将最后一位去除
        size -= 1
    ######
        ###左节点  2*i + 1 右节点 2*i+2
        i = 0
        left = i * 2 + 1
        while left < size: #左节点小于size时继续  （左节点比右节点小 如果有左节点<size那么右节点一定=size
            large = left + 1 if left + 1 < size and res[left + 1] > res[left] else left #树中看一下左右节点哪一个更大 idx赋值给large
            large = i if res[large] < res[i] else large # 树中看一下父 和 large 节点哪一个更大 idx赋值给large
            if large == i:
                break
            res[large], res[i] = res[i], res[large] #如果父节点小于子节点， 则idx 和large 位置互换 idx 往下走 替换成子节点的索引 idx
            i = large
            left = i * 2 + 1
    #############

    return res


if __name__ == '__main__':
    key = [1, 2, 4, 5, 7, 4, 3, 2, 7, 2, 3, 5234, 423, 5634, 6, 56, 234, 234, 65, 543, 23, 6, 5, 764, 456, 234, 2, 34,
           6, 345, 67, 3, 453, 7, 663, 0, 0, 0, 0, 4, 32, 24, 6, 1, 9, 2, 0]
    # print(chose(arr))
    # print(maopao(arr))
    # print(charu(arr))
    # print(mergeSort(arr))
    #print(quickSort(key))
    # print(duiSort(arr))
