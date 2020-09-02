
data = []
count = 0
with open("reviews.txt" , "r") as f :
    for line in f :
        data.append(line) #每一行line 加入至data裡面
        count += 1
        if count % 1000 == 0 :
            print(len(data)) #找進度，每1000回報一次
print(len(data)) #求總共筆數
print(data[0]) #第幾筆

sum_len = 0
for d in data :
    sum_len += len(d)
print("平均是" , sum_len / len(data) , "每一筆") #平均每一筆留言字數