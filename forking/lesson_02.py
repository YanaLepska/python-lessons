# 1
# n = int(input('Enter a number: '))
# a,b,c,d,e,f,g = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# if n == 1:
#     print(a)
# elif n == 2:
#     print(b)
# elif n == 3:
#     print(c)
# elif n == 4:
#     print(d)
# elif n == 5:
#     print(e)
# elif n == 6:
#     print(f)
# elif n == 7:
#     print(g)
# else:
#     print("Invalid number")

# 2
# date = int(input('Enter a date: '))
# month = int(input('Enter a month: '))
# year = int(input('Enter a year: '))
# if date*month == year:
#     print('The date is magic')
# else:
#     print('The date is not magic')

# 3
# user_color1 = input('Enter red, green, or blue values: ')
# user_color2 = input('Enter red, green, or blue values: ')
# if user_color1 == 'red' and user_color2 == 'red':
#     print('The resulting color is red')
# elif user_color1 == 'red' and user_color2 == 'green' or user_color1 == 'green' and user_color2 == 'red':
#     print('The resulting color is yellow')
# elif user_color1 == 'red' and user_color2 == 'blue' or user_color1 == 'blue' and user_color2 == 'red':
#     print('The resulting color is magenta')
# elif user_color1 == 'green' and user_color2 == 'green':
#     print('The resulting color is green')
# elif user_color1 == 'green' and user_color2 == 'blue' or user_color1 == 'blue' and user_color2 == 'green':
#     print('The resulting color is cyan')
# elif user_color1 == 'blue' and user_color2 == 'blue':
#     print('The resulting color is blue')
# else:
#     print('Invalid color')

# 4
# amount = int(input('Enter the amount of books: '))
# a = 0
# if amount <=2:
#    a = 0
# if amount > 2 and amount <= 4:
#    a = 5
# if amount > 4 and amount <= 6:
#    a = 15
# if amount > 6 and amount <= 8:
#     a = 30
# if amount > 8:
#     a = 60
# print(f"The discount is {a}%")

# 5
# amount = int(input('Enter the amount of products: '))
# a = 2700
# discount = 0
# total = 0
# if amount <= 9:
#     total = a * amount
# elif amount >= 10 and amount <= 19:
#     discount = 0.1
#     total = a * amount * (1 - discount)
# elif amount >= 20 and amount <= 49:
#     discount = 0.2
#     total = a * amount * (1 - discount)
# elif amount >= 50 and amount <= 99:
#     discount = 0.3
#     total = a * amount * (1 - discount)
# elif amount >= 100:
#     discount = 0.4
#     total = a * amount * (1 - discount)
# print(f"The total price is {total} with a discount of {discount*100}%")

# 6
# first_group = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
# second_group = ['April', 'June', 'September', 'November']
# third_group = ['February']
# month = input('Enter a month: ')
# if month in first_group:
#     print(f"{month} has 31 days")
# elif month in second_group:
#     print(f"{month} has 30 days")
# elif month in third_group:
#     print(f"{month} has 28 or 29 days")
# else:    print("Invalid month")

# 7
# n = int(input('Enter a number: '))
# season_1 = ['December', 'January', 'February']
# season_2 = ['March', 'April', 'May']
# season_3 = ['June', 'July', 'August']
# season_4 = ['September', 'October', 'November']
# if n == 1:
#     print(season_1)
# elif n == 2:
#     print(season_2)
# elif n == 3:
#     print(season_3)
# elif n == 4:
#     print(season_4)
# else:
#     print("Invalid number")

# 8
# a = 1000
# b = 500
# c = 5700
# s = 3200
# percent = 0
# if s<a:
#     percent = 0.0
# elif s>=a and s<b:
#     percent = 0.1
# elif s>=b and s<=c:
#     percent = 0.25
# elif s>c:
#     percent = 0.5
# total = s * (1 - percent)
# print(f"The total price is {total} with a discount of {percent*100}%")

# 9
# mark = int(input('Enter a mark: '))
# grades = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
# if mark in grades[0]:
#     print('The grade is initial level')
# elif mark in grades[1]:
#     print('The grade is average level')
# elif mark in grades[2]:
#     print('The grade is sufficient level')
# elif mark in grades[3]:
#     print('The grade is high level')

# 10
# n = input('Enter a number: ')
# if n == '1':
#     print('Windows')
# elif n == '2':
#     print('Linux')
# elif n == '3':
#     print('macOS')
# elif n == "":
#     print('It is not an operating system')
# elif n > '3':
#     print('Invalid number')



# python forking/lesson_02.py