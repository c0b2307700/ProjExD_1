import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん") # ゲームのタイトル部分
    screen = pg.display.set_mode((800, 600)) # 800x600のサイズをタプルで渡す
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") # load()で画像読み込む
    bg_img1 = pg.transform.flip(bg_img, True, False) # 練習7反転背景
    kk_img = pg.image.load("fig/3.png") # 練習2
    kk_img = pg.transform.flip(kk_img, True, False) # 練習2 反転 (画像, 左右, 上下)
    kk_rct = kk_img.get_rect() # 練習8-1 sarfaceからrectを抽出する
    kk_rct.center = 300, 200 # 練習8-1 rectを用いた初期座標の設定
    tmr = 0
    while True:
        for event in pg.event.get(): # 2回目で説明？
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed() # 練習8-3 キーの押下状態を判定
        if key_lst[pg.K_UP]: # ↑キーが押されていたら
            kk_rct.move_ip((0, -1)) # こうかとんのY座標を-1する
        if key_lst[pg.K_DOWN]: # 練習8-4 あたり
            kk_rct.move_ip((0, +1)) # move_ip(x, y)で移動させることができる
        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip((+1, 0))
        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip((-1, 0))
        
        
        x = -(tmr%3200)
        screen.blit(bg_img, [x, 0]) # 練習6 間延びと画像動かす
        screen.blit(bg_img1, [x+1600, 0]) # 練習7 2つ目の背景
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg_img1, [x+4800, 0])
        screen.blit(kk_img, kk_rct) # 練習3 貼る順番は注意する -> # 練習8-5 座標を先ほど保存したものにする
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