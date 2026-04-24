
class TreasureProject:
    print("      _               _   ")
    print("     | |             | |  ")
    print("  ___| |__   ___  ___| |_ ")
    print(" / __| '_ \ / _ \/ __| __|")
    print("| (__| | | |  __/\__ \ |_ ")
    print(" \___|_| |_|\___||___/\__|")

    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure")
    print("You're at a cross road. Where do you want to go?")
    print("Type 'left' or 'right'")
    x = str(input())

    if x == 'right':
        print("You've fallen into a hole. Game Over!")
       
    if x == 'left':
        print('swim or wait? ')
    y = str(input())

    if y == 'swim':
        print("Attacked by trout. Game Over!")
    if y == 'wait':
        print('Which door ? ')

    z = str(input())

    if z == 'Red':
        print("Burned by fire.")


    if z == 'Blue':
        print('Eaten by beasts.')
        

    if z == 'Yellow':
        print('You Win')



    if z not in ['Red','Blue','Yellow']:
        print('Game Over.')
        
        
    



c = TreasureProject()
print(c)


