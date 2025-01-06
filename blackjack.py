import tkinter
from tkinter import *
import maingui
from maingui import *
import random

#start by creating a deck of cards
def cards():

    blackjack_frame = tk.Toplevel(bg="grey")
    blackjack_frame.title("Black Jack")
    blackjack_frame.geometry("1000x800")

    #makes the gui auto open on full screen
    blackjack_frame.attributes("-fullscreen", True)


    #using canvas function to create rectangular placements for the cards
    #canvas = tk.Canvas(blackjack_frame, width=275, height=450, bg="black") 
    #canvas.pack() 

    #canvas.create_rectangle(25, 50, 275, 450, fill="white", outline="")


    #all function to link to buttons later on in code


    def getextracard1(cardsvalue, limit):
        #creates a thrid card for the player
        player_card_3 = random.choice(list(deck.keys()))  
        player_card_value_3 = deck[player_card_3]   
        player_card_label_3 = tk.Label(blackjack_frame, text=f"You got: {player_card_3}, with a value of {player_card_value_3}", font=('Times', 24), bg="white")
        player_card_label_3.pack(pady=10)
        del deck[player_card_3]
        #adds up cards and creating a running total of card value and amount of cards
        cardsvalue=cardsvalue+player_card_value_3
        limit=limit+1
        cardsvalue_label_2 = tk.Label(blackjack_frame, text=f"Your score is: {cardsvalue}", font=('Times', 18), bg="white")
        cardsvalue_label_2.pack(pady=10)
        if cardsvalue > 21:
            bust_label = tk.Label(blackjack_frame, text="You have gone bust", font=('Times', 18), bg="white")
            bust_label.pack(pady=10)
            blackjack_frame.after(3000, lambda : blackjack_frame.destroy())
        

    def nomorecard(cardsvalue, dealercardsvalue):
        #giving the dealer his own set of cards
        dealer_card_1 = random.choice(list(deck.keys()))  
        dealer_card_value_1 = deck[dealer_card_1]   
        dealer_card_label_1 = tk.Label(blackjack_frame, text=f"Dealer got: {dealer_card_1}, with a value of {dealer_card_value_1}", font=('Times', 24), bg="white")
        dealer_card_label_1.pack(pady=10)
        del deck[dealer_card_1]
    
        dealer_card_2 = random.choice(list(deck.keys()))  
        dealer_card_value_2 = deck[dealer_card_2]   
        dealer_card_label_2 = tk.Label(blackjack_frame, text=f"Dealer got: {dealer_card_2}, with a value of {dealer_card_value_2}", font=('Times', 24), bg="white")
        dealer_card_label_2.pack(pady=10)
        del deck[dealer_card_2]

        dealercardsvalue=dealer_card_value_1+dealer_card_value_2
        
        if dealercardsvalue < 22:
            while dealercardsvalue < 16:
                dealer_card_3 = random.choice(list(deck.keys()))  
                dealer_card_value_3 = deck[dealer_card_3]   
                dealer_card_label_3 = tk.Label(blackjack_frame, text=f"Dealer got: {dealer_card_3}, with a value of {dealer_card_value_3}", font=('Times', 24), bg="white")
                dealer_card_label_3.pack(pady=10)
                del deck[dealer_card_3]
                dealercardsvalue=dealercardsvalue+dealer_card_value_3

            #differnet win conditions
            if cardsvalue == dealercardsvalue:
                print(cardsvalue)
                print("draw")
                #draw user gets their bet back
            
            elif cardsvalue < 22 and cardsvalue > dealercardsvalue:
                print(cardsvalue)
                print("win")
                #user win - gets their money back and more
            
            elif dealercardsvalue < 22 and cardsvalue < dealercardsvalue:
                print(cardsvalue)
                print("loss")
                #dealer win - user loses money placed in the bet
        
        else:
            print("bust")
            #bust





    #linking cards with their values by using a data dictionary
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    #creates o deck of cards where values of linked
    deck = {
        #links the ransk and suit list with the values list
        f"{rank} of {suit}": values[index] 
        for suit in suits 
        for index, rank in enumerate(ranks)
    }


    #gives the player 2 random cards from the deck and removes them from the deck once they have been given so that cards cannot be repeated
    player_card_1 = random.choice(list(deck.keys()))  
    player_card_value_1 = deck[player_card_1]   
    player_card_label_1 = tk.Label(blackjack_frame, text=f"You got: {player_card_1}, with a value of {player_card_value_1}", font=('Times', 24), bg="white")
    player_card_label_1.pack(pady=20)
    del deck[player_card_1]
   
    player_card_2 = random.choice(list(deck.keys()))  
    player_card_value_2 = deck[player_card_2]   
    player_card_label_2 = tk.Label(blackjack_frame, text=f"You got: {player_card_2}, with a value of {player_card_value_2}", font=('Times', 24), bg="white")
    player_card_label_2.pack(pady=20)
    del deck[player_card_2]

    #making a flag variable so that i can limit user to 5 cards
    limit=2
    cardsvalue=0
    dealercardsvalue=0

    print(deck)

    cardsvalue=player_card_value_1+player_card_value_2
    cardsvalue_label_1 = tk.Label(blackjack_frame, text=f"Your score is: {cardsvalue}", font=('Times', 24), bg="white")
    cardsvalue_label_1.pack(pady=20)

    if cardsvalue == 21:
        print("blackjack")

        twist_button_inactive = Button(blackjack_frame, text="Twist", width=20, height=10, font=('Times', 14), bg="grey")
        twist_button_inactive.pack(pady=20)

        stick_button = Button(blackjack_frame, text="Stick", command=lambda: nomorecard(cardsvalue,dealercardsvalue), width=20, height=10, font=('Times', 14), bg="white")
        stick_button.pack(padx=10)
        #special animations when the buttons are hovered over
        stick_button.config(cursor="hand2")
        stick_button.bind("<Enter>", lambda e: stick_button.config(bg="grey"))
        stick_button.bind("<Leave>", lambda e: stick_button.config(bg="white"))

    else:
        twist_button1 = Button(blackjack_frame, text="Twist", command=lambda: getextracard1(cardsvalue,limit), width=20, height=10, font=('Times', 14), bg="white")
        twist_button1.pack(side="left")
        #special animations when the buttons are hovered over
        twist_button1.config(cursor="hand2")
        twist_button1.bind("<Enter>", lambda e: twist_button1.config(bg="grey"))
        twist_button1.bind("<Leave>", lambda e: twist_button1.config(bg="white"))


        stick_button = Button(blackjack_frame, text="Stick", command=lambda: nomorecard(cardsvalue,dealercardsvalue), width=20, height=10, font=('Times', 14), bg="white")
        stick_button.pack(side='right')
        #special animations when the buttons are hovered over
        stick_button.config(cursor="hand2")
        stick_button.bind("<Enter>", lambda e: stick_button.config(bg="grey"))
        stick_button.bind("<Leave>", lambda e: stick_button.config(bg="white"))


































