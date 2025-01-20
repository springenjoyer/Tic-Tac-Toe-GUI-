import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")

        self.current_player = "X"
        self.board = [""] * 9

        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text="", font=('Arial', 20), width=5, height=2,
                                   command=lambda row=i, col=j: self.button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def button_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Victory!", f"Player {self.current_player} won!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Draw!", "The game is over in a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]  # diagonals
        ]

        for combo in win_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ""):
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()
