import pygame
import math
import random
import os

# تنظیمات اولیه
pygame.init()
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gorgali The Warrior")
clock = pygame.time.Clock()

# رنگ‌ها
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# بارگذاری و تغییر اندازه تصاویر
def load_and_scale_image(filename, scale_factor):
    image = pygame.image.load(filename)
    width, height = image.get_size()
    new_size = (int(width * scale_factor), int(height * scale_factor))
    return pygame.transform.scale(image, new_size)


player_img = load_and_scale_image('img/survivor-idle_rifle_0.png', 0.4)  # تصویر بازیکن
bullet_img = load_and_scale_image('img/19.png', 0.4)  # تصویر تیر
enemy_img = load_and_scale_image('img/preview_344.png', 0.4)  # تصویر دشمن
enemy_img = pygame.transform.rotate(enemy_img, 90)  # چرخش 90 درجه پادساعتگرد
package_img = load_and_scale_image('img/—Pngtree—crimson first aid box clip_5964434.png', 0.1)  # تصویر بسته، 60 درصد کوچکتر
 # تصویر بسته، 60 درصد کوچکتر
menu_bg_img = pygame.image.load('img/backgrounddetailed2.png')  # پس‌زمینه منو (تصویر باید در پوشه پروژه باشد)
menu_bg_img = pygame.transform.scale(menu_bg_img, (width, height))

# ویژگی‌های بازیکن
player_pos = [width / 2, height / 2]
player_speed = 5
player_radius = 20
player_lives = 1.0  # نوار سلامتی به صورت درصد

# ویژگی‌های تیرها
bullets = []
bullet_speed = 20
bullet_radius = 10

# ویژگی‌های دشمنان
enemies = []
enemy_speed = 3
enemy_bullets = []
enemy_bullet_speed = 10

# ویژگی‌های بسته
package = None

# موج‌ها
wave = 1
enemies_spawned = 0
max_enemies = wave  # تعداد دشمنان در هر موج برابر با شماره موج است

# امتیاز
score = 0
high_score = 0  # امتیاز بالا

# مسیر فایل ذخیره‌سازی امتیاز بالا
high_score_file = 'high_score.txt'

def save_high_score():
    with open(high_score_file, 'w') as file:
        file.write(str(high_score))

def load_high_score():
    if os.path.exists(high_score_file):
        with open(high_score_file, 'r') as file:
            return int(file.read())
    return 0

high_score = load_high_score()

def draw_player():
    mouse_pos = pygame.mouse.get_pos()
    angle = math.degrees(math.atan2(mouse_pos[1] - player_pos[1], mouse_pos[0] - player_pos[0]))
    rotated_player_img = pygame.transform.rotate(player_img, -angle)
    player_rect = rotated_player_img.get_rect(center=(player_pos[0], player_pos[1]))
    window.blit(rotated_player_img, player_rect.topleft)

def draw_bullets():
    for bullet in bullets:
        bullet_img_rotated = pygame.transform.rotate(bullet_img, bullet['angle'])
        bullet_rect = bullet_img_rotated.get_rect(center=(bullet['pos'][0], bullet['pos'][1]))
        window.blit(bullet_img_rotated, bullet_rect.topleft)

def draw_enemies():
    for enemy in enemies:
        direction = [player_pos[0] - enemy['pos'][0], player_pos[1] - enemy['pos'][1]]
        angle = math.degrees(math.atan2(direction[1], direction[0]))
        rotated_enemy_img = pygame.transform.rotate(enemy_img, -angle)
        enemy_rect = rotated_enemy_img.get_rect(center=(enemy['pos'][0], enemy['pos'][1]))
        window.blit(rotated_enemy_img, enemy_rect.topleft)

def draw_enemy_bullets():
    for bullet in enemy_bullets:
        bullet_img_rotated = pygame.transform.rotate(bullet_img, bullet['angle'])
        bullet_rect = bullet_img_rotated.get_rect(center=(bullet['pos'][0], bullet['pos'][1]))
        window.blit(bullet_img_rotated, bullet_rect.topleft)

