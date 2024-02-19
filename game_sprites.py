import pygame
from database import title_font, game_font
from random import choice,randint


class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()

        self.power_up_dict = {"ultimate": pygame.transform.rotozoom(pygame.image.load("power_up/ultimate.png").convert_alpha(),0,1.85),
                              "power": pygame.transform.rotozoom(pygame.image.load("power_up/power.png").convert_alpha(),0,1.85),
                              "speed": pygame.transform.rotozoom(pygame.image.load("power_up/speed.png").convert_alpha(),0,1.85)}
        self.image = self.power_up_dict[choice(["ultimate","power","speed"])]
        self.rect = self.image.get_rect(center=(randint(self.screen.get_width() * 0.125, self.screen.get_width() * 0.875), randint(-300, -50)))
        self.name = [key for key in self.power_up_dict.keys() if self.power_up_dict[key] == self.image]


    def fall(self):
        if self.rect.top <= self.screen.get_height() + 80:
            self.rect.y += 10
        if self.rect.top >= self.screen.get_height() + 80:
            self.kill()

    def update(self,players):
        self.fall()
        self.check_collision(players)

    def check_collision(self,players):
        if self.rect.colliderect(players[0].rect):
            players[0].power_up = self.name[0]
            players[0].activate_power_up_state()
            self.kill()
        if self.rect.colliderect(players[1].rect):
            players[1].power_up = self.name[0]
            players[1].activate_power_up_state()
            self.kill()

