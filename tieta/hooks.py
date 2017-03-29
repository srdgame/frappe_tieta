# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "tieta"
app_title = "TieTa"
app_publisher = "Dirk Chang"
app_description = "TieTa"
app_icon = "octicon octicon-flame"
app_color = "#11AAEE"
app_email = "dirk.chang@symid.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tieta/css/tieta.css"
# app_include_js = "/assets/tieta/js/tieta.js"

# include js, css files in header of web template
# web_include_css = "/assets/tieta/css/tieta.css"
# web_include_js = "/assets/tieta/js/tieta.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "tieta.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "tieta.install.before_install"
# after_install = "tieta.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tieta.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"tieta.tasks.all"
# 	],
# 	"daily": [
# 		"tieta.tasks.daily"
# 	],
# 	"hourly": [
# 		"tieta.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tieta.tasks.weekly"
# 	]
# 	"monthly": [
# 		"tieta.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "tieta.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tieta.event.get_events"
# }

standard_queries = {
	"Stock Item Attribute": "tieta.stock.doctype.stock_item_attribute.stock_item_attribute.stock_item_attribute_query",
	"Stock Batch No": "tieta.stock.doctype.stock_batch_no.stock_batch_no.stock_batch_no_query",
	"Stock Serial No": "tieta.stock.doctype.stock_serial_no.stock_serial_no.stock_serial_no_query",
}