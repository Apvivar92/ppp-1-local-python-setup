# A function named hello() that prints a greeting to user
def hello():
  print("Hello user")

# A function named pack() that takes 3 arguemnets and returns a single list 
def pack(arg1, arg2, arg3):
  return [arg1, arg2, arg3]

# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" 
# (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". 
# The function should not return anything.
def eat_lunch(food_list):
  if len(food_list) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(food_list)):
      if i == 0:
        print(f"First I eat {food_list[0]}")
      else:
        print(f"Next I eat {food_list[i]}")

# def eat_lunch(food_list):
#   x = 0
#   for i in food_list:
#       if (x == 0):
#           print("First I eat", i)
#       else:
#           print("Next I eat", i)
#       x+=1

hello()
print(pack('arg1',"arg2","arg3"))
eat_lunch([])
eat_lunch(["pizza", "Chicken","Sushi", "Salad"])