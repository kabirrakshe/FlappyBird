import pygame
import random


pygame.init()
canvas = pygame.display.set_mode((500,500))
green = (0,255,0)
white = (255,255,255)
moving = 500
moving2 = 650
moving3 = 800
moving4 = 950
pipeaheight = random.choice(range(200,400))
pipebheight = random.choice(range(200,400))
pipecheight = random.choice(range(200,400))
pipedheight = random.choice(range(200,400))
font = pygame.font.SysFont('comicsans', 80, True)
bg = pygame.transform.smoothscale(pygame.image.load('bg.jpg'), (500,550)).convert()
title = pygame.transform.smoothscale(pygame.image.load('title.png'), (450,90))
startbutton = pygame.image.load('startbutton.png')
bigstartbutton = pygame.transform.scale(pygame.image.load('startbutton.png'), (462,253))
birdie = pygame.transform.smoothscale(pygame.image.load('birdie.png').convert(), (40,30))
birdie2 = pygame.transform.smoothscale(pygame.image.load('birdie2.png').convert(), (40,30))
reset = pygame.transform.smoothscale(pygame.image.load('reset.png'), (200,79))
setup = pygame.transform.smoothscale(pygame.image.load('Setup.png'), (150,50))
bigsetup = pygame.transform.smoothscale(pygame.image.load('Setup.png'), (225,75))
pipe = pygame.image.load('pipe.png').convert()
pipe2 = pygame.transform.flip(pipe, False, True).convert()



class pipeobject():
    def __init__(self, position, pipeheight,birdheight):
        self.birdheight = birdheight
        self.position = position
        self.pipeheight = pipeheight
    def drawpipe(self):
        canvas.blit(pipe, (self.position, self.pipeheight))
        canvas.blit(pipe2, (self.position, -1*(450 - self.pipeheight)))
    def scoreincrease(self):
        if self.position == 160:return True
    def collidecheck(self):
        piperect = pygame.draw.rect(canvas, (192, 192, 192,255), (self.position, self.pipeheight, 52, 320), 1)
        piperect2 = pygame.draw.rect(canvas, (192, 192, 192,255), (self.position, self.pipeheight-450, 52, 320), 1)
        birdrect = pygame.draw.rect(canvas, (192, 192, 0,255), (160, self.birdheight+15, 28, 16), 1)
        if birdrect.colliderect(piperect) or birdrect.colliderect(piperect2):
            return True


def illustrate(bheight, activate, rotated, scoring, countgreater):
    global pipeaheight, pipebheight, pipecheight, pipedheight, moving, moving2, moving3, moving4
    canvas.fill((0,0,0))
    text = font.render(str(scoring), 1, white)
    canvas.blit(bg, (0,0))


    if activate == True: canvas.blit(pygame.transform.rotate(birdie2, 30),(150, bheight))
    else: canvas.blit(pygame.transform.rotate(birdie, 30+rotated),(150,bheight))
    if countgreater >= 100:
        moving -= 2
        moving2 -= 2
        moving3 -= 2
        moving4 -= 2

        pipea = pipeobject(moving, pipeaheight, bheight)
        pipeb = pipeobject(moving2, pipebheight, bheight)
        pipec = pipeobject(moving3, pipecheight, bheight)
        piped = pipeobject(moving4, pipedheight, bheight)


        pipea.drawpipe()
        pipeb.drawpipe()
        pipec.drawpipe()
        piped.drawpipe()
        if pipea.collidecheck() == True: return 'collision'
        elif pipeb.collidecheck() == True: return 'collision'
        elif pipec.collidecheck() == True: return 'collision'
        elif piped.collidecheck() == True: return 'collision'
        if pipea.scoreincrease() == True or pipeb.scoreincrease()==True or pipec.scoreincrease()==True or piped.scoreincrease()==True:
            return True

        if moving == -50:
            pipeaheight = random.choice(range(200,400))
            moving = moving4 + 150
        elif moving2 == -50:
            pipebheight = random.choice(range(200,400))
            moving2 = moving + 150
        elif moving3 == -50:
            pipecheight = random.choice(range(200,400))
            moving3 = moving2 + 150
        elif moving4 == -50:
            pipedheight = random.choice(range(200,400))
            moving4 = moving3 + 150
    canvas.blit(text, (230,50))
    pygame.display.update()





def Introduction():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and x in range(40,460) and y in range(135,365): return
        canvas.blit(bg, (0,0))
        x,y = pygame.mouse.get_pos()
        if x in range(40,460) and y in range(135,365):
            canvas.blit(bigstartbutton, (19, 126))
        else:
            canvas.blit(startbutton, (40,135))
        canvas.blit(title, (25,50))
        pygame.draw.rect(canvas, (0,0,0), (25,50, 450, 90), 10)
        pygame.display.update()
        canvas.fill((0,0,0))

# def endingscreen():
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT: pygame.quit()
#         xx,yy = pygame.mouse.get_pos()
#         canvas.blit(bg, (0,0))
#         canvas.blit(setup, (200,200))
#         canvas.blit(leaderboards, (150,300))
#         canvas.blit(reset, (0,0))
#         pygame.display.update()
#         canvas.fill((0,0,0))



def main():
    count = 0
    gravity = 0
    height = 250
    jumpfactor = 13
    activation = False
    rotationfactor = 0
    score = 0
    Introduction()
    while True:
        count += 1
        rotationfactor -= 1


        for event in pygame.event.get():
            if event.type == pygame.QUIT: break

        keys = pygame.key.get_pressed()

        if count %5 == 0: ###Increases downward pull
            gravity += 1
        height += gravity


        if height >= 490: break


        if activation == True: ###if space bar pressed
            height -= jumpfactor
            jumpfactor -= 1
            rotationfactor = 0
            if jumpfactor == 1:
                activation = False
                jumpfactor = 13
                gravity = 0

        elif keys[pygame.K_SPACE] and height >= 0: ###Activates Jump
            activation = True
            gravity = 0
            rotationfactor = 0


        result = illustrate(height, activation, rotationfactor, score, count) ###draws the sprites
        if result == True: score += 1
        if result == 'collision': break




main()
pygame.quit()
