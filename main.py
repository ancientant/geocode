"""main module"""
import bowling

if __name__ == "__main__":
    game = bowling.Game()
    game.roll(2)
    game.score()
