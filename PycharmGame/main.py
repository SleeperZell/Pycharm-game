# dictionary of stats for the different roles
role_stats = {
    'warrior': {
        'attack': 6,
        'hp': 8,
        'speed': 3
    },
    'rogue': {
        'attack': 1,
        'hp': 3,
        'speed': 7
    },
    'mage': {
        'attack': 7,
        'hp': 5,
        'speed': 5
    }
}

creature_stats = {
    'wolf': {
        'attack': 3,
        'hp': 2,
        'speed': 4
    }
}

# This function shows how combat will work
def combat(role, creature):
    # new code below
    current_hp = role_stats[role]['hp']
    current_hp -= role_stats[role]['hp'] - creature_stats[creature]['attack']
    if current_hp <= 0:
        print("You failed")
    elif role_stats[role]['attack'] > creature_stats[creature]["hp"]:
        print("You killed the creature!")
    else:
        print("You were too weak, and had to run away.")


def game():
    # asking the user for their name
    name = input("Hello Adventurer, what is your name?")

    # Asking the user what role they would like to select from the current ones
    print("Ok, %s, what role would you like to choose from?" % name)

    # when confirm doesn't equal yes:
    confirm = "no"
    while confirm != "yes":
        role = input("You can pick from: Rouge, Warrior and Mage, which one would you like to choose?")

        # This will ensure that we don't need to check if the user input is case-sensitive since everything
        # should be lowercase
        role = role.lower()
        # if the role doesn't equal one of the 3 specific roles, repeat until it does
        while role != "warrior" and role != "mage" and role != "rogue":
            role = input("Please try again")
        confirm = input("So, %s, you pick %s?" % (name, role))
        confirm = confirm.lower()
        if confirm != "yes":
            print("Please try again")

    print("You are %s, the %s! These are your stats:" % (name, role))
    print(role_stats[role])

    location = input("Where would you like to travel to? The forest, the village, or the cave?")
    location = location.lower()
    if location == "forest":
        print("You are travelling through the forest, when you are suddenly attacked by a wolf!")
        creature = "wolf"
        combat(role, creature)


game()
