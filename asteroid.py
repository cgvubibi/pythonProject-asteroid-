from time import time
import pygame
import sys
import random


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()   #pygame 초기화
pygame.display.set_caption('SpaceShuttle')  #창 제목

#창크기
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

imgShuttle = pygame.image.load('choonsik.png')
img_width = imgShuttle.get_width()
img_height = imgShuttle.get_height()

imgStone1 = pygame.image.load('stone1.png')
stone1_width = imgStone1.get_width()
stone1_height = imgStone1.get_height()

imgStone2 = pygame.image.load('stone2.png')
stone2_width = imgStone2.get_width()
stone2_height = imgStone2.get_height()


myFont = pygame.font.SysFont("arial", 30, True, False)

clock = pygame.time.Clock()

# 행성 충돌 방지 구역 (로켓의 위치와 행성이 겹쳐 생성되지 않도록 설정 )
#행성 위치
loc_rock = []
for i in range(5):
    SCREEN_WIDTH_N = random.choice(list(range(1,int(SCREEN_WIDTH/2/2))) + list(range(int(SCREEN_WIDTH/2) + int(SCREEN_WIDTH/2/2), SCREEN_WIDTH)))
    SCREEN_HEIGHT_N = random.choice(list(range(1,int(SCREEN_HEIGHT/2/2))) + list(range(int(SCREEN_HEIGHT/2) + int(SCREEN_HEIGHT/2/2), SCREEN_HEIGHT)))
    #print(SCREEN_WIDTH_N,SCREEN_HEIGHT_N )
    loc_rock.append([SCREEN_WIDTH_N,SCREEN_HEIGHT_N]) 
size_rock = 10

totalRock = len(loc_rock)
rockVelocity = 5

#로켓 위치
loc_ship = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2] 
size_ship = 20
vel = []
for i in range(5): 
    a = random.randint(0, 3)
    if a == 0:
        vel.append([5,5])
    elif a == 1:
        vel.append([-5,5])
    elif a == 2:
        vel.append([5,-5])
    elif a == 3:
        vel.append([-5,-5])
     
#충돌판단 
def collision_check(loc_rock, size_rock, loc_ship, size_ship):
    dist_x = loc_rock[0] - loc_ship[0]
    dist_y = loc_rock[1] - loc_ship[1]
    
    dist = (dist_x**2 + dist_y**2)**(0.5)
    
    if dist < (size_rock + size_ship):
        collision_text = myFont.render("collision", 1, (255,0,0))
        screen.blit(collision_text, [20, 20])
        
        print("충돌시간: " + timeDiff)
        
startTime = time()

