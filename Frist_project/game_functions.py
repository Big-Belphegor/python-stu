__author__ = "Alien"
import sys
import pygame
from bullet import Bullet
from alien import Alien

def get_number_aliens_x(ai_settings,alien_width):
    '''计算每行可容纳多少个外星人'''

    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    '''计算屏幕可以容纳多少个外星人'''

    available_space_y = (ai_settings.screen_height - (5 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    '''创建一个外星人并将其加入当前行'''

    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    '''创建外星人群'''

    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_row = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    # 创建第一行外星人
    for row_number in range(number_row):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,row_number)

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    '''按键按下时执行的操作'''

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def check_keyup_events(event,ship):
    '''按键弹起时执行的操作'''

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_events(ai_settings,screen,ship,bullets):
    '''监视键盘和鼠标'''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 当鼠标单击关闭键时，执行sys系统命令
            sys.exit()

        # elif event.type == pygame.KEYDOWN:        # 此方法为每按一次右键移动一下
        #     # 向右移动飞船
        #     ship.rect.centerx += 1
        elif event.type == pygame.KEYDOWN:          # 此方法为持续或单击都会移动
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_fleet_edges(ai_settings,aliens):
    '''有外星人到达边缘时采取相应措施'''

    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    '''将整个外星人下移，并改变他们的方向'''

    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_screen(ai_settings,screen,ship,aliens,bullets):
    '''初始化窗口状态'''
    screen.fill(ai_settings.bg_color)   # 每次循环都重绘屏幕
    for bullet in bullets.sprites():    # 要在之前
        bullet.draw_bullet()
    ship.blitme()                       # 将飞船绘制在屏幕上
    # alien.blitme()
    aliens.draw(screen)                      # 将外星人绘制在屏幕上
    pygame.display.flip()               # 让最近绘制的屏幕可见

def update_bullets(aliens,bullets):
    '''更新子弹的位置，并删除已消失的子弹'''

    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 检查是否有子弹击中，如果有就删除子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

def update_aliens(ai_settings,aliens):
    '''更新外星人群中所有外星人的位置'''

    check_fleet_edges(ai_settings,aliens)
    aliens.update()