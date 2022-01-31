import pygame,sys,random,time
pygame.init()
from moviepy.editor import *
pygame.mixer.music.load("./sounds/Starwars.mp3") # 背景音乐
pygame.mixer.music.play(-1)
screen = pygame.display.set_mode(size = (1280,720),flags = pygame.FULLSCREEN)
# screen = pygame.display.set_mode(size = (1280,720))
pygame.display.set_caption("星球大战")
clip = VideoFileClip('./images/星球大战开场.gif')
clip= clip.resize(newsize = (screen.get_size()[0],screen.get_size()[1]))
clip.preview(fullscreen=True)
# clip.preview()
logo = pygame.image.load("./images/星球大战logo.png")
up = pygame.image.load("./images/up.png")
down = pygame.image.load("./images/down.png")
button1 = pygame.image.load("./images/1.png").convert()
button1.set_alpha(100)
button1_rect = button1.get_rect(x = 20,y = 100)
button1_cover = pygame.image.load("./images/tie.png")
button4 = pygame.image.load("./images/4.png").convert()
button4.set_alpha(100)
button4_rect = button4.get_rect(x = 965,y = 100)
logo_width = 1280
logo_height = 720
logo_x = 0
logo_y = 0
startlist = [up,down]
startrect = pygame.Rect(503,500,300,41)
startimg = startlist[0]
x1 = 0
y1 = 0
try:
    import ntpath # 如果成功，那么是Windows
    FONTNAME = "kaiti"
    del ntpath
except ImportError: # 如果失败，是MacOS
    FONTNAME = "kaittf"
exitrect = pygame.Rect(0,0,40,20)
color = (0,0,0)
class Star():
    def __init__(self):
        self.rect = pygame.Rect(random.randint(1,1280),random.randint(1,720),1,1)
    def show(self):
        pygame.draw.ellipse(screen,(255,255,255),self.rect,0)
    def trail(self):
        if self.rect.x<640 and self.rect.x!=0:
            self.rect.x-=640/self.rect.x
        if self.rect.x>640:
            self.rect.x+=640/(self.rect.x-640)
        if self.rect.y<360 and self.rect.y != 0:
            self.rect.y-=360/self.rect.y
        if self.rect.y>360:
            self.rect.y+=360/(self.rect.y-360)
star = []
for i in range(200):
    star.append(Star())

logo1 = pygame.transform.scale(logo,(356,200))
def show_buttons():
    screen.blit(button1, button1_rect)
    screen.blit(button1_cover, (25, 150))
    screen.blit(pygame.font.SysFont(FONTNAME, 40).render("躲避钛战机", True, (0, 0, 0)), (67.5, 450))
    screen.blit(pygame.font.SysFont(FONTNAME, 30).render("难度:小", True, (0, 0, 0)), (67.5, 500))
    screen.blit(pygame.font.SysFont(FONTNAME, 30).render("可玩性:小", True, (0, 0, 0)), (67.5, 540))
    screen.blit(pygame.font.SysFont(FONTNAME, 30).render("交互性:低", True, (0, 0, 0)), (67.5, 580))
    screen.blit(button4, button4_rect)
    pygame.draw.rect(screen, color, exitrect, 0)
    pygame.draw.rect(screen, (255, 255, 255), exitrect, 3)
    screen.blit(pygame.font.SysFont(FONTNAME, 20).render("退出", True, (255, 255, 255)), exitrect)
