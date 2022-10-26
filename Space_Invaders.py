import random
import play
import os
import sys
import time

### LOADING ASSETS ###
# BG
BG = play.new_image(os.path.join("assets", "background-black.png"), size=200)

RED_SHIP = play.new_image(os.path.join(
    "assets", "pixel_ship_red_small.png"), transparency=0)
GREEN_SHIP = play.new_image(os.path.join(
    "assets", "pixel_ship_green_small.png"), transparency=0)
BLUE_SHIP = play.new_image(os.path.join(
    "assets", "pixel_ship_blue_small.png"), transparency=0)

# Player Ship
YELLOW_SHIP = play.new_image(os.path.join(
    "assets", "pixel_ship_yellow.png"), y=-150, transparency=0)

# Lasers
RED_LASER = play.new_image(os.path.join(
    "assets", "pixel_laser_red.png"), x=1000, y=1000, transparency=0)
GREEN_LASER = play.new_image(os.path.join(
    "assets", "pixel_laser_green.png"), x=1000, y=1000, transparency=0)
BLUE_LASER = play.new_image(os.path.join(
    "assets", "pixel_laser_blue.png"), x=1000, y=1000, transparency=0)
YELLOW_LASER = play.new_image(os.path.join(
    "assets", "pixel_laser_yellow.png",), x=1000, y=1000, transparency=0)

### PROGRAMMING ###

# Variables
level = 1
lives = 3
health = 100
show_score = False
enemy_value = False

# Lists
enemies = [RED_SHIP, GREEN_SHIP, BLUE_SHIP]
random_enemies = []
enemie_numb = 5
enemy_wave = []

# Text
press_key_text = play.new_text(
    'Press any key to start...', color='white', y=150, font_size=72)
press_p_text = play.new_text("Start the attack with the 'p' key...",
                             color='white', y=80, font_size=60, transparency=0)
level_text = play.new_text('', color='white', x=300, y=250)
lives_text = play.new_text('', color='white', x=-300, y=250)
lost_text = play.new_text('YOU LOST!', color='white',
                          font_size=80, transparency=0)

# Boxes
red_health_bar = play.new_box(
    color='red', border_color='black', width=100, height=10, transparency=0)
green_health_bar = play.new_box(
    color='green', border_color='black', width=100, height=10, transparency=0)


@play.when_any_key_pressed
def begin(key):
    global show_score

    press_key_text.transparency = 0
    green_health_bar.transparency = 100
    red_health_bar.transparency = 100
    YELLOW_SHIP.transparency = 100
    show_score = True

    if len(enemy_wave) == 0:
        press_p_text.transparency = 100


@play.when_key_pressed('p', 'z')
async def enemies_come(key):
    global enemy_value
    if key == 'p':
        press_p_text.transparency = 0

        if len(enemy_wave) == 0:
            random_enemies.clear()
            for i in range(enemie_numb):
                random_enemies.append(random.choice(enemies))
            for enemy in random_enemies:
                enemy_clone = enemy.clone()
                enemy_clone.transparency = 100
                enemy_clone.x = (random.randint(-7, 7))*50
                enemy_clone.y = (random.randint(6, 12))*50
                enemy_wave.append(enemy_clone)
            enemy_value = True

    if key == 'z':  
        key = 'space'  
        end_loop = False 
        YELLOW_LASER.go_to(YELLOW_SHIP)
        YELLOW_LASER.transparency = 50
        for count in play.repeat(100):
            YELLOW_LASER.y += 5
            print(" içeri y ", YELLOW_LASER.y)
            for enemy in enemy_wave:
                # if YELLOW_LASER.is_touching(enemy):
                if YELLOW_LASER.distance_to(enemy) < 5:  
                    print("size", YELLOW_LASER.size)
                    print("top", YELLOW_LASER.top)
                    print("bottom", YELLOW_LASER.bottom)
                    end_loop = True
                    break
            if end_loop:  
                print("for count in play.repeat(180)")
                break
            await play.animate()


