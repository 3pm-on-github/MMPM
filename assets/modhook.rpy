# menu changements

screen main_menu():

    tag menu

    key "t" action ShowMenu("mmpmtoolbox")

    add gui.main_menu_background

    frame:
        style "main_menu_frame"

    use navigation

    if gui.show_name:
        vbox:
            style "main_menu_vbox"
            text "[config.name]" style "main_menu_title"
            text "[config.version]" style "main_menu_version"
            text "Modded with MMPM 0.0.1@ALPHA1.2.1" style "main_menu_version"

screen about():

    tag menu

    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")
            text _("MMPM Version 0.0.1@ALPHA1.2.1\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
            text _("Modded with MMPM by 3pm.")

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    key "t" action ShowMenu("mmpmtoolbox")

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")
    
    hbox:
        label "T"
        text _("Opens the MMPM Toolbox.")

# mmpm toolbox

init python:
    def MoneyBoost():
        persistent.money += 1000000
    def MoneyReset():
        persistent.money = 2
    def MaxMoney():
        persistent.money = 10**100

screen mmpmtoolbox():
    tag menu
    frame:
        style "main_menu_frame"
        add "mmpmimages/car.png"

        textbutton "Back" action Return()

        textbutton "Cheats" action ShowMenu("mmpmcheats") ypos 60 xpos 25

screen mmpmcheats():
    tag menu
    frame:
        style "main_menu_frame"
        add "mmpmimages/car.png"

        textbutton "Back" action Return()

        textbutton "Money Boost (gives +1000000 money)" action MoneyBoost ypos 60 xpos 25
        textbutton "Max Money (sets money to a very high amount)" action MaxMoney ypos 120 xpos 25
        textbutton "Money Reset (resets money to 2 money)" action MoneyReset ypos 205 xpos 25

# other stuff

label mmpp1:
    $ config.allow_skipping = True
    "MMPM" "MMPM Injected. Thank you."
    stop music
    jump thesrar

# kys renpy, its not overriding the credits

init python:
    # Credits content
    credits = [
        ('Game by', 'Rodrigo Travanca'),
        ('Code', 'Errors and Issues Fixed by 3pm'),
        ('Music', 'Kevin MacLeod'),
        ('Music', 'Undertale OST'),
        ('Music', 'Pixabay Sounds'),
        ('Sound Effects', 'Pixabay Sounds'),
        ('Sound Effects', 'Other Free Sources'),
        ('GUI Design', 'Feniks (itch.io)'),
        ('Special Thanks', 'Swatxx'),
        ('Special Thanks', '3pm'),
        ('Special Thanks', 'Rodrigo Travanca Friends'),
        ('Contributors', '3pm, Swatxx, and IRL Friends'),
        ('Testing', '3pm'),
        ('Testing', 'Swatxx'),
        ('Engine', 'Ren\'Py Visual Novel Engine'),
        ('Inspirations', 'DSAF Series and Five Nights at Freddy\'s'),
        ('Inspirations', 'Full credits to the assets from FNAF'),
        ('A game made for', 'Swatxx, and the friend builders & fans members!'),
        ('Thank You!', 'To Everyone Involved'),
        ('Special Thanks (added by MMPM)', 'To Myself, 3pm, who made this tool by a modder, for modders.')
    ]

    # Build the scrolling text
    credits_s = "{size=80}{color=#FF0000}Credits{/color}\n\n"
    c1 = ''
    for c in credits:
        if c1 != c[0]:
            credits_s += "\n{size=60}{color=#FF0000}" + c[0] + "{/color}\n"
        credits_s += "{size=40}{color=#FF0000}" + c[1] + "{/color}\n"
        c1 = c[0]

    # Add Ren'Py version to the credits
    credits_s += "\n{size=60}{color=#FF0000}Engine{/color}\n{size=40}{color=#FF0000}" + renpy.version() + "{/color}"

label creditsmodeltwo:
    # credits screen two sir
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}{color=#FF0000}The End..{/color}", text_align=0.5)
    image thanks = Text("{size=80}{color=#FF0000}Thanks for Playing!{/color}", text_align=0.5)
    image loveyall = Text("{size=80}{color=#FF0000}love y'all <3 - 3pm{/color}", text_align=0.5)
    stop music
    play music "audio/Mondaymorningcreditscene2.mp3" volume 0.4

    $ credits_speed = 80  # Scrolling speed in seconds (increased to make it slower)

    # Scene setup
    scene black  # Replace this with a fancier background if desired

    # Credits scrolling text
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=True, bounce=False, xanchor="center", yanchor="bottom")

    # Display "The End"
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(5)
    hide theend
    with dissolve

    # Pause for the credits scroll
    with Pause(credits_speed - 5)

    # Display splash screen
    show splash
    with dissolve
    with Pause(3)
    hide splash
    with dissolve

    # Display "Thanks for Playing!"
    with Pause(1)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(4)
    hide thanks
    with dissolve

    # Display "love y'all <3 - 3pm"
    with Pause(1)
    show loveyall:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(4)
    hide loveyall
    with dissolve

    return