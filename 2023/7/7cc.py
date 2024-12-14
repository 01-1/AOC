

def rank_hand(hand):
    labels = "AKQJT98765432"
    label_values = {label: i for i, label in enumerate(labels)}

    hand_type_order = [
        "Five of a kind",
        "Four of a kind",
        "Full house",
        "Three of a kind",
        "Two pair",
        "One pair",
        "High card",
    ]

    def hand_strength(hand):
        label_counts = {label: hand.count(label) for label in set(hand)}
        sorted_labels = sorted(label_counts, key=lambda x: (label_counts[x], label_values[x]), reverse=True)

        if len(set(label_counts.values())) == 1:
            return hand_type_order.index("Five of a kind"), sorted_labels

        if 4 in label_counts.values():
            return hand_type_order.index("Four of a kind"), sorted_labels

        if 3 in label_counts.values() and 2 in label_counts.values():
            return hand_type_order.index("Full house"), sorted_labels

        if 3 in label_counts.values():
            return hand_type_order.index("Three of a kind"), sorted_labels

        if list(label_counts.values()).count(2) == 2:
            return hand_type_order.index("Two pair"), sorted_labels

        if 2 in label_counts.values():
            return hand_type_order.index("One pair"), sorted_labels

        return hand_type_order.index("High card"), sorted_labels

    hands = hand.split()
    return hand_strength(hands[0])


def calculate_winnings(hands_with_bids):
    sorted_hands = sorted(hands_with_bids, key=lambda x: rank_hand(x)[::-1])

    total_winnings = sum((i + 1) * int(bid) for i, (hand, bid) in enumerate(sorted_hands))
    return total_winnings


if __name__ == "__main__":
    hands_with_bids = [input().split() for _ in range(1000)]
    total_winnings = calculate_winnings(hands_with_bids)
    print(total_winnings)