if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if logo_height > 200:
            logo_width = logo_width - 16
            logo_height = logo_height - 9
            logo_x = logo_x + 8
            logo_y = logo_y + 4.5
        if logo_height <= 200:
        # if 1==1:
            out_flag = False
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEMOTION:
                        x1 = event.pos[0]
                        y1 = event.pos[1]
                    if startrect.collidepoint(x1,y1):
                        startimg = startlist[1]
                        screen.blit(startimg,startrect)
                        pygame.display.update()
                    if not startrect.collidepoint(x1,y1):
                        startimg = startlist[0]
                    if exitrect.collidepoint(x1,y1):
                        color = (255,0,0)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button==1:
                                pygame.quit()
                                sys.exit()
                    if startrect.collidepoint(x1,y1):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button==1:
                                out_flag = True
                    if not exitrect.collidepoint(x1,y1):
                        color = (0,0,0)
                screen.fill((0,0,0))
                for i in star:
                    i.show()
                screen.blit(startimg,startrect)
                pygame.draw.rect(screen,color,exitrect,0)
                pygame.draw.rect(screen,(255,255,255),exitrect,3)
                screen.blit(pygame.font.SysFont(FONTNAME,20).render("退出",True,(255,255,255)),exitrect)
                screen.blit(logo1,(logo_x,logo_y))
                if out_flag == True:
                    break;
                pygame.display.update()
            out_flag = False
            # t1 = time.time()
            # t2 = time.time()
            # while True:
            #     for event in pygame.event.get():
            #         if event.type == pygame.QUIT:
            #             pygame.quit()
            #             sys.exit()
            #     for i in star:
            #         i.trail()
            #         i.show()
            #     if t2-t1>0.1:
            #         break;
            #     pygame.display.update()
            #     t2 = time.time()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if logo_height > 36:
                    logo_width = logo_width - 64
                    logo_height = logo_height - 36
                    logo_x = logo_x + 32
                    logo_y = logo_y + 18
                else:
                    out_flag = True
                screen.fill((0, 0, 0))
                for i in star:
                    i.show()
                logo1 = pygame.transform.scale(logo,(logo_width,logo_height))
                screen.blit(startimg, startrect)
                pygame.draw.rect(screen, color, exitrect, 0)
                pygame.draw.rect(screen, (255, 255, 255), exitrect, 3)
                screen.blit(pygame.font.SysFont(FONTNAME, 20).render("退出", True, (255, 255, 255)), exitrect)
                screen.blit(logo1, (logo_x, logo_y))
                if out_flag == True:
                    break;
                pygame.display.update()
            out_flag = False
            game = 0
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEMOTION:
                        x1 = event.pos[0]
                        y1 = event.pos[1]
                    if exitrect.collidepoint(x1, y1):
                        color = (255, 0, 0)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                pygame.quit()
                                sys.exit()
                    if not exitrect.collidepoint(x1, y1):
                        color = (0, 0, 0)
                    if button1_rect.collidepoint(x1,y1):
                        button1.set_alpha(150)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                out_flag = True
                                game = 1
                    if not button1_rect.collidepoint(x1,y1):
                        button1.set_alpha(100)
                screen.fill((0, 0, 0))
                for i in star:
                    i.show()
                if out_flag == True:
                    break
                show_buttons()
                pygame.display.update()
            if game == 1:
                tie_x = 1280
                black_rect = pygame.Rect(1280,0,2980,720)
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEMOTION:
                            x1 = event.pos[0]
                            y1 = event.pos[1]
                        if exitrect.collidepoint(x1, y1):
                            color = (255, 0, 0)
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    pygame.quit()
                                    sys.exit()
                        if not exitrect.collidepoint(x1, y1):
                            color = (0, 0, 0)
                    screen.fill((0,0,0))
                    show_buttons()
                    black_rect = pygame.Rect(tie_x, 0, 2980, 720)
                    pygame.draw.rect(screen,(0,0,0),black_rect,0)
                    screen.blit(button1_cover,(tie_x,200))
                    tie_x-=10;
                    if tie_x <= -300:
                        break;
                    for i in star:
                        i.show()
                    pygame.display.update()
                import game1
        screen.fill((0,0,0))
        for i in star:
            i.show()
        logo1 = pygame.transform.scale(logo,(logo_width,logo_height))
        screen.blit(logo1,(logo_x,logo_y))
        pygame.display.update()