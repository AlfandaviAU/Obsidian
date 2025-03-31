# input_string = str(input("Please enter a list of numbers: "))
# # Please enter your code here for converting the input string into a list.

# arr = list(map(float, input_string[1:len(input_string)-1].split(",")))
# # Please enter your code here for finding the index of the number with the smallest value in the input list.

# minima = arr[0]
# minindex = 0
# for i in range(len(arr)):
#   if arr[i] < minima:
#     minindex = i
#     minima = arr[i]

# # Please enter your code here for displaying the index of the number with the smallest value in the input string.

# print(f"The min index is: {minindex}")




# # "The min index is: out"




# # Intent: The code should divide all elements by two (with integer division)
# # and display the resulting list
# my_list = [3, 7, 4, 9, 12, 2]

# for i in range(len(my_list)):
#   my_list[i]  = my_list[i] // 2
# print(my_list)


# # Intent: The code should replace all 'a' characters with 'e'
# # and display the resulting message
# my_string = 'hare paws wall tuba draw'
# new_string = ''
# for i in range(len(my_string)):
#     if my_string[i] == 'a':
#       new_string += 'e'
#     else:
#       new_string += my_string[i]
# print(new_string)     


# input_string = str(input("Please enter a binary string: "))
# count = 0

# arr = input_string.split("1")
# # Please enter your code here for counting the number of 1s in the input string.
# print(f"Number of 1s in the input string is: {len(arr)-1}")
# # Please enter your code here for displaying the number of 1s in the input string.


# input_string = str(input("Please enter a list of numbers: "))
# arr = list(map(float, input_string[1:len(input_string)-1].split(",")))

# minima = min(arr)
# maxima = max(arr)

# print(f"The maximum absolute difference is: {maxima - minima}")
# Please enter your code here for converting the input string into a list.
# Please enter your code here for finding the maximum absolute difference among all pairs of numbers from the input list.
# Please enter your code here for displaying the maximum absolute difference.


# def distance_calc(x1,x2,y1,y2):
#   return (((x1-x2)**2 + (y1-y2)**2))**(0.5)

# # Please enter your code for importing math functions to be used
# x = [10.1,0.4,6.9,4.2,14.1,15.9]
# y = [17.7,3.1,9.0,2.7,41.5,33.3]
# cities = ['Elabro','Nutunyu','Barimba','Duduth','Tromsu','Pranho']
# # Please enter your code here for finding the pair of cities with the shortest distance.
# # Please enter your code here for displaying the pair of cities with the shortest distance.


# min_dist = distance_calc(x[0],y[0],x[1],y[1])
# index_i = 0
# index_j = 1

# for i in range (len(x)):
#   for j in range (i, len(x)):
#     if (i != j):
#       diff = distance_calc(x[i],y[i], x[j], y[j])
#       if (diff < min_dist):
#         print(cities[i], cities[j], diff)
#         index_i = i
#         index_j = j

# print(f"The two cities that are closest to each other are: {cities[index_i]} and {cities[index_j]}")
# arr = [1,2,3,4,5,6,7,8]
# index = 0


# for num in arr:
#   num = num // 2
#   arr[index] = num
#   index += 1


# print(arr)


# Intent: The code should replace all 'a' characters with 'e'
# and display the resulting message
# my_string = 'hare paws wall tuba draw'
# new_string = ''
# for i in range(len(my_string)):
#     if my_string[i] == 'a':
#       new_string += 'e'
#     else:
#       new_string += my_string[i]
# print(new_string)




# fav_phrase  = "6 Months Break Twice A Year"

# for i in range(len(fav_phrase)):
#   print(fav_phrase[i])

# print("=======")

# # for i in range (len(fav_phrase)):
# #   print(fav_phrase[len(fav_phrase)-i-1])

# for i in range(len(fav_phrase)-1, -1, -1):
#   print(fav_phrase[i])


# trump_quote = "I started off in Brooklyn and my father gave me a small loan of a million dollars"

# index_trump = trump_quote.find("million")

# print(index_trump)

# print(trump_quote[index_trump: index_trump+len("million")])

# print(trump_quote.count("a"))

# print(trump_quote.split(" ")[-1])

# trump_words = trump_quote.split(" ")

# print(trump_words)

# president_trump = trump_words[6]+trump_words[7]+trump_words[8]+trump_words[9]+trump_words[4]

# print(president_trump)

# print("@".join(trump_words))



# def my_func(x):
#   return x*x

# x = float(input("Input number to square: "))
# print(my_func(x))


def go_to_lobby(gold_coins: int) -> None:
    """ The start of the adventure """
    print_gold_amount(gold_coins)
    print("You are in the lobby of the dungeon. What do you do?")
    print("1. Examine the lobby.")
    print("2. Go to the throne hall.")
    print("3. Leave.")
    option = int(input())
    
    if (option == 1):
      examine_lobby(gold_coins)
    elif (option == 2):
      go_to_throne_hall(gold_coins)
    else:
      leave(gold_coins)

def examine_lobby(gold_coins: int) -> None:
    """ The user examines the lobby """
    print_gold_amount(gold_coins)
    rob_amount = 10
    print("A band of goblins rob " + str(rob_amount) + " gold from you.")
    gold_coins -= rob_amount

def leave(gold_coins: int) -> None:
    """ The end of the adventure """
    print_gold_amount(gold_coins)

    while (gold_coins < 0):
      print("You cant leave dungeon")
      print("1. Wash the dishes")
      print("2. Go back to the lobby")
      option = int(input(""))

      if (option == 1):
        gold_coins += 1
      else:
        if (gold_coins < 1):  
          gold_coins -= 10
        go_to_lobby(gold_coins)
        break

    print("You leave the dungeon.")

def go_to_throne_hall(gold_coins: int) -> None:
    """ The middle of the adventure """
    print_gold_amount(gold_coins)
    print("You are in the throne hall. What do you do?")
    print("1. Examine the throne hall.")
    print("2. Go back to the lobby.")
    option = int(input())
    
    if (option == 1):
      examine_throne_hall(gold_coins)
    else:
      go_to_lobby(gold_coins)  
    
def examine_throne_hall(gold_coins: int) -> None:
    """ The user examines the throne hall """
    print_gold_amount(gold_coins)
    rob_amount = 40
    print("You disturb the dungeon keeper who makes you pay " + str(rob_amount) + " gold.")
    gold_coins -= rob_amount

def print_gold_amount(gold_coins: int) -> None:
    """ Prints to the user their current amount of gold """
    print("You have " + str(gold_coins) + " gold.")

go_to_lobby(50)