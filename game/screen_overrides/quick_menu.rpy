################################################################################
## Initialization
################################################################################

init offset = 1

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():
    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            ypos 1007

            imagebutton auto "gui/quick_menu/back_%s.png" action Rollback()
            imagebutton auto "gui/quick_menu/history_%s.png" action ShowMenu('history')
            imagebutton auto "gui/quick_menu/skip_%s.png" action Skip() alternate Skip(fast=True, confirm=True)
            imagebutton auto "gui/quick_menu/auto_%s.png" action Preference("auto-forward", "toggle")
            imagebutton auto "gui/quick_menu/save_%s.png" action ShowMenu('save')
            imagebutton auto "gui/quick_menu/quicksave_%s.png" action QuickSave()
            imagebutton auto "gui/quick_menu/quickload_%s.png" action QuickLoad()
            imagebutton auto "gui/quick_menu/settings_%s.png" action ShowMenu('preferences')

style quick_image_button:
    xpadding 5