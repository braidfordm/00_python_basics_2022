# ask the user for their name
username =  input("what is your name? ") 

# ask the user for their favourite interger
fav_num = int(input ("favourite number? "))

# double,halve and square the number
double = fav_num * 2
half = fav_num / 2
squared = fav_num * fav_num

# greet the user
print("Hi {}, your favourite number is {}".format(username, fav_num))
print()
# output the results of doubling, halving, 
# and squaring of their favourite number 
print("double {} is {}".format(fav_num, double))
print("half {} is {}".format(fav_num, half))
print("square {} is {}".format(fav_num, squared))