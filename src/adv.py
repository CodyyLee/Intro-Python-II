from room import Room
from player import player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['Sword', 'Torch']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['Gold Coin']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
Player = player(room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while Player.room.name != "Treasure Chamber":
    print(f'{Player.room.name}. {Player.room.description}')
    direction = input('Where would you like to go? (n, e, s, w)')
    split = direction.split()

    if direction.lower() == 'n' and Player.room.n_to != None:
        Player.move(Player.room.n_to)
        if len(Player.room.items) != 0:
            print(f'The following items are available in this room: {Player.room.items}')
    elif direction.lower() == 's' and Player.room.s_to != None:
        Player.move(Player.room.s_to)
        if len(Player.room.items) != 0:
            print(f'The following items are available in this room: {Player.room.items}')
    elif direction.lower() == 'e' and Player.room.e_to != None:
        Player.move(Player.room.e_to)
        if len(Player.room.items) != 0:
            print(f'The following items are available in this room: {Player.room.items}')
    elif direction.lower() == 'w' and Player.room.w_to != None:
        Player.move(Player.room.w_to)
        if len(Player.room.items) != 0:
            print(f'The following items are available in this room: {Player.room.items}')
    elif direction.lower() == 'q':
        print('Thanks for playing!')
        break
    elif split[0].lower() == 'get':
        for i in Player.room.items:
            if split[1] == i:
                Player.get(i)
                Player.room.items.remove(i)
                print(f'You have picked up: {split[1]}')
                print(f'Current items in your inventory: {Player.items}')
            else:
                print(f'There is no item called {split[1]} in this room.')
    elif split[0].lower() == 'drop':
        for i in Player.items:
            if split[1] == i:
                Player.drop(i)
                Player.room.collect(i)
                print(f'You have dropped: {split[1]}')
                print(f'Current items in your inventory: {Player.items}')
            else:
                print(f'There is no item called {split[1]} in your inventory.')
    else:
        print('Please enter valid input.')
        
