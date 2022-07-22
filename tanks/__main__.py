import pyray
from game.director.director import Director
from game.director.scene_manager import SceneManager


def main():
    director = Director(SceneManager.VIDEO)
    director.start_game()

if __name__ == "__main__":
    main()