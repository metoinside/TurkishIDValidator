# -*- coding: utf-8 -*-
{
    'name': "TurkishIDValidator",

    'summary': """
        Turkish ID(TCKN) verification and validation module""",

    'description': """
        A generic Turkish ID(TCKN) is consist of 11 digits, and it's unique to
        corresponding person. By this module, you can have a chance to verify
        and validate given number by various methods including offline
        verification and online validation through a service provided by the
        Directorate General of Civil Registration and Citizenship Affairs in
        Turkey
    """,

    'author': "Metin AKIN",
    'website': "http://www.metoinside.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
}
