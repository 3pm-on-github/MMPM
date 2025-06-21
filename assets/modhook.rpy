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
        textbutton "Money Reset (resets money to 2 money)" action MoneyReset ypos 210 xpos 25

# other stuff

label mmpp1:
    $ config.allow_skipping = True
    "MMPM" "MMPM Injected. Thank you."
    stop music
    jump thesrar