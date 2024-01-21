import pygame

pygame.init()

character = {
  "Pikachu": {"health":35, "attack1":'Thunder Shock', "attack2":'Nuzzle', "attack3":'Spark'},
  "Charmander": {"health":39, "attack1":'FlameThrower', "attack2":'Scratch', "attack3":'Fire Fang'},
  "Squirtle": {"health":44, "attack1":'Aqua tail', "attack2":'Bite', "attack3":'Rapid Spin'},
  "Bulbasaur": {"health": 45, "attack1": 'Tackle', "attack2":'Seed Bomb', "attack3":'Razor Leaf'},
  "Charizard": {"health": 78, "attack1": 'Inferno', "attack2":'Dragon Claw', "attack3":'Slash'},
  "Eevee": {"health": 55, "attack1": 'Swift', "attack2": 'Take Down', "attack3": 'Covet'},
  "Gastly": {"health": 30, "attack1": 'Lick', "attack2": 'Sucker Punch', "attack3": 'Payback'},
  "Pidgey": {"health": 40, "attack1": 'Twister', "attack2": 'Gust', "attack3": 'Quick Attack'},
  "Snorlax": {"health": 160, "attack1": 'Crunch', "attack2": 'Hammer Arm', "attack3": 'High Horsepower'}
  
}

title_font = pygame.font.Font("fonts/8-bit-hud.ttf", 40)
game_font = pygame.font.Font("fonts/8-bit-hud.ttf",10)
