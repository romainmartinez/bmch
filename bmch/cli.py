# -*- coding: utf-8 -*-

"""Command line interface for bmch."""

import cursesmenu as cm

# categories
main_cat = ('preprocessing', 'processing', 'statistics', 'plot')
sub_cat = {
    'preprocessing': ('')
}
# main menu
menu = cm.CursesMenu(title='main title', subtitle='subtitle')
