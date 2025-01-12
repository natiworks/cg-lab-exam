import pygame
from pygame.locals import *

def main():
   
    pygame.init()

    
    canvas = pygame.display.set_mode((500, 400))  
    pygame.display.set_caption("Canvas Title")    

   
    white = (255, 255, 255)
    red = (255, 0, 0)

    
    canvas.fill(white)

    
    start_pos = (50, 50)
    end_pos = (50 + 200, 50)  
    pygame.draw.line(canvas, red, start_pos, end_pos, 3)

    
    pygame.display.update()

    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:  
                running = False
            elif event.type == KEYDOWN:  
                if event.key == K_F1:
                    running = False

    
    pygame.quit()


if __name__ == "__main__":
    main()
