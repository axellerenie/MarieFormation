from odoo import models

class ThemeMarieFormation(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_marie_formation_post_copy(self, mod):
            self.disable_view('website_theme_install.customize_modal')
