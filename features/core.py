"""Core StudySprint logic: the deck, the quiz loop, and small helpers."""


def get_cards(data):
    return data["cards"]


def check_answer(card, guess):
    return guess.strip().lower() == card["answer"].strip().lower()


def run_quiz(cards, ask=input, show=print):
    score = 0
    total = len(cards)
    incorrect_cards = []
    for card in cards:
        guess = ask(card["question"] + " ")
        if check_answer(card, guess):
            show("Correct!")
            score += 1
        else:
            show("Not quite. The answer was: " + card["answer"])
            incorrect_cards.append(card["question"])
    return score


def add_card(data, question, answer, category="general"):
    new_id = max((c["id"] for c in data["cards"]), default=0) + 1
    card = {"id": new_id, "question": question, "answer": answer, "category": category}
    data["cards"].append(card)
    return card


def list_cards(cards, show=print):
    for card in cards:
        show(str(card["id"]) + ". " + card["question"])


def cards_by_category(cards, category):
    return [c for c in cards if c["category"] == category]


def count_by_category(cards):
    """
    Return the number of cards in each category
    """
    counts = {}
    for card in cards:
        name = card["category"]
        counts[name] = counts.get(name, 0) + 1
    return counts


def top_card(cards):
    return cards[len(cards) - 1]


def percent_correct(score, total):
    if total == 0:
        return 0
    return round(100 * score / total)

def review_missed(cards, results):
    """
    Returns a list of cards that were answered incorrectly from last
    quiz (when results == False)
    """
    missed_cards = []

    #Loop through all card numbers
    for i in range(len(cards)):
        #Check if current card number was answered incorrectly
        if results[i] == False:
            missed_cards.append(cards[i])

    #Return list(will still work if nothing was missed)
    return missed_cards