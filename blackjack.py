import tkinter
from tkinter import *
import maingui
from maingui import *
import random
#py -m pip install pillow
from PIL import ImageTk, Image
#pip install pygame
#import pygame
import os
import time

#start by creating a deck of cards
def cards():

    #making the pygame sound work
    #pygame.mixer.init()


    def playbuttonclick():

        play_button1.destroy()
        play()

    def play():

        #changing the background to the verison where cards are flipped around
        #when on school pc make Jacob to VMUser2
        #bg_image1 = Image.open(r"C://Users//VMUser2//Downloads//blackjack bg - start game.png").resize((1600, 900))
        bg_image1 = Image.open(r"C://Users//Jacob//Downloads//blackjack bg - start game.png").resize((1600, 900))
        bg_photo1 = ImageTk.PhotoImage(bg_image1)  #make it so tkinter can understand so i can go as a label
        blackjack_canvas.bg_photo1 = bg_photo1
        blackjack_canvas.create_image(0, 0, image=bg_photo1, anchor=tk.NW)

        # Create a label to display the image
        #image_label = Label(blackjack_frame, image=bg_photo1)
        #image_label.image = bg_photo1  
        #image_label.place(x=0, y=0, relwidth=1, relheight=1)


        #all function to link to buttons later on in code
        def getextracard1(cardsvalue, limit):

        # Check if the user has reached the limit of 5 cards
            if limit >= 5:
                bust_label = tk.Label(blackjack_frame, text="You cannot draw more than 5 cards", font=('Times', 18), bg="white")
                blackjack_canvas.create_window(500, 150, window=bust_label)
                return cardsvalue


            #creates a third card for the player
            player_card_3 = random.choice(list(deck.keys()))  
            player_card_value_3 = deck[player_card_3]   
            player_card_label = tk.Label(blackjack_frame, text=f"You got: {player_card_3}, with a value of {player_card_value_3}", font=('Times', 14), bg="white")
            blackjack_canvas.create_window(500, 500, window=player_card_label)
            del deck[player_card_3]

            #stroing cards in a list so that they dont get overwritten and adds them together for total value of cards
            player_cards.append(player_card_value_3)
            cardsvalue=sum(player_cards)
            limit=limit+1
            cardsvalue_label_2 = tk.Label(blackjack_frame, text=f"Your score is: {cardsvalue}", font=('Times', 18), bg="white")
            blackjack_canvas.create_window(500, 550, window=cardsvalue_label_2)
            if cardsvalue > 21:
                bust_label = tk.Label(blackjack_frame, text="You have gone bust", font=('Times', 18), bg="white")
                blackjack_canvas.create_window(500, 600, window=bust_label)
                blackjack_canvas.after(3000, lambda : blackjack_canvas.destroy())
            
            return cardsvalue, player_cards

        def nomorecard(cardsvalue, dealercardsvalue, player_cards):


            global bg_photo1
            blackjack_canvas.delete("bg_image")
            blackjack_canvas.delete("dealer_elements")


            bg_image3 = Image.open(r"C://Users//Jacob//Downloads//blackjack bg - empty.png").resize((1600, 900))
            bg_photo3 = ImageTk.PhotoImage(bg_image3)  #make it so tkinter can understand so i can go as a label
            blackjack_canvas.bg_photo3 = bg_photo3
            blackjack_canvas.create_image(0, 0, image=bg_photo3, anchor=tk.NW)
            blackjack_canvas.images.append(bg_photo3)

            dealer_card_2 = random.choice(list(deck.keys()))  
            dealer_card_value_2 = deck[dealer_card_2]   
            dealer_card_label_2 = tk.Label(blackjack_frame, text=f"Dealer got: {dealer_card_2}, with a value of {dealer_card_value_2}", font=('Times', 14), bg="white")
            blackjack_canvas.create_window(500, 500, window=dealer_card_label_2)
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
                dealer_total_label = tk.Label(blackjack_frame, text=f"Dealer got: {dealercardsvalue}", font=('Times', 14), bg="white")
                blackjack_canvas.create_window(700, 550, window=dealer_total_label)
                #differnet win conditions
                if cardsvalue == dealercardsvalue:
                    win_screen_draw = tk.Label(blackjack_frame, text="It is a draw", font=('Times', 14), bg="white")
                    blackjack_canvas.create_window(700, 650, window=win_screen_draw)
                    blackjack_canvas.after(6000, lambda : blackjack_canvas.destroy())
                    #draw user gets their bet back
                
                elif cardsvalue < 22 and cardsvalue > dealercardsvalue:
                    win_screen_win = tk.Label(blackjack_frame, text="Player win", font=('Times', 14), bg="white")
                    blackjack_canvas.create_window(700, 650, window=win_screen_win)
                    blackjack_canvas.after(6000, lambda : blackjack_canvas.destroy())
                    #user win - gets their money back and more
                
                elif dealercardsvalue < 22 and cardsvalue < dealercardsvalue:
                    win_screen_loss = tk.Label(blackjack_frame, text="Dealer win", font=('Times', 14), bg="white")
                    blackjack_canvas.create_window(700, 650, window=win_screen_loss)
                    blackjack_canvas.after(6000, lambda : blackjack_canvas.destroy())
                    #dealer win - user loses money placed in the bet
            
            else:
                dealer_bust_label = tk.Label(blackjack_frame, text="Dealer has gone bust", font=('Times', 14), bg="white")
                blackjack_canvas.create_window(700, 550, window=dealer_bust_label)
                blackjack_canvas.after(6000, lambda : blackjack_canvas.destroy())
                #bust





        #linking cards with their values by using a data dictionary
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        #suits = ["Hearts"]
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
        player_card_label_1 = tk.Label(blackjack_frame, text=f"You got: {player_card_1}, with a value of {player_card_value_1}", font=('Times', 14), bg="white")
        blackjack_canvas.create_window(400, 50, window=player_card_label_1)
        del deck[player_card_1]
    
        player_card_2 = random.choice(list(deck.keys()))  
        player_card_value_2 = deck[player_card_2]   
        player_card_label_2 = tk.Label(blackjack_canvas, text=f"You got: {player_card_2}, with a value of {player_card_value_2}", font=('Times', 14), bg="white")
        blackjack_canvas.create_window(400, 100, window=player_card_label_2)
        del deck[player_card_2]

        #making a list to store the images in so tgey dont get removed
        
        blackjack_canvas.images = []  


        print(player_card_1)
        text=player_card_1.split(" ")
        if "Hearts" in text:

            print("Hearts")

            cardrank1=player_card_1.split()[0]
            cardrank1_label=tk.Label(blackjack_frame, text=cardrank1, width=5, height=3, font=('Times', 24), bg="white")
            blackjack_canvas.create_window(640, 730, window=cardrank1_label)

            #bg_image1 = Image.open(("C://Users//VMUser2//Downloads//blackjack hearts.png")).resize((100,100))
            bg_image1 = Image.open(("C://Users//Jacob//Downloads//blackjack hearts.png")).resize((30,30))
            bg_photo1 = ImageTk.PhotoImage(bg_image1)
            blackjack_canvas.create_image(540, 600, image=bg_photo1, anchor=tk.NW)
            blackjack_canvas.image = bg_photo1

            blackjack_canvas.images.append(bg_photo1)
            #making a flipping sound when cards are given out
            #sound=pygame.mixer.Sound("C://Users//VMUser2//Downloads//card-flip.mp3")
            #sound.play()
            
        if "Diamonds" in text:
            print("Diamonds")

            cardrank1=player_card_1.split()[0]
            cardrank1_label=tk.Label(blackjack_frame, text=cardrank1, width=5, height=3, font=('Times', 24), bg="white")
            blackjack_canvas.create_window(640, 730, window=cardrank1_label)
            
            #create symbol for each suit to place onto card
            #bg_image1 = Image.open(("C://Users//VMUser2//Downloads//blackjack diamonds.png")).resize((100,100))
            bg_image1 = Image.open(("C://Users//Jacob//Downloads//blackjack diamonds.png")).resize((30,30))
            bg_photo1 = ImageTk.PhotoImage(bg_image1)
            blackjack_canvas.create_image(540, 600, image=bg_photo1, anchor=tk.NW)
            blackjack_canvas.image = bg_photo1
            blackjack_canvas.images.append(bg_photo1)

        if "Clubs" in text:
            print("Clubs")
            cardrank1=player_card_1.split()[0]
            cardrank1_label=tk.Label(blackjack_frame, text=cardrank1, width=5, height=3, font=('Times', 24), bg="white")
            blackjack_canvas.create_window(640, 730, window=cardrank1_label)

            #create symbol for each suit to place onto card
            #bg_image1 = Image.open(("C://Users//VMUser2//Downloads//blackjack clubs.png")).resize((100,100))
            bg_image1 = Image.open(("C://Users//Jacob//Downloads//blackjack clubs.png")).resize((30,30))
            bg_photo1 = ImageTk.PhotoImage(bg_image1)
            blackjack_canvas.create_image(540, 600, image=bg_photo1, anchor=tk.NW)
            blackjack_canvas.image = bg_photo1
            blackjack_canvas.images.append(bg_photo1)

        if "Spades" in text:
            print("Spades")

            cardrank1=player_card_1.split()[0]
            cardrank1_label=tk.Label(blackjack_frame, text=cardrank1, width=5, height=3, font=('Times', 24), bg="white")
            blackjack_canvas.create_window(640, 730, window=cardrank1_label)

            #create symbol for each suit to place onto card
            #bg_image1 = Image.open(("C://Users//VMUser2//Downloads//blackjack spades.png")).resize((100,100))
            bg_image1 = Image.open(("C://Users//Jacob//Downloads//blackjack spades.png")).resize((30,30))
            bg_photo1 = ImageTk.PhotoImage(bg_image1)
            blackjack_canvas.create_image(540, 600, image=bg_photo1, anchor=tk.NW)
            blackjack_canvas.image = bg_photo1
            blackjack_canvas.images.append(bg_photo1)

    

        #puts a picture of the suit and the rank e.g 1,2,J on the second card spot
        text1=player_card_2.split(" ")
        if "Hearts" in text1:
            
            print("Hearts")

            cardrank2=player_card_2.split()[0]
            cardrank2_label=tk.Label(blackjack_frame, text=cardrank2, width=5, height=3, font=('Times', 24), bg="white")
            blackjack_canvas.create_window(960, 730, window=cardrank2_label)

            #bg_image2 = Image.open(("C://Users//VMUser2//Downloads//blackjack hearts.png")).resize((100,100))
            bg_image2 = Image.open(("C://Users//Jacob//Downloads//blackjack hearts.png")).resize((30,30))
            bg_photo2 = ImageTk.PhotoImage(bg_image2)
            blackjack_canvas.create_image(850, 600, image=bg_photo2, anchor=tk.NW)
            blackjack_canvas.image = bg_photo2
            blackjack_canvas.images.append(bg_photo2)

        if "Diamonds" in text1:

            cardrank2=player_card_2.split()[0]
            cardrank2_label=tk.Label(blackjack_frame, text=cardrank2, width=5, height=3, font=('Times', 24), bg="white")
            blackjack_canvas.create_window(960, 730, window=cardrank2_label)
            
            #bg_image2 = Image.open(("C://Users//VMUser2//Downloads//blackjack diamonds.png")).resize((100,100))
            bg_image2 = Image.open(("C://Users//Jacob//Downloads//blackjack diamonds.png")).resize((30,30))
            bg_photo2 = ImageTk.PhotoImage(bg_image2)
            blackjack_canvas.create_image(850, 600, image=bg_photo2, anchor=tk.NW)
            blackjack_canvas.image = bg_photo2
            blackjack_canvas.images.append(bg_photo2)

    
        if "Clubs" in text1:

            cardrank2=player_card_2.split()[0]
            cardrank2_label=tk.Label(blackjack_frame, text=cardrank2, width=5, height=3, font=('Times', 24), bg="white")
            blackjack_canvas.create_window(960, 730, window=cardrank2_label)
            
            #bg_image2 = Image.open(("C://Users//VMUser2//Downloads//blackjack clubs.png")).resize((100,100))
            bg_image2 = Image.open(("C://Users//Jacob//Downloads//blackjack clubs.png")).resize((30,30))
            bg_photo2 = ImageTk.PhotoImage(bg_image2)
            blackjack_canvas.create_image(850, 600, image=bg_photo2, anchor=tk.NW)
            blackjack_canvas.image = bg_photo2
            blackjack_canvas.images.append(bg_photo2)


        if "Spades" in text1:

            cardrank2=player_card_2.split()[0]
            cardrank2_label=tk.Label(blackjack_frame, text=cardrank2, width=5, height=3, font=('Times', 24), bg="white")
            blackjack_canvas.create_window(960, 730, window=cardrank2_label)

            #bg_image2 = Image.open(("C://Users//VMUser2//Downloads//blackjack spades.png")).resize((100,100))
            bg_image2 = Image.open(("C://Users//Jacob//Downloads//blackjack spades.png")).resize((30,30))
            bg_photo2 = ImageTk.PhotoImage(bg_image2)
            blackjack_canvas.create_image(850, 600, image=bg_photo2, anchor=tk.NW)
            blackjack_canvas.image = bg_photo2
            blackjack_canvas.images.append(bg_photo2)



        #displays the dealers first card
        dealer_card_1 = random.choice(list(deck.keys()))  
        dealer_card_value_1 = deck[dealer_card_1]  
        del deck[dealer_card_1] 

        dealer_card_image_1=dealer_card_1.split()[0]
        dealer_card_image_1=tk.Label(blackjack_frame, text=dealer_card_image_1, width=5, height=3, font=('Times', 24), bg="white")
        blackjack_canvas.create_window(960, 175, window=dealer_card_image_1)
        
        dealertext=player_card_2.split(" ")
        if "Hearts" in dealertext:
            #bg_image2 = Image.open(("C://Users//VMUser2//Downloads//blackjack hearts.png")).resize((100,100))
            bg_image2 = Image.open(("C://Users//Jacob//Downloads//blackjack hearts.png")).resize((30,30))
            bg_photo2 = ImageTk.PhotoImage(bg_image2)
            blackjack_canvas.create_image(850, 60, image=bg_photo2, anchor=tk.NW)
            blackjack_canvas.image = bg_photo2
            blackjack_canvas.images.append(bg_photo2)

        if "Diamonds" in dealertext:
            #bg_image2 = Image.open(("C://Users//VMUser2//Downloads//blackjack diamonds.png")).resize((100,100))
            bg_image2 = Image.open(("C://Users//Jacob//Downloads//blackjack diamonds.png")).resize((30,30))
            bg_photo2 = ImageTk.PhotoImage(bg_image2)
            blackjack_canvas.create_image(850, 60, image=bg_photo2, anchor=tk.NW)
            blackjack_canvas.image = bg_photo2
            blackjack_canvas.images.append(bg_photo2)

    
        if "Clubs" in dealertext:
        
            #bg_image2 = Image.open(("C://Users//VMUser2//Downloads//blackjack clubs.png")).resize((100,100))
            bg_image2 = Image.open(("C://Users//Jacob//Downloads//blackjack clubs.png")).resize((30,30))
            bg_photo2 = ImageTk.PhotoImage(bg_image2)
            blackjack_canvas.create_image(850, 60, image=bg_photo2, anchor=tk.NW)
            blackjack_canvas.image = bg_photo2
            blackjack_canvas.images.append(bg_photo2)


        if "Spades" in dealertext:
            #bg_image2 = Image.open(("C://Users//VMUser2//Downloads//blackjack spades.png")).resize((100,100))
            bg_image2 = Image.open(("C://Users//Jacob//Downloads//blackjack spades.png")).resize((30,30))
            bg_photo2 = ImageTk.PhotoImage(bg_image2)
            blackjack_canvas.create_image(850, 60, image=bg_photo2, anchor=tk.NW)
            blackjack_canvas.image = bg_photo2
            blackjack_canvas.images.append(bg_photo2)



        #making a flag variable so that i can limit user to 5 cards
        limit=2
        cardsvalue=0
        dealercardsvalue=0
        player_cards=[]

        player_cards.append(player_card_value_1)
        player_cards.append(player_card_value_2)

        cardsvalue=sum(player_cards)
        cardsvalue_label_1 = tk.Label(blackjack_frame, text=f"Your score is: {cardsvalue}", font=('Times', 14), bg="white")
        blackjack_canvas.create_window(500, 450, window=cardsvalue_label_1)
        


        if cardsvalue == 21:
            print("blackjack")

            twist_button_inactive = Button(blackjack_frame, text="Twist", width=10, height=5, font=('Times', 14), bg="grey")
            blackjack_canvas.create_window(1400, 250, window=twist_button_inactive)

            stick_button = Button(blackjack_frame, text="Stick", command=lambda: nomorecard(cardsvalue,dealercardsvalue,player_cards), width=10, height=5, font=('Times', 14), bg="white")
            blackjack_canvas.create_window(1400, 350, window=stick_button)
            #special animations when the buttons are hovered over
            stick_button.config(cursor="hand2")
            stick_button.bind("<Enter>", lambda e: stick_button.config(bg="grey"))
            stick_button.bind("<Leave>", lambda e: stick_button.config(bg="white"))

        else:
            twist_button1 = Button(blackjack_frame, text="Twist", command=lambda: getextracard1(cardsvalue,limit), width=10, height=5, font=('Times', 14), bg="white")
            blackjack_canvas.create_window(1400, 250, window=twist_button1)
            #special animations when the buttons are hovered over
            twist_button1.config(cursor="hand2")
            twist_button1.bind("<Enter>", lambda e: twist_button1.config(bg="grey"))
            twist_button1.bind("<Leave>", lambda e: twist_button1.config(bg="white"))


            stick_button = Button(blackjack_frame, text="Stick", command=lambda: nomorecard(cardsvalue,dealercardsvalue,player_cards), width=10, height=5, font=('Times', 14), bg="white")
            blackjack_canvas.create_window(1400, 350, window=stick_button)
            #special animations when the buttons are hovered over
            stick_button.config(cursor="hand2")
            stick_button.bind("<Enter>", lambda e: stick_button.config(bg="grey"))
            stick_button.bind("<Leave>", lambda e: stick_button.config(bg="white"))




    blackjack_frame = tk.Toplevel(bg="#22b14c")
    blackjack_frame.title("Black Jack")
    blackjack_frame.geometry("1000x800")

    #makes the gui auto open on full screen
    blackjack_frame.attributes("-fullscreen", True)


    #need to change VMUser with Jacob when on laptop
    #bg_image1 = ImageTk.PhotoImage(Image.open(("C://Users//Jacob//Downloads//blackjack bg - menu.png")))



    blackjack_canvas=tk.Canvas(blackjack_frame, width=1800, height=1200)
    blackjack_canvas.pack()

    #bg_image1 = Image.open(("C://Users//VMUser2//Downloads//blackjack bg - menu.png")).resize((1600,900))
    bg_image1 = Image.open(("C://Users//Jacob//Downloads//blackjack bg - menu.png")).resize((1600,900))
    bg_photo1 = ImageTk.PhotoImage(bg_image1)
    blackjack_canvas.create_image(0, 0, image=bg_photo1, anchor=tk.NW)
    blackjack_canvas.image = bg_photo1

    #need to change VMUser with Jacob when on laptop
    #bg_image1 = Image.open(r"C://Users//VMUser2//Downloads//blackjack bg - menu.png").resize((1600, 900))
    #bg_photo1 = ImageTk.PhotoImage(bg_image1)  #make it so tkinter can understand so i can go as a label

    # Create a label to display the image
    #image_label = Label(blackjack_frame, image=bg_photo1)
    #image_label.image = bg_photo1  
    #image_label.place(x=0, y=0, relwidth=1, relheight=1)


    play_button1 = Button(blackjack_frame, text="Play!", command=playbuttonclick, width=10, height=3, font=('Times', 24), bg="#22b14c", highlightthickness=0)
    #play_button1.pack()
    blackjack_canvas.create_window(800, 450, window=play_button1)
    #special animations when the buttons are hovered over
    play_button1.config(cursor="hand2")































