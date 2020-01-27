{
    'name': 'Marie Formation',
    'version': '1.0',
    'category': 'theme',
    'sequence': 2,
    'summary': 'Marie Formation',
    'description': """
Marie Formation
""",
    'author': 'Odoo SA',
    'images': [
        'static/description/website_theme_screenshot.jpg',
    ],
    'depends': [
        'website_sale',
    ],
    'data': [

    'data/website_menu.xml',

    #data

    #website assets
    'views/assets.xml',

    #layout

    #pages

    'views/pages/page_with_controller.xml',
    'views/pages/some_qweb_logics.xml',
    'views/pages/without_odoo_context.xml',
    'views/pages/with_odoo_context.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
