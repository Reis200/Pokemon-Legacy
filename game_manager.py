import pygame
from random import choice
from database import title_font, game_font


class GameStateManager:
  def __init__(self,game_sprites=[]):

    self.game_sprites = game_sprites
    

    self.start_menu = StartMenu()
    self.character_menu = CharacterMenu()
    self.game_state = GameState()

    self.game_over = False

  def format_game(self):
    self.start_menu = StartMenu()
    self.character_menu = CharacterMenu()
    self.game_state = GameState()

    self.game_over = True

  def update(self):
    if not self.game_over:
      if self.start_menu.menu_active:
        self.start_menu.update()
        if not self.start_menu.menu_active:
          self.character_menu.menu_active = True

      if self.character_menu.menu_active:
        self.character_menu.update()
        if not self.character_menu.menu_active:
          self.game_state.menu_active = True


      if self.game_state.menu_active:
        self.game_state.update()
        self.game_sprites[0].update(self.game_sprites[1])
        self.game_sprites[1].update(self.game_sprites[0])

        for object in self.game_sprites:
          if object.health <= 0:
            self.format_game()

class StartMenu:
  def __init__(self):

    #menu state
    self.menu_active = True

    self.in_about_section = False

    #other properties

    bg_list = ['background/ocean.jpg', 'background/sunrise.jpg','background/LateEvening.png']
    self.background = pygame.image.load(choice(bg_list)).convert()
    self.background_rect = self.background.get_rect(topleft = (0,0))

    self.screen = pygame.display.get_surface()



    self.title = title_font.render("Pokemon Legacy",False,(0,0,0))
    self.title_rect = self.title.get_rect(center = (400,100))

    self.play_button = pygame.transform.rotozoom(pygame.image.load("buttons/play_button.png").convert_alpha(),0,2)
    self.play_button_rect = self.play_button.get_rect(center = (400,170))

    self.about_button = pygame.transform.rotozoom(pygame.image.load("buttons/about_button.png").convert_alpha(), 0, 2.5)
    self.about_button_rect = self.about_button.get_rect(center=(400, 250))

    self.description_button = pygame.transform.rotozoom(pygame.image.load("buttons/empty_description_area.png").convert_alpha(), 0, 4)
    self.description_button_rect = self.description_button.get_rect(center=(400, 200))
    

  def display_menu(self):
    self.screen.blit(self.background,self.background_rect)

    if not self.in_about_section:
      self.screen.blit(self.title, self.title_rect)
      self.screen.blit(self.play_button, self.play_button_rect)
      self.screen.blit(self.about_button, self.about_button_rect)
    if self.in_about_section:
      self.screen.blit(self.description_button,self.description_button_rect)


  def check_collision(self):
    if pygame.mouse.get_pressed()[0]:
      if self.play_button_rect.collidepoint(pygame.mouse.get_pos()):
        self.menu_active = False
      if self.about_button_rect.collidepoint(pygame.mouse.get_pos()):
        self.in_about_section = True


  def update(self):
    self.display_menu()
    self.check_collision()



class AboutMenu:
  def __init__(self):

    # menu state
    self.menu_active = False

    bg_list = ['background/ocean.jpg', 'background/sunrise.jpg',
               'background/LateEvening.png']
    self.background = pygame.image.load(choice(bg_list)).convert()
    self.background_rect = self.background.get_rect(topleft=(0, 0))

    self.screen = pygame.display.get_surface()

    # character images frames

  def display(self):
    self.screen.blit(self.background,self.background_rect)


  def check_collision(self):
    pass

  def update(self):
    self.display()


class CharacterMenu:
  def __init__(self):

    # menu state
    self.menu_active = False

    bg_list = ['background/ocean.jpg', 'background/sunrise.jpg',
               'background/LateEvening.png']
    self.background = pygame.image.load(choice(bg_list)).convert()
    self.background_rect = self.background.get_rect(topleft=(0, 0))

    self.screen = pygame.display.get_surface()

    # character images frames

  def display(self):
    self.screen.blit(self.background,self.background_rect)


  def check_collision(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_x]:
      self.menu_active = False

  def update(self):
    self.check_collision()
    self.display()
    

class GameState(CharacterMenu):
  def update(self):
    self.display()
  
