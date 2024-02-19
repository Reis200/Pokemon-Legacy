import pygame
from database import title_font, game_font,player_1_rect_pos,player_2_rect_pos
from random import randint
from os import listdir

class Player1:
  def __init__(self,player_assets):
    self.image = player_assets["image"].convert_alpha()
    self.rect = self.image.get_rect(midbottom=player_1_rect_pos)

    self.origin_location = self.rect.midbottom

    self.screen = pygame.display.get_surface()
    self.screen_w, self.screen_h = self.screen.get_width(), self.screen.get_height()

    self.speed = player_assets["speed"]

    # jump mechanic
    self.on_jump_state = False
    self.gravity = 1
    self.jump_height = 30
    self.velocity = self.jump_height

    self.previous_heal_time = pygame.time.get_ticks()
    self.heal_time_loading = 0
    self.heal_bar_time_length = 400
    self.max_heal_delay_time = 5000
    self.delay_ratio = self.max_heal_delay_time / self.heal_bar_time_length

    self.health_max = player_assets["health"]
    self.health = player_assets["health"]

    self.damage = player_assets["damage"]

    self.previous_attack_time = 0

    self.active_attacks = []

    self.pos = "on_the_left"

    self.power_up = "None"
    self.power_up_time = 0

    self.ui_pos_centerx = self.screen.get_width() * 0.875

    self.player_assets = player_assets

  def check_death(self):
    if self.health <= 0:
      return True
    return False

  def activate_power_up_state(self):
    if self.power_up != "None":
      if self.power_up == "speed":
        self.speed *= 1.75
        self.power_up_time = pygame.time.get_ticks()
      elif self.power_up == "power":
        self.damage *= 2
        self.power_up_time = pygame.time.get_ticks()
      elif self.power_up == "ultimate":
        self.speed *= 1.75
        self.damage *= 2
        self.power_up_time = pygame.time.get_ticks()


  def refresh_power_up_state(self):
    if pygame.time.get_ticks() - self.power_up_time > 10000:
      self.speed = self.player_assets["speed"]
      self.damage = self.player_assets["damage"]
      self.power_up = "None"

  def display_healing_loading(self):
    if pygame.time.get_ticks() - self.previous_heal_time > self.max_heal_delay_time and self.heal_time_loading == 0:
      self.previous_heal_time = pygame.time.get_ticks()
    elif self.heal_time_loading <= self.max_heal_delay_time:
      self.heal_time_loading = pygame.time.get_ticks() - self.previous_heal_time



    heal_loading_max = pygame.Rect(self.ui_pos_centerx,150,self.heal_bar_time_length,50); heal_loading_max.center = (self.ui_pos_centerx,120)
    heal_loading = pygame.Rect(self.ui_pos_centerx,150,int(self.heal_time_loading / self.delay_ratio),50); heal_loading.midleft = (heal_loading_max.left,120)

    heal_text = game_font.render(f"Heal:", False, (0, 0, 0))
    heal_text_rect = heal_text.get_rect(center=(heal_loading_max.centerx, heal_loading_max.centery))

    if self.heal_time_loading >= self.max_heal_delay_time:
      pygame.draw.rect(self.screen, (19,156,107), heal_loading)
      pygame.draw.rect(self.screen, "#000000", heal_loading_max, 5)
    else:
      pygame.draw.rect(self.screen, (252, 214, 9), heal_loading)
      pygame.draw.rect(self.screen, "#000000", heal_loading_max, 5)

    self.screen.blit(heal_text,heal_text_rect)


  def display_health(self):
    health_bar_max = pygame.Rect(self.rect.left -20, 20, self.health_max * 3, 50); health_bar_max.center = (self.ui_pos_centerx,50)
    health_bar = pygame.Rect(self.rect.left -20, 20, self.health * 3, 50); health_bar.midleft = (health_bar_max.left,50)

    health_text = game_font.render(f"Health: {self.health}", False, (0, 0, 0))
    health_text_rect = health_text.get_rect(center=(health_bar_max.centerx, health_bar_max.centery))


    if self.health / self.health_max >= 0.75:
      pygame.draw.rect(self.screen,(139,172,15),health_bar)
    if self.health / self.health_max < 0.75 and self.health / self.health_max > 0.25:
      pygame.draw.rect(self.screen,(255,215,0),health_bar)
    if self.health / self.health_max <= 0.25:
      pygame.draw.rect(self.screen,(178,34,34),health_bar)


    pygame.draw.rect(self.screen,"#000000",health_bar_max,4)

    self.screen.blit(health_text,health_text_rect)

  def display_stats(self):
    self.state_text = game_font.render(f"PowerUp:{self.power_up}",False,(0,0,0))
    self.state_text_rect = self.state_text.get_rect(center = (self.ui_pos_centerx,170))

    self.screen.blit(self.state_text,self.state_text_rect)

  # def move(self):
  #   keys = pygame.key.get_pressed()
  #
  #   # left and right
  #   if keys[pygame.K_RIGHT]:
  #     self.rect.x += self.speed
  #
  #   if keys[pygame.K_LEFT]:
  #     self.rect.x -= self.speed
  #
  #   # jump
  #   if keys[pygame.K_UP] and (pygame.time.get_ticks() - self.previous_jump_time >= 500) and self.rect.bottom >= 350:
  #     self.previous_jump_time = pygame.time.get_ticks()
  #     self.on_jump_state = True
  #
  #   if self.on_jump_state and pygame.time.get_ticks() - self.previous_jump_time <= 120:
  #     self.rect.y -= 30
  #   else: self.on_jump_state = False
  #
  #   if not self.on_jump_state and self.rect.bottom < 350:
  #     self.rect.y += 13
  #
  #
  #   if self.rect.right >= self.screen.get_width():
  #     self.rect.right = self.screen.get_width()
  #   if self.rect.left <= 0:
  #     self.rect.left = 0

  def move(self):
    keys = pygame.key.get_pressed()

    # left and right
    if keys[pygame.K_RIGHT]:
      self.rect.x += self.speed

    if keys[pygame.K_LEFT]:
      self.rect.x -= self.speed

    # jump
    if keys[pygame.K_UP]:
      self.on_jump_state = True

    # improved jump
    if self.on_jump_state:
      self.rect.y -= self.velocity
      self.velocity -= self.gravity
      if self.velocity < -self.jump_height:
        self.on_jump_state = False
        self.velocity = self.jump_height

    if not self.on_jump_state and self.rect.bottom < self.screen_h * 0.9:
      self.rect.bottom += self.screen_h * 0.9 - self.rect.bottom
    elif not self.on_jump_state and self.rect.bottom > self.screen_h * 0.9:
      self.rect.bottom = self.screen_h * 0.9



    if self.rect.right >= self.screen.get_width():
      self.rect.right = self.screen.get_width()
    if self.rect.left <= 0:
      self.rect.left = 0



  def attack_movement(self):
    keys = pygame.key.get_pressed()

    #attacks 1,2,3
    if (keys[pygame.K_KP1] or keys[pygame.K_1]) and pygame.time.get_ticks() - self.previous_attack_time >= 400:
      attack = PlayerAttack(self)
      self.active_attacks.append(attack)
      self.previous_attack_time = pygame.time.get_ticks()
    if (keys[pygame.K_KP2] or keys[pygame.K_2]) and pygame.time.get_ticks() - self.previous_heal_time >= 5000 and self.health != self.health_max:
      if self.health < self.health_max: self.health += 20
      if self.health > self.health_max: self.health = self.health_max
      self.previous_heal_time = pygame.time.get_ticks()
      self.heal_time_loading = 0

    if len(self.active_attacks) != 0:
      for active_attack in self.active_attacks:
        if active_attack != None and active_attack.rect.left >= self.screen.get_width() or active_attack.rect.right <= 0:
          del active_attack

    if len(self.active_attacks) != 0:
      for active_attack in self.active_attacks:
        active_attack.update()

  def check_collision(self,opponent):
    # attack collide with opponent
    for attack in self.active_attacks:
      if attack.rect.colliderect(opponent.rect) and opponent.health > 0:
        opponent.health -= self.damage
        self.active_attacks.remove(attack)

    # attack collide with another
    for attack in self.active_attacks:
      for enemy_attack in opponent.active_attacks:
        if attack.rect.colliderect(enemy_attack.rect) and enemy_attack != None and attack != None:
          opponent.active_attacks.remove(enemy_attack)
          self.active_attacks.remove(attack)

    # player collide with another
    if self.rect.colliderect(opponent.rect):
      if self.rect.midbottom[1] + 20 < opponent.rect.midbottom[1] and opponent.health > 0:
        opponent.health -= self.damage * 2
        self.rect.midbottom = self.origin_location
      else:
        self.rect.midbottom = self.origin_location

  def delete_unrendered_attacks(self):
    for attack in self.active_attacks:
      if attack.check_above_border(): self.active_attacks.remove(attack)

  def display_player(self):
    self.screen.blit(self.image,self.rect)


  def update(self,opponent):
    self.move()
    self.display_health()
    self.display_healing_loading()
    self.display_stats()
    self.display_player()
    self.attack_movement()
    self.check_collision(opponent)
    self.delete_unrendered_attacks()
    self.refresh_power_up_state()


