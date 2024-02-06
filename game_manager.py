import pygame
from player import Player1,Player2
from random import choice
from database import title_font, game_font, menu_font, character_set_player1, character_set_player2

pygame.mixer.init()

class MusicManager:
  def __init__(self):
    self.title_music = pygame.mixer.Sound("music/xDeviruchi - Title Theme .wav")
    self.game_music1 = pygame.mixer.Sound("music/xDeviruchi - And The Journey Begins .wav")
    self.game_music2 = pygame.mixer.Sound("music/xDeviruchi - Decisive Battle.wav")
    self.game_music3 = pygame.mixer.Sound("music/xDeviruchi - Prepare for Battle! .wav")

    self.music_dict = {"title":self.title_music,"game1":self.game_music1,"game2":self.game_music2,"game3":self.game_music3}

    self.current_music = ""

  def set_music(self,music_name):
    self.current_music = music_name

  def randomize_play_game_music(self):
    self.play_music(choice(["game1","game2","game3"]))

  def play_music(self,music_name):
    if music_name == self.current_music:
      self.music_dict[music_name].play(loops = -1)
    else:
      pygame.mixer.stop()
      self.set_music(music_name)
      self.music_dict[music_name].play(loops = -1)

class GameStateManager:

  def __init__(self):

    self.start_menu = StartMenu()
    self.character_menu = CharacterMenu()
    self.game_state = GameState()
    self.game_end = GameEnd()

    self.music_manager = MusicManager()
    self.music_manager.play_music("title")

    self.game_over = False


  def format_game(self):
    self.game_over = True

  def update(self,power_up_sprite_group):
    if not self.game_over:
      if self.start_menu.menu_active:
        self.start_menu.update()
        if not self.start_menu.menu_active:
          self.character_menu.menu_active = True
          pygame.time.wait(500)

      if self.character_menu.menu_active:
        self.character_menu.update()
        if not self.character_menu.menu_active:
          self.game_state.menu_active = True
          self.music_manager.randomize_play_game_music()

          player1_assets, player2_assets = self.character_menu.return_player_assets()

          # players
          self.player1 = Player1(player1_assets)
          self.player2 = Player2(player2_assets)

      if self.game_state.menu_active:
        self.game_state.update()

        # [0] player 1
        self.player1.update(self.player2)
        self.player2.update(self.player1)

        if self.player1.check_death():
          self.game_end.menu_active = True
          self.winner = "player2"
          self.winner_image = self.player2.image
        if self.player2.check_death():
          self.game_end.menu_active = True
          self.winner = "player1"
          self.winner_image = self.player1.image

        if self.game_end.menu_active:
          self.music_manager.play_music("title")

      if self.game_end.menu_active:
        self.game_end.update(self.winner,self.winner_image)
        if not self.game_end.menu_active:
          self.format_game()
        
          
        


