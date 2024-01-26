import pygame
from database import title_font, game_font
from random import choice,randint


class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.power_up_dict = {"ultimate": pygame.transform.rotozoom(pygame.image.load("power_up/ultimate.png").convert_alpha(),0,0.75),
                              "power": pygame.transform.rotozoom(pygame.image.load("power_up/power.png").convert_alpha(),0,0.75),
                              "speed": pygame.transform.rotozoom(pygame.image.load("power_up/speed.png").convert_alpha(),0,0.75)}
        self.image = self.power_up_dict[choice(["ultimate","power","speed"])]
        self.rect = self.image.get_rect(center=(randint(200, 600), randint(-300, -50)))
        self.name = [key for key in self.power_up_dict.keys() if self.power_up_dict[key] == self.image]

        self.screen = pygame.display.get_surface()


    def fall(self):
        if self.rect.top <= 470:
            self.rect.y += 5
        if self.rect.top >= 470:
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

