# number = int(input())
# number = 6

# if number == 1:
#     print('one')
# elif number == 2:
#     print('two')
# elif number == 3:
#     print('three')
# elif number == 4:
#     print('four')
# elif number == 5:
#     print('five')
# else:
#     print(str(number) + ' is not a number from 1 - 5.')

###############################################################################

# myArray = ['Mary', 'had', 'a', 'little', 'lamb']
# print('Length of myArray ' + str(len(myArray)))

# for item in xrange(len(myArray)):
#     print(myArray[item])

###############################################################################

# product = 'Nike Shoes'
# price = '49.99'
# myObj = {'product': 'Asus PG249Q', 'price': '$599.99'}

# sentence = 'The product {0} costs {1} dollars.'.format(
#     product, price)
# sentence = 'The product {1} costs {0} dollars.'.format(
#     product, price)
# sentence = 'The product {product} costs {price} dollars.'.format(
#     product=myObj['product'], price=myObj['price'])
# sentence = 'The product {product} costs {price} dollars.'.format(
#     product=product, price=price)
# sentence = f'The product {product} costs {price} dollars.'
# sentence = 'The product {product} costs {price}'.format(**myObj)

# print(sentence)

###############################################################################
# Python code to demonstrate range() vs xrange() on basis of return type
# a = range(1, 10000)
# x = xrange(1, 10000)

# print('The return type of range() is : ')
# print(type(a))

# print('The return type of xrange() is : ')
# print(type(x))

####

# squares = [x**2 for x in range(10)]
# print(squares)

###############################################################################

# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k, v)

###############################################################################

# def saySomething():
#     print('Hello')


# saySomething()

###############################################################################

# a, b = 0, 1
# print(b)

###############################################################################

# def fib2(n):  # return Fibonacci series up to n
#     """Return a list containing the Fibonacci series up to n."""
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)    # see below
#         a, b = b, a+b
#     return result


# f100 = fib2(100)    # call it
# f100                # write the result
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

###############################################################################

# Test whether a copied dictionary's keys can be assigned new values without
# affecting original copy

# dictionary = {'name': 'George', 'age': '15'}

# dictionaryCopy = dictionary
# dictionaryCopy['age'] = '21'

# print(dictionary['age'])  # 21
# print(dictionaryCopy['age'])  # 21

###############################################################################


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")

    for arg in arguments:
        print(arg)

    print("-" * 40)

    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("money",
           "The MacBook Pro is still here.",
           "iPhones are smartphones.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# 4/28/2020 ###################################################################
# Write a function that adds two numbers

# def sum(a, b):
    # a = int(a)
    # b = int(b)

    # if isinstance(a, int) is False or isinstance(b, int) is False:
    #     return "'a' or 'b' is not an integer."

    # print("I should not see this if 'a' or 'b' is not an integer.")
    # return a+b


# print(sum("1", 2))  # Triggers conditional
# print(sum("one", 2))  # Error
# print(sum(1, 2))  # 3

###############################################################################
