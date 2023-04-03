{
    
     'name' : 'School',
     'summary':"School Management System",
     'sequence': 1,
     'description' : 'This is school management sysytem software suport in odoo v31',
     'depends' : ["base"],
     'author' : "Gautamsinh Makwana",
     #'image' : [ ]    add image path hear in thsi use images
      'data' : [
         "security/ir.model.access.csv",
          'security/security.xml',
          "views/school_form.xml",
          'views/web_school.xml',
          'views/web_public_page.xml',
          'views/shop_custom_url.xml',
          "views/web_inherit_teacher_class.xml",
          'views/web_scholl_data.xml',
          'views/attachment_file.xml',
          'views/web_file.xml',
          'views/user_add_fields.xml',
          'views/user_create.xml',
          'views/web_login_file.xml',
          'views/login_check_up.xml',
          'views/attachments.xml',
          'views/file_view.xml'
          
         ],
      
    'installable' : True,
    'application' : True,
    'auto_install' : False ,
    'license':'LGPL-3'
}
