#Create a list for menu, dictonary for stock and price by combining lists
'''menu = ["Americano", "Latte", "Expresso", "Cookie"]
stock_list = [10,20,40,100]
price_list = [8,12,5,5]

stock_dict = dict(zip(menu, stock_list))
price_dict = dict(zip(menu, price_list))
print(stock_dict)
print(price_dict)

#compare the keys in each dictionary, if the keys are the same, multiply the price and stock to calculate the total stock value
total_stock = 0
for i,j in stock_dict.items():
    for a,b in price_dict.items():
        if i == a:
            total_stock += b*j
        else:
            continue

print(total_stock)

#Verify the answer of total_stock
print(8*10+20*12+40*5+100*5)'''


total_stock = 0

sample_data = {
    "menu" : ["Americano", "Latte", "Expresso", "Cookie"],
    "stock": [10,20,40,100],
    "price": [8,12,5,5]
}

print(sample_data["price"][:1])

for i in range(len(sample_data["stock"])):
    for a in range(len(sample_data["price"])):
        if i == a:
            total_stock += sample_data["stock"][i] * sample_data["price"][a]
        else:
            continue

print(total_stock)