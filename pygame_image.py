import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん") # ゲームのタイトル部分
    screen = pg.display.set_mode((800, 600)) # 800x600のサイズをタプルで渡す
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") # load()で画像読み込む
    kk_img = pg.image.load("fig/3.png") # 練習2
    kk_img = pg.transform.flip(kk_img, True, False) # 練習2 反転 (画像, 左右, 上下)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = -(tmr%800)
        screen.blit(bg_img, [x, 0])
        screen.blit(kk_img, [300, 200]) # 練習3 貼る順番は注意する
        pg.display.update()
        tmr += 1
        # if tmr > 800:
        #     tmr = 0       
        clock.tick(200) # 練習5 


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()