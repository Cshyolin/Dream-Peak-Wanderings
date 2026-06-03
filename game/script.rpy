image pure_white = "#ffffff"
image pure_black = "#000000"
image logo = Transform("logo.png", size=(450,450), fit = "contain")
label splashscreen:
    scene pure_white
    show pure_white with Dissolve(2.0)
    show logo at truecenter with Dissolve(2.0)
    pause 1.0
    hide logo with Dissolve(2.0)

    return

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

init:
    $ center_image = Position(xpos=0.5, ypos=1.18)
    $ left_image = Position(xpos=0.15, ypos=1.18)
    $ right_image = Position(xpos=0.85, ypos=1.18)
    $ centerleft_image = Position(xpos=0.3, ypos=1.18)
    $ leftleft_image = Position(xpos=0.05, ypos=1.18)
    $ rightright_image = Position(xpos=0.95, ypos=1.18)
    $ centerright_image = Position(xpos=0.7, ypos=1.18)

transform happy_jump:
    linear 0.125 yoffset -15
    linear 0.125 yoffset 15
    yoffset 0
    repeat 2
transform shake:
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    repeat 5
#来回踱步
transform walk:
    linear 0.5 xoffset -400
    xzoom -1
    linear 1.0 xoffset 400
    xzoom 1
    linear 0.5 xoffset 0
#快速踱步
transform walk_fast:
    linear 0.2 xoffset -400
    xzoom -1
    linear 0.4 xoffset 400
    xzoom 1
    linear 0.2 xoffset 0

define e = Character("艾琳", image = "eileen")
define sakuya = Character("十六夜咲夜", image = "sakuya", who_color = "#1e90ff")


# 游戏在此开始。
label start:
    scene pure_black with fade
    """
    这是焦作THP03的剧情测试工程

    接下来将会播放测试片段

    正式完成后会提供选项以跳到正式剧情
    """
    menu:
        "测试片段":
            jump test
        "正式剧情":
            return


label test:

    scene bg meeting_room with dissolve

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    # 此处显示各行对话。
    show sakuya normal at center_image
    sakuya "您已创建一个新的 Ren'Py 游戏。"

    sakuya happy "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    show sakuya normal at center_image:
        happy_jump
        pause 0.5
    sakuya "啊！"
    show sakuya happy:
        linear 0.5 xpos 0.15
    sakuya "大小姐在叫我了！"

    return
