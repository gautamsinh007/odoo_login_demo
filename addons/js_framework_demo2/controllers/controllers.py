# -*- coding: utf-8 -*-
# from odoo import http


# class JsFrameworkDemo2(http.Controller):
#     @http.route('/js_framework_demo2/js_framework_demo2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/js_framework_demo2/js_framework_demo2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('js_framework_demo2.listing', {
#             'root': '/js_framework_demo2/js_framework_demo2',
#             'objects': http.request.env['js_framework_demo2.js_framework_demo2'].search([]),
#         })

#     @http.route('/js_framework_demo2/js_framework_demo2/objects/<model("js_framework_demo2.js_framework_demo2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('js_framework_demo2.object', {
#             'object': obj
#         })
