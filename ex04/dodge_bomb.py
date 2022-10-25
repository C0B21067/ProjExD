import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！コウカトン")
    scrn_sfc = pg.display.set_mode((1600,900))

    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    #3
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    

    clock = pg.time.Clock()#練習1
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)#練習2

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_states= pg.key.get_pressed()
        if key_states[pg.K_UP]: #コウカトンの縦座標を-1
            tori_rct.centery -=20
        if key_states[pg.K_DOWN]:
            tori_rct.centery +=20
        if key_states[pg.K_LEFT]:
            tori_rct.centerx -=20
        if key_states[pg.K_RIGHT]:
            tori_rct.centerx +=20

        scrn_sfc.blit(tori_sfc, tori_rct)

        pg.display.update()
        clock.tick(1000)



if __name__ == "__main__":
    pg.init()         #モジュールを初期化
    main()            #ゲームの本体
    pg.quit()         #モジュールの初期化を解除する
    sys.exit()