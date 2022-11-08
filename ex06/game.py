import pygame as pg
import sys
from random import randint
import pygame.mixer
import time


class Screen:#スクリーン表示
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title) #逃げろ！こうかとん
        self.sfc = pg.display.set_mode(wh) #(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) #"fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect()
    
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Kokaton:#こうかとん表示
    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) # "fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy # 400, 420

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.blit(scr)


class EnemyBird:#敵の鳥
    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) # "enemy_bird.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy # 1200, 420

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.blit(scr)


class Fight:#合図
    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) # "enemy_bird.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy # 1200, 420

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.blit(scr)


class Judgment:#判定する
    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) 
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy 

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.blit(scr)


def main():
    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    kkt = Kokaton("fig/2.png", 2.0, (400, 420))#こうかとんインスタンス化
    ebd = EnemyBird("fig/enemy_bird.png", 0.7/2, (1200, 420))#敵鳥インスタンス化
    fgt = Fight("fig/gogo.png", 0.5, (800,400))#合図インスタンス化
    win = Judgment("fig/win.jpg", 2, (400,420))
    fight_time = 0

    diley_frame = randint(2000, 5000)#2秒から5秒で表示させる

    clock = pg.time.Clock()


    while True:
        scr.blit() 
        kkt.blit(scr)
        ebd.blit(scr)
        key_status = pg.key.get_pressed()

        if pg.time.get_ticks() >= diley_frame and pg.time.get_ticks() <= 10000:#diley_frame以上、10秒以下の時fgtを呼び出す
            fgt.update(scr)
            if fight_time == 0:
                fight_time = pg.time.get_ticks()
                cpu = fight_time + randint(1000,1500)#cpuの時間は計測開始から1から1.5秒後
        

        if key_status[pg.K_SPACE]:
            push_time = pg.time.get_ticks()
            if push_time - fight_time < cpu:#コンピュータより早いかどうかの判定
                print("WIN")
            else:
                print("LOSE")

        if pg.time.get_ticks() >= 10000:#10秒以内に押せないと強制終了
            return


        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        pg.display.update() 
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()