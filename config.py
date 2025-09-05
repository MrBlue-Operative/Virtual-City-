import pygame

pygame.init()
pygame.font.init()
WIDTH, HEIGHT = 980, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA | pygame.HWSURFACE | pygame.DOUBLEBUF)
font = pygame.font.SysFont('Arial', 20)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 150, 0)
WHITE = (255, 255, 255)
FPS = 60

clock = pygame.time.Clock()
BACKGROUND = GREEN

ofx = 0
ofy = 0
offsets_changed = False
car_x = 0
car_y = 0
follow_player = False

def KEYS():
    return pygame.key.get_pressed()

def update_car_position(x, y, follow):
    global car_x, car_y, follow_player
    car_x, car_y = x, y
    follow_player = follow

def update_offsets():
    global ofx, ofy, offsets_changed
    old_ofx, old_ofy = ofx, ofy
    if follow_player:
        ofx = WIDTH / 2 - car_x
        ofy = HEIGHT / 2 - car_y
    else:
        # Manual panning
        keys = KEYS()
        pan_speed = 15
        if keys[pygame.K_LEFT]:
            ofx += pan_speed
        if keys[pygame.K_RIGHT]:
            ofx -= pan_speed
        if keys[pygame.K_UP]:
            ofy += pan_speed
        if keys[pygame.K_DOWN]:
            ofy -= pan_speed
        if pygame.mouse.get_pressed()[0]:
            pygame.mouse.get_rel()
            dx, dy = pygame.mouse.get_rel()
            if abs(dx) > 1 or abs(dy) > 1:
                ofx += dx
                ofy += dy
    offsets_changed = (abs(ofx - old_ofx) > 0.1 or abs(ofy - old_ofy) > 0.1)

def MOUSE():
    pos = list(pygame.mouse.get_pos())
    pos[0] -= ofx
    pos[1] -= ofy
    return tuple(pos)