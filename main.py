import pygame
from player import Player1, Player2
from game_manager import GameStateManager
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
    self.font = pygame.font.Font(None, 50)

    self.player1 = Player1("Charmander.png",(700,360))
    self.player2 = Player2("Charmander2.png",(100,360))

    

    self.game_sprites = [self.player1,self.player2]

    self.game_state_manager = GameStateManager(self.game_sprites)
    
  def reset(self):
    if self.game_state_manager.game_over:
      self.player1 = Player1("Charmander.png", (700, 360))
      self.player2 = Player2("Charmander2.png", (100, 360))

      self.game_sprites = [self.player1, self.player2]

      self.game_state_manager = GameStateManager(self.game_sprites)

      self.game_state_manager.game_over = False

  def run(self):
    while self.running:

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()

      self.game_state_manager.update()

      if self.game_state_manager.game_over: self.reset()
      
      pygame.display.update()
      self.clock.tick(60)
  

if __name__ == '__main__':
  game = Game()
  game.run()

# https://www.pokecommunity.com/threads/pokemon-rpgm-mv-ultimate-resource-pack-v0-97-06-20-20-actual-progress.407655/