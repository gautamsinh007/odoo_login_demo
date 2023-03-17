from odoo import http
from odoo.http import request
from odoo.addons.auth_signup.controllers.main import AuthSignupHome



class Teacherdata(http.Controller):
   
    @http.route('/teacher_webform', type='http' , auth="public" , website='True')
    def school_form(self,**kw):
        print("-=-=-===-=-===--=-=-===-=-==-=- from main class Teacherdata")
        return  http.request.render('school.create_teacher')
    
    
    @http.route('/teacher', type='http' , auth="user" , website='True')  
    def teacher(self, **kw):
        print("data has been cretaed.....", kw)
        abc = request.env['school.profile'].create(kw)
        print(abc,"======================================")
        return "data cretaed"
    
    
    @http.route('/demo', type='http' , auth="public" , website='True')
    def public_page(self,**kw):

        return  http.request.render('school.public_page')
    
    
    
    
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
    


# class  signupcustom(AuthSignupHome):
    
#     @http.route('/web/signup', type='http', auth='public', website=True, sitemap=False)
#     def testsignup(self , **kw):
#         return  http.request.render('school.abcd')
                    

    
#     @http.route('/test', type='http', auth='public', website=True, sitemap=False)
#     def web_auth_signup(self, *args, **kw):
        
#         abc = request.env['res.users'].create(kw)
#         print(abc.role, '-=-=-=-=-=-==-==-888888888888888888888888888')
#         res = super(signupcustom , self).web_auth_signup(*args, **kw)
        # print(abc, 'this is add field in sign up form n -=-===-==-=-=-=--=-=-=-==--=-==--=--=-=-=-=-==-=----====-=') 
        # response = super(signupcustom, self).web_auth_custom(**kw)
        # print( 'call from inherit users  ontrolers -=-==-=-=--=-=-=-=--= -=- -=-   users   ===--=-=-==--=---')
        # res =  request.render('auth_signup.signup')
        # return  "sdksjdksj"
    
    
    # custom make signup
    
    
    
    