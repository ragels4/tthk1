import random

# Welcome message
print("========================================")
print("             YO GURT WASSUP             ")
print("========================================")

# Player character selection
print("1 - SPARTAN\nLegendary rebel leader, master of sword and shield\nHealth - 100\nStamina - 60\n")
print("2 - KRIKSU\nA fierce Gaul who crusades his enemies with a two-handed sword\nHealth - 120\nStamina - 40\n")
print("3 - FLAMMA\nFast as the wind, deadly trident and net\nHealth - 90\nStamina - 70\n")
print("4 - COMMODUS\nRoman emperor who thirsts for blood in the arena\nHealth - 110\nStamina - 50\n")

usrchar = input("Choose 1-4: ")

# Set player stats based on choice
if usrchar == "1":
    pmaxhealth, phealth = 100, 100
    pmaxstamina, pstamina = 60, 60
elif usrchar == "2":
    pmaxhealth, phealth = 120, 120
    pmaxstamina, pstamina = 40, 40
elif usrchar == "3":
    pmaxhealth, phealth = 90, 90
    pmaxstamina, pstamina = 70, 70
else:
    pmaxhealth, phealth = 110, 110
    pmaxstamina, pstamina = 50, 50

# Opponent selection
print("\nNow, choose your opponent:")
print("1 - SPARTAN\nLegendary rebel leader, master of sword and shield\nHealth - 100\nStamina - 60")
print("2 - FLAMMA\nFast as the wind, deadly trident and net\nHealth - 90\nStamina - 70")
print("3 - COMMODUS\nRoman emperor who thirsts for blood in the arena\nHealth - 110\nStamina - 50")

enmchar = input("Choose 1-3: ")

# Set enemy stats based on choice
if enmchar == "1":
    emaxhealth, ehealth = 100, 100
    emaxstamina, estamina = 60, 60
elif enmchar == "2":
    emaxhealth, ehealth = 90, 90
    emaxstamina, estamina = 70, 70
else:
    emaxhealth, ehealth = 110, 110
    emaxstamina, estamina = 50, 50

actions = ["Attack", "Rest", "Defend"]

# Main game loop
while phealth > 0 and ehealth > 0:
    print(f"\nYour health: {phealth} / {pmaxhealth}, Stamina: {pstamina} / {pmaxstamina}")
    print(f"Enemy health: {ehealth} / {emaxhealth}, Stamina: {estamina} / {emaxstamina}")

    # Player turn
    print("\nYour turn! Choose an action:")
    print("1 - Crushing blow with an axe (15 stamina)")
    print("2 - Intimidating roar (10 stamina)")
    print("3 - Battle stance (5 stamina)")
    print("4 - Rest (restores 20 stamina)")
    choice = int(input("Enter the number of your choice: "))

    # Player action handling
    if choice == 1:
        if pstamina >= 15:
            pstamina -= 15
            damage = random.randint(25, 35)
            print(f"\nYou swing as hard as you can with your axe and deal {damage} damage!")
            ehealth -= damage
        else:
            print("Not enough stamina to attack!")
    elif choice == 2:
        pstamina += 20
        if pstamina > pmaxstamina:
            pstamina = pmaxstamina
        print("\nYou roar loudly, boosting your morale and stamina!")
    elif choice == 3:
        print("\nYou assume a battle stance, preparing for the enemy's attack.")
        # Defensive stance logic handled during enemy attack
        # For simplicity, we'll set a flag
        defending = True
    elif choice == 4:
        pstamina += 20
        if pstamina > pmaxstamina:
            pstamina = pmaxstamina
        print("\nYou rest and regain 20 stamina!")
        defending = False
    else:
        print("Invalid choice, turn skipped.")
        defending = False

    # Enemy turn
    enemy_action = random.choice(actions)
    print(f"\nEnemy chooses to: {enemy_action}")

    # Handle enemy action
    if enemy_action == "Attack":
        # Check if player is defending
        if 'defending' in locals() and defending:
            damage = random.randint(5, 15)
            print(f"The enemy attacks, but you defend successfully and take only {damage} damage!")
            phealth -= damage
        else:
            damage = random.randint(25, 35)
            print(f"The enemy attacks and deals {damage} damage!")
            phealth -= damage
        # Reset defending status after attack
        if 'defending' in locals():
            del defending
    elif enemy_action == "Rest":
        estamina += 20
        if estamina > emaxstamina:
            estamina = emaxstamina
        print("The enemy rests and regains stamina!")
    elif enemy_action == "Defend":
        print("The enemy defends this round!")
    

    if phealth <= 0:
        print("\nYou have been defeated! Game over.")
        break
    if ehealth <= 0:
        print("\nCongratulations! You won the fight!")
        break