def draw_health_bar():
    health_bar_width = 200
    health_bar_height = 20
    bar_x = 10
    bar_y = height - 30
    pygame.draw.rect(window, WHITE, (bar_x, bar_y, health_bar_width, health_bar_height), 2)
    fill_width = (health_bar_width - 4) * (player_lives / 1.0)
    pygame.draw.rect(window, GREEN, (bar_x + 2, bar_y + 2, fill_width, health_bar_height - 4))

def draw_package():
    if package:
        package_rect = package_img.get_rect(center=(package['pos'][0], package['pos'][1]))
        window.blit(package_img, package_rect.topleft)

def move_player():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_pos[0] -= player_speed
    if keys[pygame.K_d]:
        player_pos[0] += player_speed
    if keys[pygame.K_w]:
        player_pos[1] -= player_speed
    if keys[pygame.K_s]:
        player_pos[1] += player_speed

def shoot_bullet(mouse_pos):
    direction = [mouse_pos[0] - player_pos[0], mouse_pos[1] - player_pos[1]]
    distance = math.hypot(direction[0], direction[1])
    direction[0] /= distance
    direction[1] /= distance
    bullet_pos = [player_pos[0], player_pos[1]]
    angle = math.degrees(math.atan2(direction[1], direction[0]))
    bullets.append({'pos': bullet_pos, 'dir': direction, 'angle': -angle})

def shoot_enemy_bullet(enemy):
    direction = [player_pos[0] - enemy['pos'][0], player_pos[1] - enemy['pos'][1]]
    distance = math.hypot(direction[0], direction[1])
    direction[0] /= distance
    direction[1] /= distance
    bullet_pos = [enemy['pos'][0], enemy['pos'][1]]
    angle = math.degrees(math.atan2(direction[1], direction[0]))
    enemy_bullets.append({'pos': bullet_pos, 'dir': direction, 'angle': -angle})

def update_bullets():
    global bullets
    bullets = [bullet for bullet in bullets if 0 <= bullet['pos'][0] < width and 0 <= bullet['pos'][1] < height]
    for bullet in bullets:
        bullet['pos'][0] += bullet['dir'][0] * bullet_speed
        bullet['pos'][1] += bullet['dir'][1] * bullet_speed

def update_enemy_bullets():
    global enemy_bullets
    enemy_bullets = [bullet for bullet in enemy_bullets if 0 <= bullet['pos'][0] < width and 0 <= bullet['pos'][1] < height]
    for bullet in enemy_bullets:
        bullet['pos'][0] += bullet['dir'][0] * enemy_bullet_speed
        bullet['pos'][1] += bullet['dir'][1] * enemy_bullet_speed

def update_enemies():
    global enemies, enemies_spawned, wave, max_enemies
    if enemies_spawned < max_enemies:
        spawn_enemy()
        enemies_spawned += 1
    for enemy in enemies:
        direction = [player_pos[0] - enemy['pos'][0], player_pos[1] - enemy['pos'][1]]
        distance = math.hypot(direction[0], direction[1])
        direction[0] /= distance
        direction[1] /= distance
        enemy['pos'][0] += direction[0] * enemy_speed
        enemy['pos'][1] += direction[1] * enemy_speed
        if random.random() < 0.01:  # شلیک تصادفی دشمن
            shoot_enemy_bullet(enemy)

def spawn_enemy():
    for _ in range(wave):  # تعداد دشمنان بر اساس موج تعیین می‌شود
        side = random.choice(['left', 'right', 'top', 'bottom'])
        if side == 'left':
            x = -20
            y = random.randint(0, height)
        elif side == 'right':
            x = width + 20
            y = random.randint(0, height)
        elif side == 'top':
            x = random.randint(0, width)
            y = -20
        elif side == 'bottom':
            x = random.randint(0, width)
            y = height + 20
        enemies.append({'pos': [x, y], 'radius': 20})

