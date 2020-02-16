#__author:"longjin"
#date:  2019/6/1

def coupon(price):
    if price < 50:
        discount = 1
        finalprice = price*discount
    elif 50 <= price <= 100:
        discount = 0.9
        finalprice = price*discount
    elif price > 100:
        discount = 0.8
        finalprice = price*discount

    return discount, finalprice

price = float(input('please input the price: '))
print("the discount is %.2f and the finalprice is %.2f" %(coupon(price)))