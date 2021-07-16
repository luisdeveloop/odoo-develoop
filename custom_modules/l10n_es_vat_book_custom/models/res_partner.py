# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from odoo import api, fields, models, _
from odoo.tools import ormcache

_logger = logging.getLogger(__name__)

class l10n_es_aeat_res_partner_custom(models.AbstractModel):

    _inherit = 'res.partner'

    @ormcache("self.vat, self.country_id")
    def _parse_aeat_vat_info(self):
        """ Return tuple with split info (country_code, identifier_type and
            vat_number) from vat and country partner
        """
        if self:
            self.ensure_one()
            vat_number = self.vat or ""
            prefix = self._map_aeat_country_code(vat_number[:2].upper())
            if prefix in self._get_aeat_europe_codes():
                country_code = prefix
                vat_number = vat_number[2:]
                identifier_type = "02"
            else:
                country_code = self._map_aeat_country_code(self.country_id.code) or ""
                if country_code in self._get_aeat_europe_codes():
                    identifier_type = "02"
                else:
                    identifier_type = "04"
            if country_code == "ES":
                identifier_type = ""
            return country_code, identifier_type, vat_number
        else:
            return False, False, False