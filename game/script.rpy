define sakura = Character("{b}【立山樱】{/b}", who_color="#00eeff", what_prefix="『", what_suffix="』")
define zuco = Character("{b}【左桃】{/b}", who_color="#ff0000", what_prefix="『", what_suffix="』")
define hisaki = Character("{b}【鸠山寿希】{/b}", who_color="#000dff", what_prefix="『", what_suffix="』")
define ryuka = Character("{b}【原林柳香】{/b}", who_color="#ff8989", what_prefix="『", what_suffix="』")
define wakayo = Character("{b}【淳谷若夜】{/b}", who_color="#ff00f2", what_prefix="『", what_suffix="』")
define toichi = Character("{b}【淳谷桐市】{/b}", who_color="#26ff00", what_prefix="『", what_suffix="』")
define mina = Character("{b}【素山未菜】{/b}", who_color="#b8b324", what_prefix="『", what_suffix="』")

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


init python:
    import random
    max_musics = 11
    menu_musics = "audio/opbgm/opbgm" + str(random.randint(1,max_musics)) + ".mp3"

define config.main_menu_music = menu_musics

# define build.game_only_update = True

label start:
    jump chapters_1