@play.repeat_forever
async def enemy_fire():  
    for enemy in enemy_wave:
        random_int = random.randint(0, 3)
        print("enemy_wave = ", len(enemy_wave))
        if random_int == 1:
            if (sys.platform == "darwin") or (sys.platform == "linux") or (sys.platform == "linux2"):
                
                mac_red_ship = RED_SHIP.image.split("/")
                mac_red_ship = mac_red_ship[1]

                mac_green_ship = GREEN_SHIP.image.split("/")
                mac_green_ship = mac_green_ship[1]

                mac_blue_ship = BLUE_SHIP.image.split("/")
                mac_blue_ship = mac_blue_ship[1]

                if enemy == mac_red_ship:
                    RED_LASER.go_to(enemy)
                    RED_LASER.transparency = 100
                    while RED_LASER.is_touching(YELLOW_SHIP) == False and RED_LASER.y >= -320:
                        RED_LASER.y -= 5
                        await play.animate()

                if enemy == mac_green_ship:
                    GREEN_LASER.go_to(enemy)
                    GREEN_LASER.transparency = 100
                    while GREEN_LASER.is_touching(YELLOW_SHIP) == False and GREEN_LASER.y >= -320:
                        GREEN_LASER.y -= 5
                        await play.animate()

                if enemy == mac_blue_ship:
                    BLUE_LASER.go_to(enemy)
                    BLUE_LASER.transparency = 100
                    while BLUE_LASER.is_touching(YELLOW_SHIP) == False and BLUE_LASER.y >= -320:
                        RED_LASER.y -= 5
                        await play.animate()

            else: 
                win_red_ship = RED_SHIP.image 
                
                win_green_ship = GREEN_SHIP.image[7:]

                win_blue_ship = BLUE_SHIP.image[7:]
                print("win_red_ship" + win_red_ship + " enemy = ", enemy.image)

                if enemy.image == win_red_ship:  
                    print("enemy == win_red_ship")
                    RED_LASER.go_to(enemy)
                    RED_LASER.transparency = 50
                    while (RED_LASER.is_touching(YELLOW_SHIP) == False) and (RED_LASER.y >= -320):
                        RED_LASER.y -= 5
                        await play.animate()

                if enemy == win_green_ship:
                    GREEN_LASER.go_to(enemy)
                    GREEN_LASER.transparency = 100
                    while GREEN_LASER.is_touching(YELLOW_SHIP) == False and GREEN_LASER.y >= -320:
                        GREEN_LASER.y -= 5
                        await play.animate()

                if enemy == win_blue_ship:
                    BLUE_LASER.go_to(enemy)
                    BLUE_LASER.transparency = 100
                    while BLUE_LASER.is_touching(YELLOW_SHIP) == False and BLUE_LASER.y >= -320:
                        RED_LASER.y -= 5
                        await play.animate()


@play.repeat_forever
def controls():
    if play.key_is_pressed('w'):
        YELLOW_SHIP.y += 5
    if play.key_is_pressed('s'):
        YELLOW_SHIP.y -= 5
    if play.key_is_pressed('d'):
        YELLOW_SHIP.x += 5
    if play.key_is_pressed('a'):
        YELLOW_SHIP.x -= 5


@play.repeat_forever
def collisions():
    if YELLOW_SHIP.y >= -80:
        YELLOW_SHIP.y = -80
    if YELLOW_SHIP.y <= play.screen.height // -2 + 60:
        YELLOW_SHIP.y = play.screen.height // -2 + 60
    if YELLOW_SHIP.x >= play.screen.width // 2 - 50:
        YELLOW_SHIP.x = play.screen.width // 2 - 50
    if YELLOW_SHIP.x <= play.screen.width // -2 + 50:
        YELLOW_SHIP.x = play.screen.width // -2 + 50

    for enemy in enemy_wave:
        if YELLOW_LASER.distance_to(enemy) < 10:  
            print("yellow size", YELLOW_LASER.size)
            YELLOW_LASER.transparency = 100
            enemy.x = 1000
            enemy.transparency = 0
            enemy_wave.remove(enemy)
            YELLOW_LASER.transparency = 0
            YELLOW_LASER.go_to(YELLOW_SHIP)


@play.repeat_forever
def text_on_screen():
    if show_score == True:
        level_text.words = f'Level: {level}'
        lives_text.words = f'Lives: {lives}'


@play.repeat_forever
def moving_enemies():
    for enemy in enemy_wave:
        enemy.y -= 1


@play.repeat_forever
async def main():
    global health, lives, level, enemie_numb
    for enemy in enemy_wave:
        if YELLOW_SHIP.is_touching(enemy):
            health -= 20
            green_health_bar.width -= 20
            await play.timer(seconds=0.5)
        if enemy.y <= play.screen.height // -2 - 30:
            lives -= 1
            enemy_wave.remove(enemy)
            await play.timer(seconds=0.5)

        if RED_LASER.is_touching(YELLOW_SHIP) or GREEN_LASER.is_touching(YELLOW_SHIP) \
                or BLUE_LASER.is_touching(YELLOW_SHIP):
            health -= 10
            green_health_bar.width -= 10
            await play.timer(seconds=0.5)


@play.repeat_forever
def len_check():
    global level, enemie_numb, enemy_value

    if len(enemy_wave) == 0 and enemy_value == True:
        press_p_text.transparency = 100
        level += 1
        enemie_numb += 1
        enemy_value = False


@play.repeat_forever
def show_health_bar():
    green_health_bar.go_to(YELLOW_SHIP.x, YELLOW_SHIP.y-60)
    red_health_bar.go_to(YELLOW_SHIP.x, YELLOW_SHIP.y-60)


@play.repeat_forever
async def check_health(): 
    global health, lives

    if health <= 0:
        lives -= 1
        if lives != 0:
            health += 100  
            green_health_bar.width = 100
        await play.timer(seconds=0.3) 

    if lives <= 0:
        lost_text.transparency = 100
        await play.timer(seconds=3)  
        sys.exit()


play.start_program()
