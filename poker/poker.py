def poker(hands):

    category_weights = {'nothing': 0,
                        'one pair': 1,
                        'two pair': 2,
                        'three of a kind': 3,
                        'straight': 4,
                        'flush': 5,
                        'full house': 6,
                        'four of a kind': 7,
                        'straight flush': 8}

    rank_weights = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                    '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    hand_set_dict = {}      # {hand: sets of flushes and ranks and count of ranks}

    # separating the flushes and the ranks
    for hand in hands:
        flushes = [card[-1] for card in hand]
        ranks = [card[0] for card in hand]

        hand_set_dict[tuple(hand)] = (flushes, ranks)
        print(flushes, ranks)

    hand_categories = []

    for hand in hand_set_dict.keys():
        category = hand_category(hand_set_dict[hand][0], hand_set_dict[hand][-1])
        category_weight = category_weights[category]
        high = high_card(hand)
        hand_categories.append(hand)
        hand_categories.append((category, category_weight, high, rank_weights[high]))

    print(hand_categories)

    if hand_categories[1][1] > hand_categories[-1][1]:
        result = hand_categories[0]
    elif hand_categories[1][1] < hand_categories[-1][1]:
        result = hand_categories[-2]
    else:
        result = hand_categories[0] if hand_categories[1][-1] > hand_categories[-1][-1]\
                 else hand_categories[-2]

    return [list(result)]


def hand_category(flushes, ranks):
    arranged_ranks = [{'A', '2', '3', '4', '5'},
                     {'2', '3', '4', '5', '6'},
                     {'3', '4', '5', '6', '7'},
                     {'4', '5', '6', '7', '8'},
                     {'5', '6', '7', '8', '9'},
                     {'6', '7', '8', '9', '10'},
                     {'7', '8', '9', '10', 'J'},
                     {'8', '9', '10', 'J', 'Q'},
                     {'9', '10', 'J', 'Q', 'K'},
                     {'10', 'J', 'Q', 'K', 'A'}]

    flushes_set = set(flushes)
    ranks_set = set(ranks)

    if len(flushes_set) == 1 and ranks_set in arranged_ranks:
        return 'straight flush'

    if len(ranks_set) == 2 and len(flushes_set) == 4:
        return 'four of a kind'

    if len(ranks_set) == 2 and len(flushes_set) >= 3:
        return 'full house'

    if len(flushes_set) == 1:
        return 'flush'

    if ranks_set in arranged_ranks:
        return 'straight'

    if len(flushes_set) >= 3 and len(ranks_set) == 3 and max_repeats(ranks) == 3:
        return 'three of a kind'

    if len(ranks_set) == 3 and len(flushes_set) >= 2 and max_repeats(ranks) == 2:
        return 'two pair'

    if len(ranks_set) == 4 and len(flushes_set) >= 2:
        return 'one pair'

    return 'nothing'


def high_card(hand):
    ranks = [card[0] for card in hand]
    if 'A' in ranks:
        result = 'A'
    elif 'K' in ranks:
        result = 'K'
    elif 'Q' in ranks:
        result = 'Q'
    elif 'J' in ranks:
        result = 'J'
    else:
        result = '2'
        for rank in ranks:
            if int(rank) > int(result):
                result = rank

    return result


def max_repeats(ranks):
    repeats = {rank: 0 for rank in ranks}
    for rank in ranks:
        repeats[rank] += 1
    result = 1
    for key in repeats.keys():
        if repeats[key] > result:
            result = repeats[key]
    return result