def check_collisions():
    global bullets, enemies, enemy_bullets, player_lives, score, wave, enemies_spawned, max_enemies, package
    # برخورد تیر بازیکن با دشمن
    for bullet in bullets:
        for enemy in enemies:
            if math.hypot(bullet['pos'][0] - enemy['pos'][0], bullet['pos'][1] - enemy['pos'][1]) < bullet_radius + enemy['radius']:
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 10
                break

    # برخورد تیر دشمن با بازیکن
    for bullet in enemy_bullets:
        if math.hypot(bullet['pos'][0] - player_pos[0], bullet['pos'][1] - player_pos[1]) < bullet_radius + player_radius:
            player_lives -= 0.05  # هر تیر 5 درصد از جان را کم می‌کند
            enemy_bullets.remove(bullet)
            if player_lives <= 0:
                game_over()
            break

    # بررسی برخورد بازیکن با بسته
    if package:
        if math.hypot(package['pos'][0] - player_pos[0], package['pos'][1] - player_pos[1]) < package_img.get_width() / 2 + player_radius:
            player_lives = 1.0  # پر شدن نوار سلامت
            package = None  # حذف بسته بعد از جمع‌آوری

    # بررسی اگر همه دشمنان کشته شدند، به موج بعدی برویم
    if len(enemies) == 0 and enemies_spawned >= max_enemies:
        spawn_package()
        wave += 1
        enemies_spawned = 0
        max_enemies = wave  # افزایش تعداد دشمنان در هر موج

def spawn_package():
    global package
    package_x = random.randint(50, width - 50)
    package_y = random.randint(50, height - 50)
    package = {'pos': [package_x, package_y]}

def draw_score():
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f'Score: {score}', True, WHITE)
    lives_text = font.render(f'Lives: {int(player_lives * 100)}%', True, WHITE)
    wave_text = font.render(f'Wave: {wave}', True, WHITE)
    high_score_text = font.render(f'High Score: {high_score}', True, WHITE)
    window.blit(score_text, (10, 10))
    window.blit(lives_text, (10, 50))
    window.blit(wave_text, (10, 90))
    window.blit(high_score_text, (10, 130))

def game_over():
    global high_score
    if score > high_score:
        high_score = score
        save_high_score()
    font = pygame.font.SysFont(None, 72)
    text = font.render("GAME OVER", True, RED)
    rect = text.get_rect(center=(width / 2, height / 2))
    window.blit(text, rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    main_menu()

def main_menu():
    font = pygame.font.SysFont('comicsansms', 48)
    title_font = pygame.font.SysFont('comicsansms', 80)
    window.blit(menu_bg_img, (0, 0))  # پس‌زمینه منو

    # عنوان
    title = title_font.render("Gorgali The Warrior", True, WHITE)
    window.blit(title, (width // 2 - title.get_width() // 2, height // 2 - title.get_height() // 2 - 100))

    # متن شروع
    start_text = font.render("Press ENTER to Start", True, GREEN)
    window.blit(start_text, (width // 2 - start_text.get_width() // 2, height // 2 + 50))

    # متن خروج
    quit_text = font.render("Press ESC to Quit", True, RED)
    window.blit(quit_text, (width // 2 - quit_text.get_width() // 2, height // 2 + 150))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

def main():
    global score, player_lives, wave, enemies_spawned, max_enemies, enemies, bullets, enemy_bullets, package
    score = 0
    player_lives = 1.0
    wave = 1
    enemies_spawned = 0
    max_enemies = wave
    enemies = []
    bullets = []
    enemy_bullets = []
    package = None

    running = True
    while running:
        window.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    shoot_bullet(pygame.mouse.get_pos())

        move_player()
        update_bullets()
        update_enemy_bullets()
        update_enemies()
        check_collisions()

        draw_player()
        draw_bullets()
        draw_enemies()
        draw_enemy_bullets()
        draw_health_bar()
        draw_score()
        draw_package()  # رسم بسته

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main_menu()
