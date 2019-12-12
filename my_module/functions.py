"""A collection of functions for my project.
   Each and every function is original, I wrote them line by line.
"""

# name and price for burgers, fries, and shakes
list_burger = {'double-double': 3.65, 'cheeseburger': 2.55, 'hamburger': 2.25, 'no burger': 0}
list_fries = {'fries': 1.75, 'no fries': 0}
list_shake = {'shake': 2.25, 'no shake': 0}

def start_order(input_string):
    """Start the ordering process. Order burger.
    Parameters
    ----------
    input_string: string
        String that contains user's 1st input.
        
    Returns
    ----------
            boolean
        Boolean whether input is as expected or not.
    """
    # indicate that the user wants to order
    if 'order' in input_string:
        print("Let's start ordering! \nWhich burger do you want today?")      
        return True
    
    # user not indicating to order
    else:
        return False

    
def burger_selection(burger):
    """Store and tell the user the price for the selected burger. Ask if they want to order fries.
    Parameters
    ----------
    burger: string
        String that indicates which burger is ordered.
        
    Returns
    --------
    list_burger[burger]: dictionary value
        Dictionary value that stores the price for the selected burger.
    """
    # tell the user the price, and to order fries
    print('Gotcha! The price for ' + burger + ' is $' + str(list_burger[burger]) + '. \nWould you want any fries today?')
    
    # store the price for selected burger
    return list_burger[burger]


def fries_selection(fries):
    """Store and tell the user the price for fries. Ask if they want to order shake.
    Parameters
    ----------
    fries: string
        String that indicates if fries is ordered,
        
    Returns
    ----------
    list_fries[fries]: dictionary value
        Dictionary value that stores the price for the fries.
    """
    # tell the user the price, and to order shakes
    print('Got it! The price for the fries is $' + str(list_fries[fries]) + '. \nWould you like any shakes today? \nWe have strawberry. vanilla, and chocolate shakes!')
    
    # store the price for fries
    return list_fries[fries]


def shake_selection(shake):
    """Store and tell the user the price for shake. Ask if they want to know the total.
    Parameters
    ----------
    shake: string
        String that indicates if shake is ordered.
        
    Returns
    ----------
    list_shake[shake]: dictionary value
        Dictionary value that stores the price for the shake.
    """
    # tell the user the price, and whether tell the total
    print('The price is $' + str(list_shake[shake]) + ". \nWe are done ordering~ \nSimply reply 'yes' or ask me the total price, I will tell you!")
    
    # store the price for shake
    return list_shake[shake]


def total_cost(input_total, burger, fries, shake):
    """Calculate and tell the total price for the order. Ask if the user want discount.
    Parameters
    ----------
    input_total: string
        String that contains the user's 5th input.
    burger: string
        String that indicates which burger is ordered.
    fries: string
        String that indicates if fries is ordered.
    shake: string
        String that indicates if shake is ordered.
        
    Returns
    ----------
    total_price: float
        Float that stores the total price for the order.
    """
    # calculate and tell the total, and ask if discount is needed
    if 'yes' in input_total or 'total' in input_total:
        total_price = list_burger[burger] + list_fries[fries] + list_shake[shake]
        print('Your total is gonna be $' + str(total_price) + '. \nWe have a special 10% discount today only. \nWould you like to unlock the discount?')
    
    # the user indicate no need to tell total
    # end ordering process
    else:
        total_price = None
        print('Please go see the cute counter guy. \nHe will tell you the price and give you the food~')
     
    # store the total price
    return total_price


def discount_cost(input_discount, burger, fries, shake):
    """Calculate and tell the total discounted price.
    Parameters
    ----------
    input_discount: string
        String that contains the user's 6th input.
    burger: string
        String that indicates which burger is ordered.
    fries: string
        String that indicates if fries is ordered.
    shake: string
        String that indicates if shake is ordered.
        
    Returns
    ----------
    total_discounred: float
        Float that stores the total discounted price for the order.
    """
    # calculate and tell the discounted price
    if 'yes' in input_discount:
        total_discounted = 0.9 * (list_burger[burger] + list_fries[fries] + list_shake[shake])
        print('The new total is ' + str(total_discounted) + ". \nPlease pay and pick up your order at the counter! \nLet's hope Lidan can get an A for COGS 18 final project~")
    
    # discount not needed, keep the original price
    else:
        total_discounted = list_burger[burger] + list_fries[fries] + list_shake[shake]
        print('Ok.. Then no discount today :/ \nHope you can wish Lidan to get an A for her COGS 18 final project. \nAnd please go to the counter to pay and pick up your food~')
    
    # store the discounted price
    return total_discounted


def lets_order(): 
    """Main function to run the ordering machine."""
    
    chat = True
    
    while chat:
        
        # get the first message from the user
        input_string = input('INPUT :\t')
        input_string = input_string.lower()
        
        # the user not indicating to order
        # end chat
        if 'order' not in input_string:
            print("Sorry, I don't understand what you're saying. \nI can only help you to order! Bye~")
            chat = False
        
        # start the ordering process
        else:
            start_order(input_string)
            
            # get the second message from the user
            input_burger = input('INPUT :\t')
            input_burger = input_burger.lower()
            
            # check which burger is ordered
            if 'double-double' in input_burger:
                burger = 'double-double'
                burger_selection(burger)
            elif 'cheeseburger' in input_burger:
                burger = 'cheeseburger'
                burger_selection(burger)   
            elif 'hamburger' in input_burger:
                burger = 'hamburger'
                burger_selection(burger)    
            else:
                burger = 'no burger'
                print('Ok... Any fries?')
             
            # get the third message from the user
            input_fries = input('INPUT :\t')
            input_fries = input_fries.lower()
            
            # check if fries is ordered
            if 'yes' in input_fries:
                fries = 'fries'
                fries_selection(fries)    
            else:
                fries = 'no fries'
                print('So no fries today! \nHow about strawberry shake? Chocolate shake? Vanilla shake?')
            
            # get the fourth message from the user
            input_shake = input('INPUT :\t')
            input_shake = input_shake.lower()
            
            # check if shake is ordered
            if 'strawberry' in input_shake or 'chocolate' in input_shake or 'vanilla' in input_shake:
                shake = 'shake'
                shake_selection(shake)    
            else:
                shake = 'no shake'
                print("No shakes~ \nOk, simply reply 'yes' to get your total price, I will tell you!")
            
            # get the fifth message from the user
            input_total = input('INPUT :\t')
            input_total = input_total.lower()
            
            # check if the user want to know the total price
            total_cost(input_total, burger, fries, shake)
            if 'yes' not in input_total:
                return None
            
            # get the sixth message from the user
            input_discount = input('INPUT :\t')
            input_discount = input_discount.lower()
            
            # check if the user applies discount
            discount_cost(input_discount, burger, fries, shake)
            
            # end ordering process
            chat = False