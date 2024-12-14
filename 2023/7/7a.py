def gcc(hand):
    card_counts = {}
    for card in hand:
        card_counts[card] = card_counts.get(card, 0) + 1
    sorted_cards = sorted(card_counts.values())[::-1] + [0,0]
    print(hand, sorted_cards)

    if sorted_cards[0] == 5:
        return 7  # Five of a kind
    elif sorted_cards[0] == 4:
        return 6  # Four of a kind
    elif sorted_cards[0] == 3 and sorted_cards[1] == 2:
        return 5  # Full house
    elif sorted_cards[0] == 3:
        return 4  # Three of a kind
    elif sorted_cards[0] == 2 and sorted_cards[1] == 2:
        return 3  # Two pair
    elif sorted_cards[0] == 2:
        return 2  # One pair
    else:
        return 1  # High card

    sorted_cards = sorted(card_counts.keys(), key=lambda x: (card_counts[x], ranks.index(x)), reverse=True)

def calculate_winnings(hands):
    total_winnings = 0
    hand_ranks = []

    ranks = "AKQJT98765432"
    nhands = []
    for hand, bid in hands:
        rank = [14-ranks.index(x) for x in hand]
        nhands.append(((gcc(hand), rank), bid)) 

    nhands.sort()
    #nhands = nhands[::-1]
    print(nhands)
    rank = 0
    for hand, bid in nhands:
        rank += 1
        total_winnings += bid * rank

    return hand_ranks, total_winnings

# Read input
hands = []
n = 1000
for _ in range(n):
    line = input().strip().split()
    hands.append((line[0], int(line[1])))

# Calculate ranks and total winnings
hand_ranks, total_winnings = calculate_winnings(hands)

# Print results
print("Hand Ranks:", hand_ranks)
print("Total Winnings:", total_winnings)
