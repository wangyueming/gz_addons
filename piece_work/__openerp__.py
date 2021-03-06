# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': '计件计量',
    'version': '0.1',
    'category': 'Wages',
    'description': """
计件计量。
=======================================================================================
计件计量。
""",
    'author': 'Wang Yue Ming',
    'website': 'http://openerp.com',
    'depends': ['piece_rate', 'hr_factory'],
    'data': [
        #'security/sale_security.xml',
        #'security/ir.model.access.csv',
        'wizard/piece_work_line_view.xml',
        'piece_work_line_workflow.xml',
        'piece_work_view.xml',
        'res_config_view.xml',
    ],
    'demo': [],
    'test':[],
    'installable': True,
    'images': [],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
