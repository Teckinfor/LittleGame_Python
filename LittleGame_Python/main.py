from gameclass import Board
from gameclass import Player

joueur = Player("Julien")
plateau = Board(joueur)
joueur.board = plateau


plateau.play_game()