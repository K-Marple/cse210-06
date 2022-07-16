import csv
from constants import *
from game.cast.animation import Animation
from game.cast.bullet import Bullet
from game.cast.body import Body
from game.cast.walls import Walls
from game.cast.image import Image
from game.cast.label import Label
from game.cast.point import Point
from game.cast.tank import Tank
from game.cast.stats import Stats
from game.cast.text import Text

from game.script.change_scene_action import ChangeSceneAction
from game.script.check_over_action import CheckOverAction
from game.script.collide_borders_action import CollideBordersAction
from game.script.collide_walls_action import CollideWallsAction
from game.script.collide_tank_action import CollidTankAction
from game.script.control_tank_action import ControlTankAction
from game.script.draw_bullet_action import DrawBulletAction
from game.script.draw_walls_action import DrawWallsAction
from game.script.draw_dialog_action import DrawDialogAction
from game.script.draw_hud_action import DrawHudAction
from game.script.draw_tank_action import DrawTankAction
from game.script.end_drawing_action import EndDrawingAction
from game.script.initialize_devices_action import InitializeDevicesAction
from game.script.load_assets_action import LoadAssetsAction
from game.script.move_bullet_action import MoveBulletAction
from game.script.move_tank_action import MoveTankAction
from game.script.play_sound_action import PlaySoundAction
from game.script.release_devices_action import ReleaseDevicesAction
from game.script.start_drawing_action import StartDrawingAction
from game.script.timed_change_scene_action import TimedChangeSceneAction
from game.script.unload_assets_action import UnloadAssetsAction

from game.services.raylib.raylib_audio import RaylibAudio
from game.services.raylib.raylib_keyboard import RaylibKeyboard
from game.services.raylib.raylib_physics import RaylibPhysics
from game.services.raylib.raylib_video import RaylibVideo


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""

    AUDIO = RaylibAudio()
    KEYBOARD = RaylibKeyboard()
    PHYSICS = RaylibPhysics()
    VIDEO = RaylibVideo()

    CHECK_OVER_ACTION = CheckOverAction()
    COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS, AUDIO)
    COLLIDE_WALLS_ACTION = CollideWallsAction(PHYSICS, AUDIO)
    COLLIDE_TANK_ACTION = CollidTankAction(PHYSICS, AUDIO)
    CONTROL_TANK_ACTION = ControlTankAction(KEYBOARD)
    DRAW_BULLET_ACTION = DrawBulletAction(VIDEO)
    DRAW_WALLS_ACTION = DrawWallsAction(VIDEO)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO)
    DRAW_TANK_ACTION = DrawTankAction(VIDEO)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO, VIDEO)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO, VIDEO)
    MOVE_BULLET_ACTION = MoveBulletAction()
    MOVE_TANK_ACTION = MoveTankAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO, VIDEO)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO, VIDEO)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:
            self._prepare_game_over(cast, script)

    # SCENE METHODS

    def _prepare_new_game(self, cast, script):
        self._add_stats(cast)
        self._add_level(cast)
        self._add_lives(cast)
        self._add_score(cast)
        self._add_bullet(cast)
        self._add_walls(cast)
        self._add_tank(cast)
        self._add_dialog(cast, ENTER_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)

    def _prepare_next_level(self, cast, script):
        self._add_bullet(cast)
        self._add_walls(cast)
        self._add_tank(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO, WELCOME_SOUND))

    def _prepare_try_again(self, cast, script):
        self._add_bullet(cast)
        self._add_tank(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        self._activate_bullet(cast)
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_TANK_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        self._add_bullet(cast)
        self._add_tank(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # CAST METHODS

    def _activate_bullet(self, cast):
        bullet = cast.get_first_actor(BULLET_GROUP)
        bullet.release()

    def _add_bullet(self, cast):
        cast.clear_actors(BULLET_GROUP)
        x = CENTER_X - BULLET_WIDTH / 2
        y = SCREEN_HEIGHT - TANK_HEIGHT - BULLET_HEIGHT
        position = Point(x, y)
        size = Point(BULLET_WIDTH, BULLET_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BULLET_IMAGE)
        bullet = Bullet(body, image, True)
        cast.add_actors(BULLET_GROUP, bullet)

    def _add_walls(self, cast):
        cast.clear_actors(WALL_GROUP)

        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level() % BASE_LEVELS
        filename = LEVEL_FILE.format(level)

        with open(filename, 'r') as file:
            reader = csv.reader(file, skipinitialspace=True)

            for r, row in enumerate(reader):
                for c, column in enumerate(row):
                    x = FIELD_LEFT + c * WALL_WIDTH
                    y = FIELD_TOP + r * WALL_HEIGHT
                    color = column[0]
                    frames = int(column[1])
                    points = WALL_POINTS

                    if frames == 1:
                        points *= 2

                    position = Point(x, y)
                    size = Point(WALL_WIDTH, WALL_HEIGHT)
                    velocity = Point(0, 0)
                    images = WALL_IMAGES[color][0:frames]

                    body = Body(position, size, velocity)
                    animation = Animation(images, WALL_RATE, WALL_DELAY)

                    wall = Walls(body, animation, points)
                    cast.add_actor(WALL_GROUP, wall)

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_tank(self, cast):
        cast.clear_actors(TANK_GROUP)
        x = CENTER_X - TANK_WIDTH / 2
        y = SCREEN_HEIGHT - TANK_HEIGHT
        position = Point(x, y)
        size = Point(TANK_WIDTH, TANK_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(TANK_IMAGES, TANK_RATE)
        tank = Tank(body, animation)
        cast.add_actor(TANK_GROUP, tank)

    # SCRIPT METHODS

    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)

    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_BULLET_ACTION)
        script.add_action(OUTPUT, self.DRAW_WALLS_ACTION)
        script.add_action(OUTPUT, self.DRAW_TANK_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)
        
    def _add_release_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)

    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)

    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_BULLET_ACTION)
        script.add_action(UPDATE, self.MOVE_TANK_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_WALLS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_TANK_ACTION)
        script.add_action(UPDATE, self.MOVE_TANK_ACTION)
        script.add_aciton(UPDATE, self.CHECK_OVER_ACTION)