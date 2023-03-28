from odoo import http
from odoo.http import request
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
import base64
import xmlrpc.client

from odoo.addons.auth_oauth.controllers.main import OAuthLogin


class Teacherdata(http.Controller):
   
    @http.route('/teacher_webform', type='http' , auth="public" , website='True')
    def school_form(self,**kw):
        
          
        # pr = request.env['res.users'].search([])
       
        # print(pr,'==-=-=-==-==-=-==-=-=--==-=-==')
        # for i in pr:
        #     print(i.login)
        pr = request.session.uid
        print(type(pr))
        data = request.env['res.users'].browse(pr)
        print(type(data))
        for i in data:
            t = request.session['op'] = i.role
            print(t)    
            
            if "Hr" == t:
                return  http.request.render('school.create_teacher')
          
            return "this  page is not aacessble you"    
     
        
        
    
    
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
    
    @http.route('/shop', type='http' , auth="user" , website='True')
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
    
    
    @http.route('/loginform', type='http', auth='public', website=True, sitemap=False)
    def loginform(self, *args, **kw):
        
        return http.request.render('school.login')
        
    
    
    @http.route('/logins', type='http', auth='public', website=True, sitemap=False)
    def logincheck(self, *args, **kw):
      url = 'http://0.0.0.0:8069'
      db = 'backup_odoo_15_login' 
      login =  kw['login']  
      password = kw['password']  
      
      print(login,'lolollllll-=-=-==--=-=-=--=-=-=--=')
      
      common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
      print(common, 'comman in odoo -=----=------=-=-=')
      uid = common.authenticate(db,login, password, {})
      
      if uid:
          print("thsi  authentication succesfully")
          return http.request.render('school.shops')
        #   return uid, url, db, common, password

          
      else:
          print("auth failed")
              
    #   o = super(OAuthLogin, self).web_login(*args, **kw)  
      return  "dsflsdklk"
    
    
    
    
    
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
        
      
        pr = request.env['res.users'].search([])
       
        print(pr,'==-=-=-==-==-=-==-=-=--==-=-==')
        # for i in pr:
        #         o  = i.login
        #         print(o,'in the funxction=\=\==\==\=\==\=\\=s')
        #         return "enter other username"
           
        request.env['res.users'].sudo().create({'role':role, 'login':login , 'password':password,'name':name})
        
        print('=\\\=====================================')
        
        p = request.session['names'] = role
        
        print( p, "this is from inhertoimg ...... sign up form")
        
    
        # response = super(signupcustom, self).web_auth_signup(*args, **kw)
        
        return 'data is created'
    

 
 
    # @http.route('/web/login', type='http', auth='public', website=True, sitemap=False)
    # def web_login(self, *args, **kw):
    #         print()
    #         print()
    #         print()
                                 
            # print(request.params['login'], request.params['password']) 
           
            # request.session['names'] =  'saas'
            # print(kw, 'kw===============================')
            # pr = request.session.uid
            
            # print(pr,'prprprprprpprprprooppopo-=-=====-=-=---')
            # data = request.env['res.users'].browse(pr)
            # print(data, '===---=-====-==-=-=--=--=-0=0-=0=0=-0=0=0=0=00 ')
            # for i in data:
            #     o = i.role
            # p =  request.session['roles'] = kw
            # print(p, "this is -=-=-==-==-=-=-=-=--=-===--=-=----==-")
            # data = super(signupcustom, self).web_login(*args, **kw)
                
            # return data
            
    @http.route('/web/login', type='http', auth='public', website=True, sitemap=False)
    def web_login(self, *args, **kw):
        print(kw , "this is from inherit web logins")
        print(kw, '-------------------')
        data = super(signupcustom, self).web_login(*args, **kw)
        # a = request.env['res.users'].search([])
        # for i in a:
        #     print(i.role)
        # print(a)
        # print("-=-=-=")
        # if request.session.uid:
        #     pr = request.session.uid
            
        #     dataa = request.env['res.users'].browse(pr)
        #     for i in dataa:
        #         print(i)
           
        #     print(dataa)
        
        print(data , '----------------------------------')
        return data


        

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
    
    
    
    