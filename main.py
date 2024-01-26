import pygame
from player import Player1, Player2
from game_manager import GameStateManager
from database import character_set_player1,character_set_player2
from game_sprites import PowerUp
from sys import exit

pygame.init()

class Game:
  def __init__(self):
    self.screen = pygame.display.set_mode((800, 400))

    pygame.display.set_caption('Pokemon Legacy')
    icon = pygame.image.load("pikachu.png").convert_alpha()
    pygame.display.set_icon(icon)

    self.clock = pygame.time.Clock()
    self.running = True

    self.player1 = Player1("Charmander.png",0,0,0,(700,360))
    self.player2 = Player2("Charmander2.png",0,0,0,(100,360))

    self.game_sprites = [self.player1,self.player2]

    self.game_state_manager = GameStateManager(self.game_sprites)

    # power_ups
    self.power_up_sprite_group = pygame.sprite.Group()

    self.power_up_event = pygame.USEREVENT + 1
    pygame.time.set_timer(self.power_up_event,10000)

  def reset(self):
    if self.game_state_manager.game_over:
      self.player1 = Player1("Charmander.png", (700, 360))
      self.player2 = Player2("Charmander2.png", (100, 360))

      self.game_sprites = [self.player1, self.player2]

      self.game_state_manager = GameStateManager(self.game_sprites)

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
        if event.type == self.power_up_event and self.game_state_manager.game_state.menu_active:
            self.power_up_sprite_group.add(PowerUp())


      self.game_state_manager.update(self.power_up_sprite_group)

      self.power_up_sprite_group.draw(self.screen)
      self.power_up_sprite_group.update(self.game_state_manager.game_sprites)

      if self.game_state_manager.game_over: self.reset()
      
      pygame.display.update()
      self.clock.tick(60)


if __name__ == '__main__':
  game = Game()
  game.run()

# https://www.pokecommunity.com/threads/pokemon-rpgm-mv-ultimate-resource-pack-v0-97-06-20-20-actual-progress.407655/