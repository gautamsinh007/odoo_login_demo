from odoo import http
from odoo.http import request
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
import base64


class Teacherdata(http.Controller):
   
    @http.route('/teacher_webform', type='http' , auth="public" , website='True')
    def school_form(self,**kw):
        print("-=-=-===-=-===--=-=-===-=-==-=- from main class Teacherdata")
        return  http.request.render('school.create_teacher')
    
    
    @http.route('/teacher', type='http' , auth="user" , website='True')  
    def teacher(self, **kw):
        # print("data has been cretaed.....", kw)
        
        file = request.httprequest.files.get("file").read()
        
        file = base64.b64encode(file)
        
        print(file)
        name  = kw['name']
        email = kw['email']
        gender = kw['gender']
        phone = kw['phone']
        
        
        abc = request.env['school.profile'].create({'name':name, 'email':email ,
                                                    'gender':gender, 'phone':phone})
        print(abc,"======================================")
        return "data cretaed"
    
    
    @http.route('/demo', type='http' , auth="public" , website='True')
    def public_page(self,**kw):

        return  http.request.render('school.public_page')
    
    
    @http.route('/lols', type='http' , auth="public" , website='True')
    def public_page(self,**kw):

        return  http.request.render('school.detail')
    

    @http.route('/project/uploaded', type='http', auth="public", website=True)
    def upload_files(self, **post):
        values = {}
        if post.get('attachment',False):
            Attachments = request.env['ir.attachment']
            name = post.get('attachment').filename      
            file = post.get('attachment')
            project_id = post.get('project_id')
            attachment = file.read() 
            attachment_id = Attachments.sudo().create({
                'name':name,
                'datas_fname': name,
                'res_name': name,
                'type': 'binary',   
                'res_model': 'attachment.files',
                'res_id': project_id,
                'datas': attachment.encode('base64'),
            })
            value = {
                'attachment' : attachment_id
            }
            print(value)
            return request.render("modulename.template_to_render", value)
        
            # return "data created"
    
#=======----------=--=\--\--=-\--- Inherit controller and url  =-\-=\---------======================================= 

  
  
class  Inherit_teacher_class(Teacherdata):

    # Inherit exsisting url  
    
    @http.route('/shop', type='http' , auth="public" , website='True')
    def shop_data(self,**kw):
        # res = super(Inherit_teacher_class, self).shop_data(page=0,**kw)    # if need then use super both functionality work existing and new 
        print("this is  new url for shop --------------")
        # return res
        return http.request.render('school.shops')
    
    
    
    # inherit controller 
      
    @http.route('/teacher_webform', type='http' , auth="public" , website='True')
    def school_form(self,**kw):
        res = super(Inherit_teacher_class, self).school_form(page=0,**kw)    # if need then use super both functionality work existing and new 
        print("=======----------=--=\--\--=-\---=-\-=\-------- from Inherit_teacher_class")
        print('-==-----=-=-=-=', res.qcontext, '=================================================' )
        return res
    

    @http.route('/schooldata', type='http' , auth="public" , website='True')
    def school_data(self,**kw):
        print('fjdskfjjsdflsjd')
        op = request.env['school.profile'].search([])
        print(op)
        
        return http.request.render("school.sdata", {'op':op})
    
    
    
class  signupcustom(AuthSignupHome):
    
    
    @http.route('/web/signup', type='http', auth='public', website=True, sitemap=False)
    def testdata(self, *args, **kw):
      return http.request.render('school.abcd')
        
    
    
    @http.route('/test', type='http', auth='public', website=True, sitemap=False)
    def web_auth_signup(self, *args, **kw):
        print()
        print("this sc lalla =====0=0")
        print()
        role =  kw['role']
        login = kw['login']
        password = kw['password']
        name  = kw['name']
        request.env['res.users'].create({'role':role, 'login':login , 'password':password,'name':name})
        
        print('=\\\=====================================')
        p = request.session['names'] = 'abc'
        
        print( p, "this is from inhertoimg ...... sign up form")
        # response = super(signupcustom, self).web_auth_signup(*args, **kw)
        
        return 'data is created'
 
 
 
 

 
 
 
        
    
    # @http.route('/web/signup', type='http', auth='public', website=True, sitemap=False)
    # def web_auth_signup(self , *args,**kw):
    #     res = super(signupcustom , self).web_auth_signup(*args, **kw)
    #     op = request.session['names']  = lambda self: self.env.user
    #     print(op,'oopopoppopopopopopop90909009909090----==-=-=∂')
    #     return  res
                    

    
    # @http.route('/test', type='http', auth='public', website=True, sitemap=False)
    # def web_auth_signup(self, *args, **kw):
        
    #     abc = request.env['res.users'].create(kw)
    #     print(abc.role, '-=-=-=-=-=-==-==-888888888888888888888888888')
    #     res = super(signupcustom , self).web_auth_signup(*args, **kw)
    #     print(abc, 'this is add field in sign up form n -=-===-==-=-=-=--=-=-=-==--=-==--=--=-=-=-=-==-=----====-=') 
    #     # response = super(signupcustom, self).web_auth_custom(**kw)
    #     print( 'call from inherit users  ontrolers -=-==-=-=--=-=-=-=--= -=- -=-   users   ===--=-=-==--=---')
    #     res =  request.render('auth_signup.signup')
    #     return  res
    
    
    # custom make signup
    
    
    
    