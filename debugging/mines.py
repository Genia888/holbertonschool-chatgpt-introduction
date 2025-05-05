#!/usr/bin/python3
import random
import os

def clear_screen():
    """Efface l'écran du terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        """Initialise le jeu Minesweeper."""
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        """Affiche le plateau de jeu."""
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        """Compte les mines adjacentes à la case donnée."""
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        """Révèle une case. Si la case contient une mine, le jeu se termine."""
        if (y * self.width + x) in self.mines:
            return False
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def play(self):
        """Lance le jeu et gère les entrées de l'utilisateur."""
        while True:
            self.print_board()
            try:
                # Entrée des coordonnées avec vérification
                x = int(input("Enter x coordinate (0 to {}): ".format(self.width - 1)))
                y = int(input("Enter y coordinate (0 to {}): ".format(self.height - 1)))

                if x < 0 or x >= self.width or y < 0 or y >= self.height:
                    print("Coordinates out of bounds. Try again.")
                    continue

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

            # Vérification de la victoire (si toutes les cases sans mine sont révélées)
            if self.check_victory():
                self.print_board(reveal=True)
                print("Congratulations! You've won!")
                break

    def check_victory(self):
        """Vérifie si toutes les cases sans mine ont été révélées."""
        for y in range(self.height):
            for x in range(self.width):
                if (y * self.width + x) not in self.mines and not self.revealed[y][x]:
                    return False
        return True

if __name__ == "__main__":
    game = Minesweeper()
    game.play()

