import pygame
from database import title_font, game_font
from random import randint

class Player1:
  def __init__(self,selected_pokemon,health,speed,damage,relative_pos):
    self.image = pygame.transform.rotozoom(pygame.image.load(f"assets/{selected_pokemon}").convert_alpha(),0,0.5)
    self.rect = self.image.get_rect(midbottom=relative_pos)

    self.origin_location = self.rect.center

    self.screen = pygame.display.get_surface()

    self.speed = 5
    self.previous_jump_time = 0
    self.jumping_speed = 0.75
    self.falling_speed = 0.3
    self.on_jump_state = False

    self.previous_heal_time = 0
    self.heal_time_loading = 0
    self.heal_bar_time_length = 100
    self.max_heal_delay_time = 5000
    self.delay_ratio = self.max_heal_delay_time / self.heal_bar_time_length

    self.health_max = 100
    self.health = 100

    self.damage = 5

    self.previous_attack_time = 0

    self.active_attacks = []

    self.pos = "on_the_left"

    self.power_up = "None"
    self.power_up_time = 0


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

      print(self.speed,self.damage)


  def refresh_power_up_state(self):
    if pygame.time.get_ticks() - self.power_up_time > 10000:
      self.speed = 5
      self.damage = 5
      self.power_up = "None"

  def display_healing_loading(self):
    if self.heal_time_loading <= self.max_heal_delay_time:
      self.heal_time_loading = pygame.time.get_ticks() - self.previous_heal_time

    heal_loading_max = pygame.Rect(self.rect.left,90,self.heal_bar_time_length,25)
    heal_loading = pygame.Rect(self.rect.left,90,int(self.heal_time_loading / self.delay_ratio),20)

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
    health_bar_max = pygame.Rect(self.rect.left, 20, self.health_max, 20)
    health_bar = pygame.Rect(self.rect.left, 20, self.health, 20)

    health_text = game_font.render(f"Health: {self.health}", False, (0, 0, 0))
    health_text_rect = health_text.get_rect(center=(health_bar_max.centerx, health_bar_max.centery + 20))


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
    self.state_text_rect = self.state_text.get_rect(center = (self.rect.centerx, 70))

    self.screen.blit(self.state_text,self.state_text_rect)

  def move(self):
    keys = pygame.key.get_pressed()

    # left and right
    if keys[pygame.K_RIGHT]:
      self.rect.x += self.speed

    if keys[pygame.K_LEFT]:
      self.rect.x -= self.speed

    # jump
    if keys[pygame.K_UP] and (pygame.time.get_ticks() - self.previous_jump_time >= 500) and self.rect.bottom >= 350:
      self.previous_jump_time = pygame.time.get_ticks()
      self.on_jump_state = True

    if self.on_jump_state and pygame.time.get_ticks() - self.previous_jump_time <= 120:
      self.rect.y -= 30
    else: self.on_jump_state = False

    if not self.on_jump_state and self.rect.bottom < 350:
      self.rect.y += 15
    
    
    if self.rect.right >= self.screen.get_width():
      self.rect.right = self.screen.get_width()
    if self.rect.left <= 0:
      self.rect.left = 0



  def attack_movement(self):
    keys = pygame.key.get_pressed()

    #attacks 1,2,3
    if keys[pygame.K_1] and pygame.time.get_ticks() - self.previous_attack_time >= 400:
      attack = PlayerAttack(self)
      self.active_attacks.append(attack)
      self.previous_attack_time = pygame.time.get_ticks()
    if keys[pygame.K_2] and pygame.time.get_ticks() - self.previous_heal_time >= 5000:
      if self.health < self.health_max: self.health += 20
      if self.health > self.health_max: self.health = self.health_max
      self.previous_heal_time = pygame.time.get_ticks()
      self.heal_time_loading = 0
    # if keys[pygame.K_3] and pygame.time.get_ticks() - self.previous_attack_time >= 200:
    #   self.previous_attack_time = pygame.time.get_ticks()

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
      for enemy_attack in opponent.active_attacks:
        if attack.rect.colliderect(enemy_attack.rect):
          opponent.active_attacks.remove(enemy_attack)
          self.active_attacks.remove(attack)
    # player collide with another
    if self.rect.colliderect(opponent.rect):
      if self.rect.midbottom[1] + 20 < opponent.rect.midbottom[1] and opponent.health > 0:
        opponent.health -= self.damage * 2
        self.rect.midbottom = (self.origin_location[0],self.origin_location[1] - 200)
      else:
        self.rect.midbottom = (self.origin_location[0], self.origin_location[1])



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
    self.refresh_power_up_state()


