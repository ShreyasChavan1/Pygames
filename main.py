import pygame
import random

# initializinng game
pygame.init()

#setting colors
white = (255,255,255)
red = (255,0,0)
black =(0,0,0)

# seting up game dimentions
GAME_WIDTH = 700
GAME_HEIGHT = 500


# settinig aup main window
window = pygame.display.set_mode((GAME_WIDTH,GAME_HEIGHT))
pygame.display.set_caption("SnakeByShreyas")

# background image
bgimage = pygame.image.load('download.jpg')
bgimage = pygame.transform.scale(bgimage,(GAME_WIDTH,GAME_HEIGHT)).convert_alpha()

bgimage1 = pygame.image.load('snake-game.jpg')
bgimage1 = pygame.transform.scale(bgimage1,(GAME_WIDTH,GAME_HEIGHT)).convert_alpha()

bgimage2 = pygame.image.load('razor.jpg')
bgimage2 = pygame.transform.scale(bgimage2,(GAME_WIDTH,GAME_HEIGHT)).convert_alpha()

#initialized the clock
clock = pygame.time.Clock()
def plot_snake(window,color,snake_size,snk_list):
    for x,y in snk_list:
        pygame.draw.rect(window,color,[x,y,snake_size,snake_size])

font = pygame.font.SysFont(None,50)

def text(text,color,x,y):
    screen_text = font.render(text,True,color)
    window.blit(screen_text,[x,y])

def welcome():
    exit_game = False
    while not exit_game:
        window.fill(white)
        window.blit(bgimage1,(0,0))
        text('Welcome to snake',black,180,200)
        text('press SPACE to play',black,170,250)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                exit_game = True
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_SPACE:
                    pygame.mixer.init()
                    pygame.mixer.music.load('Nagin--Been-Music--Suchitra-Nitha-Colombo.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(60)

def gameloop():
    snk_list = []
    snk_length = 1
    # defining snake head dimenstiono
    snake_x = 50
    snake_y = 100
    snake_size = 20

    # defining food demention
    food_x = random.randint(10, GAME_WIDTH / 2)
    food_y = random.randint(10, GAME_HEIGHT / 2)
    food_size = 20

    # setting the velocity of snake , value of velocity will be addred to x,y coordinates of snake head till while loop
    velocity_x = 0
    velocity_y = 0

    score = 0

    # frame rate to be given in clock function
    fps = 30
    exit_game = False
    game_over = False

    with open('highscore','r') as f:
        hiscore = f.read()


    while not exit_game:
        if game_over:
            window.fill(white)
            window.blit(bgimage2,(0,0))
            text('game over',red,250,200)
            text('press enter to continue',red,150,250)
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    exit_game = True
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_RETURN:
                        welcome()
            with open('highscore','w') as x:
                x.write(str(hiscore))
        else:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    exit_game = True
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_RIGHT:
                        velocity_x = 4
                        velocity_y = 0
                    if events.key == pygame.K_LEFT:
                        velocity_x = -4
                        velocity_y = 0
                    if events.key == pygame.K_UP:
                        velocity_y = -4
                        velocity_x = 0
                    if events.key == pygame.K_DOWN:
                        velocity_y = 4
                        velocity_x = 0
                    if events.key == pygame.K_SPACE:
                        velocity_x = 0
                        velocity_y = 0
                        print('paused')
                    if events.key == pygame.K_q:
                        score+=10

            # adding the velocity to coordinates
            snake_x+=velocity_x
            snake_y+=velocity_y

            if snake_x<0 or snake_x>GAME_WIDTH or snake_y<0 or snake_y>GAME_HEIGHT:
                game_over = True
                pygame.mixer.init()
                pygame.mixer.music.load('ara_ara.mp3')
                pygame.mixer.music.play()
                print('final score: ',score)

            if abs(snake_x - food_x)<7 and abs(snake_y - food_y)<7:
                score += 1
                food_x = random.randint(10, GAME_WIDTH/2)
                food_y = random.randint(10, GAME_HEIGHT/2)
                snk_length+=5

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)


            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over= True
                pygame.mixer.init()
                pygame.mixer.music.load('ara_ara.mp3')
                pygame.mixer.music.play()

            if score > int(hiscore):
                hiscore = score

            window.fill(white)
            window.blit(bgimage,(0,0))
            text('score: '+str(score)+ ' highscore: '+str(hiscore),red,5,5)

            # creating the first head of snake
            # following function gets main window,followed by color,in the list contains coordinates of snake head
            # and snake's size
            pygame.draw.rect(window, black, [food_x, food_y, food_size, food_size])
            plot_snake(window, red, snake_size,snk_list)
        pygame.display.update()
        # think of it as setting the fps for game
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()


