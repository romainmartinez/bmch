# -*- coding: utf-8 -*-

"""Command line interface for bmch."""

import cursesmenu as cm


class Menu:
    """the menu class."""

    def __init__(self):
        self.main_cat = ['preprocessing', 'processing', 'statistics', 'plot']
        self.sub_cat = {
            'preprocessing': [
                'create new project', 'import project', 'import files', 'model construction', 'kinematic reconstruction'
            ]
        }

    def mainmenu(self):
        """Getting a selection out of a list of strings."""
        selection = cm.SelectionMenu.get_selection(self.main_cat)
        return selection


if __name__ == '__main__':
    menu = Menu()
    selection = menu.mainmenu()
