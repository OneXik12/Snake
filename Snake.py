
import random
import pygame

def waz():
    pygame.init()
    oknoGry=pygame.display.set_mode((600,600),0,32)
    pygame.display.set_caption("Gra Wąż")
    run=True
    zmiennaX=300
    zmiennaY=300
    jablkoX=random.randint(0,19)*30
    jablkoY=random.randint(0,19)*30

    punkty = 0
    while(run):

        oknoGry.fill((0,0,0))
        pygame.time.delay(1)
        for zdarzenia in pygame.event.get():
            if zdarzenia.type==pygame.QUIT:
                run=False
            elif zdarzenia.type==pygame.KEYDOWN:
                if zdarzenia.key==pygame.K_RIGHT and zmiennaX<570:
                    zmiennaX += 30
                elif zdarzenia.key==pygame.K_LEFT and zmiennaX > 0:
                    zmiennaX -= 30
                elif zdarzenia.key==pygame.K_UP and zmiennaY > 0:
                    zmiennaY -= 30
                elif zdarzenia.key==pygame.K_DOWN and zmiennaY < 570:
                    zmiennaY += 30
        ksztaltWaz=pygame.Rect((zmiennaX,zmiennaY),(30,30))
        pygame.draw.rect(oknoGry,(100,100,100),ksztaltWaz)
        if zmiennaX==jablkoX and zmiennaY == jablkoY:
            jablkoX=random.randint(0,19)*30
            jablkoY=random.randint(0,19)*30
            punkty += 1
    
        pygame.draw.circle(oknoGry,(255,0,0),(jablkoX+15,jablkoY+15),15)

        czcionka  = pygame.font.SysFont('arial', 25)
        tekst = czcionka.render("Zdobyłeś punkty {0}".format(zmiennaX), 1, (200,200,200))
        oknoGry.blit(tekst, (10,10))
         
        pygame.display.update()

waz()