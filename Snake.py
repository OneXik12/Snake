
import random
import pygame

def waz():
    pygame.init()
    oknoGry=pygame.display.set_mode((600,600),0,32)
    pygame.display.set_caption("Gra Wąż")
    run=True

    zmiennaX=300
    zmiennaY=300

    pozycjeWaz = [(zmiennaX,zmiennaY)]
    dlugoscWaz = 1

    jablkoX=random.randint(0,19)*30
    jablkoY=random.randint(0,19)*30

    punkty = 0
    # 10 - prawo, -10 - lewo, 01 - dół, 0-1 - góra
    kierunek = [1,0]
    while(run):

        oknoGry.fill((0,0,0))
        pygame.time.delay(200)
        for zdarzenia in pygame.event.get():
            if zdarzenia.type==pygame.QUIT:
                run=False
            elif zdarzenia.type==pygame.KEYDOWN:
                if zdarzenia.key==pygame.K_RIGHT:
                    kierunek = [1,0]
                elif zdarzenia.key==pygame.K_LEFT:
                    kierunek = [-1,0]
                elif zdarzenia.key==pygame.K_UP:
                    kierunek = [0,-1]
                elif zdarzenia.key==pygame.K_DOWN:
                    kierunek = [0,1]

        zmiennaX = zmiennaX + kierunek[0]*30
        zmiennaY = zmiennaY + kierunek[1]*30

        if zmiennaX >= 600:
            zmiennaX = 0
        if zmiennaX < 0:
            zmiennaX = 600 - 30
        if zmiennaY >= 600:
            zmiennaY = 0
        if zmiennaY < 0:
            zmiennaY = 600 - 30
        ksztaltWaz=pygame.Rect((zmiennaX,zmiennaY),(30,30))
        pygame.draw.rect(oknoGry,(1,250,100),ksztaltWaz)

        pozycjeWaz.append((zmiennaX,zmiennaY))

        if zmiennaX==jablkoX and zmiennaY == jablkoY:
            jablkoX=random.randint(0,19)*30
            jablkoY=random.randint(0,19)*30
            punkty += 1
            dlugoscWaz = dlugoscWaz + 1
    
        pygame.draw.circle(oknoGry,(255,0,0),(jablkoX+15,jablkoY+15),15)

        if len(pozycjeWaz) > dlugoscWaz:
            del pozycjeWaz[0]
        
        for poz in pozycjeWaz[::-1]:
            ksztaltWaz = pygame.Rect((poz[0],poz[1]),(30,30))
            pygame.draw.rect(oknoGry,(100,100,100), ksztaltWaz)


        czcionka  = pygame.font.SysFont('arial', 25)
        tekst = czcionka.render("Zdobyłeś punkty {0}".format(punkty), 1, (200,200,200))
        oknoGry.blit(tekst, (10,10))
         
        pygame.display.update()

waz()
