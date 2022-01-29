import pygame as pg
import os

pos = os.path.dirname(__file__) + "/"

pg.init()

#아이콘, 화면 크기, 재화 아이콘 크기
ic1size = 90
ic2size = 65
width = 1000
height = 562
msize = 45
character = [367, 477]

size = [width, height]
screen = pg.display.set_mode(size)
black = (0,0,0)

#재화량
moneyn = 1000000 #골드
clovern = 100000 #클로버
fullen = 15 #최대 에너지
nowen = 12 #현재 에너지
starn = 14 #핑크스타

#재화 콤마 표시 함수
def makepoint(num) :
    ns = len(str(num))
    res = ""
    nums = ns//3
    comma = 0
    if ns <= 3 :
        return str(num), 0, len(str(num))
    
    for i in range (nums) :
        res = "," + str(num)[ns-3*(i+1):ns-3*i] + res
        comma += 1
    if num//10**(nums*3) != 0 :
        res = str(num//10**(nums*3)) + res
    else :
        res = res[1:]
        comma -= 1
    return res, comma, len(res)-comma

#재화 글자 표시 함수
def display(arr, screen, yaxis, flags = None) :
    if flags == None :
        basic = 795 + 6*(2-arr[1]) + 13*(9-arr[2])
        for i in range (len(arr[0])) :
            text = font.render(arr[0][i], True, (255,255,255))
            if arr[0][i] == "," :
                basic += 12
                screen.blit(text,(basic,yaxis))  
                basic -= 6
            else :
                basic += 13
                screen.blit(text,(basic,yaxis))  
    else :
        basic = 785 + 6*(2-arr[1]-flags[1]) + 13*(9-arr[2]-flags[2])
        for i in range (len(arr[0])) :
            text = font.render(arr[0][i], True, (255,255,255))
            if arr[0][i] == "," :
                basic += 12
                screen.blit(text,(basic,yaxis))  
                basic -= 6
            else :
                basic += 13
                screen.blit(text,(basic,yaxis))

        text = font.render("/", True, (255,255,255))
        basic += 14
        screen.blit(text,(basic,yaxis))
        basic -= 4

        for i in range (len(flags[0])) :
            text = font.render(flags[0][i], True, (255,255,255))
            if arr[0][i] == "," :
                basic += 12
                screen.blit(text,(basic,yaxis))  
                basic -= 6
            else :
                basic += 13
                screen.blit(text,(basic,yaxis))


done = False
clock = pg.time.Clock()
pg.display.set_caption("UI Front Type")

#배경 이미지
backg = pg.image.load(pos + "images/" + "bg.jpg")
backg = pg.transform.scale(backg, (1000, 562))

#캐릭터 이미지
player = pg.image.load(pos + "images/" + "character.png")

#아이콘 이미지
icon1 = pg.image.load(pos + "images/" + "icon1.png")
icon2 = pg.image.load(pos + "images/" + "icon2.png")
icon3 = pg.image.load(pos + "images/" + "icon2.png")

#재화 이미지
gold = pg.image.load(pos + "images/" + "money.png")
clover = pg.image.load(pos + "images/" + "clover.png")
pinkstar = pg.image.load(pos + "images/" + "pinkstar.png")
energy = pg.image.load(pos + "images/" + "energy.png")

#좌상단 프로필 이미지
profile = pg.image.load(pos + "images/" + "profile.png")

while not done :

    for event in pg.event.get() :
        if event.type == pg.QUIT :
            done = True

    clock.tick(30)
    screen.blit(backg, (0,0))

    screen.blit(player,(300, 85))

    #좌하단 메뉴 표시
    screen.blit(icon1, (5, height - ic1size - 5))
    screen.blit(icon2, (ic1size + 10, height - ic2size - 5))
    screen.blit(icon3, (ic1size + ic2size + 15, height - ic2size - 5))

    #우하단 메뉴 표시
    screen.blit(icon1, (width - ic1size - 5, height - ic1size - 5))
    screen.blit(icon2, (width - ic1size - ic2size - 10, height - ic2size - 5))
    screen.blit(icon3, (width - ic1size - ic2size*2 - 15, height - ic2size - 5))

    #좌상단 아이콘 표시
    screen.blit(icon3, (width - ic2size - 5, height - ic1size - ic2size - 10))
    screen.blit(profile, (5, 5))

    #우상단 재화 표시
    #돈 표시
    pg.draw.rect(screen, black, [width - 210, 15, 205, 30])
    screen.blit(gold, (width - msize - 10, 5))

    #클로버 표시
    pg.draw.rect(screen, black, [width - 210, 20+msize, 205, 30])
    screen.blit(clover, (width - msize - 10, msize + 10))

    #에너지 표시
    pg.draw.rect(screen, black, [width - 210, 70+msize, 205, 30])
    screen.blit(energy, (width - msize - 5, msize * 2 + 15))

    #핑크스타 표시
    pg.draw.rect(screen, black, [width - 210, 120+msize, 205, 30])
    screen.blit(pinkstar, (width - msize - 10, msize * 3 + 20))

    font = pg.font.SysFont('hy견고딕',20)  #폰트 설정

    #자리수당 13, 8
    nummoney = makepoint(moneyn)
    display(nummoney, screen, 20) 
    

    numclover = makepoint(clovern)
    display(numclover, screen, 25 + msize) 

    numfulle = makepoint(fullen)
    numnowen = makepoint(nowen)
    display(numnowen, screen, 75 + msize, numfulle)

    numstar = makepoint(starn)
    display(numstar, screen, 125 + msize) 

    pg.display.update()

    

