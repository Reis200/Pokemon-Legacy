import pygame

pygame.font.init()

#electric fire grass water
# ? we have to find another
# at the right side looking left

pygame.init()

info = pygame.display.Info() #called before set_mode
screen_w,screen_h = info.current_w, info.current_h


character_set_player1 = {
  "Pikachu": {"display_pos":(screen_w * 0.60,screen_h * 0.2),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Pikachu.png"),0,1),"attack":"animations/electric","health":100,"speed":12,"damage":5},
  "Charmander": {"display_pos":(screen_w * 0.75,screen_h * 0.2),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Charmander.png"),0,1),"attack":"animations/fire","health":100,"speed":9,"damage":5},
  "Squirtle": {"display_pos":(screen_w * 0.90,screen_h * 0.2),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Squirtle.png"),0,1),"attack":"animations/water","health":120,"speed":4.5,"damage":8},
  "Bulbasaur": {"display_pos":(screen_w * 0.60,screen_h * 0.4),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Bulbasaur.png"),0,1),"attack":"animations/grass","health": 150,"speed":3,"damage":10},
  "Charizard": {"display_pos":(screen_w * 0.75,screen_h * 0.4),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Charizard.png"),0,1),"attack":"animations/fire","health": 120,"speed":9,"damage":7},
  "Eevee": {"display_pos":(screen_w * 0.90,screen_h * 0.4),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Eevee.png"),0,1),"attack":"animations/fire","health": 90,"speed":10.5,"damage":4},
  "Gastly": {"display_pos":(screen_w * 0.60,screen_h * 0.6),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Gastly.png"),0,1),"attack":"animations/water","health": 80,"speed":9,"damage":6},
  "Pidgey": {"display_pos":(screen_w * 0.75,screen_h * 0.6),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Pidgey.png"),0,1),"attack":"animations/electric","health": 80,"speed":9,"damage":4},
  "Snorlax": {"display_pos":(screen_w * 0.90,screen_h * 0.6),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Snorlax.png"),0,1),"attack":"animations/water","health": 130,"speed":4.5,"damage":9}
}
# at the left side looking right
character_set_player2 = {
  "Pikachu2": {"display_pos":(screen_w * 0.40,screen_h * 0.2),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Pikachu2.png"),0,1),"attack":"animations/electric","health":100,"speed":12,"damage":5},
  "Charmander2": {"display_pos":(screen_w * 0.25,screen_h * 0.2),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Charmander2.png"),0,1),"attack":"animations/fire","health":100,"speed":9,"damage":5},
  "Squirtle2": {"display_pos":(screen_w * 0.10,screen_h * 0.2),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Squirtle2.png"),0,1),"attack":"animations/water","health":120,"speed":4.5,"damage":8},
  "Bulbasaur2": {"display_pos":(screen_w * 0.40,screen_h * 0.4),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Bulbasaur2.png"),0,1),"attack":"animations/grass","health": 150,"speed":3,"damage":10},
  "Charizard2": {"display_pos":(screen_w * 0.25,screen_h * 0.4),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Charizard2.png"),0,1),"attack":"animations/fire","health": 120,"speed":9,"damage":7},
  "Eevee2": {"display_pos":(screen_w * 0.10,screen_h * 0.4),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Eevee2.png"),0,1),"attack":"animations/fire","health": 90,"speed":10.5,"damage":4},
  "Gastly2": {"display_pos":(screen_w * 0.40,screen_h * 0.6),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Gastly2.png"),0,1),"attack":"animations/water","health": 80,"speed":9,"damage":6},
  "Pidgey2": {"display_pos":(screen_w * 0.25,screen_h * 0.6),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Pidgey2.png"),0,1),"attack":"animations/electric","health": 80,"speed":9,"damage":5},
  "Snorlax2": {"display_pos":(screen_w * 0.10,screen_h * 0.6),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Snorlax2.png"),0,1),"attack":"animations/water","health": 130,"speed":4.5,"damage":9}
}

title_font = pygame.font.Font("fonts/8-bit-hud.ttf", 80)
game_font = pygame.font.Font("fonts/8-bit-hud.ttf",20)
menu_font = pygame.font.Font("fonts/8-bit-hud.ttf",30)

player_1_rect_pos = (screen_w * 0.875,screen_h * 0.9)
player_2_rect_pos = (screen_w * 0.125,screen_h * 0.9)





