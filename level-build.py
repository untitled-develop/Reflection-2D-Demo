import json, pygame, sys, pygame.transform
from pygame.locals import *

pygame.init()

VIEWSURF = pygame.Surface((400,400))

DISPLAYSURF = pygame.display.set_mode((800,800))
level = [
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
]

tutorial = pygame.image.load("tutorial.png")

textures = [

pygame.image.load("air.png"),
pygame.image.load("beam.png"), # Not a valid tile type, just a texture
pygame.image.load("beam_corner.png"), # Not a valid tile type, just a texture
pygame.image.load("conduit.png"),
pygame.image.load("catcher.png"),
pygame.image.load("emitter.png"),
pygame.image.load("contact.png"),
pygame.image.load("contact_powered.png"), # Not a valid tile type, just a texture
pygame.image.load("cube.png"),
pygame.image.load("flipcore.png")

]

cursor_pos=[0,0]
selected_tile=0
current_rotation=0

while True: # Main loop
    for event in pygame.event.get():
        if event.type is QUIT:
            pygame.quit()
            sys.exit()
        if event.type is KEYDOWN:


            if event.key is K_q:
                selected_tile = selected_tile - 1
            if event.key is K_e:
                selected_tile = selected_tile + 1
            if event.key is K_SPACE:
                level[cursor_pos[0]][cursor_pos[1]][0] = selected_tile
                level[cursor_pos[0]][cursor_pos[1]][1] = current_rotation
                
            if event.key is K_r:
                current_rotation = current_rotation + 1
            
            if event.key is K_RETURN:
                print("yeah")
                
            if event.key is K_s:
                cursor_pos[0] = cursor_pos[0] + 1 
            if event.key is K_w:
                cursor_pos[0] = cursor_pos[0] - 1
            if event.key is K_a:
                cursor_pos[1] = cursor_pos[1] - 1
            if event.key is K_d:
                cursor_pos[1] = cursor_pos[1] + 1

            if current_rotation == 4:
                current_rotation = 0
            if selected_tile == -1:
                selected_tile = 9
            if selected_tile == 10:
                selected_tile = 0
            
    i = 0
    for row in level: # Render Tiles
        j = 0
        for tile in row:
            texture = textures[tile[0]]
            VIEWSURF.blit(textures[0],(j*25,i*25))
            if tile[0] == 6:
                VIEWSURF.blit(textures[3],(j*25,i*25))
            VIEWSURF.blit(pygame.transform.rotate(textures[tile[0]],tile[1]*-90),(j*25,i*25))
            j = j + 1
        i = i + 1

    i = 0

    

    VIEWSURF.blit(pygame.transform.rotate(textures[selected_tile],current_rotation*-90),(cursor_pos[1]*25,cursor_pos[0]*25))
    #VIEWSURF.blit(tutorial,(0,0))

    
    DISPLAYSURF.blit(pygame.transform.scale(VIEWSURF,(800,800)),(0,0))
    pygame.display.update()

