def find_last_person(n):
    # Initialize the list of players from 1 to n
    players = list(range(1, n + 1))
    eliminated_order = []  # List to store the order of elimination

    # Continue eliminating until only one person is left
    while len(players) > 1:
        temp_list = []
        for i in range(len(players)):
            if i % 2 == 0:
                temp_list.append(players[i])
            else:
                eliminated_order.append(players[i])  # Store the eliminated player
                print(f"Eliminated: {players[i]}")  # Print the eliminated player

        if len(players) % 2 != 0:
            temp_list = [players[-1]] + temp_list

        players = temp_list

    last_person = players[0]
    return last_person, eliminated_order

# Read the number of players from input
n = int(input("Enter the number of players: "))

# Find the last remaining player and the order of elimination
last_person, eliminated_order = find_last_person(n)

print("\nThe last remaining player is:", last_person)
print("Order of elimination:", eliminated_order)
