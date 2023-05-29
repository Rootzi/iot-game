#import necessary libraries
import sys
import os
import pygame
import time
import re
# from playsound import playsound

fname = "Prototype.py"
dn = os.path.abspath(fname)
truepath=os.path.dirname(dn)
try:
    os.chdir("cyberdungeons\protocode0505\gamefiles")
    print(os.getcwd())
except FileNotFoundError as e:
    print(os.getcwd())
    pass

# # # from pydrive2.auth import GoogleAuth
# # # from pydrive2.drive import GoogleDrive
# # # gauth = GoogleAuth()

# # # # Try to load saved client credentials
# # # gauth.LoadCredentialsFile("mycreds.txt")

# # # if gauth.credentials is None:
# # #     # Authenticate if they're not there

    
# # #     gauth.GetFlow()
# # #     gauth.flow.params.update({'access_type': 'offline'})
# # #     gauth.flow.params.update({'approval_prompt': 'force'})

# # #     gauth.LocalWebserverAuth()

# # # else:

# # #     gauth.LocalWebserverAuth()

# # #     gauth.Authorize()

# # # # Save the current credentials to a file
# # # gauth.SaveCredentialsFile("mycreds.txt")  

# # # drive = GoogleDrive(gauth)

ENEMY_SCALING = 0.6
TARGET_SCALING = 0.3

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Prototype Window"
SCREEN_X_CENTER = SCREEN_WIDTH / 2
SCREEN_Y_CENTER = SCREEN_HEIGHT / 2

print(SCREEN_X_CENTER,SCREEN_Y_CENTER)

pygame.init()

