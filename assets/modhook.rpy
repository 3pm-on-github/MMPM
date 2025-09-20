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
            text "Modded with MMPM 0.0.2@ALPHA1.2.1" style "main_menu_version"

screen about():

    tag menu

    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")
            text _("MMPM Version 0.0.2@ALPHA1.2.1\n")

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
    def AllowSkipping():
        config.allow_skipping = True
    def UnlockChapter2():
        persistent.chapter1_completed = True
    def LockChapter2():
        persistent.chapter1_completed = False

screen mmpmtoolbox():
    tag menu
    add "mmpmimages/car.png"

    textbutton "Back" action Return()

    textbutton "Cheats" action ShowMenu("mmpmcheats") ypos 60 xpos 25
    textbutton "Allow Skipping" action AllowSkipping ypos 90 xpos 25
    textbutton "Modshop" action Jump("open_modshop") ypos 120 xpos 25

screen mmpmcheats():
    tag menu
    add "mmpmimages/car.png"

    textbutton "Back" action Return()

    textbutton "Money Boost (gives +1000000 money)" action MoneyBoost ypos 60 xpos 25
    textbutton "Max Money (sets money to a very high amount)" action MaxMoney ypos 120 xpos 25
    textbutton "Money Reset (resets money to 2 money)" action MoneyReset ypos 210 xpos 25
    textbutton "Unlock Chapter 2" action UnlockChapter2 ypos 270 xpos 25
    textbutton "Lock Chapter 2" action LockChapter2 ypos 300 xpos 25

init python:
    renpy.music.register_channel("mmpmmodshopmusic", mixer="music", loop=False)
    import renpy.exports as renpy_exports
    modshop_music_list = [
        "audio/mmpmaudio/renzofrog - wheww.mp3",
        "audio/mmpmaudio/Yoshi's Woolly World - World 1.mp3",
        "audio/mmpmaudio/WiiU (Old) EShop Theme.mp3",
        "audio/mmpmaudio/Super Mario Maker - SMW (Edit) Ground Theme.mp3",
    ]
    current_modshop_song = ""

    def removesuffix(text, suffix):
        if text.endswith(suffix):
            return text[:-len(suffix)]
        return text

    def removeprefix(text, prefix):
        if text.startswith(prefix):
            return text[len(prefix):]
        return text

    def send_mod_request(modid):
        url = f"https://threepm.xyz/mmpm/mod_script?id={modid}"
        renpy_exports.fetch(url)
        renpy.exports.notify(f"Sent request for mod ID: {modid}")

    def play_modshop_music():
        global current_modshop_song
        renpy.music.stop(channel="sound", fadeout=0)

        for i, song in enumerate(modshop_music_list):            
            renpy.music.queue(song, channel="mmpmmodshopmusic", loop=(i == len(modshop_music_list) - 1), fadein=(1.0 if i == 0 else 0.0))

        if modshop_music_list:
            current_modshop_song = modshop_music_list[0]

    def stop_modshop_music():
        renpy.music.stop(channel="mmpmmodshopmusic", fadeout=1.0)

    def set_current_song(song_path):
        global current_modshop_song
        current_modshop_song = song_path

    def pause_main_music():
        renpy.music.set_pause(True, channel="music")

    def resume_main_music():
        renpy.music.set_pause(False, channel="music")


label open_modshop:
    $ pause_main_music()
    $ play_modshop_music()
    python:
        modshoplist = None
        status_code = None

        try:
            result = renpy.fetch("https://threepm.xyz/mmpm/modshoplist", result="json")
            result.join()

            try:
                status_code = result.code
            except:
                if result.headers:
                    for header in result.headers.splitlines():
                        if header.startswith("HTTP/"):
                            parts = header.split(" ")
                            if len(parts) >= 2:
                                status_code = int(parts[1])
                            break

            modshoplist = result.data
        except Exception as e:
            status_code = 530
    call screen mmpmmodshop
    return

label returnsir:
    $ stop_modshop_music()
    $ resume_main_music()
    call screen mmpmtoolbox
    return

screen mmpmmodshop():
    tag menu
    add "mmpmimages/mmpmmodshopbackground.jpeg"
    
    textbutton "Back" action Jump("returnsir")

    if modshoplist:
        vbox:
            spacing 10
            xpos 25
            ypos 60

            for mod in modshoplist:
                textbutton mod.get("modname", "Unknown Mod") action Function(send_mod_request, mod.get("modid", ""))
    elif status_code == 530:
        text "Error: The modshop is in maintenance or there was a problem fetching the modshop list." ypos 60 xpos 25
    else:
        text "Fetching Modshop List..." ypos 60 xpos 25

    # python:
    #     while True:
    #         songname = removesuffix(removeprefix(current_modshop_song, 'audio/mmpmaudio/'), '.mp3')
    #         renpy.pause(1.0)

    # text "🎵  [songname]" xpos 120
        
# other stuff

label mmpp1:
    "MMPM" "MMPM Injected. Thank you."
    stop music
    jump thesrar