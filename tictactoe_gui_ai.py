import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Minimax AI")
        self.board = [' ' for _ in range(10)]
        self.buttons = {}
        self.create_board()
        self.player_symbol = 'X'
        self.ai_symbol = 'O'

    def create_board(self):
        label = tk.Label(self.root, text="Tic Tac Toe with AI", font=('Helvetica', 16))
        label.grid(row=0, column=0, columnspan=3, pady=10)
        for i in range(1, 10):
            button = tk.Button(self.root, text=' ', font=('Helvetica', 20), height=3, width=6,
                               command=lambda i=i: self.player_move(i))
            self.buttons[i] = button
            button.grid(row=(i - 1) // 3 + 1, column=(i - 1) % 3)

    def player_move(self, pos):
        if self.board[pos] == ' ':
            self.insert_letter(self.player_symbol, pos)
            if self.is_winner(self.board, self.player_symbol):
                self.end_game("Congratulations! You won!")
                return
            if self.is_board_full():
                self.end_game("It's a tie!")
                return
            self.root.after(500, self.ai_move)

    def ai_move(self):
        move = self.get_best_move()
        if move != 0:
            self.insert_letter(self.ai_symbol, move)
            if self.is_winner(self.board, self.ai_symbol):
                self.end_game("Computer wins! Better luck next time.")
            elif self.is_board_full():
                self.end_game("It's a tie!")

    def insert_letter(self, letter, pos):
        self.board[pos] = letter
        self.buttons[pos].config(text=letter, state='disabled')

    def is_winner(self, bo, le):
        return (bo[1] == bo[2] == bo[3] == le or
                bo[4] == bo[5] == bo[6] == le or
                bo[7] == bo[8] == bo[9] == le or
                bo[1] == bo[4] == bo[7] == le or
                bo[2] == bo[5] == bo[8] == le or
                bo[3] == bo[6] == bo[9] == le or
                bo[1] == bo[5] == bo[9] == le or
                bo[3] == bo[5] == bo[7] == le)

    def is_board_full(self):
        return self.board.count(' ') <= 1

    def get_best_move(self):
        possible_moves = [x for x, letter in enumerate(self.board) if letter == ' ' and x != 0]
        for let in [self.ai_symbol, self.player_symbol]:
            for i in possible_moves:
                board_copy = self.board[:]
                board_copy[i] = let
                if self.is_winner(board_copy, let):
                    return i
        corners = [i for i in [1, 3, 7, 9] if i in possible_moves]
        if corners:
            return random.choice(corners)
        if 5 in possible_moves:
            return 5
        edges = [i for i in [2, 4, 6, 8] if i in possible_moves]
        if edges:
            return random.choice(edges)
        return 0

    def end_game(self, message):
        for btn in self.buttons.values():
            btn.config(state='disabled')
        messagebox.showinfo("Game Over", message)
        if messagebox.askyesno("Play Again?", "Do you want to play again?"):
            self.reset_game()

    def reset_game(self):
        self.board = [' ' for _ in range(10)]
        for btn in self.buttons.values():
            btn.config(text=' ', state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()