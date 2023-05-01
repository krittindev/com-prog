class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "(%s %s)" % (self.value, self.suit)

    def next1(self):
        values = ["3", "4", "5", "6", "7", "8",
                  "9", "10", "J", "Q", "K", "A", "2"]
        suits = ["club", "diamond", "heart", "spade"]
        score = values.index(self.value) * 4 + suits.index(self.suit)
        score += 1
        score %= 52
        new_card = Card(values[score // 4], suits[score % 4])
        return new_card

    def next2(self):
        values = ["3", "4", "5", "6", "7", "8",
                  "9", "10", "J", "Q", "K", "A", "2"]
        suits = ["club", "diamond", "heart", "spade"]
        score = values.index(self.value) * 4 + suits.index(self.suit)
        score += 1
        score %= 52
        self.value = values[score // 4]
        self.suit = suits[score % 4]


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
