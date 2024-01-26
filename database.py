import pygame

pygame.font.init()

#electric fire grass water
# ? we have to find another
# at the right side looking left
character_set_player1 = {
  "Pikachu": {"display_pos":(600,50),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Pikachu.png"),0,0.5),"attack":"animations/electric","health":100,"speed":7,"damage":5},
  "Charmander": {"display_pos":(750,50),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Charmander.png"),0,0.5),"attack":"animations/fire","health":100,"speed":5,"damage":5},
  "Squirtle": {"display_pos":(600,150),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Squirtle.png"),0,0.5),"attack":"animations/water","health":120,"speed":3,"damage":8},
  "Bulbasaur": {"display_pos":(750,150),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Bulbasaur.png"),0,0.5),"attack":"animations/grass","health": 150,"speed":2,"damage":10},
  "Charizard": {"display_pos":(600,250),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Charizard.png"),0,0.5),"attack":"animations/fire","health": 120,"speed":6,"damage":7},
  "Eevee": {"display_pos":(750,250),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Eevee.png"),0,0.5),"attack":"animations/?","health": 90,"speed":6,"damage":4},
  "Gastly": {"display_pos":(600,350),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Gastly.png"),0,0.5),"attack":"animations/?","health": 80,"speed":6,"damage":5},
  "Pidgey": {"display_pos":(750,350),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Pidgey.png"),0,0.5),"attack":"animations/electric","health": 80,"speed":5,"damage":5},
  "Snorlax": {"display_pos":(600,450),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Snorlax.png"),0,0.5),"attack":"animations/water","health": 130,"speed":3,"damage":9}
}
# at the left side looking right
character_set_player2 = {
  "Pikachu2": {"display_pos":(50,50),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Pikachu2.png"),0,0.5),"attack":"animations/electric","health":100,"speed":7,"damage":5},
  "Charmander2": {"display_pos":(200,50),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Charmander2.png"),0,0.5),"attack":"animations/fire","health":100,"speed":5,"damage":5},
  "Squirtle2": {"display_pos":(50,150),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Squirtle2.png"),0,0.5),"attack":"animations/water","health":120,"speed":3,"damage":8},
  "Bulbasaur2": {"display_pos":(200,150),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Bulbasaur2.png"),0,0.5),"attack":"animations/grass","health": 150,"speed":2,"damage":10},
  "Charizard2": {"display_pos":(50,250),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Charizard2.png"),0,0.5),"attack":"animations/fire","health": 120,"speed":6,"damage":7},
  "Eevee2": {"display_pos":(200,250),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Eevee2.png"),0,0.5),"attack":"animations/?","health": 90,"speed":6,"damage":4},
  "Gastly2": {"display_pos":(50,350),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Gastly2.png"),0,0.5),"attack":"animations/?","health": 80,"speed":6,"damage":5},
  "Pidgey2": {"display_pos":(200,350),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Pidgey2.png"),0,0.5),"attack":"animations/electric","health": 80,"speed":5,"damage":5},
  "Snorlax2": {"display_pos":(50,450),"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Snorlax2.png"),0,0.5),"attack":"animations/water","health": 130,"speed":3,"damage":9}
}

title_font = pygame.font.Font("fonts/8-bit-hud.ttf", 40)
game_font = pygame.font.Font("fonts/8-bit-hud.ttf",10)







