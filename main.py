import pygame

pygame.init()
pygame.font.init()
current = ["currency         V", "EUR €", "USD $", "CAD $", "YEN ¥", "WON ₩", "RUB ₽", "CHF ₣"]
percent = [[-1.0, -1.00, -1.0, -1.0 , -1.0, -1.00, -1.0], 
           [1, 1.090, 1.45, 141.71, 1336.53, 76.02, 1.0], 
           [0.92, 1, 1.33, 130.36, 1229.06, 69.92, 0.92],
           [0.69, 0.75, 1, 97.690, 921.09, 52.40, 0.690],
           [0.0071, 0.0077, 0.010, 1, 9.43, 0.54, 0.071],
           [.00075, .00081, .0011, .11, 1, .057, .00075],
           [0.013, 0.014, 0.019, 1.860, 17.58, 1, 0.013],
           [1, 1.090, 1.45, 141.71, 1336.53, 76.02, 1.0]]

my_font = pygame.font.SysFont('Comic Sans MS', 18)
second_font = pygame.font.SysFont("Comic Sans Ms", 12)
B = pygame.font.SysFont("Comic Sans Ms", 20)
screen = pygame.display.set_mode([500, 300])
running = True
l = ["Amount", "From Currency :", "To Currency :", "Converted Amount :"]
L = ["Conver", "Clear All"]
screen.fill((230,229,229))
for a in range(3):
    text_surface = my_font.render(l[a], False, (0,)*3)
    screen.blit(text_surface, (70, 40 + 40 * a))
    if a == 0:
        pygame.draw.rect(screen, (222,)*3, (250, 42 + 40 * a, 1, 26))
        pygame.draw.rect(screen, (205,)*3, (250, 40 + 40 * a, 149, 1))
        pygame.draw.rect(screen, (234, 233, 233), (351, 40 + 40 * a, 1, 26))
        pygame.draw.rect(screen, (166,)*3, (251, 41 + 40 * a, 149, 26))
        pygame.draw.rect(screen, (249,)*3, (252, 42 + 40 * a, 149, 26))
        pygame.draw.rect(screen, (255,)*3, (252, 42 + 40 * a, 148, 25))
    else:
        pygame.draw.rect(screen, (240,)*3, (250, 40 + 40 * a, 150, 30))
        pygame.draw.rect(screen, (250,)*3, (252, 42 + 40 * a, 144, 24))
        pygame.draw.rect(screen, (130,)*3, (253, 44 + 40 * a, 144, 24))
        pygame.draw.rect(screen, (238,)*3, (253, 43 + 40 * a, 142, 22))
        pygame.draw.rect(screen, (157,)*3, (254, 44 + 40 * a, 142, 22))
        pygame.draw.rect(screen, (240,)*3, (254, 44 + 40 * a, 141, 21))
        text_surface = second_font.render("currency"+" "*9+"V", False, (0,)*3)
        screen.blit(text_surface, (290, 46 + 40 * a))

text_surface = my_font.render(l[3], False, (0,)*3)
screen.blit(text_surface, (70 , 200))
pygame.draw.rect(screen, (222, 221, 221), (250, 202, 1, 26))
pygame.draw.rect(screen, (205,)*3, (250, 200, 149, 1))
pygame.draw.rect(screen, (234, 233, 233), (351, 200, 1, 26))
pygame.draw.rect(screen, (166,)*3, (251, 201, 149, 26))
pygame.draw.rect(screen, (249,)*3, (252, 202, 149, 26))
pygame.draw.rect(screen, (255,)*3, (252, 202, 148, 25))

pygame.draw.rect(screen, (155, 155, 246), (130, 156, 100, 40))
pygame.draw.rect(screen, (43, 43, 255), (132, 157, 96, 1))
pygame.draw.rect(screen, (68, 68, 255), (131, 158, 1, 38))
pygame.draw.rect(screen, (192, 191, 191), (130, 197, 99, 1))
pygame.draw.rect(screen, (34, 34, 48), (131, 196, 98, 1))
pygame.draw.rect(screen, (0, 0, 12), (228, 157, 1, 39))
pygame.draw.rect(screen, (0, 0, 255), (132, 158, 96, 38))
text_surface = B.render("Convert", False, (255,)*3)
screen.blit(text_surface, (145, 160))

