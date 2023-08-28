#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount
        self.prices=[]

    def add_item(self, item, price, quantity=1):
        self.items.extend([item] * quantity)
        self.total += price * quantity
        self.prices.append(price)
    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * self.discount / 100
            rounded_discount = round(discount_amount)
            self.total -= rounded_discount
            print(f"After the discount, the total comes to ${self.total}.")
        else:    
           print( "There is no discount to apply.")

    def get_all_items(self):
        return self.items

    def void_last_transaction(self):
        if self.prices:
            last_item_price = self.prices.pop()
            self.total -= last_item_price 
        else:
            self.prices = []
            self.total -= 0.0
            

          
        
     