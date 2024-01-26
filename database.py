import pygame

pygame.font.init()

#electric fire grass water
# ? we have to find another
# at the right side looking left
character_set_player1 = {
  "Pikachu": {"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Pikachu.png"),0,0.5),"attack":"animations/electric","health":100,"speed":7,"damage":5},
  "Charmander": {"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Charmander.png"),0,0.5),"attack":"animations/fire","health":100,"speed":5,"damage":5},
  "Squirtle": {"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Squirtle.png"),0,0.5),"attack":"animations/water","health":120,"speed":3,"damage":8},
  "Bulbasaur": {"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Bulbasaur.png"),0,0.5),"attack":"animations/grass","health": 150,"speed":2,"damage":10},
  "Charizard": {"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Charizard.png"),0,0.5),"attack":"animations/fire","health": 120,"speed":6,"damage":7},
  "Eevee": {"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Eevee.png"),0,0.5),"attack":"animations/?","health": 90,"speed":6,"damage":4},
  "Gastly": {"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Gastly.png"),0,0.5),"attack":"animations/?","health": 80,"speed":6,"damage":5},
  "Pidgey": {"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Pidgey.png"),0,0.5),"attack":"animations/electric","health": 80,"speed":5,"damage":5},
  "Snorlax": {"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Snorlax.png"),0,0.5),"attack":"animations/water","health": 130,"speed":3,"damage":9}
}
# at the left side looking right
character_set_player2 = {
  "Pikachu2": {"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Pikachu2.png"),0,0.5),"attack":"animations/electric","health":100,"speed":7,"damage":5},
  "Charmander2": {"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Charmander2.png"),0,0.5),"attack":"animations/fire","health":100,"speed":5,"damage":5},
  "Squirtle2": {"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Squirtle2.png"),0,0.5),"attack":"animations/water","health":120,"speed":3,"damage":8},
  "Bulbasaur2": {"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Bulbasaur2.png"),0,0.5),"attack":"animations/grass","health": 150,"speed":2,"damage":10},
  "Charizard2": {"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Charizard2.png"),0,0.5),"attack":"animations/fire","health": 120,"speed":6,"damage":7},
  "Eevee2": {"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Eevee2.png"),0,0.5),"attack":"animations/?","health": 90,"speed":6,"damage":4},
  "Gastly2": {"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Gastly2.png"),0,0.5),"attack":"animations/?","health": 80,"speed":6,"damage":5},
  "Pidgey2": {"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Pidgey2.png"),0,0.5),"attack":"animations/electric","health": 80,"speed":5,"damage":5},
  "Snorlax2": {"image":pygame.transform.rotozoom(pygame.image.load(f"assets/Snorlax2.png"),0,0.5),"attack":"animations/water","health": 130,"speed":3,"damage":9}
}

title_font = pygame.font.Font("fonts/8-bit-hud.ttf", 40)
game_font = pygame.font.Font("fonts/8-bit-hud.ttf",10)
