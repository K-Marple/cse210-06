from constants import *
from game.cast.sound import Sound
from game.script.action import Action
from game.cast.image import Image
from game.cast.point import Point


class CollideTankAction(Action):

    def __init__(self, physics, audio, video):
        self._physics = physics
        self._audio = audio
        self._video = video

    def execute(self, cast, script, callback):
        bullets = cast.get_first_actor(BULLET_GROUP)
        barricades = cast.get_actors(BARRICADE_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)

        if bullets != []:
            for bullet in bullets:
                bullet_body = bullet.get_body()

                for barricade in barricades:
                    barricade_body = barricade.get_body()

                    if self._physics.has_collided(bullet_body, barricade_body):
                        if bullet in bullets:
                            cast.remove_actor(BULLET_GROUP, bullet)
                        sound = Sound(FIRE_SOUND)
                        self._audio.play_sound(sound)
                        hits = barricade.get_hits()
                        stats.add_hits(hits)
                        points = barricade.get_points()
                        stats.add_points(points)
                        old_image = barricade.get_image()
                        old_image_file = old_image.get_filename()
                        size = barricade_body.get_size()
                        next_image, next_size, remove = self._handle_barricade(old_image)
                        new_image = Image(next_image)
                        barricade.set_image(new_image)
                        barricade_body.set_size(next_size)
                        image = barricade.get_image()
                        position = barricade_body.get_position()
                        self._video.draw_image(image, position)

                        if bullet in bullets:
                            if remove == True:
                                cast.remove_actor(BULLET_GROUP, bullet)
                                cast.remove_actor(BARRICADE_GROUP, barricade)

    def _handle_barricade(self, image, size, remove=False):
        if image == ROCK_BARRICADE_IMAGE:
            new_image = SAND_BARRICADE_IMAGE
            new_size = Point(SAND_BARRICADE_WIDTH, SAND_BARRICADE_HEIGHT)
        elif image == SAND_BARRICADE_IMAGE:
            new_image = DIRT_BARRICADE_IMAGE
            new_size = Point(DIRT_BARRICADE_WIDTH, DIRT_BARRICADE_HEIGHT)
        elif image == DIRT_BARRICADE_IMAGE:
            new_image = GRASS_BARRICADE_IMAGE
            new_size = Point(GRASS_BARRICADE_WIDTH, GRASS_BARRICADE_HEIGHT)
        else:
            new_image = image
            new_size = size
            remove = True
        return new_image, new_size, remove