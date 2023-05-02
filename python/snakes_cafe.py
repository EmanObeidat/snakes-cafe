
menu={
  "Appetizers": ["Wings",'Cookies'," Spring Rolls"],
   "Entrees":["Salmon","Steak","Meat Tornado","A Literal Garden"],
   "Desserts" :["Ice Cream","Cake","Pie"],
   "Drinks" :["Coffee","Tea","Unicorn Tears"]
}
def intro():
    print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

''')

def Menu():
    for value, item in menu.items():
        print(f'\n {value} \n {"----"}')
        print("\n".join(item))




def user_insertion():
    print('''
    ***********************************
    What would you like to order?
    ***********************************
    ''')

def end_application():
    print("thanks for using snakes cafe application !")   
##----------------------------------------------------
orders = {}
# number=number.strip().capitalize()
# for item in menu:
#     if item in orders:
#         orders[item] += 1
#     else:
#         orders[item] = 1

# for item, count in orders.items():
#     print(f"{item}: {count}")
##----------------------------------------------------

def main():
    user_input=""
    while(user_input.lower() !="quit"):
         user_input=input(">")  
         if user_input in menu["Appetizers"] or user_input in menu["Entrees"] or user_input in menu["Desserts"] or user_input in menu["Drinks"] :
            if user_input not in orders:
                orders[user_input]=1
                # print(orders)
                # print(orders[user_input])
                print(orders[user_input],"order of "+ user_input +" has been added to you meal")
            else:
                    orders[user_input]+=1
                    # print(orders)
                    print(orders[user_input],"order of"+user_input+" has been added to you meal")

       

         else:
                print("sorry we dont have this item ! can you choose another one please?")  




if __name__=="__main__": 
    intro()  
    Menu()
    user_insertion()
    main()
    end_application()