pygame.draw.rect(screen, (240,)*3, (130, 238, 100, 40))
pygame.draw.rect(screen, (255,)*3, (131, 239, 98, 38))
pygame.draw.rect(screen, (9,)*3, (130, 277, 100, 1))
pygame.draw.rect(screen, (42,)*3, (229, 238, 1, 40))
pygame.draw.rect(screen, (171, 170, 170), (230, 238, 1, 40))
pygame.draw.rect(screen, (198, 197, 197), (130, 278, 100, 1))
pygame.draw.rect(screen, (133,)*3, (131, 276, 98, 1))
pygame.draw.rect(screen, (162,)*3, (228, 238, 1, 39))
text_surface = B.render("Clear", False, (255, 0, 0))
screen.blit(text_surface, (155,240))

pygame.display.flip()
x = 0
value = ""
valuable = [str(a) for a in range(10)]+["."]
N = [0,0]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            xy = pygame.mouse.get_pos()
            if 249 < xy[0] < 400 and 40 < xy[1] < 70:
                x = 1
            elif 249 < xy[0] < 400 and 80 < xy[1] < 110 and x != 2:
                x = 2
            elif x == 2 and 249 < xy[0] < 400 and 80 < xy[1] < 236:
                for a in range(7):
                    if (80 + 26 * a) < xy[1] < (106 + 26 * a):
                        N[0] = a + 1
                        x = 0
                        screen.fill((230,229,229))
                        for a in range(3):
                            text_surface = my_font.render(l[a], False, (0,)*3)
                            screen.blit(text_surface, (70, 40 + 40 * a))
                            if a == 0:
                                pygame.draw.rect(screen, (222,)*3, (250, 42 + 40 * a, 1, 26))
                                pygame.draw.rect(screen, (205,)*3, (250, 40 + 40 * a, 149, 1))
                                pygame.draw.rect(screen, (234, 233, 233), (351, 40 + 40 * a, 1, 26))
                                pygame.draw.rect(screen, (166,)*3, (251, 41 + 40 * a, 149, 26))
                                pygame.draw.rect(screen, (249,)*3, (252, 42 + 40 * a, 149, 26))
                                pygame.draw.rect(screen, (255,)*3, (252, 42 + 40 * a, 148, 25))
                                text_surface = second_font.render(value, False, (0,)*3)
                                screen.blit(text_surface, (390 - 7 * len(value),50))
                            else:
                                pygame.draw.rect(screen, (240,)*3, (250, 40 + 40 * a, 150, 30))
                                pygame.draw.rect(screen, (250,)*3, (252, 42 + 40 * a, 144, 24))
                                pygame.draw.rect(screen, (130,)*3, (253, 44 + 40 * a, 144, 24))
                                pygame.draw.rect(screen, (238,)*3, (253, 43 + 40 * a, 142, 22))
                                pygame.draw.rect(screen, (157,)*3, (254, 44 + 40 * a, 142, 22))
                                pygame.draw.rect(screen, (240,)*3, (254, 44 + 40 * a, 141, 21))
                                text_surface = second_font.render(current[N[a-1]], False, (0,)*3)
                                screen.blit(text_surface, (290, 46 + 40 * a))

                        text_surface = my_font.render(l[3], False, (0,)*3)
                        screen.blit(text_surface, (70 , 200))
                        pygame.draw.rect(screen, (222, 221, 221), (250, 202, 1, 26))
                        pygame.draw.rect(screen, (205,)*3, (250, 200, 149, 1))
                        pygame.draw.rect(screen, (234, 233, 233), (351, 200, 1, 26))
                        pygame.draw.rect(screen, (166,)*3, (251, 201, 149, 26))
                        pygame.draw.rect(screen, (249,)*3, (252, 202, 149, 26))
                        pygame.draw.rect(screen, (255,)*3, (252, 202, 148, 25))

                        pygame.draw.rect(screen, (155, 155, 246), (130, 156, 100, 40))
                        pygame.draw.rect(screen, (43, 43, 255), (132, 157, 96, 1))
                        pygame.draw.rect(screen, (68, 68, 255), (131, 158, 1, 38))
                        pygame.draw.rect(screen, (192, 191, 191), (130, 197, 99, 1))
                        pygame.draw.rect(screen, (34, 34, 48), (131, 196, 98, 1))
                        pygame.draw.rect(screen, (0, 0, 12), (228, 157, 1, 39))
                        pygame.draw.rect(screen, (0, 0, 255), (132, 158, 96, 38))
                        text_surface = B.render("Convert", False, (255,)*3)
                        screen.blit(text_surface, (145, 160))

                        pygame.draw.rect(screen, (240,)*3, (130, 238, 100, 40))
                        pygame.draw.rect(screen, (255,)*3, (131, 239, 98, 38))
                        pygame.draw.rect(screen, (9,)*3, (130, 277, 100, 1))
                        pygame.draw.rect(screen, (42,)*3, (229, 238, 1, 40))
                        pygame.draw.rect(screen, (171, 170, 170), (230, 238, 1, 40))
                        pygame.draw.rect(screen, (198, 197, 197), (130, 278, 100, 1))
                        pygame.draw.rect(screen, (133,)*3, (131, 276, 98, 1))
                        pygame.draw.rect(screen, (162,)*3, (228, 238, 1, 39))
                        text_surface = B.render("Clear", False, (255, 0, 0))
                        screen.blit(text_surface, (155,240))

                        pygame.display.flip()
                        break
            
            elif 249 < xy[0] < 400 and 120 < xy[1] < 150 and x != 2:
                x = 3
            
            elif x == 3 and 249 < xy[0] < 400 and 120 < xy[1] < 276:
                for a in range(7):
                    if (120 + 26 * a) < xy[1] < (146 + 26 * a):
                        N[1] = a + 1
                        x = 0
                        screen.fill((230,229,229))
                        for a in range(3):
                            text_surface = my_font.render(l[a], False, (0,)*3)
                            screen.blit(text_surface, (70, 40 + 40 * a))
                            if a == 0:
                                pygame.draw.rect(screen, (222,)*3, (250, 42 + 40 * a, 1, 26))
                                pygame.draw.rect(screen, (205,)*3, (250, 40 + 40 * a, 149, 1))
                                pygame.draw.rect(screen, (234, 233, 233), (351, 40 + 40 * a, 1, 26))
                                pygame.draw.rect(screen, (166,)*3, (251, 41 + 40 * a, 149, 26))
                                pygame.draw.rect(screen, (249,)*3, (252, 42 + 40 * a, 149, 26))
                                pygame.draw.rect(screen, (255,)*3, (252, 42 + 40 * a, 148, 25))
                                text_surface = second_font.render(value, False, (0,)*3)
                                screen.blit(text_surface, (390 - 7 * len(value),50))
                            else:
                                pygame.draw.rect(screen, (240,)*3, (250, 40 + 40 * a, 150, 30))
                                pygame.draw.rect(screen, (250,)*3, (252, 42 + 40 * a, 144, 24))
                                pygame.draw.rect(screen, (130,)*3, (253, 44 + 40 * a, 144, 24))
                                pygame.draw.rect(screen, (238,)*3, (253, 43 + 40 * a, 142, 22))
                                pygame.draw.rect(screen, (157,)*3, (254, 44 + 40 * a, 142, 22))
                                pygame.draw.rect(screen, (240,)*3, (254, 44 + 40 * a, 141, 21))
                                text_surface = second_font.render(current[N[a-1]], False, (0,)*3)
                                screen.blit(text_surface, (290, 46 + 40 * a))

                        text_surface = my_font.render(l[3], False, (0,)*3)
                        screen.blit(text_surface, (70 , 200))
                        pygame.draw.rect(screen, (222, 221, 221), (250, 202, 1, 26))
                        pygame.draw.rect(screen, (205,)*3, (250, 200, 149, 1))
                        pygame.draw.rect(screen, (234, 233, 233), (351, 200, 1, 26))
                        pygame.draw.rect(screen, (166,)*3, (251, 201, 149, 26))
                        pygame.draw.rect(screen, (249,)*3, (252, 202, 149, 26))
                        pygame.draw.rect(screen, (255,)*3, (252, 202, 148, 25))

                        pygame.draw.rect(screen, (155, 155, 246), (130, 156, 100, 40))
                        pygame.draw.rect(screen, (43, 43, 255), (132, 157, 96, 1))
                        pygame.draw.rect(screen, (68, 68, 255), (131, 158, 1, 38))
                        pygame.draw.rect(screen, (192, 191, 191), (130, 197, 99, 1))
                        pygame.draw.rect(screen, (34, 34, 48), (131, 196, 98, 1))
                        pygame.draw.rect(screen, (0, 0, 12), (228, 157, 1, 39))
                        pygame.draw.rect(screen, (0, 0, 255), (132, 158, 96, 38))
                        text_surface = B.render("Convert", False, (255,)*3)
                        screen.blit(text_surface, (145, 160))

                        pygame.draw.rect(screen, (240,)*3, (130, 238, 100, 40))
                        pygame.draw.rect(screen, (255,)*3, (131, 239, 98, 38))
                        pygame.draw.rect(screen, (9,)*3, (130, 277, 100, 1))
                        pygame.draw.rect(screen, (42,)*3, (229, 238, 1, 40))
                        pygame.draw.rect(screen, (171, 170, 170), (230, 238, 1, 40))
                        pygame.draw.rect(screen, (198, 197, 197), (130, 278, 100, 1))
                        pygame.draw.rect(screen, (133,)*3, (131, 276, 98, 1))
                        pygame.draw.rect(screen, (162,)*3, (228, 238, 1, 39))
                        text_surface = B.render("Clear", False, (255, 0, 0))
                        screen.blit(text_surface, (155,240))

                        pygame.display.flip()
                        break
            elif 130 < xy[0] < 230 and 158 < xy[1] < 198:
                if value == "" or value == "." or  ("." in value and len(value.replace(".",""))+1 != len(value)) or 0 in N:
                    text_surface = second_font.render("ERROR", False, (0,)*3)
                    screen.blit(text_surface,(300,205))
                else:
                    text_surface = second_font.render(str(round(eval(value)*percent[N[0]][N[1]],2)), False, (0,)*3)
                    screen.blit(text_surface,(300,205))
                    eval(value)*percent[N[1]]
            elif 130 < xy[0] < 230 and 238 < xy[1] < 278:
                value = ""
                N = [0,0]
                screen.fill((230,229,229))
                for a in range(3):
                    text_surface = my_font.render(l[a], False, (0,)*3)
                    screen.blit(text_surface, (70, 40 + 40 * a))
                    if a == 0:
                        pygame.draw.rect(screen, (222,)*3, (250, 42 + 40 * a, 1, 26))
                        pygame.draw.rect(screen, (205,)*3, (250, 40 + 40 * a, 149, 1))
                        pygame.draw.rect(screen, (234, 233, 233), (351, 40 + 40 * a, 1, 26))
                        pygame.draw.rect(screen, (166,)*3, (251, 41 + 40 * a, 149, 26))
                        pygame.draw.rect(screen, (249,)*3, (252, 42 + 40 * a, 149, 26))
                        pygame.draw.rect(screen, (255,)*3, (252, 42 + 40 * a, 148, 25))
                        
                    else:
                        pygame.draw.rect(screen, (240,)*3, (250, 40 + 40 * a, 150, 30))
                        pygame.draw.rect(screen, (250,)*3, (252, 42 + 40 * a, 144, 24))
                        pygame.draw.rect(screen, (130,)*3, (253, 44 + 40 * a, 144, 24))
                        pygame.draw.rect(screen, (238,)*3, (253, 43 + 40 * a, 142, 22))
                        pygame.draw.rect(screen, (157,)*3, (254, 44 + 40 * a, 142, 22))
                        pygame.draw.rect(screen, (240,)*3, (254, 44 + 40 * a, 141, 21))
                        text_surface = second_font.render("currency"+" "*9+"V", False, (0,)*3)
                        screen.blit(text_surface, (290, 46 + 40 * a))

                text_surface = my_font.render(l[3], False, (0,)*3)
                screen.blit(text_surface, (70 , 200))
                pygame.draw.rect(screen, (222, 221, 221), (250, 202, 1, 26))
                pygame.draw.rect(screen, (205,)*3, (250, 200, 149, 1))
                pygame.draw.rect(screen, (234, 233, 233), (351, 200, 1, 26))
                pygame.draw.rect(screen, (166,)*3, (251, 201, 149, 26))
                pygame.draw.rect(screen, (249,)*3, (252, 202, 149, 26))
                pygame.draw.rect(screen, (255,)*3, (252, 202, 148, 25))

                pygame.draw.rect(screen, (155, 155, 246), (130, 156, 100, 40))
                pygame.draw.rect(screen, (43, 43, 255), (132, 157, 96, 1))
                pygame.draw.rect(screen, (68, 68, 255), (131, 158, 1, 38))
                pygame.draw.rect(screen, (192, 191, 191), (130, 197, 99, 1))
                pygame.draw.rect(screen, (34, 34, 48), (131, 196, 98, 1))
                pygame.draw.rect(screen, (0, 0, 12), (228, 157, 1, 39))
                pygame.draw.rect(screen, (0, 0, 255), (132, 158, 96, 38))
                text_surface = B.render("Convert", False, (255,)*3)
                screen.blit(text_surface, (145, 160))

                pygame.draw.rect(screen, (240,)*3, (130, 238, 100, 40))
                pygame.draw.rect(screen, (255,)*3, (131, 239, 98, 38))
                pygame.draw.rect(screen, (9,)*3, (130, 277, 100, 1))
                pygame.draw.rect(screen, (42,)*3, (229, 238, 1, 40))
                pygame.draw.rect(screen, (171, 170, 170), (230, 238, 1, 40))
                pygame.draw.rect(screen, (198, 197, 197), (130, 278, 100, 1))
                pygame.draw.rect(screen, (133,)*3, (131, 276, 98, 1))
                pygame.draw.rect(screen, (162,)*3, (228, 238, 1, 39))
                text_surface = B.render("Clear", False, (255, 0, 0))
                screen.blit(text_surface, (155,240))

                pygame.display.flip()
                
                x = 0
            else:
                screen.fill((230,229,229))
                for a in range(3):
                    text_surface = my_font.render(l[a], False, (0,)*3)
                    screen.blit(text_surface, (70, 40 + 40 * a))
                    if a == 0:
                        pygame.draw.rect(screen, (222,)*3, (250, 42 + 40 * a, 1, 26))
                        pygame.draw.rect(screen, (205,)*3, (250, 40 + 40 * a, 149, 1))
                        pygame.draw.rect(screen, (234, 233, 233), (351, 40 + 40 * a, 1, 26))
                        pygame.draw.rect(screen, (166,)*3, (251, 41 + 40 * a, 149, 26))
                        pygame.draw.rect(screen, (249,)*3, (252, 42 + 40 * a, 149, 26))
                        pygame.draw.rect(screen, (255,)*3, (252, 42 + 40 * a, 148, 25))
                        text_surface = second_font.render(value, False, (0,)*3)
                        screen.blit(text_surface, (390 - 7 * len(value),50))
                    else:
                        pygame.draw.rect(screen, (240,)*3, (250, 40 + 40 * a, 150, 30))
                        pygame.draw.rect(screen, (250,)*3, (252, 42 + 40 * a, 144, 24))
                        pygame.draw.rect(screen, (130,)*3, (253, 44 + 40 * a, 144, 24))
                        pygame.draw.rect(screen, (238,)*3, (253, 43 + 40 * a, 142, 22))
                        pygame.draw.rect(screen, (157,)*3, (254, 44 + 40 * a, 142, 22))
                        pygame.draw.rect(screen, (240,)*3, (254, 44 + 40 * a, 141, 21))
                        text_surface = second_font.render(current[N[a-1]], False, (0,)*3)
                        screen.blit(text_surface, (290, 46 + 40 * a))

                text_surface = my_font.render(l[3], False, (0,)*3)
                screen.blit(text_surface, (70 , 200))
                pygame.draw.rect(screen, (222, 221, 221), (250, 202, 1, 26))
                pygame.draw.rect(screen, (205,)*3, (250, 200, 149, 1))
                pygame.draw.rect(screen, (234, 233, 233), (351, 200, 1, 26))
                pygame.draw.rect(screen, (166,)*3, (251, 201, 149, 26))
                pygame.draw.rect(screen, (249,)*3, (252, 202, 149, 26))
                pygame.draw.rect(screen, (255,)*3, (252, 202, 148, 25))

                pygame.draw.rect(screen, (155, 155, 246), (130, 156, 100, 40))
                pygame.draw.rect(screen, (43, 43, 255), (132, 157, 96, 1))
                pygame.draw.rect(screen, (68, 68, 255), (131, 158, 1, 38))
                pygame.draw.rect(screen, (192, 191, 191), (130, 197, 99, 1))
                pygame.draw.rect(screen, (34, 34, 48), (131, 196, 98, 1))
                pygame.draw.rect(screen, (0, 0, 12), (228, 157, 1, 39))
                pygame.draw.rect(screen, (0, 0, 255), (132, 158, 96, 38))
                text_surface = B.render("Convert", False, (255,)*3)
                screen.blit(text_surface, (145, 160))

                pygame.draw.rect(screen, (240,)*3, (130, 238, 100, 40))
                pygame.draw.rect(screen, (255,)*3, (131, 239, 98, 38))
                pygame.draw.rect(screen, (9,)*3, (130, 277, 100, 1))
                pygame.draw.rect(screen, (42,)*3, (229, 238, 1, 40))
                pygame.draw.rect(screen, (171, 170, 170), (230, 238, 1, 40))
                pygame.draw.rect(screen, (198, 197, 197), (130, 278, 100, 1))
                pygame.draw.rect(screen, (133,)*3, (131, 276, 98, 1))
                pygame.draw.rect(screen, (162,)*3, (228, 238, 1, 39))
                text_surface = B.render("Clear", False, (255, 0, 0))
                screen.blit(text_surface, (155,240))

                pygame.display.flip()
                x = 0
                
        if event.type == pygame.TEXTINPUT and x:
            if str(event)[31] in valuable:
                value += str(event)[31]
                pygame.draw.rect(screen, (222,)*3, (250, 42, 1, 26))
                pygame.draw.rect(screen, (205,)*3, (250, 40, 149, 1))
                pygame.draw.rect(screen, (234, 233, 233), (351, 40, 1, 26))
                pygame.draw.rect(screen, (166,)*3, (251, 41, 149, 26))
                pygame.draw.rect(screen, (249,)*3, (252, 42, 149, 26))
                pygame.draw.rect(screen, (255,)*3, (252, 42, 148, 25))
                text_surface = second_font.render(value, False, (0,)*3)
                screen.blit(text_surface, (390 - 7 * len(value),50))
        if event.type == pygame.MOUSEBUTTONUP and x == 2:
            for b in range(1,8):
                pygame.draw.rect(screen, (240,)*3, (250, 54 + 26 * b, 150, 30))
                pygame.draw.rect(screen, (250,)*3, (252, 55 + 26 * b, 144, 24))
                pygame.draw.rect(screen, (130,)*3, (253, 58 + 26 * b, 144, 24))
                pygame.draw.rect(screen, (238,)*3, (253, 57 + 26 * b, 142, 22))
                pygame.draw.rect(screen, (157,)*3, (254, 58 + 26 * b, 142, 22))
                pygame.draw.rect(screen, (240,)*3, (254, 58 + 26 * b, 141, 21))
                text_surface = second_font.render(current[b], False, (0,)*3)
                screen.blit(text_surface, (300, 60 + 26 * b))
        if event.type == pygame.MOUSEBUTTONUP and x == 3:
            for b in range(1,8):
                pygame.draw.rect(screen, (240,)*3, (250, 94 + 26 * b, 150, 30))
                pygame.draw.rect(screen, (250,)*3, (252, 95 + 26 * b, 144, 24))
                pygame.draw.rect(screen, (130,)*3, (253, 98 + 26 * b, 144, 24))
                pygame.draw.rect(screen, (238,)*3, (253, 97 + 26 * b, 142, 22))
                pygame.draw.rect(screen, (157,)*3, (254, 98 + 26 * b, 142, 22))
                pygame.draw.rect(screen, (240,)*3, (254, 98 + 26 * b, 141, 21))
                text_surface = second_font.render(current[b], False, (0,)*3)
                screen.blit(text_surface, (300, 100 + 26 * b))
           
                
    pygame.display.flip()
pygame.quit()
