from app.components.game import Game

if __name__ == "__main__":
    player_name = input("Enter the Dino name to Start: ")
    game = Game(player_name)
    game.run()
    print("hello there...")
