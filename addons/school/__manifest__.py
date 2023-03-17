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
          "views/school_form.xml",
          'views/web_school.xml',
          'views/web_public_page.xml',
          'views/shop_custom_url.xml',
          "views/web_inherit_teacher_class.xml",
          # 'views/user_add_fields.xml',
          # 'views/user_create.xml'
          
         
         ],
    'installable' : True,
    'application' : True,
    'auto_install' : False ,
    'license':'LGPL-3'
}
