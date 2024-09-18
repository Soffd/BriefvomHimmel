define sakura = Character("{b}【立山樱】{/b}", who_color="#00eeff", what_prefix="『", what_suffix="』")
define zuco = Character("{b}【左桃】{/b}", who_color="#ff0000", what_prefix="『", what_suffix="』")
define hisaki = Character("{b}【鸠山寿希】{/b}", who_color="#000dff", what_prefix="『", what_suffix="』")
define ryuka = Character("{b}【原林柳香】{/b}", who_color="#ff8989", what_prefix="『", what_suffix="』")
define wakayo = Character("{b}【淳谷若夜】{/b}", who_color="#ff00f2", what_prefix="『", what_suffix="』")
define toichi = Character("{b}【淳谷桐市】{/b}", who_color="#26ff00", what_prefix="『", what_suffix="』")
define mina = Character("{b}【素山未菜】{/b}", who_color="#b8b324", what_prefix="『", what_suffix="』")
define kazumi = Character("{b}【九楽佳澄】{/b}", who_color="#ff0066", what_prefix="『", what_suffix="』")
define mosheng = Character("{b}【陌生的声音】{/b}", who_color="#000000", what_prefix="『", what_suffix="』")

image sakurab = "a/A1-2.png"
image sakurac = "a/A1-3.png"

image zucoa = "b/B3-1.png"
image zucob = "b/B3-2.png"
image zucoc = "b/B3-3.png"
image zucod = "b/B3-4.png"
image zucoe = "b/B3-5.png"
image zucog = "b/B3-7.png"
image zucoh = "b/B3-8.png"
image zucof = "b/B3-6.png"

image ryukaa = "c/C1-1.png"
image ryukah = "c/C1-8.png"
image ryukag = "c/C1-7.png"
image ryukac = "c/C1-3.png"
image ryukad = "c/C1-4.png"
image ryukab = "c/C1-2.png"
image ryukae = "c/C1-5.png"
image ryukaf = "c/C1-6.png"

image wakayo1 = "RJ01155638/a1.png"
image wakayo2 = "RJ01155638/a2.png"
image wakayo3 = "RJ01155638/a3.png"
image wakayo4 = "RJ01155638/a4.png"
image wakayo5 = "RJ01155638/a5.png"
image wakayo6 = "RJ01155638/a6.png"
image wakayo7 = "RJ01155638/a7.png"
image wakayo8 = "RJ01155638/a8.png"
image wakayo9 = "RJ01155638/a9.png"
image wakayo10 = "RJ01155638/a10.png"
image wakayo11 = "RJ01155638/a11.png"

image toichi1 = "sozai/sozai_47_b.png"
image toichi2 = "sozai/sozai_48_b.png"
image toichi3 = "sozai/sozai_49_b.png"
image toichi4 = "sozai/sozai_50_b.png"
image toichi5 = "sozai/sozai_51_b.png"
image toichi6 = "sozai/sozai_52_b.png"

image mina1 = "sozai1/sozai_42.png"
image mina2 = "sozai1/sozai_43.png"
image mina3 = "sozai1/sozai_44.png"
image mina4 = "sozai1/sozai_45.png"
image mina5 = "sozai1/sozai_46.png"

image kazumi1 = "RJ01235150/xile1.png"
image kazumi2 = "RJ01235150/xile2.png"
image kazumi3 = "RJ01235150/xile3.png"
image kazumi4 = "RJ01235150/xile4.png"
image kazumi5 = "RJ01235150/xile5.png"
image kazumi6 = "RJ01235150/xile6.png"
image kazumi7 = "RJ01235150/xile7.png"
image kazumi8 = "RJ01235150/xile8.png"
image kazumi9 = "RJ01235150/xile9.png"
image kazumi10 = "RJ01235150/xile10.png"

init python:
    import random
    max_musics = 11
    menu_musics = "audio/opbgm/opbgm" + str(random.randint(1,max_musics)) + ".mp3"

define config.main_menu_music = menu_musics
## 标题菜单和游戏菜单使用的图像。
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"

init python:
    import datetime
    def get_month():
        return datetime.datetime.now().month
    def get_day():
        return datetime.datetime.now().day

image splash = "splash.png"

label splashscreen:
    $ _dismiss_pause = False
    scene black
    with Pause(1)
    scene splash with dissolve
    with Pause(2)
    scene black with dissolve
    with Pause(1)
    show text "{b}{size=+20}{color=#f00}检测游戏版本中......" with dissolve
    with Pause(2)
    hide text
    $ _dismiss_pause = True
    jump updata
label updata:
    $ _dismiss_pause = False
    $ quick_menu = False
    define config.save = False
    scene black
    show text "{b}{size=+20}{color=#f00}检测游戏版本中......"
    python:
        version = 16
        validate = 0
        updata = 0
        updata_error = 0
        new_version = renpy.fetch("https://yukisoffd.com/new_version.txt", result="text")
        new_version_num = int(new_version)
        if version == new_version_num:
            validate += 1
        if version < new_version_num:
            updata += 1
        if version > new_version_num:
            updata_error += 1
    hide text with dissolve
    if validate == 1:
        show text "{b}{size=+20}{color=#f00}游戏版本检测完毕！已是最新版本！" with dissolve
        with Pause(2)
        hide text with dissolve
        return
    if updata == 1:
        call screen updata_screem
    if updata_error == 1:
        call screen error_screem
    $ _dismiss_pause = True
    $ quick_menu = True
    define config.save = True         
    return

label start:
    jump chapters_1

screen updata_screem():
    frame:
        xcenter 0.5
        ycenter 0.5
        xsize 800
        ysize 300
        vbox:
            text "{b}你当前的游戏版本不是最新的，建议前往官网更新！\n\n\n"
            textbutton _("仍要进入") action Return("updata_screem")
            text "{a=https://yukisoffd.com/bvhdownload/}{b}前往更新{/a}{/b}"

screen error_screem():
    frame:
        xcenter 0.5
        ycenter 0.5
        xsize 800
        ysize 300
        vbox:
            text "{b}你当前的游戏可能不是官方版本！\n\n\n"
            textbutton _("退出游戏") action Quit()
            text "{a=https://yukisoffd.com/bvhdownload/}{b}前往下载最新版本{/a}{/b}"