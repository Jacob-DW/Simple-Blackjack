import tkinter
from tkinter import *
import maingui
from maingui import *
import random
#py -m pip install pillow
from PIL import Image, ImageTk

#start by creating a deck of cards
def cards():

    def playbuttonclick():
        play_button1.destroy()
        play()

    def play():

        #changing the background to the verison where cards are flipped around
        #when on school pc make Jacob to VMUser2
        bg_image1 = Image.open(r"C://Users//VMUser2//Downloads//blackjack bg - start game.png").resize((1600, 900))
        bg_photo1 = ImageTk.PhotoImage(bg_image1)  #make it so tkinter can understand so i can go as a label

        # Create a label to display the image
        image_label = Label(blackjack_frame, image=bg_photo1)
        image_label.image = bg_photo1  
        image_label.place(x=0, y=0, relwidth=1, relheight=1)


        #all function to link to buttons later on in code
        def getextracard1(cardsvalue, limit):

        # Check if the user has reached the limit of 5 cards
            if limit >= 5:
                bust_label = tk.Label(blackjack_canvas, text="You cannot draw more than 5 cards", font=('Times', 18), bg="white")
                bust_label.pack(pady=10)
                return cardsvalue


            #creates a third card for the player
            player_card_3 = random.choice(list(deck.keys()))  
            player_card_value_3 = deck[player_card_3]   
            player_card_label = tk.Label(blackjack_canvas, text=f"You got: {player_card_3}, with a value of {player_card_value_3}", font=('Times', 14), bg="white")
            player_card_label.pack(pady=10)
            del deck[player_card_3]

            #stroing cards in a list so that they dont get overwritten and adds them together for total value of cards
            player_cards.append(player_card_value_3)
            cardsvalue=sum(player_cards)
            limit=limit+1
            cardsvalue_label_2 = tk.Label(blackjack_canvas, text=f"Your score is: {cardsvalue}", font=('Times', 18), bg="white")
            cardsvalue_label_2.pack(pady=10)
            if cardsvalue > 21:
                bust_label = tk.Label(blackjack_canvas, text="You have gone bust", font=('Times', 18), bg="white")
                bust_label.pack(pady=10)
                blackjack_canvas.after(3000, lambda : blackjack_canvas.destroy())
            
            return cardsvalue, player_cards

        def nomorecard(cardsvalue, dealercardsvalue, player_cards):
            
            #giving the dealer his own set of cards
            dealer_card_1 = random.choice(list(deck.keys()))  
            dealer_card_value_1 = deck[dealer_card_1]   
            dealer_card_label_1 = tk.Label(blackjack_canvas, text=f"Dealer got: {dealer_card_1}, with a value of {dealer_card_value_1}", font=('Times', 14), bg="white")
            dealer_card_label_1.pack(pady=10)
            del deck[dealer_card_1]
        
            dealer_card_2 = random.choice(list(deck.keys()))  
            dealer_card_value_2 = deck[dealer_card_2]   
            dealer_card_label_2 = tk.Label(blackjack_canvas, text=f"Dealer got: {dealer_card_2}, with a value of {dealer_card_value_2}", font=('Times', 14), bg="white")
            dealer_card_label_2.pack(pady=10)
            del deck[dealer_card_2]


            dealer_cards=[]
            dealer_cards.append(dealer_card_value_1)
            dealer_cards.append(dealer_card_value_2)
            dealercardsvalue=sum(dealer_cards)
            
            if dealercardsvalue < 22:
                while dealercardsvalue < 16 and dealercardsvalue < 22:
                    dealer_card_3 = random.choice(list(deck.keys()))  
                    dealer_card_value_3 = deck[dealer_card_3]   
                    dealer_card_label_3 = tk.Label(blackjack_canvas, text=f"Dealer got: {dealer_card_3}, with a value of {dealer_card_value_3}", font=('Times', 14), bg="white")
                    dealer_card_label_3.pack(pady=10)
                    del deck[dealer_card_3]
                    dealer_cards.append(dealer_card_value_3)
                    dealercardsvalue=sum(dealer_cards)
                    cardsvalue=sum(player_cards)
                dealer_total_label = tk.Label(blackjack_canvas, text=f"Dealer got: {dealercardsvalue}", font=('Times', 14), bg="white")
                dealer_total_label.pack(pady=10)
                #differnet win conditions
                if cardsvalue == dealercardsvalue:
                    win_screen_draw = tk.Label(blackjack_canvas, text="It is a draw", font=('Times', 14), bg="white")
                    win_screen_draw.pack(pady=10)
                    blackjack_canvas.after(3000, lambda : blackjack_canvas.destroy())
                    #draw user gets their bet back
                
                elif cardsvalue < 22 and cardsvalue > dealercardsvalue:
                    win_screen_win = tk.Label(blackjack_canvas, text="Player win", font=('Times', 14), bg="white")
                    win_screen_win.pack(pady=10)
                    blackjack_canvas.after(3000, lambda : blackjack_canvas.destroy())
                    #user win - gets their money back and more
                
                elif dealercardsvalue < 22 and cardsvalue < dealercardsvalue:
                    win_screen_loss = tk.Label(blackjack_canvas, text="Dealer win", font=('Times', 14), bg="white")
                    win_screen_loss.pack(pady=10)
                    blackjack_canvas.after(3000, lambda : blackjack_canvas.destroy())
                    #dealer win - user loses money placed in the bet
            
            else:
                dealer_bust_label = tk.Label(blackjack_canvas, text="Dealer has gone bust", font=('Times', 14), bg="white")
                dealer_bust_label.pack(pady=10)
                blackjack_canvas.after(3000, lambda : blackjack_canvas.destroy())
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
        player_card_label_1 = tk.Label(blackjack_canvas, text=f"You got: {player_card_1}, with a value of {player_card_value_1}", font=('Times', 14), bg="white")
        player_card_label_1.pack(pady=20)
        del deck[player_card_1]
    
        player_card_2 = random.choice(list(deck.keys()))  
        player_card_value_2 = deck[player_card_2]   
        player_card_label_2 = tk.Label(blackjack_canvas, text=f"You got: {player_card_2}, with a value of {player_card_value_2}", font=('Times', 14), bg="white")
        player_card_label_2.pack(pady=20)
        del deck[player_card_2]


        #puts a picture of the suit and the rank e.g 1,2,J on the card spot
        if "Hearts" in player_card_1:
            
            cardrank1=player_card_1.split()[0]
            cardrank1_label=tk.Label(blackjack_canvas, text=cardrank1, width=10, height=10, font=('Times', 24), bg="white")
            cardrank1_label.place(x=550, y=600)

            cardrank2=player_card_2.split()[0]
            cardrank2_label=tk.Label(blackjack_canvas, text=cardrank2, width=10, height=10, font=('Times', 24), bg="white")
            cardrank2_label.place(x=850, y=600)

        if "Diamonds" in player_card_1:



            cardrank1=player_card_1.split()[0]
            cardrank1_label=tk.Label(blackjack_canvas, text=cardrank1, width=10, height=10, font=('Times', 24), bg="white")
            cardrank1_label.place(x=550, y=600)

            cardrank2=player_card_2.split()[0]
            cardrank2_label=tk.Label(blackjack_canvas, text=cardrank2, width=10, height=10, font=('Times', 24), bg="white")
            cardrank2_label.place(x=850, y=600)

            
        if "Clubs" in player_card_1:


            cardrank1=player_card_1.split()[0]
            cardrank1_label=tk.Label(blackjack_canvas, text=cardrank1, width=10, height=10, font=('Times', 24), bg="white")
            cardrank1_label.place(x=550, y=600)

            cardrank2=player_card_2.split()[0]
            cardrank2_label=tk.Label(blackjack_canvas, text=cardrank2, width=10, height=10, font=('Times', 24), bg="white")
            cardrank2_label.place(x=850, y=600)
            
        if "Spades" in player_card_1:

            cardrank1=player_card_1.split()[0]
            cardrank1_label=tk.Label(blackjack_canvas, text=cardrank1, width=10, height=10, font=('Times', 24), bg="white")
            cardrank1_label.place(x=550, y=600)


            cardrank2=player_card_2.split()[0]
            cardrank2_label=tk.Label(blackjack_canvas, text=cardrank2, width=10, height=10, font=('Times', 24), bg="white")
            cardrank2_label.place(x=850, y=600)


        #making a flag variable so that i can limit user to 5 cards
        limit=2
        cardsvalue=0
        dealercardsvalue=0
        player_cards=[]

        player_cards.append(player_card_value_1)
        player_cards.append(player_card_value_2)

        cardsvalue=sum(player_cards)
        cardsvalue_label_1 = tk.Label(blackjack_canvas, text=f"Your score is: {cardsvalue}", font=('Times', 14), bg="white")
        cardsvalue_label_1.pack(pady=10)
        


        if cardsvalue == 21:
            print("blackjack")

            twist_button_inactive = Button(blackjack_canvas, text="Twist", width=10, height=5, font=('Times', 14), bg="grey")
            twist_button_inactive.place(x=1375, y=20)

            stick_button = Button(blackjack_canvas, text="Stick", command=lambda: nomorecard(cardsvalue,dealercardsvalue,player_cards), width=10, height=5, font=('Times', 14), bg="white")
            stick_button.place(x=1375, y=200)
            #special animations when the buttons are hovered over
            stick_button.config(cursor="hand2")
            stick_button.bind("<Enter>", lambda e: stick_button.config(bg="grey"))
            stick_button.bind("<Leave>", lambda e: stick_button.config(bg="white"))

        else:
            twist_button1 = Button(blackjack_canvas, text="Twist", command=lambda: getextracard1(cardsvalue,limit), width=10, height=5, font=('Times', 14), bg="white")
            twist_button1.place(x=1375, y=20)
            #special animations when the buttons are hovered over
            twist_button1.config(cursor="hand2")
            twist_button1.bind("<Enter>", lambda e: twist_button1.config(bg="grey"))
            twist_button1.bind("<Leave>", lambda e: twist_button1.config(bg="white"))


            stick_button = Button(blackjack_canvas, text="Stick", command=lambda: nomorecard(cardsvalue,dealercardsvalue, player_cards), width=10, height=5, font=('Times', 14), bg="white")
            stick_button.place(x=1375, y=200)
            #special animations when the buttons are hovered over
            stick_button.config(cursor="hand2")
            stick_button.bind("<Enter>", lambda e: stick_button.config(bg="grey"))
            stick_button.bind("<Leave>", lambda e: stick_button.config(bg="white"))




    blackjack_frame = tk.Toplevel(bg="#22b14c")
    blackjack_frame.title("Black Jack")
    blackjack_frame.geometry("1000x800")

    #makes the gui auto open on full screen
    blackjack_frame.attributes("-fullscreen", True)



    bg_image1 = ImageTk.PhotoImage(Image.open(("C://Users//VMUser2//Downloads//blackjack bg - menu.png")))


    blackjack_canvas=tk.Canvas(blackjack_frame, width=1000, height=800)
    blackjack_canvas.create_image(100, 100, image=bg_image1, anchor=tk.CENTER)

    blackjack_canvas.pack()


    #testing how to import an image
    #need to change VMUser with Jacob when on laptop
    #bg_image1 = Image.open(r"C://Users//VMUser2//Downloads//blackjack bg - menu.png").resize((1600, 900))
    #bg_photo1 = ImageTk.PhotoImage(bg_image1)  #make it so tkinter can understand so i can go as a label

    # Create a label to display the image
    #image_label = Label(blackjack_frame, image=bg_photo1)
    #image_label.image = bg_photo1  
    #image_label.place(x=0, y=0, relwidth=1, relheight=1)


    play_button1 = Button(blackjack_frame, text="Play!", command=playbuttonclick, width=10, height=3, font=('Times', 24), bg="#22b14c", highlightthickness=0)
    play_button1.place(relx=0.5, rely=0.5, anchor=CENTER)
    #special animations when the buttons are hovered over
    play_button1.config(cursor="hand2")































