"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.

    'J', 'Q', 'K' = 10
    'A' = 1
    '2' - '10' = numeric value
    """
    if card == "A":
        return 1
    if card in ("J", "Q", "K"):
        return 10
    # card is string like '2', '3', ..., '10'
    if card.isdigit():
        return int(card)
    # fallback (shouldn't happen with valid input)
    raise ValueError(f"Unknown card: {card}")


def higher_card(card_one, card_two):
    """Return which card is higher. If equal, return both as a tuple.

    :param card_one, card_two: str
    :return: str or tuple(str, str)
    """
    val1 = value_of_card(card_one)
    val2 = value_of_card(card_two)

    if val1 > val2:
        return card_one
    if val2 > val1:
        return card_two
    # tie: return the original card strings as a tuple
    return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace (1 or 11).

    :param card_one, card_two: str - current two cards in hand
    :return: int - 11 if placing 11 keeps total <= 21 and is advantageous, otherwise 1

    Rules:
    - If either existing card is an 'A', the new ace must be 1 (since one ace will count as 11).
    - Otherwise, if sum of current values <= 10, return 11 (because 11 + sum <= 21).
    - Else return 1.
    """
    # If either existing card is an Ace, new ace must be 1
    if card_one == "A" or card_two == "A":
        return 1

    total = value_of_card(card_one) + value_of_card(card_two)
    if total <= 10:
        return 11
    return 1


def is_blackjack(card_one, card_two):
    """Determine if the two-card hand is a natural blackjack (an Ace + a 10-valued card)."""
    # True if one card is 'A' and the other is 10-valued
    ten_valued = {"10", "J", "Q", "K"}
    return (card_one == "A" and card_two in ten_valued) or (card_two == "A" and card_one in ten_valued)


def can_split_pairs(card_one, card_two):
    """Can the hand be split? (cards of equal value)"""
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Can double down? (sum is 9, 10, or 11)"""
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in (9, 10, 11)
