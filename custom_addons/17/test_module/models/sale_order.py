from odoo import api, fields, models

class SaleOrder(models.Model):
    # _name ="sale.order"
    _inherit = "sale.order"
    _description = "This is test_module profile."


    confirmed_user_id = fields.Many2one('res.users', string='Confirmed User')
    # # patient_name = fields.Char("Name")
    # # name1 = fields.Char("RollNo.")
    # partner_id = fields.Char("Subjects")
    # name3 = fields.Char("Marks")
    # name4 = fields.Char("Address")
    # name5 = fields.Char("Division")
    # value = fields.Integer("RollNo.")
