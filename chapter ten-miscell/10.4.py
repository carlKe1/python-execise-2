# Use the following two lists and the format method to create a list of card names in the format
# card value of suit name (for example, 'Two of Clubs').
# suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
# values = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
# 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

def create_card_names(suits, values):
    card_names = []
    for suit in suits:
        for value in values:
            card_names.append(f"{value} of {suit}")
    return card_names

def main():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

    card_names = create_card_names(suits, values)

    for card_name in card_names:
        print(card_name)

if __name__ == "__main__":
    main()
