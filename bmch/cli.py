# -*- coding: utf-8 -*-

"""Command line interface for bmch."""

import menu

import bmch


def show_menu():
    """Display command line interface (without arguments and outputs)."""

    # create main menu
    main = menu.Menu(title="Main Menu")

    # create submenu

    # 1) preprocessing submenu
    preproc = menu.Menu(title="preprocessing")
    preproc.set_options([('create project', bmch.preprocessing.create_project),
                         ('import project', bmch.preprocessing.import_project),
                         ('import files', bmch.preprocessing.import_files),
                         ('return', preproc.close)])

    # 2) processing submenu
    proc = menu.Menu(title='processing')
    proc.set_options([('return', proc.close)])

    # 3) statistics submenu
    stats = menu.Menu(title='statistics')
    stats.set_options([('return', stats.close)])

    # 4) plot submenu
    plt = menu.Menu(title='plot')
    plt.set_options([('return', plt.close)])

    # add submenus
    main.set_options([('preprocessing', preproc.open),
                      ('processing', proc.open),
                      ('statistics', stats.open),
                      ('plot', plt.open),
                      ('exit', main.close)])

    main.open()


if __name__ == '__main__':
    show_menu()