class Player2(Player1):
  def __init__(self,player_assets):
    super().__init__(player_assets)
    self.rect = self.image.get_rect(midbottom=player_2_rect_pos)
    self.origin_location = self.rect.center
    self.pos = "on_the_right"
    self.ui_pos_centerx = self.screen.get_width() * 0.125


  def move(self):
    keys = pygame.key.get_pressed()

    # left and right
    if keys[pygame.K_d]:
      self.rect.x += self.speed

    if keys[pygame.K_a]:
      self.rect.x -= self.speed

    if keys[pygame.K_w]:
      self.on_jump_state = True

    # improved jump
    if self.on_jump_state:
      self.rect.y -= self.velocity
      self.velocity -= self.gravity
      if self.velocity < -self.jump_height:
        self.on_jump_state = False
        self.velocity = self.jump_height

    if not self.on_jump_state and self.rect.bottom < self.screen_h * 0.9:
      self.rect.bottom += self.screen_h * 0.9 - self.rect.bottom
    elif not self.on_jump_state and self.rect.bottom > self.screen_h * 0.9:
      self.rect.bottom = self.screen_h * 0.9


    if self.rect.right >= self.screen.get_width():
      self.rect.right = self.screen.get_width()
    if self.rect.left <= 0:
      self.rect.left = 0

  def attack_movement(self):
    keys = pygame.key.get_pressed()

    # attacks 1,2,3
    if keys[pygame.K_z] and pygame.time.get_ticks() - self.previous_attack_time >= 400:
      attack = PlayerAttack(self)
      self.active_attacks.append(attack)
      self.previous_attack_time = pygame.time.get_ticks()
    if keys[pygame.K_x] and pygame.time.get_ticks() - self.previous_heal_time >= 5000 and self.health != self.health_max:
      if self.health < self.health_max: self.health += 20
      if self.health > self.health_max: self.health = self.health_max
      self.previous_heal_time = pygame.time.get_ticks()
      self.heal_time_loading = 0

    if len(self.active_attacks) != 0:
      for active_attack in self.active_attacks:
        if active_attack != None and active_attack.rect.left >= self.screen.get_width() or active_attack.rect.right <= 0:
          del active_attack


    if len(self.active_attacks) != 0:
      for active_attack in self.active_attacks:
        active_attack.update()

