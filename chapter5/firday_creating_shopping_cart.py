from IPython.display import clear_output
cart = []
def addItem(item):
    clear_output()
    cart.append(item)
    print(f'{item} has been added')
def removeItem(item):
    clear_output()
    try:
        cart.remove(item)
        print(f'{item} has been removed')
    except:
        print('sorry we could not remove that item')
def showCart():
    clear_output()
    if cart:
        print('here is your cart: ')
        for item in cart:
            print(f'- {item}')
    else:
        print('your cart is empty')
def clearCart():
    clear_output()
    cart.clear()
    print('your cart is empty.')
def main():
    done = False
    while not done:
        ans = input('quit/add/remove/show/clear: ').lower()
        if ans == 'quit':
            print('Thanks for using our program.')
            showCart()
            done = True
        elif ans == 'add':
            item = input('what would you like to add? ').title()
            addItem(item)
        elif ans == 'remove':
            item = input('what would you like to rem ove? ').title()
            removeItem(item)
        elif ans == 'show':
            showCart()
        elif ans == 'clear':
            clearCart()
        else:
            print('sorry that was not an option.')
main()


