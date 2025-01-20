print(9)                        # 此函數能列印資料至終端機上
print('hello world!')           # 引號內的空格也會印出來
print( "1024" )                 # 引號外的空格會被忽略

print(1,2,3)                    # 欲一次列印多個資料，需加上逗號
print('a', 'i', 'u', 'e', 'o')  # 使用逗號隔開的資料，列印時彼此間將出現空格

print(9,9,sep=' ')              # 此函數內加上sep(其值只能是字串)，可設定資料間的連結文字，預設為空格(故此行與 print(9,9) 一樣)
print('>', '>', sep='>')        # 列印時會將連結文字顯示出來
print(7,7,7,sep='')             # 如果給空字串，則資料之間不會出現空格(故此行相當於 print('7' + '7' + '7') )

print('neko', end='\n')         # 此函數內加上end(其值只能是字串)，可設定下次輸出與此次輸出要如何隔開，預設為\n(故此行與 print('neko') 一樣)
print('https', end='://')       # 此次輸出與下次輸出將以://隔開
print('www.tut.edu.tw')         # 此次輸出會與上次輸出印在同一行
print(42,end='')                # 如果給空字串，則下次輸出將與此次輸出印在同一行
print(0)                        # 此次輸出會相連在上次輸出後方

# -----以下為本程式的輸出結果-----

"""
9
hello world!
1024
1 2 3
a i u e o
9 9
>>>
777
neko
https://www.tut.edu.tw
420
"""