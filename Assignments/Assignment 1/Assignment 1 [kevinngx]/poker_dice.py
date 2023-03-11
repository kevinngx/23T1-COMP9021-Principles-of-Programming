from random import randint, seed

cards = ['Ace', 'King', 'Queen', 'Jack', '10', '9']

def generate_hand(hand):
    # Generate hand up to 5 cards / rolls
    for i in range(5-len(hand)):
        hand.append(cards[randint(0,5)])
    hand = sorted(hand, key=cards.index)
    return hand   
    
def identify_hand(hand):
    # Identify the number of each cards rolled
    hand_values = {card: 0 for card in cards} 
    for card in hand:
        hand_values[card] += 1
    
    # Sort the hands, and grab the two most common cards
    sorted_hand = sorted(hand_values.items(), key=lambda item: item[1], reverse=True)
    combo = sorted_hand[0][1], sorted_hand[1][1]
    
    # If there are no combos i.e. all cards occur just once then it is either a straight or a bust
    # We know it's a straight if either 9 or Ace does not appear in the hand of 5
    if combo == (1, 1): 
        if hand_values['9'] == 0 or hand_values['Ace'] == 0:
            return "Straight"
        else:
            return "Bust"
    
    # Identify the combo that we have received
    combos = {
        (5,0): "Five of a kind",
        (4,1): "Four of a kind",
        (3,2): "Full house",
        (3,1): "Three of a kind",
        (2,2): "Two pair",
        (2,1): "One pair"
    } 
    return combos[combo]

def remove_card(hand, card):
    hand.pop(hand.index(card))

def ask_for_keeps(hand, round):
    cards_to_keep = []
    while True:
        try:
            temp_hand = hand.copy()
            cards_to_keep = input(f'Which dice do you want to keep for the {round} roll? ').split(" ")
            
            # Return empty list if they requst 'all' or 'All'
            if cards_to_keep[0] == 'all' or cards_to_keep[0] == 'All':
                return hand
            
            # Returns an empty hand if no input is provided
            if cards_to_keep[0] == '':
                return []
            
            for card in cards_to_keep:
                if card not in temp_hand:
                    raise ValueError
                remove_card(temp_hand, card)
            break
            
        except ValueError:
            print('That is not possible, try again!')
            
    return cards_to_keep
    
    
def play(simulate=False): 
    
    # Starting first round
    hand = []
    hand = generate_hand(hand)
    hand_value = identify_hand(hand)
    
    # If we are running in simulate mode, simply return the result
    if simulate:
        return hand_value
    
    print('The roll is:', ' '.join(hand))
    print('It is a', hand_value)
    
    # Starting Second round
    hand = ask_for_keeps(hand, 'second')
    if len(hand) == 5:
        print('Ok, done.')
        return
    
    hand = generate_hand(hand)
    hand_value = identify_hand(hand)
    
    print('The roll is:', ' '.join(hand))
    print('It is a', hand_value)
    
    # Starting Third Round
    hand = ask_for_keeps(hand, 'third')
    if len(hand) == 5:
        print('Ok, done.')
        return
    
    hand = generate_hand(hand)
    hand_value = identify_hand(hand)
    
    print('The roll is:', ' '.join(hand))
    print('It is a', hand_value)

def simulate(n):
    # print("***************************")
    # print(f'poker_dice.simulate({n})')
    hands = {
        "Five of a kind": 0,
        "Four of a kind": 0,
        "Full house": 0,
        "Straight": 0,
        "Three of a kind": 0,
        "Two pair": 0,
        "One pair": 0,
        # "Bust": 0 # We don't want to show busts
    } 
    
    for _ in range(n):
        result = play(simulate=True)
        if result != "Bust":
            hands[result] += 1

    for hand, count in hands.items():
        print(f'{hand:15}: {(count/n*100):.2f}%')