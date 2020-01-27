import json, pygame, sys, pygame.transform
from pygame.locals import *

pygame.init()

VIEWSURF = pygame.Surface((400,400))

DISPLAYSURF = pygame.display.set_mode((800,800))
level = json.load(open("map.json"))

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

while True: # Main loop
    for event in pygame.event.get():
        if event.type is QUIT:
            pygame.quit()
            sys.exit()

    '''
    i = 0 # Reset Power
    for row in level:
        j = 0
        for tile in row:
            level[i][j][2] = 0
            j = j + 1
        i = i + 1
    '''
  
    i = 0
    for row in level: 
        j = 0
        for tile in row:
            if tile[0] == 8: # Cube
                if level[i+1][j][0] == 6 and level[i+1][j][1] == 0:
                    
                    level[i+1][j][2] = 1
                    finished = False

                if level[i][j-1][0] == 6 and level[i][j-1][1] == 1:
                    
                    level[i][j-1][2] = 1
                    finished = False

                if level[i-1][j][0] == 6 and level[i-1][j][1] == 2:
                    
                    level[i-1][j][2] = 1
                    finished = False

                if level[i][j+1][0] == 6 and level[i][j+1][1] == 3:
                    
                    level[i][j+1][2] = 1
                    finished = False

            if ( tile[0] == 3 or tile[0] == 6 or tile[0] == 4) and tile[2] == 1: # Powered Conduit, Powered Catcher and Powered Contact
                if level[i+1][j][0] == 3 or level[i+1][j][0] == 5 or level[i+1][j][0] == 6:
                    
                    level[i+1][j][2] = 1
                    finished = False
                    
                if level[i][j-1][0] == 3 or level[i][j-1][0] == 5 or level[i][j-1][0] == 6:
                    
                    level[i][j-1][2] = 1
                    finished = False

                if level[i-1][j][0] == 3 or level[i-1][j][0] == 5 or level[i-1][j][0] == 6:
                    
                    level[i-1][j][2] = 1
                    finished = False

                if level[i][j+1][0] == 3 or level[i][j+1][0] == 5 or level[i][j+1][0] == 6:
                    
                    level[i][j+1][2] = 1
                    finished = False
            if tile[0] == 5 and tile[2] == 1: # Powered Emmiter
                
                k = 0
                while True: # Shoot a beam until it hits something.
                    k = k + 1
                    if tile[1] == 0:

                        if level[i-k][j][0] == 0:
                            level[i-k][j][2] = 1
                        elif level[i-k][j][0] == 4 and level[i-k][j][1] == 2:
                            level[i-k][j][2] = 1
                            break
                        else:
                            break
                       
                    if tile[1] == 1:

                        if level[i][j+k][0] == 0:
                            level[i][j+k][2] = 1
                        elif level[i][j+k][0] == 4 and level[i][j+k][1] == 3:
                            level[i][j+k][2] = 1
                            break
                        else:
                            break

                        
                    if tile[1] == 2:

                        if level[i+k][j][0] == 0:
                            level[i+k][j][2] = 1
                        elif level[i+k][j][0] == 4 and level[i+k][j][1] == 0:
                            level[i+k][j][2] = 1
                            break
                        else:
                            break
                        
                    if tile[1] == 3:

                        if level[i][j-k][0] == 0:
                            level[i][j-k][2] = 1
                        elif level[i][j-k][0] == 4 and level[i][j-k][1] == 1:
                            level[i][j-k][2] = 1
                            break
                        else:
                            break
                    
                    
            j = j + 1
        i = i + 1
            


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
    for row in level: # Render Power Beams
        j = 0
        for tile in row:
            if tile[2] == 1:
                VIEWSURF.blit(textures[1],(j*25,i*25))
            j = j + 1
        i = i + 1

    #print(level)
    
    DISPLAYSURF.blit(pygame.transform.scale(VIEWSURF,(800,800)),(0,0))
    pygame.display.update()

