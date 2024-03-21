# 二維清單
products = []
products1 = []
products2 = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
	    break
	price = input('這商品價錢為何: ')
	p = [] # 定義為小清單
	p.append(name) #將上述input 資訊加入再p清單中
	p.append(price)
	products.append(p) #最後再將p加入prodcuts大清單中
	l = [name, price] #也可以透過直接將"已定義" str來加入清單之中
	products2.append([name, price]) #或是透過此方式
	products1.append(l)
print(products[0][0])
print(products[0][1])
print('------------------')
print(products1[0][0])
print(products1[0][1])
print('------------------')
print(products2[0][0])
print(products2[0][1])




