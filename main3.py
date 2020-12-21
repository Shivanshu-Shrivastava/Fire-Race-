import pygame
import random
import math,time,random
from pygame import mixer

pygame.init()
# screen
screen =pygame.display.set_mode((800,600))
pygame.display.set_caption("RACING")
#pygame.draw.circle(screen,(255,0,0),(400,233),16)
clock=pygame.time.Clock()
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
lessgreen=(0,155,0)
red=(255,0,0)
lessred=(155,0,0)
#players
carImg=pygame.image.load("f1.png")
carX=350
carY=480
car_chan=0

#road
roadImg=pygame.image.load("road1.png")
roadX=-140
roadY=-90
rod_chan=3

#treee
treeImg=pygame.image.load("tree.png")
treeX=random.randint(230,235)
treeY=random.randint(80,82)
tree_chan=3

#circle
circleX=random.randint(380,700)
circleY=random.randint(0,300)
circle_chan=3
#cars
car1Img=pygame.image.load("f1 (1).png")
car1X=random.randint(300,600)
car1Y=200
car2X=350
car2Y=250
car3X=350
car3Y=300
car4X=350
car4Y=320
car2Img=pygame.image.load("f1 (2).png")
car3Img=pygame.image.load("f1 (3).png")
car4Img=pygame.image.load("f1 (4).png")
cars_chan=1
visible=""

#score

#scoredis=pygame.font.Font("freesansbold.ttf",20)
score_chan=0.5
score=0

def score_show(x,y,fontimt,string,scoreset=0):
    dispaly= pygame.font.Font("freesansbold.ttf", fontimt)
    if scoreset==0:
        scr = dispaly.render(string , True,(0,0,0))
    else:
        scr = dispaly.render(string + str(scoreset), True,(0,0,0))

    screen.blit(scr,(x,y))



def car(x,y):
    screen.blit(carImg,(x,y))
def road(x,y):
    screen.blit(roadImg,(x,y))
def tree(x,y):
    screen.blit(treeImg,(x,y))
def iscollison(x1,y1,x2,y2):
    distance=math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
    if distance<34:
        return True
def button(x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    mouse_press=pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if mouse_press[0]==1 and ac==green:
            #pygame.draw.rect(screen, black, (x, y+3, w, h))

            game_loop()
        if mouse_press[0] == 1 and ac == red:
            pygame.quit
            quit()

    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))
#thr end
def end():
    first=True
    screen.fill((255,255,255))
    while first:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit
                quit()

        score_show(300,200,60,"the end")
        score_show(400,300,32,"final score ",score)
        
        #time.sleep(4)
        #pygame.quit
        #quit()
        pygame.display.update()
#more cars

def more_cars(img,x,y):

    screen.blit(img,(x,y))


#game intro:
def game_intro():
    entre=True
    screen.fill((255,255,244))
    while entre:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit
                quit()
        score_show(150,100,60,"SATYAM RACE ")
        button(140,400,100,50,lessgreen,green)
        button(600,400,100,50,lessred,red)

        #mixer.music.load("starting.wav")
        #mixer.music.play(-1)


        score_show(620,420,15,"QUIT")
        score_show(160, 420, 15, "PLAY")
        pygame.display.update()





#game loop

running=True
def game_loop():
    global running,visible,car1Y,car1X,car2Y,car3Y,car4Y,cars_chan,score,score_chan,circle_chan,treeImg,tree_chan,treeX,treeY,carX,carY,carImg,car_chan,circleX,circleY,rod_chan,roadX,roadY
    #mixer.music.pause()
    while running:
        mixer.music.load("starting.wav")
        mixer.music.play(-1)
        screen.fill((0,0,0))
        sound1=mixer.Sound("carstart.wav")
        sound1.play(-1)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit
                quit()
        #movement
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    car_chan=-6
                if event.key == pygame.K_RIGHT:
                    car_chan=6
                if event.key==pygame.K_UP:
                    rod_chan+=3
                    tree_chan+=3
                    circle_chan+=3
                    score_chan+=1
                    cars_chan+=1
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    car_chan=0
                if event.key==pygame.K_UP:
                    rod_chan=3
                    tree_chan=3
                    circle_chan=3
                    score_chan=0.5
                    cars_chan=1



        #car4Y+=cars_chan



        ##score
        score+=score_chan
        #print(score)

        carX+=car_chan
        #movement of road
        roadY+=rod_chan
        if roadY>=-0.6:
            roadY=-100
        #movemnt  of tree
        treeY+=tree_chan
        #movemvt of circle
        circleY+=circle_chan

        #boundries
        if carX>=636:
            carX=636

        if carX<=210:
            carX=210
        if car4Y>650 and car4Y<653:
            visible=""
            car1X=random.randint(300,600)
            car1Y=200
            car2Y = 250
            car3Y = 300
            car4Y = 320

        #collison
        collisonT=iscollison(carX,carY,treeX,treeY)
        if collisonT==True:
            carY=2000
            end()
        collisonC=iscollison(carX,carY,circleX,circleY)
        if collisonC==True:
            carY = 2000
            end()
        collisonCar=iscollison(carX,carY,car1X,car4Y)
        if collisonCar==True:
            car4Y=2000
            carY=2000
            end()


        #reloop
        if circleY>=600:
            circleX=random.randint(380,700)
            circleY=random.randint(-800,400)
        if treeY>=600:
            treeY=random.randint(80,82)

        road(roadX,roadY)
        car(carX, carY)
        tree(treeX,treeY)



          # movement cars
        if visible=="":
            more_cars(car1Img, car1X, car1Y)

            car1Y += cars_chan
        if car1Y>=250: #and car1Y<120:
            car1Y=2000
            visible="ha1"
        if visible=="ha1":
            more_cars(car2Img, car1X, car2Y)
            car2Y += cars_chan

        if car2Y>=300: #and car2Y<190:
            car2Y=2000
            visible="ha2"
        if visible=="ha2":
            more_cars(car3Img, car1X, car3Y)
            car3Y+=cars_chan
        if car3Y>=320: #and car3Y<220:
            car3Y=2000
            visible="ha3"
        if visible=="ha3":
            more_cars(car4Img, car1X, car4Y)
            sound=mixer.Sound("bmw.wav")
            sound.play(0)
            sound.stop()
            car4Y+=cars_chan+1



        # movement cars

        #car1Y += 20


       # (x, y, dispaly, fontimt, string, scoreset=None):
        score_show(46,200,20,"score:: ",score)
        pygame.draw.circle(screen, (0, 0, 0), (circleX, circleY), 16)
        clock.tick(30)
        pygame.display.update()
game_intro()
game_loop()