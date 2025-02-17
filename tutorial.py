import sqlite3
import time
import tkinter
from tkinter import *
import tkinter as tk


def tutorial():

    def blackjack():

        blackjack_button.destroy()

        #text to show how toplay blackjack
        tutorialtext=tk.Label(tutorial_frame, text="Blackjack is a card game where the goal is to get as close to 21 as possible without going over", font=('Times', 24))
        tutorialtext.pack(pady=5)

        tutorialtext1=tk.Label(tutorial_frame, text="Each player, including the dealer, is dealt two cards", font=('Times', 24))
        tutorialtext1.pack(pady=5)

        tutorialtext2=tk.Label(tutorial_frame, text="Numbered cards are worth their face value, face cards (Jack, Queen, and King) are worth 10, and Aces can count as either 1 or 11", font=('Times', 24))
        tutorialtext2.pack(pady=5)

        tutorialtext3=tk.Label(tutorial_frame, text="Players can choose to 'Twist' (take another card) or 'Stick' (keep their current total). ", font=('Times', 24))
        tutorialtext3.pack(pady=5)

        tutorialtext4=tk.Label(tutorial_frame, text="If a player’s total exceeds 21, they bust and lose automatically. ", font=('Times', 24))
        tutorialtext4.pack(pady=5)

        tutorialtext5=tk.Label(tutorial_frame, text="After the players finish, the dealer reveals their hidden card and must continue drawing until they reach at least 17. ", font=('Times', 24))
        tutorialtext5.pack(pady=5)

        tutorialtext6=tk.Label(tutorial_frame, text="The player wins if they have a higher total than the dealer without busting or if the dealer busts. If both have the same total, the game is a draw. ", font=('Times', 24))
        tutorialtext6.pack(pady=5)


    tutorial_frame = tk.Toplevel()
    tutorial_frame.title("Tutorial")
    tutorial_frame.geometry("1000x800")

    #makes the gui auto open on full screen
    tutorial_frame.attributes("-fullscreen", True)

    #game button on menu screen
    blackjack_button = Button(tutorial_frame, command=blackjack, text="Blackjack", width=20, height=10, font=('Times', 14), bg="white")
    blackjack_button.place(x=100, y=100)
    #special animations when the buttons are hovered over
    blackjack_button.config(cursor="hand2")
    blackjack_button.bind("<Enter>", lambda e: blackjack_button.config(bg="grey"))
    blackjack_button.bind("<Leave>", lambda e: blackjack_button.config(bg="white"))

    