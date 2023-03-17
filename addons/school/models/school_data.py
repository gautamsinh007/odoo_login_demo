from odoo import fields , models , api,_
# import  datetime 
from odoo import exceptions
from datetime import date, datetime



class Schoolmodel(models.Model):
    _name = "school.profile"
    _description = "this is scholl management model"

                                                                                                                                    
    name  = fields.Char(string='schoolname',required="1",track_visibility='always')
    email = fields.Char(string="email")
    gender = fields.Selection([('male','Male'),('female','Female')],string='gender')
    phone = fields.Char(string='phone', readonly=True, defult="1334569874")



# class Newuser(models.Model):
    
#     _inherit = "res.users"
#     role = fields.Char(string="role")
    
    
#     @api.model
#     def create(self, values):
#         if not values.get('login', False):
#             action = self.env.ref('base.action_res_users')
#             msg = _("You cannot create a new user from here.\n To create new user please go to configuration panel.")
#             raise exceptions.RedirectWarning(msg, action.id, _('Go to the configuration panel'))

#         return super(Newuser, self).create(values)