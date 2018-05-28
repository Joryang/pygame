import pygame
from pygame.locals import *
from time import time
from os.path import dirname, realpath

def main():
    tempo = time()
    maior_update = 0
    maior_draw = 0
    maior_running = 0
    soma_update = 0
    soma_draw = 0
    soma_running = 0
    quant = 0
    running, settings = load()
    print("load: %.4f" %(time()-tempo))
    while running:
        quant+=1
        init = time()
        #settings = update(settings)
        settings = update(settings)

        if time()-init>maior_update:
            maior_update = time()-init
        soma_update += time()-init
        init = time()

        draw(settings)

        if time()-init>maior_draw:
            maior_draw = time()-init
        soma_draw += time()-init
        init = time()

        running = check_exit(settings)

        if time()-init>maior_running:
            maior_running = time()-init
        soma_running += time()-init
    
    print
    print('maior_update : %.4f sec' % (maior_update))
    print('maior_draw   : %.4f sec' % (maior_draw))
    print('maior_running: %.4f sec' % (maior_running))
    print
    print('media_update : %.4f sec' % (soma_update/quant))
    print('media_draw   : %.4f sec' % (soma_draw/quant))
    print('media_running: %.4f sec' % (soma_running/quant))
    pygame.quit()

def load():
    screen_size = (670, 515)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('SHADERS TEST - ULISSES GANDINI')
    game_object = {
        'bg'            : [],
        'text'          : [], #not printed in the screen, just invert the color behind
    }
    var = {
        'folder'        : dirname(realpath(__file__)),
        'exit_request'  : False
    }
    return True, {
        'screen_size'   : screen_size,
        'screen'        : screen,
        'game_object'   : game_object,
        'var'           : var,
    }

def update(settings):
    return settings

def draw(settings):
    pass

def check_exit(settings):
    if settings['var']['exit_request']:
        return False
    k = pygame.key.get_pressed()
    for e in pygame.event.get():
        if e.type == QUIT or k[K_ESCAPE]:
            return False
    return True

class Sprite():
    def __init__(self, x, y, path):
        self.x = x
        self.y = y
        self.img = pygame.image.load(path)

main()