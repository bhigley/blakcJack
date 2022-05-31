from tkinter import *
import random
from PIL import Image, ImageTk
from click import command
from Deck import Deck
from game import Game
from Player import Player


root = Tk()
root.title('Codemy.com - Card Deck')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("1000x800")
root.configure(background="green")

frame = Frame(root, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

deck = Deck()
player1 = Player("player1")
dealer = Player("Dealer")

def update_bet():
    player1.bet = int(bet_entry.get())

def update_bank():
    if player1.bust == True:
        player1.bank -= player1.bet
    elif dealer.bust == True:
        player1.bank += player1.bet
    elif player1.showScore() > dealer.showScore():
        player1.bank += player1.bet
    elif player1.showScore() < dealer.showScore():
        player1.bank -= player1.bet
    # else tie, no change in bank
    bank_label.config(text=f'Current bank: {player1.bank}')


# Resize Cards
def resize_cards(card):
	# Open the image
	our_card_img = Image.open(card)

	# Resize The Image
	our_card_resize_image = our_card_img.resize((100, 150))
	
	# output the card
	global our_card_image
	our_card_image = ImageTk.PhotoImage(our_card_resize_image)

	# Return that card
	return our_card_image

# Shuffle The Cards
def shuffle():
	# Define Our Deck
    deck.newDeck()
    deck.shuffle()
    root.title(f'Codemy.com - {len(deck.cards)} Cards Left')

    # clear labels
    clear_labels()


def deal():
    if len(deck.cards) < 15:
        shuffle()
    clear_labels()

    global dealer_image1, dealer_image2
    global player_image1, player_image2
    dealer.hand = []
    player1.hand = []
    dealer.bust = False
    player1.bust = False
    dealer.draw(deck, 2)
    player1.hand = []
    player1.draw(deck, 2)
    deckDealer = []
    deckPlayer = []

    for card in dealer.hand:
        deckDealer.append(f'{card.value}_of_{card.suit}')
    for card in player1.hand:
        deckPlayer.append(f'{card.value}_of_{card.suit}')

    dealer_image1 = resize_cards(f'/Users/benhigley/Desktop/CodingFun/BlackJack/cards/{deckDealer[0]}.png')
    dealer_label_1.config(image=dealer_image1)
    if dealer.showScore() == 21:
        dealer_label_6.config(text='Blackjack')
        dealer_image2 = resize_cards(f'/Users/benhigley/Desktop/CodingFun/BlackJack/cards/{deckDealer[1]}.png')
        dealer_label_3.config(image=dealer_image3)
        if player1.showScore() != 21:
            player_label_6.config(text="You lose")
            player1.bank = player1.bank - player1.bet
        else:
           player_label_6.config(text="Push") 

    player_image1 = resize_cards(f'/Users/benhigley/Desktop/CodingFun/BlackJack/cards/{deckPlayer[0]}.png')
    player_label_1.config(image=player_image1)
    player_image2 = resize_cards(f'/Users/benhigley/Desktop/CodingFun/BlackJack/cards/{deckPlayer[1]}.png')
    player_label_2.config(image=player_image2)
    player_label_6.config(text=player1.showScore())

    root.title(f'Codemy.com - {len(deck.cards)} Cards Left')


def dealer_turn():
    global dealer_image5, dealer_image4, dealer_image3, dealer_image2
    newCard =f'{dealer.hand[-1].value}_of_{dealer.hand[-1].suit}'
    dealer_image2 = resize_cards(f'/Users/benhigley/Desktop/CodingFun/BlackJack/cards/{newCard}.png')
    dealer_label_2.config(image=dealer_image2)
    while dealer.showScore() < 17:
        dealer.draw(deck)
        root.title(f'Codemy.com - {len(deck.cards)} Cards Left')
        newCard =f'{dealer.hand[-1].value}_of_{dealer.hand[-1].suit}'
        if len(dealer.hand) == 3:
            dealer_image3 = resize_cards(f'/Users/benhigley/Desktop/CodingFun/BlackJack/cards/{newCard}.png')
            dealer_label_3.config(image=dealer_image3)
        elif len(dealer.hand) == 4:
            dealer_image4 = resize_cards(f'/Users/benhigley/Desktop/CodingFun/BlackJack/cards/{newCard}.png')
            dealer_label_4.config(image=dealer_image4)
        elif len(dealer.hand) == 5:
            dealer_image5 = resize_cards(f'/Users/benhigley/Desktop/CodingFun/BlackJack/cards/{newCard}.png')
            dealer_label_5.config(image=dealer_image5)
    dealer_label_6.config(text=dealer.showScore())
    update_bank()


def player_hit():
    global player_image5, player_image4, player_image3
    player1.draw(deck)
    root.title(f'Codemy.com - {len(deck.cards)} Cards Left')
    newCard =f'{player1.hand[-1].value}_of_{player1.hand[-1].suit}'
    if len(player1.hand) == 3:
        player_image3 = resize_cards(f'/Users/benhigley/Desktop/CodingFun/BlackJack/cards/{newCard}.png')
        player_label_3.config(image=player_image3)
    elif len(player1.hand) == 4:
        player_image4 = resize_cards(f'/Users/benhigley/Desktop/CodingFun/BlackJack/cards/{newCard}.png')
        player_label_4.config(image=player_image4)
    elif len(player1.hand) == 5:
        player_image5 = resize_cards(f'/Users/benhigley/Desktop/CodingFun/BlackJack/cards/{newCard}.png')
        player_label_5.config(image=player_image5)
    if player1.showScore() >= 21:
        if player1.bust is True:
            player_label_6.config(text='Bust')
        else:
            player_label_6.config(text='21!')
        dealer_turn()
    else:
        player_label_6.config(text=player1.showScore())

def card_count():
    count_button.config(text=deck.cardCount)

def clear_labels():
    dealer_label_1.config(image='')
    dealer_label_2.config(image='')
    dealer_label_3.config(image='')
    dealer_label_4.config(image='')
    dealer_label_5.config(image='')
    dealer_label_6.config(text='')

    player_label_1.config(image='')
    player_label_2.config(image='')
    player_label_3.config(image='')
    player_label_4.config(image='')
    player_label_5.config(image='')
    player_label_6.config(text='')


my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# Create Frames For Cards
dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.pack(padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.pack(ipadx=20, pady=10)

# Put Dealer cards in frames
dealer_label_1 = Label(dealer_frame, text='')
dealer_label_1.grid(row=0, column=0, pady=20, padx=20)

dealer_label_2 = Label(dealer_frame, text='')
dealer_label_2.grid(row=0, column=1, pady=20, padx=20)

dealer_label_3 = Label(dealer_frame, text='')
dealer_label_3.grid(row=0, column=2, pady=20, padx=20)

dealer_label_4 = Label(dealer_frame, text='')
dealer_label_4.grid(row=0, column=3, pady=20, padx=20)

dealer_label_5 = Label(dealer_frame, text='')
dealer_label_5.grid(row=0, column=4, pady=20, padx=20)

dealer_label_6 = Label(dealer_frame, text='')
dealer_label_6.grid(row=0, column=5, pady=20, padx=20)

# Put Player cards in frames
player_label_1 = Label(player_frame, text='')
player_label_1.grid(row=1, column=0, pady=20, padx=20)

player_label_2 = Label(player_frame, text='')
player_label_2.grid(row=1, column=1, pady=20, padx=20)

player_label_3 = Label(player_frame, text='')
player_label_3.grid(row=1, column=2, pady=20, padx=20)

player_label_4 = Label(player_frame, text='')
player_label_4.grid(row=1, column=3, pady=20, padx=20)

player_label_5 = Label(player_frame, text='')
player_label_5.grid(row=1, column=4, pady=20, padx=20)

player_label_6 = Label(player_frame, text='')
player_label_6.grid(row=1, column=5, pady=20, padx=20)

# Create Button Frame
button_frame = Frame(root, bg="green")
button_frame.pack(pady=20)

# Create a couple buttons
deal_button = Button(button_frame, text="Deal cards", font=("Helvetica", 14), command=deal)
deal_button.grid(row=0, column=3)

shuffle_button = Button(button_frame, text="Shuffle Deck", font=("Helvetica", 14), command=shuffle)
shuffle_button.grid(row=0, column=0)

card_button = Button(button_frame, text="Hit Me!", font=("Helvetica", 14), command=player_hit)
card_button.grid(row=0, column=1, padx=10)

stand_button = Button(button_frame, text="Stand!", font=("Helvetica", 14), command=dealer_turn)
stand_button.grid(row=0, column=2)

# betting widgets
betting_frame = Frame(root, bg="green")
betting_frame.pack(pady=20)

bet_label = Button(betting_frame, text='Confirm Bet', command=update_bet)
bet_label.grid(row=0, column=3)

bet_entry = Entry(betting_frame, width=10)
bet_entry.grid(row=0, column=4)

bank_label = Label(betting_frame, text=f'Current bank: {player1.bank}')
bank_label.grid(row=1, column=4)

count_button = Button(betting_frame, text='Card count', font=("Helvetica", 14), command=card_count)
count_button.grid(row=0, column=5)



root.mainloop()