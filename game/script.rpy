image pure_white = "#ffffff"
image pure_black = "#000000"
image logo = Transform("logo.png", size=(450,450), fit = "contain")
label splashscreen:
    scene pure_white
    show pure_white with Dissolve(1.0)
    show logo at truecenter with Dissolve(1.5)
    pause 1.5
    hide logo with Dissolve(1.5)

    return

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。


init python:
    config.auto_voice = "voice/{id}.ogg"

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
define knowledge = Character("帕秋莉·诺蕾姬", image = "knowledge", who_color = "#ba55d3")
define aya = Character("射命丸文", image = "aya", who_color = "#d2691e")
define meiling = Character("红美铃", image = "meiling", who_color = "#ff0000")
define reimu = Character("博丽灵梦", image = "reimu", who_color = "#b22222")
define remilia = Character("蕾米莉亚·斯卡雷特", image = "remilia", who_color = "#dc143c")
define sun = Character("孙美天", image = "sun", who_color = "#227b22")


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
        #"高考祝福":
        #    jump exam
        "正式剧情":
            jump act1


label test:

    scene bg meeting_room with dissolve

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    # 此处显示各行对话。
    show sakuya normal at center_image

    #play voice "test_c6bd8c7c.wav"
    sakuya "您已创建一个新的游戏。"

    #voice "test-sakuya-2.wav"
    sakuya happy "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    show sakuya normal at center_image:
        happy_jump
        pause 0.5
    
    #voice "test-sakuya-3.wav"
    sakuya "啊！"
    show sakuya happy:
        linear 0.5 xpos 0.15
    #voice "test-sakuya-4.wav"
    sakuya "大小姐在叫我了！"

    return

#label exam:
#    scene bg library with dissolve
#    show knowledge normal at center_image
#    show meiling normal at left_image
#    show sakuya normal at right_image
#
#    knowledge "外面世界的年轻人，每年都会面对一场名为高考的试炼呢"
#    sakuya serious "是啊，听说就在这几天。"
#    sakuya "希望他们都能顺利把积累的实力好好发挥出来。"
#    meiling unhappy "不过一年的时间会不会太短了？"
#    sakuya relieved "别这么说，他们可是准备了三年甚至更久呢。"
#    sakuya "对他们来说，这不仅是一场测试，也是一场事关人生的重要分类"
#    knowledge relieved "愿意用这么长的时间积累知识，这份努力值得我们的尊敬。"
#    meiling happy "那我们需要做的，就是为他们祈福了吧！"
#    sakuya happy "高考结束后，记得来焦作玩哦！"
#    sakuya "下半年的焦作东方活动应该会在十一期间举行哦!"
#    show meiling confused
#    knowledge surprised "笑夜，你在说什么？"
#
#    scene pure_black with fade
#
#    return