class PlayerAttack:
  def __init__(self, player):

    self.screen = pygame.display.get_surface()

    self.player = player

    # attack

    file_directory = self.player.player_assets["attack"]
    animation_files = listdir(file_directory)

    self.attack_speed = 10

    if self.player.pos == "on_the_right":
      # self.attack1_sprites = [pygame.transform.rotozoom(pygame.image.load("animations/fire/frame_0.png").convert_alpha(),0,2),
      #                         pygame.transform.rotozoom(pygame.image.load("animations/fire/frame_1.png").convert_alpha(),0,2),
      #                         pygame.transform.rotozoom(pygame.image.load("animations/fire/frame_2.png").convert_alpha(),0,2),
      #                         pygame.transform.rotozoom(pygame.image.load("animations/fire/frame_3.png").convert_alpha(),0,2),
      #                         pygame.transform.rotozoom(pygame.image.load("animations/fire/frame_4.png").convert_alpha(),0,2)]
      self.attack1_sprites = [pygame.transform.rotozoom(pygame.image.load(f"{file_directory}/{file}").convert_alpha(),0,4) for file in animation_files]
    else:
      # self.attack1_sprites = [
      #   pygame.transform.rotozoom(pygame.image.load("animations/fire/frame_0.png").convert_alpha(), 180, 2),
      #   pygame.transform.rotozoom(pygame.image.load("animations/fire/frame_1.png").convert_alpha(), 180, 2),
      #   pygame.transform.rotozoom(pygame.image.load("animations/fire/frame_2.png").convert_alpha(), 180, 2),
      #   pygame.transform.rotozoom(pygame.image.load("animations/fire/frame_3.png").convert_alpha(), 180, 2),
      #   pygame.transform.rotozoom(pygame.image.load("animations/fire/frame_4.png").convert_alpha(), 180, 2)]
      self.attack1_sprites = [pygame.transform.rotozoom(pygame.image.load(f"{file_directory}/{file}").convert_alpha(), 180, 4) for file in animation_files]

    self.animation_index = 0
    self.animation_speed = 0.1

    self.image = self.attack1_sprites[self.animation_index]
    self.rect = self.image.get_rect(center=self.player.rect.center)


  def attack_animation(self):
    self.animation_index += self.animation_speed
    if self.animation_index >= len(self.attack1_sprites):
      self.animation_index = 0

    self.image = self.attack1_sprites[int(self.animation_index)]


  def display_attack(self):
    self.screen.blit(self.image,self.rect)

  def attack_movement(self):
    if self.player.pos == "on_the_right":
      self.rect.x += self.attack_speed
    if self.player.pos == "on_the_left":
      self.rect.x -= self.attack_speed

  def check_above_border(self):
    if self.rect.right >= self.screen.get_width() + 50:
      return True
    elif self.rect.left <= -80:
      return True

    if self.rect.top <= -80:
      return True
    elif self.rect.bottom >= self.screen.get_height() + 80:
      return True


  def update(self):
    self.display_attack()
    self.attack_animation()
    self.attack_movement()

