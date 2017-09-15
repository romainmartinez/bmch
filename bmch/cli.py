# -*- coding: utf-8 -*-

"""Command line interface for bmch."""

import menu


# def coucou():
#     print('coucou')
#
# header = '-' * 21
#
# main = menu.Menu(title=header, message='root')
# main.set_options([("new option name", coucou),
#                   ('exit', menu.Menu.CLOSE)])
#
# main.open()
#
#
# main.close()

main = menu.Menu(title="Main Menu")
sub = menu.Menu(title="Submenu")
main.set_options([("Open submenu", sub.open),
                  ("Close main menu", main.close)])
sub.set_options([("Return to main menu", sub.close)])
main.open()
