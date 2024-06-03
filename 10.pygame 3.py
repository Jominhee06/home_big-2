# 게임 조건
# 1. 캐릭터는 화면 아래에 위치, 좌우로만 이동 가능
# 2. 스페이스를 누르면 무기를 쏘아 올림
# 3. 큰 공 1개가 나타나서 바운스
# 4. 무기에 닿으면 공은 작은 크기 2개로 분할, 가장 작은 크기의 공은 사라짐
# 5. 모든 공을 없애면 게임 종료(성공)
# 6. 캐릭터는 공에 닿으면 게임 종료(실패)
# 7. 시간 제한 99초 초과 시 게임 종료(실패)
# 8. FPS는 30 으로 고정 (필요시 spped 값을 조정)

import os
import pygame

##########################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 640  # 가로 크기 설정
screen_height = 480 # 세로 크기 설정
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Pang")

# FPS
clock = pygame.time.Clock()
############################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path , "backgrounds.png"))


# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용


running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 3. 게임 캐릭터 위치 정의 
    
    # 4. 충돌처리    
    
    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    pygame.display.update() # 게임화면을 다시 그리기!
    clock.tick(60)

# pygame 종료
pygame.quit()