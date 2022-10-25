from turtle import speed
import pygame as pg
import sys
from random import randint


#7
def check_bound(obj_rct, scr_rct):#obj_rct:コウカトンrctまたは爆弾rct, scr_rct:スクリーンrct
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

def main():
    pg.display.set_caption("逃げろ！コウカトン")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    #3
    num=0#初期値0
    tori_sfc = pg.image.load(f"fig/{num}.png")#変更
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    #5
    bomb_sfc = pg.Surface((20,20))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, scrn_rct.width)
    bomb_rct.centery = randint(0,scrn_rct.height)

    #爆弾2個め
    bomb2_sfc = pg.Surface((20,20))
    bomb2_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb2_sfc, (255, 0, 0), (10, 10), 10)
    bomb2_rct = bomb2_sfc.get_rect()
    bomb2_rct.centerx = randint(0, scrn_rct.width)
    bomb2_rct.centery = randint(0,scrn_rct.height)
    
    #6
    #爆弾のスピード速く
    vx, vy = +3, +3
    vx2, vy2 = +3, +3

    clock = pg.time.Clock()#練習1
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)#練習2

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        #4
        key_states= pg.key.get_pressed()
        if key_states[pg.K_UP]: #コウカトンの縦座標を-1
            tori_rct.centery -=1
        if key_states[pg.K_DOWN]:
            tori_rct.centery +=1
        if key_states[pg.K_LEFT]:
            tori_rct.centerx -=1
        if key_states[pg.K_RIGHT]:
            tori_rct.centerx +=1

        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_states[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -=1
        if tate == -1:
            if key_states[pg.K_UP]:
                tori_rct.centery += 1
            if key_states[pg.K_DOWN]:
                tori_rct.centery -=1
        scrn_sfc.blit(tori_sfc, tori_rct)#3

        #7
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        yoko2, tate2 = check_bound(bomb2_rct, scrn_rct)
        vx2 *= yoko2
        vy2 *= tate2       

        bomb_rct.move_ip(vx, vy)#6
        bomb2_rct.move_ip(vx2, vy2)
        scrn_sfc.blit(bomb_sfc, bomb_rct)#5
        scrn_sfc.blit(bomb2_sfc, bomb2_rct)

        #8

        #爆弾に当たると画像変わる
        if tori_rct.colliderect(bomb_rct):
            num+=1
            if num > 9:
                num=0
            tori_sfc = pg.image.load(f"fig/{num}.png")
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
        
        if tori_rct.colliderect(bomb2_rct):
            num+=1
            if num > 9:
                num=0
            tori_sfc = pg.image.load(f"fig/{num}.png")
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)

        #Escapeキーで終了
        if key_states[pg.K_ESCAPE]:
            return

        pg.display.update()
        clock.tick(1000)



if __name__ == "__main__":
    pg.init()         #モジュールを初期化
    main()            #ゲームの本体
    pg.quit()         #モジュールの初期化を解除する
    sys.exit()