class Player2(Player1):
  def __init__(self,selected_pokemon,health,speed,damage,relative_pos):
    super().__init__(selected_pokemon,health,speed,damage,relative_pos)
    self.pos = "on_the_right"


  def move(self):
    keys = pygame.key.get_pressed()

    # left and right
    if keys[pygame.K_d]:
      self.rect.x += self.speed

    if keys[pygame.K_a]:
      self.rect.x -= self.speed

    # jump
    if keys[pygame.K_w] and (pygame.time.get_ticks() - self.previous_jump_time >= 500) and self.rect.bottom >= 350:
      self.previous_jump_time = pygame.time.get_ticks()
      self.on_jump_state = True

    if self.on_jump_state and pygame.time.get_ticks() - self.previous_jump_time <= 120:
      self.rect.y -= 30
    else:
      self.on_jump_state = False

    if not self.on_jump_state and self.rect.bottom < 350:
      self.rect.y += 15


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
    if keys[pygame.K_x] and pygame.time.get_ticks() - self.previous_heal_time >= 5000:
      if self.health < self.health_max: self.health += 20
      if self.health > self.health_max: self.health = self.health_max
      self.previous_heal_time = pygame.time.get_ticks()
      self.heal_time_loading = 0
    # if keys[pygame.K_x] and pygame.time.get_ticks() - self.previous_attack_time >= 200:
    #   self.previous_attack_time = pygame.time.get_ticks()
    # if keys[pygame.K_c] and pygame.time.get_ticks() - self.previous_attack_time >= 200:
    #   self.previous_attack_time = pygame.time.get_ticks()

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


    self.attack_speed = 5

    if self.player.pos == "on_the_right":
      self.attack1_sprites = [pygame.transform.rotozoom(pygame.image.load("animations/fire/frame_0.png").convert_alpha(),0,2),
                              pygame.transform.rotozoom(pygame.image.load("animations/fire/frame_1.png").convert_alpha(),0,2),
                              pygame.transform.rotozoom(pygame.image.load("animations/fire/frame_2.png").convert_alpha(),0,2),
                              pygame.transform.rotozoom(pygame.image.load("animations/fire/frame_3.png").convert_alpha(),0,2),
                              pygame.transform.rotozoom(pygame.image.load("animations/fire/frame_4.png").convert_alpha(),0,2)]
    else:
      self.attack1_sprites = [
        pygame.transform.rotozoom(pygame.image.load("animations/fire/frame_0.png").convert_alpha(), 180, 2),
        pygame.transform.rotozoom(pygame.image.load("animations/fire/frame_1.png").convert_alpha(), 180, 2),
        pygame.transform.rotozoom(pygame.image.load("animations/fire/frame_2.png").convert_alpha(), 180, 2),
        pygame.transform.rotozoom(pygame.image.load("animations/fire/frame_3.png").convert_alpha(), 180, 2),
        pygame.transform.rotozoom(pygame.image.load("animations/fire/frame_4.png").convert_alpha(), 180, 2)]

    self.animation_index = 0
    self.animation_speed = 0.1

    self.image = self.attack1_sprites[self.animation_index]
    self.rect = self.image.get_rect(center=self.player.rect.center)

    # self.attack2_sprites = [pygame.image.load("animations/fire/frame_0.png").convert_alpha(),
    #                        pygame.image.load("animations/fire/frame_1.png").convert_alpha(),
    #                        pygame.image.load("animations/fire/frame_2.png").convert_alpha(),
    #                        pygame.image.load("animations/fire/frame_3.png").convert_alpha(),
    #                        pygame.image.load("animations/fire/frame_4.png").convert_alpha()]
    #
    # self.attack3_sprites = [pygame.image.load("animations/electric/frame_0.png").convert_alpha(),
    #                        pygame.image.load("animations/electric/frame_1.png").convert_alpha(),
    #                        pygame.image.load("animations/electric/frame_2.png").convert_alpha(),
    #                        pygame.image.load("animations/electric/frame_3.png").convert_alpha(),
    #                        pygame.image.load("animations/electric/frame_4.png").convert_alpha()]


  def attack_animation(self):
    self.animation_index += self.animation_speed
    if self.animation_index >= len(self.attack1_sprites):
      self.animation_index = 0

    self.image = self.attack1_sprites[int(self.animation_index)]
    #self.rect = self.image.get_rect(center=self.player.rect.center)


  def display_attack(self):
    self.screen.blit(self.image,self.rect)

  def attack_movement(self):
    if self.player.pos == "on_the_right":
      self.rect.x += self.attack_speed
    if self.player.pos == "on_the_left":
      self.rect.x -= self.attack_speed

    # if self.rect.left >= self.screen.get_width() or self.rect.right <= 0:

  def update(self):
    self.display_attack()
    self.attack_animation()
    self.attack_movement()