while True:

    OSCFONT = pygame.font.Font(None, 70)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    # Set the window size and title
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(SCREEN_TITLE)
    clock = pygame.time.Clock()

    # Set level number int (default =1)
    lvl = 1

    # Draw On-screen keyboard
    def draw_osc():
        keys = []
        for i in range(26):
            letter = chr(i + 65)  # A is chr(65)
            x_pos = 65 + 90 * (i % 10)
            y_pos = SCREEN_Y_CENTER + 90 * (i // 10)
            rect = pygame.draw.rect(screen, RED, (x_pos, y_pos, 80, 80), 2)
            text = OSCFONT.render(letter, True, RED)
            screen.blit(text, (x_pos + 5, y_pos + 5))
            keys.append((letter, rect))
        undo = "UNDO"
        x_pos = 65 + 90 * (26 % 10)
        y_pos = SCREEN_Y_CENTER + 90 * (26 // 10)
        rect = pygame.draw.rect(screen, RED, (x_pos, y_pos, 350, 80), 2)
        text = OSCFONT.render(undo, True, RED)
        screen.blit(text, (x_pos + 5, y_pos + 5))
        keys.append(([undo], rect))

        return keys


    # Draw SUBMIT button
    # x_pos = 90
    # y_pos = SCREEN_Y_CENTER + 90
    button_width, button_height = 150, 50
    button_rect = pygame.Rect((screen.get_width() - 600 - button_width) // 2,
                            (screen.get_height() - 200 - button_height) // 2,
                            button_width,
                            button_height)
    text = OSCFONT.render("SUBMIT", True, RED)



    def text1(word, x, y):
        font = pygame.font.SysFont(None, 50)
        text = font.render("Please enter your name: " + word, True, (255, 0, 0))
        return screen.blit(text, (x,y))

    def inpt():
        max_chars = 10
        draw_osc()
        word=""
        text1("",SCREEN_WIDTH*.1,SCREEN_HEIGHT*.1) 
        pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    screen.fill(BLACK)
                    keys=draw_osc()
                    for key in keys:
                        if key == keys[26] and key[1].collidepoint(event.pos): # check if the key is key[27]
                            print("Undo / Backspace key clicked.")
                            if len(word) > 0:
                                word = word[:-1]
                                print(word)
                        else: 
                            if key[1].collidepoint(event.pos):
                                if len(word) < max_chars:
                                    word+=(key[0])
                                    print(word)
                        
                    if button_rect.collidepoint(event.pos):
                        if len(word) > 1:
                            print("Submit button clicked.")
                            done = True
                            username = word
                            return done, username
                        else:
                            print("Must have more than 1 characters.")
                        
                # if event.type == pygame.KEYDOWN:
                #     if event.key in [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z]:
                #         word+=chr(event.key)
                #         screen.fill((0, 0, 0))
                #         text1(word, SCREEN_WIDTH*.4, SCREEN_HEIGHT*.5)
                #         pygame.display.flip()
                #         print(word)
                #     if event.key == pygame.K_RETURN:
                #         done = True
                #         username = word
                #         return done, username
            
            screen.fill(BLACK)
            draw_osc()
            screen.blit(text, (button_rect.centerx - text.get_width() // 2,
                            button_rect.centery - text.get_height() // 2))
            text1(word, SCREEN_WIDTH*.1, SCREEN_HEIGHT*.1)
            pygame.display.flip()
            
    def savescore(username,score):
        scorestr2=str(score)
        savedata=username+': '+scorestr2+'\n'

        # # # file1 = drive.CreateFile({'parents':[{'id': '1t639SXnzHOlMMB3WRj-jaiqoA2pQRkfk'}],'id': '1d6TCPkiGthP_OSSJYrAnMIEPrzNl9WbN','title': 'highscores.txt'})  
        # # # # Set content of the file from the given string.
        
        # # # content = file1.GetContentString()
        # # # file1.SetContentString(content+savedata) 
        # # # file1.Upload()

        filename = "highscores.txt"

        if os.path.isfile(filename):
            print(f"{filename} already exists.")
        else:
            with open(filename, 'x') as f:
                print(f"{filename} created successfully.")
        with open(filename, "a") as file:
            file.write(savedata)




    def game_intro():
        intro=True
        while intro:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        intro=False
                done, username=inpt() 
                if done:
                    print("Username Accepted")
                    intro=False
                    break
            screen.fill((0, 0, 0))
            pygame.display.update()
            clock.tick(60)
        return username
    username=game_intro()

    def draw_highscores():
        # read the contents of the text file
        with open('highscores.txt', 'r') as file:
            lines = file.readlines()

        # initialize the list of data
        data = []

        # process each line of the text file
        for line in lines:
            # extract the text and number from the line using string manipulation
            text = line.rstrip()
            number = int(re.findall('\d+', line)[0])

            # calculate the highest value integer
            max_number = max(re.findall('\d+', line), key=int)

            # store the extracted data in a tuple
            data.append((text, number, max_number))

        # sort the list in descending order of the highest value integer
        data.sort(key=lambda x: int(x[2]), reverse=True)

        # display the data onscreen using Pygame
        font = pygame.font.SysFont(None, 30)
        for i, (text, number, max_number) in enumerate(data):
            rendered_text = font.render(f'{text}', True, (RED))
            screen.blit(rendered_text, (20, 20 + i * 22.5))


    screen.fill((255, 255, 255))
    # Create target 1
    target_1_1 = pygame.image.load("gameimages\output-onlinepngtools.png").convert_alpha()
    target_1_1 = pygame.transform.scale(target_1_1, (int(target_1_1.get_width() * TARGET_SCALING), int(target_1_1.get_height() * TARGET_SCALING)))
    # Create target 2
    target_2_1 = pygame.image.load("gameimages\output-onlinepngtools.png").convert_alpha()
    target_2_1 = pygame.transform.scale(target_2_1, (int(target_2_1.get_width() * TARGET_SCALING), int(target_2_1.get_height() * TARGET_SCALING)))
    # Create target 3
    target_3_1 = pygame.image.load("gameimages\output-onlinepngtools.png").convert_alpha()
    target_3_1 = pygame.transform.scale(target_3_1, (int(target_3_1.get_width() * TARGET_SCALING), int(target_3_1.get_height() * TARGET_SCALING)))
    # Create target 4
    target_4_1 = pygame.image.load("gameimages\output-onlinepngtools.png").convert_alpha()
    target_4_1 = pygame.transform.scale(target_4_1, (int(target_4_1.get_width() * TARGET_SCALING), int(target_4_1.get_height() * TARGET_SCALING)))
    # Create target 5
    target_5_1 = pygame.image.load("gameimages\output-onlinepngtools.png").convert_alpha()
    target_5_1 = pygame.transform.scale(target_5_1, (int(target_5_1.get_width() * TARGET_SCALING), int(target_5_1.get_height() * TARGET_SCALING)))

    target_rect1_1 = target_1_1.get_rect(center=(512, 300))
    target_rect2_1 = target_2_1.get_rect(center=(340, 401))
    target_rect3_1 = target_3_1.get_rect(center=(701, 320))

    target_rect1_2 = target_1_1.get_rect(center=(707, 236))
    target_rect2_2 = target_2_1.get_rect(center=(487, 286))
    target_rect3_2 = target_3_1.get_rect(center=(335, 236))

    target_rect1_3 = target_1_1.get_rect(center=(648, 499))
    target_rect2_3 = target_2_1.get_rect(center=(287, 514))
    target_rect3_3 = target_3_1.get_rect(center=(593, 234))
    target_rect4_3 = target_4_1.get_rect(center=(437, 339))
    target_rect5_3 = target_5_1.get_rect(center=(743, 327))


    # (701, 320)
    # (340, 401)

    # Load the background image
    background = pygame.image.load(os.path.join(os.getcwd(), "gameimages/pxart.png")).convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    background_rect = background.get_rect(center=screen.get_rect().center)


    # Load the enemy sprite
    enemy_1 = pygame.image.load(os.path.join(str(os.getcwd()), "gameimages/45dc86f84906fcf2e90cae87f54758fd.gif")).convert_alpha()
    enemy_1 = pygame.transform.scale(enemy_1, (int(enemy_1.get_width() * ENEMY_SCALING), int(enemy_1.get_height() * ENEMY_SCALING)))
    enemy_rect1 = enemy_1.get_rect(center=(SCREEN_X_CENTER, SCREEN_Y_CENTER+20))

    enemy_2 = pygame.image.load(os.path.join(str(os.getcwd()), "gameimages/aa4.gif")).convert_alpha()
    enemy_2 = pygame.transform.scale(enemy_2, (int(enemy_2.get_width() * ENEMY_SCALING * 3), int(enemy_2.get_height() * ENEMY_SCALING) * 3))
    enemy_rect2 = enemy_2.get_rect(center=(SCREEN_X_CENTER, SCREEN_Y_CENTER+50))

    enemy_3 = pygame.image.load(os.path.join(str(os.getcwd()), "gameimages/brainstorm-robbits-3.png")).convert_alpha()
    enemy_3 = pygame.transform.scale(enemy_3, (int(enemy_3.get_width() * ENEMY_SCALING * 3), int(enemy_3.get_height() * ENEMY_SCALING) * 3))
    enemy_rect3 = enemy_3.get_rect(center=(SCREEN_X_CENTER, SCREEN_Y_CENTER+20))

    # Set score int
    score = 0
    # Set lives int
    lives = 3
    # Set gameover int
    gameover = 1
    # Set correct int
    correct = 1
    # Set incorrect int
    incorrect = 0
    # Create the font object
    font48 = pygame.font.SysFont(None, 48)
    font72 = pygame.font.SysFont(None, 72)
    font88 = pygame.font.SysFont(None, 88)
    font144 = pygame.font.SysFont(None, 144)
    font1000 = pygame.font.SysFont(None, 1000)


    




    # Draw the images
    def draw_images():
        screen.blit(background, background_rect)
        if lvl==1:
            screen.blit(enemy_1, enemy_rect1)
            screen.blit(target_1_1, target_rect1_1)
            screen.blit(target_2_1, target_rect2_1)
            screen.blit(target_3_1, target_rect3_1)
        if lvl==2:
            screen.blit(enemy_2, enemy_rect2)
            screen.blit(target_1_1, target_rect1_2)
            screen.blit(target_2_1, target_rect2_2)
            screen.blit(target_3_1, target_rect3_2)
        if lvl==3:
            screen.blit(enemy_3, enemy_rect3)
            screen.blit(target_1_1, target_rect1_3)
            screen.blit(target_2_1, target_rect2_3)
            screen.blit(target_3_1, target_rect3_3)
            screen.blit(target_4_1, target_rect4_3)
            screen.blit(target_5_1, target_rect5_3)




    # Set question1 text positioning variables
    question1_x=0
    question1_y=50
    # Draw the score text
    def draw_q1():
        q1_backing = font88.render("    Question 1: A virus appears! How will you defend your PC?    ", True, (0,0,0), (0,0,0))
        screen.blit(q1_backing, (question1_x, question1_y-15))
        q1_text = font48.render("    Question 1: A virus appears! How will you defend your PC?    ", True, (255, 255, 255), (0,0,0))
        screen.blit(q1_text, (question1_x, question1_y))

    def draw_q2():
        q2_backing1 = font88.render("    Question 2: You receive an email containing a website link from an unknown sender. What will you do?    ", True, (0,0,0), (0,0,0))
        screen.blit(q2_backing1, (question1_x, question1_y-0))
        q2_backing2 = font88.render("    Question 2: You receive an email containing a website link from an unknown sender. What will you do?    ", True, (0,0,0), (0,0,0))
        screen.blit(q2_backing2, (question1_x, question1_y-50))
        q2_text1 = font48.render("    Question 2: You receive an email containing a website link", True, (255, 255, 255), (0,0,0))
        screen.blit(q2_text1, (question1_x, question1_y-40))
        q2_text2 = font48.render("    from an unknown sender. What will you do?    ", True, (255, 255, 255), (0,0,0))
        screen.blit(q2_text2, (question1_x+199, question1_y))
        
    def draw_q3():
        q3_backing1 = font88.render("    Question 3: A DDoS attack appears! What does DDoS stand for?    ", True, (0,0,0), (0,0,0))
        screen.blit(q3_backing1, (question1_x, question1_y-50))
        q3_backing2 = font88.render("    Question 3: A DDoS attack appears! What does DDoS stand for?    ", True, (0,0,0), (0,0,0))
        screen.blit(q3_backing2, (question1_x, question1_y))
        q3_text1 = font48.render("    Question 3: A DDoS attack appears!                                   ", True, (255, 255, 255), (0,0,0))
        screen.blit(q3_text1, (question1_x, question1_y-40))
        q3_text2 = font48.render("                         What does DDoS stand for?    ", True, (255, 255, 255), (0,0,0))
        screen.blit(q3_text2, (question1_x, question1_y))

    def draw_q1_ans1():
        q1a1_text = font48.render("            Run a virus scan and delete or quarantine the virus.            ", True, (255, 255, 255), (0,0,0))
        screen.blit(q1a1_text, (0,105))

    def draw_q1_ans2():
        q1a2_text = font48.render("                        Leave the virus on the PC, it will die anyway.                        ", True, (255, 255, 255), (0,0,0))
        screen.blit(q1a2_text, (-47,105))

    def draw_q1_ans3():
        q1a3_text = font48.render("            Download more viruses so that they fight each other.            ", True, (255, 255, 255), (0,0,0))
        screen.blit(q1a3_text, (-5,105))

    def draw_q2_ans1():
        q1a1_text = font48.render("                      Report it as spam and block the sender.                ", True, (255, 255, 255), (0,0,0))
        screen.blit(q1a1_text, (0,105))

    def draw_q2_ans2():
        q1a2_text = font48.render("               Forward the email to another user, they can open it.                            ", True, (255, 255, 255), (0,0,0))
        screen.blit(q1a2_text, (-47,105))

    def draw_q2_ans3():
        q1a3_text = font48.render("                        Open the link, what's the harm in that?                    ", True, (255, 255, 255), (0,0,0))
        screen.blit(q1a3_text, (-5,105))

    def draw_q3_ans1():
        q1a1_text = font48.render("                                    Distributed Denial of Service                                                            ", True, (255, 255, 255), (0,0,0))
        screen.blit(q1a1_text, (0,105))

    def draw_q3_ans2():
        q1a2_text = font48.render("                                     Disturbance Directed on Servers                                                ", True, (255, 255, 255), (0,0,0))
        screen.blit(q1a2_text, (-47,105))

    def draw_q3_ans3():
        q1a3_text = font48.render("                                 Distributed Denial of Servers                                                ", True, (255, 255, 255), (0,0,0))
        screen.blit(q1a3_text, (-5,105))

    def draw_q3_ans4():
        q1a2_text = font48.render("                                    Dinosaurs Doughnuts open Sesame                        ", True, (255, 255, 255), (0,0,0))
        screen.blit(q1a2_text, (-47,105))

    def draw_q3_ans5():
        q1a3_text = font48.render("                                    Direct Denial of Service                                                ", True, (255, 255, 255), (0,0,0))
        screen.blit(q1a3_text, (-5,105))


    # Draw incorrect red flash
    def draw_incorrect():
        incorrect_text = font1000.render("Incorrect", True, (255, 0, 0), (255,0,0))
        screen.blit(incorrect_text, (0, 0)) 
    # Set score text positioning variables
    score_x=10
    score_y=SCREEN_HEIGHT-50
    # Draw the score text
    def draw_score():
        score_text = font48.render(f"Score: {score}", True, (57, 255, 20), (0,0,0))
        screen.blit(score_text, (score_x, score_y))

    # Set lives text positioning variables
    draw_x=10
    draw_y=SCREEN_HEIGHT-90
    # Draw lives text
    def draw_lives():
        lives_text = font48.render(f"Lives: {lives}", True, (255, 33, 133), (0,0,0))
        screen.blit(lives_text, (draw_x, draw_y))  

    # Set gameover text positioning variables
    gameover_x=SCREEN_X_CENTER-300
    gameover_y=SCREEN_Y_CENTER-72
    # Draw gameover text
    def draw_gameover():
        gameover_text = font144.render("GAME OVER", True, (255, 0, 0), (0,0,0))
        screen.blit(gameover_text, (gameover_x, gameover_y))  
    def draw_win():
        win_background = font1000.render("GREENWINNERTEXTINVISIBLE", True, (57, 255, 20), (57, 255, 20))
        screen.blit(win_background, (0, 0)) 
        win_text = font144.render("YOU WIN!", True, (255,255,255))
        screen.blit(win_text, (270,235))
    finalscore_x=SCREEN_WIDTH*.2
    finalscore_y=SCREEN_HEIGHT*.8
    def draw_win_score(): 
        scorestr=str(score)
        win_text = font88.render("Final Score: "+scorestr, True, (255,255,255), (57, 255, 20))
        screen.blit(win_text, (finalscore_x,finalscore_y))
    def draw_loss_score(): 
        scorestr=str(score)
        win_text = font88.render("Final Score: "+scorestr, True, (255,255,255), (255,0,0))
        screen.blit(win_text, (finalscore_x,finalscore_y))
    # Set gameclose text positioning variables
    gameclose_x=SCREEN_X_CENTER-296
    gameclose_y=SCREEN_Y_CENTER+30
    # Draw gameclosing text
    def draw_gameclosing():
        gameclose_text = font72.render("The game will now close.", True, (255, 0, 0), (0,0,0))
        screen.blit(gameclose_text, (gameclose_x, gameclose_y))

    mouse_enabled = True
    timer = 0

    print("You have ",lives,"lives, spend them wisely.")
    breaker = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if mouse_enabled:
                    if lvl==1:
                        if target_rect1_1.collidepoint(event.pos):
                            score += 1000*lvl
                            correct=1
                            lvl += 1
                            print("\n\nCorrect Target Clicked\nUpdated score: ",score)
                        elif target_rect2_1.collidepoint(event.pos) or target_rect3_1.collidepoint(event.pos):
                            lives -= 1
                            incorrect=1
                            print("\n\nWrong Target Clicked\nUpdated score: ",score)
                            print("\n\nLives left: ",lives)
                    elif lvl==2:
                        if target_rect1_2.collidepoint(event.pos):
                            score += 1000*lvl
                            correct=1
                            lvl += 1
                            print("\n\nCorrect Target Clicked\nUpdated score: ",score)
                        elif target_rect2_2.collidepoint(event.pos) or target_rect3_2.collidepoint(event.pos):
                            lives -= 1
                            incorrect=1
                            print("\n\nWrong Target Clicked\nUpdated score: ",score)
                            print("\n\nLives left: ",lives)
                    elif lvl==3:
                        if target_rect1_3.collidepoint(event.pos):
                            score += 1000*lvl
                            correct=1
                            lvl += 1
                            print("\n\nCorrect Target Clicked\nUpdated score: ",score)
                        elif target_rect2_3.collidepoint(event.pos) or target_rect3_3.collidepoint(event.pos) or target_rect4_3.collidepoint(event.pos) or target_rect5_3.collidepoint(event.pos):
                            lives -= 1
                            incorrect=1
                            print("\n\nWrong Target Clicked\nUpdated score: ",score)
                            print("\n\nLives left: ",lives)
                    mouse_enabled = False
                    timer = pygame.time.get_ticks()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     print(event.pos)
        if not mouse_enabled and pygame.time.get_ticks() - timer >= 500:
            mouse_enabled = True
        draw_images()        
        if lvl==1:
            draw_q1()
            if target_rect1_1.collidepoint(pygame.mouse.get_pos()):
                    print("target1 hovered")
                    draw_q1_ans1()
            if target_rect2_1.collidepoint(pygame.mouse.get_pos()):
                    print("target2 hovered")
                    draw_q1_ans2()
            if target_rect3_1.collidepoint(pygame.mouse.get_pos()):
                    print("target3 hovered")
                    draw_q1_ans3()
        if lvl==2:
            draw_q2()
            if target_rect1_2.collidepoint(pygame.mouse.get_pos()):
                    print("target1 hovered")
                    draw_q2_ans1()
            if target_rect2_2.collidepoint(pygame.mouse.get_pos()):
                    print("target2 hovered")
                    draw_q2_ans2()
            if target_rect3_2.collidepoint(pygame.mouse.get_pos()):
                    print("target3 hovered")
                    draw_q2_ans3()
        if lvl==3:
            draw_q3()
            if target_rect1_3.collidepoint(pygame.mouse.get_pos()):
                    print("target1 hovered")
                    draw_q3_ans1()
            if target_rect2_3.collidepoint(pygame.mouse.get_pos()):
                    print("target2 hovered")
                    draw_q3_ans2()
            if target_rect3_3.collidepoint(pygame.mouse.get_pos()):
                    print("target3 hovered")
                    draw_q3_ans3()
            if target_rect4_3.collidepoint(pygame.mouse.get_pos()):
                    print("target4 hovered")
                    draw_q3_ans4()
            if target_rect5_3.collidepoint(pygame.mouse.get_pos()):
                    print("target5 hovered")
                    draw_q3_ans5()
        if lvl==4:
            # draw submit button
            OSCFONT = pygame.font.Font(None, 70)
            button_width, button_height = 510, 50
            button_rect = pygame.Rect((screen.get_width() + 400 - button_width) // 2,
                            (screen.get_height() - 200 - button_height) // 2,
                            button_width,
                            button_height)
            text = OSCFONT.render("CLICK HERE TO PLAY", True, RED)
            
            
            mouse_enabled = True
            timer = 0

            savescore(username,score)
            draw_win()
            draw_win_score()
            pygame.display.flip()
            
            highscore_pause = True
            highscore_loop = True
            pygame.time.delay(2000)
            screen.fill(BLACK)
            draw_highscores()
            pygame.display.flip()

            while highscore_loop:
                if mouse_enabled:
                    while highscore_pause:
                        # print("PAUSE CLICK DETECTION STARTED")
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                print("PAUSE CLICK DETECTED")
                                if button_rect.collidepoint(event.pos):
                                    print("BUTTON CLICKED")
                                    # User has clicked the button
                                    highscore_loop = False
                                    highscore_pause = False
                                    breaker = True
                                    break
                            
                    

                        screen.fill(BLACK)
                        draw_highscores()

                        screen.blit(text, (button_rect.centerx - text.get_width() // 2,
                                        button_rect.centery - text.get_height() // 2))
                        pygame.display.flip()

                    mouse_enabled = False
                    timer = pygame.time.get_ticks()
                    clock.tick(60)
                if not mouse_enabled and pygame.time.get_ticks() - timer >= 5000:
                    mouse_enabled = True
                    if breaker:
                        break


                if breaker:
                    break
                clock.tick(60)
            if breaker:
                break
            clock.tick(60)
            if breaker:
                break

        draw_score()
        draw_lives()
        # if correct==True:
        #     target_position()
        #     pygame.display.flip()
        #     time.sleep(0.5)
        #     correct=False
        if incorrect==True:
            draw_incorrect()
            pygame.display.flip()
            time.sleep(0.5)
            score-=lvl*100
            incorrect=False
        if lives<=0:
            # draw submit button
            OSCFONT = pygame.font.Font(None, 70)
            button_width, button_height = 510, 50
            button_rect = pygame.Rect((screen.get_width() + 400 - button_width) // 2,
                            (screen.get_height() - 200 - button_height) // 2,
                            button_width,
                            button_height)
            text = OSCFONT.render("CLICK HERE TO PLAY", True, RED)


            mouse_enabled = True
            timer = 0

            savescore(username,score)
            print("PLAYER HAS 0 LIVES")
            draw_incorrect()
            draw_gameover()
            draw_loss_score()
            pygame.display.flip()
            
            highscore_pause = True
            highscore_loop = True
            pygame.time.delay(2000)
            screen.fill(BLACK)
            draw_highscores()
            pygame.display.flip()

            while highscore_loop:
                if mouse_enabled:
                    while highscore_pause:
                        # print("PAUSE CLICK DETECTION STARTED")
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                print("PAUSE CLICK DETECTED")
                                if button_rect.collidepoint(event.pos):
                                    print("BUTTON CLICKED")
                                    # User has clicked the button
                                    highscore_loop = False
                                    highscore_pause = False
                                    breaker = True
                                    break
                            
                    

                        screen.fill(BLACK)
                        draw_highscores()

                        screen.blit(text, (button_rect.centerx - text.get_width() // 2,
                                        button_rect.centery - text.get_height() // 2))
                        pygame.display.flip()

                    mouse_enabled = False
                    timer = pygame.time.get_ticks()
                    clock.tick(60)
                if not mouse_enabled and pygame.time.get_ticks() - timer >= 5000:
                    mouse_enabled = True
                    if breaker:
                        break


                if breaker:
                    break
                clock.tick(60)
            if breaker:
                break
            clock.tick(60)
        if breaker:
            break

        pygame.display.flip() #"Flip" the frame on the back buffer to the front buffer so that it is displayed at the end of each iteration of the while loop AKA update the screen.
        clock.tick(60)
