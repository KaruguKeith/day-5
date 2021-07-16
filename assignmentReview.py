def calculateInclusive(products ,tax):
    for product in products:
        incl = product['excl'] + (product['excl']) * tax
        print(product['name'] , product['description'], incl)

products = [{ 
            "name" : "milk",
            "description" : "cow milk",
            "excl" : 35.50
           }]

calculateInclusive(products, 0.16)








