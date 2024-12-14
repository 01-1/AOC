
def compare_hands(hand1, hand2):
    # Compare two hands based on the rules
    # Return -1 if hand1 is stronger, 1 if hand2 is stronger, and 0 if they are equal
    # (This comparison assumes hands are valid and of the same type)
    for card1, card2 in zip(hand1, hand2):
        if card1 != card2:
            return -1 if card1 > card2 else 1
    return 0

def calculate_rank(hand, index):
    # Calculate the rank of a hand based on its type and cards
    # Return a tuple (rank, index) where rank is the calculated rank and index is the original index in the input
    hand_type_order = {'AAAAA': 7, 'AAABB': 6, 'AAA22': 5, 'AABBB': 4, 'AAABC': 3, 'ABCDE': 2, 'AABCD': 1}
    
    hand_type = ''.join(sorted(hand))
    rank = hand_type_order[hand_type]
    return (rank, index)

def calculate_total_winnings(hands):
    # Calculate total winnings for a set of hands
    total_winnings = 0
    
    # Sort hands based on type and cards
    sorted_hands = sorted(enumerate(hands), key=lambda x: calculate_rank(x[1], x[0]), reverse=True)
    
    # Calculate winnings
    for i, (hand, bid) in enumerate(sorted_hands):
        total_winnings += bid * (i + 1)
    
    return total_winnings

if __name__ == "__main__":
    # Read input from standard input
    #num_hands = int(input())
    num_hands = 1000
    hands = []
    for _ in range(num_hands):
        hand, bid = input().split()
        hands.append((hand, int(bid)))
    
    # Calculate total winnings
    winnings = calculate_total_winnings(hands)
    
    print(winnings)
