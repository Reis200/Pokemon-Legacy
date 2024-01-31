import pygame
from pygame.constants import FULLSCREEN
from game_manager import GameStateManager
from game_sprites import PowerUp
from sys import exit

pygame.init()

class Game:
  def __init__(self):
    self.screen = pygame.display.set_mode((800, 400), pygame.RESIZABLE)

    pygame.display.set_caption('Pokemon Legacy')
    icon = pygame.image.load("power_up/ultimate.png").convert_alpha()
    pygame.display.set_icon(icon)

    self.clock = pygame.time.Clock()
    self.running = True

    self.game_state_manager = GameStateManager()

    # power_ups
    self.power_up_sprite_group = pygame.sprite.Group()

    self.power_up_event = pygame.USEREVENT + 1
    pygame.time.set_timer(self.power_up_event,25000)

  def reset(self):
    if self.game_state_manager.game_over:

      self.game_state_manager = GameStateManager()

      self.game_state_manager.game_over = False

      # power_ups
      self.power_up_sprite_group = pygame.sprite.Group()

      self.power_up_event = pygame.USEREVENT + 1
      pygame.time.set_timer(self.power_up_event, 25000)

  def run(self):
    while self.running:

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        if event.type == pygame.VIDEORESIZE:
          self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        if event.type == self.power_up_event and self.game_state_manager.game_state.menu_active:
            self.power_up_sprite_group.add(PowerUp())


      self.game_state_manager.update(self.power_up_sprite_group)

      if self.game_state_manager.game_state.menu_active:
        self.power_up_sprite_group.draw(self.screen)
        self.power_up_sprite_group.update([self.game_state_manager.player1,self.game_state_manager.player2])
      else: self.power_up_sprite_group.empty()

      if self.game_state_manager.game_over: self.reset()

      pygame.display.update()
      self.clock.tick(60)


if __name__ == '__main__':
  game = Game()
  game.run()

# https://www.pokecommunity.com/threads/pokemon-rpgm-mv-ultimate-resource-pack-v0-97-06-20-20-actual-progress.407655/