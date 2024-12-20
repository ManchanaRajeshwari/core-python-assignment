def select_item(cart):
    if not cart:
        return "empty"
    cost=sum(cart.values())
    if len(cart)>5:
        cost*=(1-0.1)
    return cost
cart = eval(input("Enter {key,value} items"))
print(f"The cost of the cart items :{select_item(cart)}")
