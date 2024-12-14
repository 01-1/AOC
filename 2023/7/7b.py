def gcc(hand):
    card_counts = {}
    jokers = 0
    for card in hand:
        if card == 'J':
            jokers += 1
        else:
            card_counts[card] = card_counts.get(card, 0) + 1
    sorted_cards = sorted(card_counts.values())[::-1] + [0, 0]

    if sorted_cards[0] + jokers == 5:
        return 7  # Five of a kind
    elif sorted_cards[0] + jokers == 4:
        return 6  # Four of a kind
    elif sorted_cards[0] + jokers == 3 and sorted_cards[1] == 2:
        return 5  # Full house
    elif sorted_cards[0] == 3 and sorted_cards[1] + jokers == 2:
        return 5  # Full house
    elif sorted_cards[0] + jokers == 3:
        return 4  # Three of a kind
    elif sorted_cards[0] + jokers == 2 and sorted_cards[1] == 2:
        return 3  # Two pair
    elif sorted_cards[1] + jokers == 2 and sorted_cards[0] == 2:
        return 3  # Two pair
    elif sorted_cards[0] + jokers == 2:
        return 2  # One pair
    else:
        return 1  # High card

def calculate_winnings(hands):
    total_winnings = 0
    hand_ranks = []

    ranks = "AKQJT98765432"
    nhands = []
    for hand, bid in hands:
        rank = [14-ranks.index(x) if x != 'J' else 0 for x in hand]
        nhands.append(((gcc(hand), rank), bid))

    nhands.sort()
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