while True:
    clock.tick(30)
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        loc_ship[0] -= 5
        
        #대각선 처리
        if keys[pygame.K_UP]:
            loc_ship[1] -= 5
        elif keys[pygame.K_DOWN]:
            loc_ship[1] += 5
            
    elif keys[pygame.K_RIGHT]:
        loc_ship[0] += 5
        
        #대각선 처리
        if keys[pygame.K_UP]:
            loc_ship[1] -= 5
        elif keys[pygame.K_DOWN]:
            loc_ship[1] += 5
    
    elif keys[pygame.K_UP]:
        loc_ship[1] -= 5
    elif keys[pygame.K_DOWN]:
        loc_ship[1] += 5
    
    elif keys[pygame.K_q]:          #q 입력
        pygame.quit()               #pygame을 종료한다
        sys.exit()
    
    for event in pygame.event.get():    #발생한 입력 event 목록의  event마다 검사
        if event.type == pygame.QUIT:   #event의 type이 QUIT에 해당할 경우
            pygame.quit()               #pygame을 종료한다
            sys.exit()
 

    #행성 태두리 충돌
    for i in range(totalRock):
        if i % 2 == 0:
            screen.blit(imgStone1, [ loc_rock[i][0] - stone1_width/2 , loc_rock[i][1] - stone1_height/2])
        else:
            screen.blit(imgStone2, [ loc_rock[i][0] - stone2_width/2 , loc_rock[i][1] - stone2_height/2])
            # 운석을 그린다
        pygame.draw.circle(screen, (255,255,255), loc_rock[i], size_rock) # 운석을 그린다
        
        loc_rock[i][0] = loc_rock[i][0] + vel[i][0]
        loc_rock[i][1] = loc_rock[i][1] + vel[i][1]

    for i in range(totalRock):
        print(totalRock)
        #행성이 꼭지점에 도달할시 발생하는 오류 확인
        # 꼭지점에 관한 예외처리
        if loc_rock[i][0] >= SCREEN_WIDTH and loc_rock[i][1] >= SCREEN_HEIGHT:
            vel[i][0] = -vel[i][0]
            vel[i][1] = -vel[i][1]
        elif loc_rock[i][0] >= SCREEN_WIDTH and loc_rock[i][1] <= 0:
            vel[i][0] = -vel[i][0]
            vel[i][1] = -vel[i][1]
        elif loc_rock[i][0] <= 0 and loc_rock[i][1] >= SCREEN_HEIGHT:
            vel[i][0] = -vel[i][0]
            vel[i][1] = -vel[i][1]
        elif loc_rock[i][0] <= 0 and loc_rock[i][1] <= 0:
            vel[i][0] = -vel[i][0]
            vel[i][1] = -vel[i][1]
            
        if loc_rock[i][0] >= SCREEN_WIDTH:
            vel[i][0] = -vel[i][0]
        elif loc_rock[i][0] <= 0:
            vel[i][0] = -vel[i][0] 
        elif loc_rock[i][1] >= SCREEN_HEIGHT:
            vel[i][1] = -vel[i][1]
        elif loc_rock[i][1] <= 0:
            vel[i][1] = -vel[i][1]
    
    #행성 수 
    #print(totalRock)
    #행성 수 증가
    if round(time() - startTime,2) % 15 == 0:
        totalRock += 1
    
    if totalRock != len(loc_rock):
       
        loc_rock.append([2,2])
        
        a = random.randint(0, 3)
        if a == 0:
            vel.append([rockVelocity,rockVelocity])
        elif a == 1:
            vel.append([-rockVelocity,rockVelocity])
        elif a == 2:
            vel.append([rockVelocity,-rockVelocity])
        elif a == 3:
            vel.append([-rockVelocity,-rockVelocity])
            
        addRock_text = myFont.render("Rock +1", 1, (255,0,0))
        for i in range(10):
            screen.blit(addRock_text, [20, 20])
    print(loc_rock)
    
    #속도 증가
    if round(time() - startTime,2) % 10 == 0:
        for i in range(len(vel)):
            if vel[i][0] < 0:
                vel[i][0] = vel[i][0] - 2
            elif vel[i][0] > 0:
                vel[i][0] = vel[i][0] + 2
            if vel[i][1] < 0:
                vel[i][1] = vel[i][1] - 2
            elif vel[i][1] > 0:
                vel[i][1] = vel[i][1] + 2
        rockVelocity += 2
        
        SpeedUP_text = myFont.render("Speed UP!! ", 1, (255,0,0))
        for i in range(10):
            screen.blit(SpeedUP_text, [20, 20])
    print(vel)
    
    x = loc_ship[0] - img_width/2
    y = loc_ship[1] - img_height/2
    screen.blit(imgShuttle, [x , y])
    
    pygame.draw.circle(screen, (255,255,255), loc_ship, size_ship,1)# 로켓 
    
    # 행성의 수 표시
    totalRock_text = myFont.render("Rock: " + str(totalRock), 1, (255,255,255))
    screen.blit(totalRock_text, [SCREEN_WIDTH-320, 20])
    
    # 속도 표시
    currentVelocity_text = myFont.render("Speed: " + str(rockVelocity), 1, (255,255,255))
    screen.blit(currentVelocity_text, [SCREEN_WIDTH-210, 20])
    
    #시간 표시
    timeDiff = str(round(time() - startTime,2))
    currentTime_text = myFont.render(timeDiff, 1, (255,255,255))
    screen.blit(currentTime_text, [SCREEN_WIDTH-80, 20])
    
    #충돌 분석 함수 호출
    for i in range(totalRock):
        collision_check(loc_rock[i], size_rock, loc_ship, size_ship)
        
    pygame.display.update() # 화면을 업데이트한다