'''
    def on_button_click():
        twist_button1.destroy() 
        getextracard1(cardsvalue,limit)
        new_twist_1()

    def on_button_click_1(twist_button2):
        twist_button2.destroy() 
        getextracard2(cardsvalue,limit)
        new_twist_2()
    def on_button_click_2():
        twist_button1.destroy() 
        getextracard3(cardsvalue,limit)



def new_twist_1():
        twist_button2 = Button(blackjack_frame, text="Twist",command=on_button_click_1, width=20, height=10, font=('Times', 14), bg="white")
        twist_button2.pack(pady=20)
        #special animations when the buttons are hovered over
        twist_button2.config(cursor="hand2")
        twist_button2.bind("<Enter>", lambda e: twist_button2.config(bg="grey"))
        twist_button2.bind("<Leave>", lambda e: twist_button2.config(bg="white"))

    def new_twist_2():
        twist_button3 = Button(blackjack_frame, text="Twist",command=on_button_click_2, width=20, height=10, font=('Times', 14), bg="white")
        twist_button3.pack(pady=20)
        #special animations when the buttons are hovered over
        twist_button3.config(cursor="hand2")
        twist_button3.bind("<Enter>", lambda e: twist_button3.config(bg="grey"))
        twist_button3.bind("<Leave>", lambda e: twist_button3.config(bg="white"))

    def getextracard1(cardsvalue, limit):
        player_card_3 = random.choice(list(deck.keys()))  
        player_card_value_3 = deck[player_card_3]   
        player_card_label_3 = tk.Label(blackjack_frame, text=f"You got: {player_card_3}, with a value of {player_card_value_3}", font=('Times', 24), bg="white")
        player_card_label_3.pack(pady=20)
        del deck[player_card_3]
        cardsvalue=cardsvalue+player_card_value_3
        limit=limit+1
        cardsvalue_label_2 = tk.Label(blackjack_frame, text=f"Your score is: {cardsvalue}", font=('Times', 24), bg="white")
        cardsvalue_label_2.pack(pady=20)
        if cardsvalue > 21:
            bust_label = tk.Label(blackjack_frame, text="You have gone bust", font=('Times', 24), bg="white")
            bust_label.pack(pady=20)
            blackjack_frame.after(3000, lambda : blackjack_frame.destroy())
        
        return cardsvalue, limit

    def getextracard2(cardsvalue, limit):
        player_card_3 = random.choice(list(deck.keys()))  
        player_card_value_3 = deck[player_card_3]   
        player_card_label_3 = tk.Label(blackjack_frame, text=f"You got: {player_card_3}, with a value of {player_card_value_3}", font=('Times', 24), bg="white")
        player_card_label_3.pack(pady=20)
        del deck[player_card_3]
        cardsvalue=cardsvalue+player_card_value_3
        limit=limit+1
        cardsvalue_label_2 = tk.Label(blackjack_frame, text=f"Your score is: {cardsvalue}", font=('Times', 24), bg="white")
        cardsvalue_label_2.pack(pady=20)
        if cardsvalue > 21:
            bust_label = tk.Label(blackjack_frame, text="You have gone bust", font=('Times', 24), bg="white")
            bust_label.pack(pady=20)
            blackjack_frame.after(3000, lambda : blackjack_frame.destroy())
        
        return cardsvalue, limit


    def getextracard3(cardsvalue, limit):
        player_card_3 = random.choice(list(deck.keys()))  
        player_card_value_3 = deck[player_card_3]   
        player_card_label_3 = tk.Label(blackjack_frame, text=f"You got: {player_card_3}, with a value of {player_card_value_3}", font=('Times', 24), bg="white")
        player_card_label_3.pack(pady=20)
        del deck[player_card_3]
        cardsvalue=cardsvalue+player_card_value_3
        limit=limit+1
        cardsvalue_label_2 = tk.Label(blackjack_frame, text=f"Your score is: {cardsvalue}", font=('Times', 24), bg="white")
        cardsvalue_label_2.pack(pady=20)
        if cardsvalue > 21:
            bust_label = tk.Label(blackjack_frame, text="You have gone bust", font=('Times', 24), bg="white")
            bust_label.pack(pady=20)
            blackjack_frame.after(3000, lambda : blackjack_frame.destroy())
        
        return cardsvalue, limit '''























