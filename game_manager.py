import pygame
from random import choice
from database import title_font, game_font, character_set_player1, character_set_player2


class GameStateManager:

  def __init__(self, game_sprites=[]):

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

  def update(self,power_up_sprite_group):
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

        for sprite in power_up_sprite_group.sprites():
          if sprite.rect.colliderect(self.game_sprites[0].rect):
            # self.game_sprites[0].power_up
            pass

        for object in self.game_sprites:
          if object.health <= 0:
            self.format_game()


class StartMenu:

  def __init__(self):

    #menu state
    self.menu_active = True

    self.in_about_section = False

    #other properties

    bg_list = [
        'background/start_menu_bg1.gif', 'background/start_menu_bg2.png',
        'background/start_menu_bg3.png'
    ]
    self.background = pygame.image.load(choice(bg_list)).convert()
    self.background_rect = self.background.get_rect(topleft=(0, 0))

    self.screen = pygame.display.get_surface()

    self.title = title_font.render("Pokemon Legacy", False, (0, 0, 0))
    self.title_rect = self.title.get_rect(center=(400, 100))

    self.play_button = pygame.transform.rotozoom(
        pygame.image.load("buttons/play_button.png").convert_alpha(), 0, 2)
    self.play_button_rect = self.play_button.get_rect(center=(400, 170))

    self.about_button = pygame.transform.rotozoom(
        pygame.image.load("buttons/about_button.png").convert_alpha(), 0, 2.5)
    self.about_button_rect = self.about_button.get_rect(center=(400, 330))

    self.description_button = pygame.transform.rotozoom(
        pygame.image.load(
            "buttons/empty_description_area.png").convert_alpha(), 0, 4)
    self.description_button_rect = self.description_button.get_rect(
        center=(400, 200))

    # credits

    self.in_credits_section = False

    self.credits_button = pygame.transform.rotozoom(pygame.image.load("buttons/credits_button.png").convert_alpha(),0,2)
    self.credits_button_rect = self.credits_button.get_rect(center = (400,250))

    self.credit_description = pygame.transform.rotozoom(pygame.image.load("buttons/empty_description_area.png").convert_alpha(), 0, 4)
    self.credit_description_rect = self.credit_description.get_rect(center=(400, 200))

    self.credit_text1 = game_font.render(
      'A pokemon game made after a request...', False, (255, 255, 255))
    self.credit_text1_rect = self.credit_text1.get_rect(center=(400, 100))

    self.credit_text2 = game_font.render(
      'two programming bros combined to build', False, (255, 255, 255))
    self.credit_text2_rect = self.credit_text2.get_rect(center=(400, 140))

    self.credit_text3 = game_font.render(
      'where blood, sweat, tears and hours of work', False, (255, 255, 255))
    self.credit_text3_rect = self.credit_text3.get_rect(center=(400, 180))

    self.credit_text4 = game_font.render(
      'for you to enjoy the nostalgic pixel gameplay', False, (255, 255, 255))
    self.credit_text4_rect = self.credit_text4.get_rect(center=(400, 220))

    self.credit_text5 = game_font.render(
      'Made by:', False, (255, 255, 255))
    self.credit_text5_rect = self.credit_text5.get_rect(center=(400, 260))

    self.credit_text6 = game_font.render(
      'Programming Legend aka Vivek Ajesh...', False, (255, 255, 255))
    self.credit_text6_rect = self.credit_text6.get_rect(center=(400, 300))

    self.credit_text7 = game_font.render(
      'Reis200 aka Behlul Zengin', False, (255, 255, 255))
    self.credit_text7_rect = self.credit_text7.get_rect(center=(400, 330))


    #about section

    self.go_back_button = pygame.transform.rotozoom(pygame.image.load("buttons/exit_button.png").convert_alpha(),0,2)
    self.go_back_button_rect = self.go_back_button.get_rect(center = (750,350))

    self.about_text1 = game_font.render(
        'In Pokemon Legacy, two players engage in a', False, (255, 255, 255))
    self.about_text1_rect = self.about_text1.get_rect(center=(400, 130))

    self.about_text2 = game_font.render(
        'thrilling 2d pixelated battles set in a', False, (255, 255, 255))
    self.about_text2_rect = self.about_text2.get_rect(center=(400, 150))

    self.about_text3 = game_font.render(
        'nostalgic world. Trainers choose their Pokemon,', False, (255, 255, 255))
    self.about_text3_rect = self.about_text3.get_rect(center=(400, 170))

    self.about_text4 = game_font.render(
        'strategise moves and compete for victory.', False, (255, 255, 255))
    self.about_text4_rect = self.about_text4.get_rect(center=(400, 190))

    self.about_text5 = game_font.render(
        'As they explore the landscape, each duel is a', False, (255, 255, 255))
    self.about_text5_rect = self.about_text5.get_rect(center=(400, 210))

    self.about_text6 = game_font.render(
        'test of skill and strategy, shaping the', False, (255, 255, 255))
    self.about_text6_rect = self.about_text6.get_rect(center=(400, 230))

    self.about_text7 = game_font.render(
        'legacy of their rivalry. ', False, (255, 255, 255))
    self.about_text7_rect = self.about_text7.get_rect(center=(400, 250))

  def display_menu(self):
    self.screen.blit(self.background, self.background_rect)

    if not self.in_about_section and not self.in_credits_section:
      self.screen.blit(self.title, self.title_rect)
      self.screen.blit(self.play_button, self.play_button_rect)
      self.screen.blit(self.about_button, self.about_button_rect)
      self.screen.blit(self.credits_button,self.credits_button_rect)
    if self.in_about_section:
      self.screen.blit(self.description_button, self.description_button_rect)
      self.screen.blit(self.about_text1, self.about_text1_rect)
      self.screen.blit(self.about_text2, self.about_text2_rect)
      self.screen.blit(self.about_text3, self.about_text3_rect)
      self.screen.blit(self.about_text4, self.about_text4_rect)
      self.screen.blit(self.about_text5, self.about_text5_rect)
      self.screen.blit(self.about_text6, self.about_text6_rect)
      self.screen.blit(self.about_text7, self.about_text7_rect)
      self.screen.blit(self.go_back_button,self.go_back_button_rect)
    if self.in_credits_section:
      self.screen.blit(self.credit_description, self.credit_description_rect)
      self.screen.blit(self.credit_text1, self.credit_text1_rect)
      self.screen.blit(self.credit_text2, self.credit_text2_rect)
      self.screen.blit(self.credit_text3, self.credit_text3_rect)
      self.screen.blit(self.credit_text4, self.credit_text4_rect)
      self.screen.blit(self.credit_text5, self.credit_text5_rect)
      self.screen.blit(self.credit_text6, self.credit_text6_rect)
      self.screen.blit(self.credit_text7, self.credit_text7_rect)
      self.screen.blit(self.go_back_button, self.go_back_button_rect)


  def check_collision(self):
    if pygame.mouse.get_pressed()[0]:
      if self.play_button_rect.collidepoint(pygame.mouse.get_pos()):
        self.menu_active = False
      if self.about_button_rect.collidepoint(pygame.mouse.get_pos()):
        self.in_about_section = True
      if self.go_back_button_rect.collidepoint(pygame.mouse.get_pos()):
        self.in_about_section = False
        self.in_credits_section = False
      if self.credits_button_rect.collidepoint(pygame.mouse.get_pos()):
        self.in_credits_section = True

  def update(self):
    self.display_menu()
    self.check_collision()