class StartMenu:

  def __init__(self):

    #menu state
    self.menu_active = True

    self.in_about_section = False

    #other properties

    bg_list = [
        'background/start_menu_bg1.gif', 'background/start_menu_bg2.png'
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
    self.credit_text1_rect = self.credit_text1.get_rect(center=(400, 80))

    self.credit_text2 = game_font.render(
      'two programming bros combined to build', False, (255, 255, 255))
    self.credit_text2_rect = self.credit_text2.get_rect(center=(400, 120))

    self.credit_text3 = game_font.render(
      'where blood, sweat, tears and hours of work', False, (255, 255, 255))
    self.credit_text3_rect = self.credit_text3.get_rect(center=(400, 160))

    self.credit_text4 = game_font.render(
      'for you to enjoy the nostalgic pixel gameplay', False, (255, 255, 255))
    self.credit_text4_rect = self.credit_text4.get_rect(center=(400, 200))

    self.credit_text5 = game_font.render(
      'Made by:', False, (255, 255, 255))
    self.credit_text5_rect = self.credit_text5.get_rect(center=(400, 240))

    self.credit_text6 = game_font.render(
      'Programming Legend aka Vivek Ajesh...', False, (255, 255, 255))
    self.credit_text6_rect = self.credit_text6.get_rect(center=(400, 280))

    self.credit_text7 = game_font.render(
      'Reis200 aka Behlul Zengin', False, (255, 255, 255))
    self.credit_text7_rect = self.credit_text7.get_rect(center=(400, 310))

    self.credit_text8 = game_font.render(
      'music by Marllon Silva (a.k.a) xDeviruchi', False, (255, 255, 255))
    self.credit_text8_rect = self.credit_text8.get_rect(center=(400, 340))


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
      self.screen.blit(self.credit_text8,self.credit_text8_rect)
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

    self.player1_text = menu_font.render("Player1:",False,(0,0,0))
    self.player1_text_rect = self.player1_text.get_rect(center = (480,50))

    self.player2_text = menu_font.render("Player2:", False, (0, 0, 0))
    self.player2_text_rect = self.player2_text.get_rect(center=(320, 50))

    self.screen = pygame.display.get_surface()

    self.initilise_character_selection_player1()
    self.initilise_character_selection_player2()

    self.player_1_character_names = [name for name in character_set_player1.keys()]
    self.player_2_character_names = [name for name in character_set_player2.keys()]

    self.player_1_assets = None;
    self.player_2_assets = None;


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




  def display_menu(self):
    self.screen.blit(self.background, self.background_rect)
    self.screen.blit(self.player1_text,self.player1_text_rect)
    self.screen.blit(self.player2_text,self.player2_text_rect)

  def check_collision(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_g]:
      self.menu_active = False

    if pygame.mouse.get_pressed()[0] and self.player_1_assets == None:
      for image, rect in self.game_characters1.items():
        if rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
          self.find_pokemon_properties_player1(rect.center)
    if pygame.mouse.get_pressed()[0] and self.player_2_assets == None:
      for image, rect in self.game_characters2.items():
        if rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
          self.find_pokemon_properties_player2(rect.center)

  def find_pokemon_properties_player1(self,rect_pos):
    for name in self.player_1_character_names:
      if rect_pos == character_set_player1[name]["display_pos"]:
        self.player_1_assets = character_set_player1[name]
  def find_pokemon_properties_player2(self,rect_pos):
    for name in self.player_2_character_names:
      if rect_pos == character_set_player2[name]["display_pos"]:
        self.player_2_assets = character_set_player2[name]

  def return_player_assets(self):
    return self.player_1_assets, self.player_2_assets

  def check_end_menu(self):
    if self.player_1_assets != None and self.player_2_assets != None:
      self.menu_active = False

  def update(self):
    self.display_menu()
    self.display_characters()
    self.check_collision()
    self.check_end_menu()


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


class GameEnd:
  def __init__(self):

    self.menu_active = False

    bg_list = [
      'background/start_menu_bg1.gif', 'background/start_menu_bg2.png',
      'background/start_menu_bg3.png'
    ]
    self.background = pygame.image.load(choice(bg_list)).convert()
    self.background_rect = self.background.get_rect(topleft=(0, 0))

    self.screen = pygame.display.get_surface()

    self.go_back_button = pygame.transform.rotozoom(pygame.image.load("buttons/exit_button.png").convert_alpha(), 0, 2)
    self.go_back_button_rect = self.go_back_button.get_rect(center=(750, 350))

  def display_background(self):
    self.screen.blit(self.background,self.background_rect)
    self.screen.blit(self.go_back_button,self.go_back_button_rect)

  def display_winner(self,winner,winner_image):
    self.winner_text = title_font.render(f"Winner:{winner}",False,(0,0,0))
    self.winner_rect = self.winner_text.get_rect(center = (400,200))

    winner_image = winner_image
    winner_rect = winner_image.get_rect(center = (400,300))

    self.screen.blit(self.winner_text,self.winner_rect)
    self.screen.blit(winner_image,winner_rect)


  def check_menu_active(self):
    if pygame.mouse.get_pressed()[0] and self.go_back_button_rect.collidepoint(pygame.mouse.get_pos()):
      self.menu_active = False

  def update(self,winner,winner_image):
    self.display_background()
    self.display_winner(winner,winner_image)
    self.check_menu_active()
