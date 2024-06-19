import random

def initialize_game():
    player1 = input("Enter name for Player 1: ")
    player2 = input("Enter name for Player 2: ")
    player1_hp = 3
    player2_hp = 3
    return player1, player2, player1_hp, player2_hp

def load_shotgun():
    bullets = ['Empty'] * 6
    full_bullets = random.randint(1, 5)
    for i in range(full_bullets):
        bullets[i] = 'Full'
    random.shuffle(bullets)
    empty_bullets = 6 - full_bullets
    print(f"Shotgun reloaded! {full_bullets} full bullets, and {empty_bullets} empty bullets.")
    return bullets

def take_turn(player, opponent, hp, bullets):
    action = input(f"{player}'s turn. Shoot at (1) {opponent} or (2) yourself? Enter 1 or 2: ")
    if action == '1':
        target = opponent
    elif action == '2':
        target = player
    else:
        print("Invalid input. Try again.")
        return take_turn(player, opponent, hp, bullets)

    bullet = bullets.pop(0)
    if bullet == 'Full':
        print(f"The bullet was Full! {target} loses 1 HP.")
        hp[target] -= 1
        return False  # Switch turn
    else:
        print("The bullet was Empty! No damage.")
        if target == player:
            return True  # Player's turn continues
        else:
            return False  # Switch turn

def display_hp(player1, player2, hp):
    print(f"{player1} HP: {hp[player1]}, {player2} HP: {hp[player2]}")

def main():
    player1, player2, player1_hp, player2_hp = initialize_game()
    hp = {player1: player1_hp, player2: player2_hp}
    bullets = load_shotgun()
    current_player = player1
    opponent = player2

    while hp[player1] > 0 and hp[player2] > 0:
        display_hp(player1, player2, hp)
        turn_continues = take_turn(current_player, opponent, hp, bullets)
        if not turn_continues:
            current_player, opponent = opponent, current_player
        if len(bullets) == 0:
            bullets = load_shotgun()

    winner = player1 if hp[player2] == 0 else player2
    print(f"Game over! {winner} wins!")

if __name__ == "__main__":
    main()