class CharacterMenu:
  def __init__(self):

    # menu state
    self.menu_active = False

    bg_list = [
        'background/ocean.jpg', 'background/sunrise.jpg',
        'background/LateEvening.png', "background/sunny.jpg"
    ]
    self.background = pygame.image.load(choice(bg_list)).convert()
    self.background_rect = self.background.get_rect(topleft=(0, 0))

    self.screen = pygame.display.get_surface()

    self.initilise_character_selection_player1()
    self.initilise_character_selection_player2()

  def initilise_character_selection_player1(self):
    self.game_characters1 = {}
    for key, item in character_set_player1.items():
      image = item["image"].convert_alpha()
      rect = image.get_rect(center = item["display_pos"])
      self.game_characters1[image] = rect

  def initilise_character_selection_player2(self):
    self.game_characters2 = {}
    for key, item in character_set_player2.items():
      image = item["image"].convert_alpha()
      rect = image.get_rect(center = item["display_pos"])
      self.game_characters2[image] = rect

  def display_characters(self):
    for image, rect in self.game_characters1.items():
      self.screen.blit(image,rect)
    for image, rect in self.game_characters2.items():
      self.screen.blit(image,rect)




  def display_background(self):
    self.screen.blit(self.background, self.background_rect)

  def check_collision(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_g]:
      self.menu_active = False

  def update(self):
    self.check_collision()
    self.display_background()

    self.display_characters()




class GameState:
  def __init__(self):

    # menu state
    self.menu_active = False

    bg_list = [
      'background/ocean.jpg', 'background/sunrise.jpg',
      'background/LateEvening.png', "background/sunny.jpg"
    ]
    self.background = pygame.image.load(choice(bg_list)).convert()
    self.background_rect = self.background.get_rect(topleft=(0, 0))

    self.screen = pygame.display.get_surface()

  def display_background(self):
    self.screen.blit(self.background, self.background_rect)

  def update(self):
    self.display_background()
