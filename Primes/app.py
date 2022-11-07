import pygame as pg
import ulamspiral as us
import sacksspiral as ss

class App:
    def __init__(self, res=(700, 500)):
        pg.init()
        self.WIDTH, self.HEIGHT = res
        self.screen = pg.display.set_mode(res)
        self.clock = pg.time.Clock()
        self.array_size = 1000

        # self.spiral_array = us.UlamSpiral(size=self.array_size).get_spiral()
        self.spiral_array = ss.SacksSpiral(size=self.array_size).get_spiral()

        self.spiral = pg.surfarray.make_surface(self.spiral_array)
        self.speed = 5
        self.array_size *= 7
        self.spiral_surface = pg.transform.scale(self.spiral, (self.array_size, self.array_size))
        self.get_pos()

    def get_pos(self):
        self.pos = pg.math.Vector2(self.WIDTH // 2 - self.array_size // 2,
                                   self.HEIGHT // 2 - self.array_size // 2)

    def draw(self):
        self.screen.fill('black')
        self.screen.blit(self.spiral_surface, self.pos)

    def scale(self):
        self.spiral_surface = pg.transform.scale(self.spiral, (self.array_size, self.array_size))

    def control(self):
        pressed_keys = pg.key.get_pressed()
        if pressed_keys[pg.K_a]:
            self.pos[0] += self.speed
        if pressed_keys[pg.K_d]:
            self.pos[0] -= self.speed
        if pressed_keys[pg.K_w]:
            self.pos[1] += self.speed
        if pressed_keys[pg.K_s]:
            self.pos[1] -= self.speed
        if pressed_keys[pg.K_UP]:
            self.array_size *= 1.1
            self.array_size = min(self.array_size, 20000)
            self.scale()
            self.get_pos()
        if pressed_keys[pg.K_DOWN]:
            self.array_size //= 1.1
            self.scale()
            self.get_pos()

    def update(self):
        pg.display.flip()
        self.clock.tick(60)

    def run(self):
        while True:
            [exit() for i in pg.event.get() if i.type == pg.QUIT
             or (i.type == pg.KEYDOWN and i.key == pg.K_ESCAPE)]
            self.control()
            self.update()
            self.draw()