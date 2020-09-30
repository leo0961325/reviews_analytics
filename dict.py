#1.印出超過10000次的字
#2.查字典共有幾次
#3.所選單字出現幾次(簡易)
#4.字典查閱功能
import progressbar

data = [] 
count = 0
bar = progressbar.ProgressBar(max_value = 1000000) #最多1000000筆

with open('reviews.txt' , 'r') as f :
    for line in f :
        data.append(line)
        count += 1
        bar.update(count)
print('共有' , len(data))



wc = {} #word_count
for d in data :
    words = d.split() #預設為去掉空白 
    for word in words :
        if word in wc :
            wc[word] +=1
        else :
            wc[word] = 1

for word in wc :
    if wc[word] > 10000 :   #出現超過10000次的    
        print(word , wc[word]) #對應上面wc[word]

#print(len(wc)) 字典共有幾個字
#print(wc['leo']) 查找出現過幾次

while True : #要查的單字
    word = input('輸入要查的單字 : ')
    if word == 'q' :
        print('結束')
        break
    if word in wc :
        print(word ,'出現次數為 : ', wc[word])
    else :
        pass
