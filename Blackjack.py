import random

def create_deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [{"rank": rank, "suit": suit} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck


def card_value(card):
    rank = card["rank"]
    if rank in ["Jack", "Queen", "King"]:
        return 10
    elif rank == "Ace":
        return 11
    else:
        return int(rank)
    
def draw_card(deck):
    return deck.pop()
    
def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        card_val = card_value(card)
        if card["rank"] == "Ace":
            aces += 1
        value += card_val
    
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def play_blackjack():
    deck = create_deck()

    player_hand = [draw_card(deck), draw_card(deck)]
    dealer_hand = [draw_card(deck), draw_card(deck)]

    print(f"Your hand: {player_hand}, value: {calculate_hand_value(player_hand)}")
    print(f"Dealer's hand: [{dealer_hand[0]}, {'Hidden'}]")

    while calculate_hand_value(player_hand) < 21:
        action = input("Do you want to hit or stand?").lower()
        if action == "hit":
             player_hand.append(draw_card(deck))
             print(f"Your hand: {player_hand}, value: {calculate_hand_value(player_hand)}")
        elif action == 'stand':
            break
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(draw_card(deck))
    print(f"Dealer's hand: {dealer_hand}, value: {calculate_hand_value(dealer_hand)}")

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    if player_value > 21:
        print ("You bust! Dealer wins.")
    elif dealer_value > 21 or player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie")

play_blackjack()


input("Press Enter to close the program...")