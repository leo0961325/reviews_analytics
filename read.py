#1.求總共筆數
#2.第幾筆
#3.找進度，每1000回報一次
#4.平均每一筆留言字數
#5.篩選出小於每留言字數<100的筆數
#6.篩選出內含有valuable單字的留言

data = []
count = 0
with open("reviews.txt" , "r") as f :
    for line in f :
        data.append(line) #每一行line 加入至data裡面，轉換成清單
        count += 1
        if count % 1000 == 0 :
            print(len(data)) #找進度，每1000回報一次
print(len(data)) #求總共筆數
print(data[0]) #第幾筆

#-------------------------------------------------------------------------------------+

sum_len = 0
for d in data :
    sum_len += len(d) #len(d) 是字數
print("平均是" , sum_len / len(data) , "每一筆") #平均每一筆留言字數

#-------------------------------------------------------------------------------------+
new = []

for d in data :
    if len(d) < 100 :
        new.append(d)
print("共有" , len(new) , "小於100字數的留言")  #每一個小於100的留言


#-------------------------------------------------------------------------------------+

valuable = []

for d in data :
    if "valuable" in d :
        valuable.append(d)
print("一共有 ", len(valuable) ,"個留言提到valuable")
print(valuable[1]) #找出其中一個提到valuable的留言