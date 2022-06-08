#item1 = 'Phone'
#item1_price = 100
#item1_quantity = 5
#item1_price_total = item1_price * item1_quantity

class Item:
    pass

#Creating instance of a class
item1 = Item()
#^ That is equal to random_str = str("4") because random_str is an instance of the object "4" which is part of the class "string"
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
#These attributes are now related because they are tied to the same instance of the class Item

#random_str = "aaa"
#print(random_str.upper()) -> In this example, .upper() is a method when which called, will output the random_str obj all upper case.



