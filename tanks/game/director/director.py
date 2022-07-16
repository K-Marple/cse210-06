from constants import *
from game.cast.cast import Cast
from game.director.scene_manager import SceneManager
from game.script.action_callback import ActionCallback
from game.script.script import Script


class Director(ActionCallback):
    """A person who directs the game."""

    def __init__(self, video):
        """Constructs a new Director using the specified video service.
        
        Args:
            video (Video): an instance of Video.
        """
        self._video = video
        self._cast = Cast()
        self._script = Script()
        self._scene_manager = SceneManager()

    def on_next(self, scene):
        """Overridden ActionCallback method transitions to next scene.
        
        Args:
            A number representing the next scene to transition to.
        """
        self._scene_manager.prepare_scene(scene, self._cast, self._script)

    def start_game(self):
        """Starts the game. Runs the main game loop."""
        self.on_next(NEW_GAME)
        self._execute_actions(INITIALIZE)
        self._execute_actions(LOAD)
        while self._video.is_window_open():
            self._execute_actions(INPUT)
            self._execute_actions(UPDATE)
            self._execute_actions(OUTPUT)
        self._execute_actions(UNLOAD)
        self._execute_actions(RELEASE)

    def _execute_actions(self, group):
        """Calls execute for each action in the given group.
        
        Args:
            group (str): the action group name.
            cast (Cast): the cast of actors.
            script (Script): the script of actions.
        """
        actions = self._script.get_actions(group)
        for action in actions:
            action.execute(self._cast, self._script, self)