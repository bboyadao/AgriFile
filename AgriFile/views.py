from django.contrib.auth.views import LoginView


class Login(LoginView):
	template_name = "user/login.html"


class Zone(object):
	def __init__(self, name, child):
		self.name = name
		self.child = child


class Menu(object):
	def __init__(self, name, child, open=None):
		self.name = name
		self.open = open
		self.child = child


class Nav(object):
	def __init__(self, name, icon, link):
		self.name = name
		self.icon = icon
		self.link = link


data = [
	{
		"name": "ADMIN ZONE",
		"menu": [
			{
				"name": "Quản lý người dùng",
				"icon": "",
				"navs": [

					{"name": "Danh sách", "icon": "nav-icon fas fa-circle", "link": 'user_list'},
					{"name": "Tạo mới", "icon": "nav-icon fas fa-circle", "link": "user_create"},

				]
			},
			{
				"name": "Cài đặt",
				"icon": "",
				"navs": [
					{"name": "Phòng ban", "icon": "", "link": "user_list"},
					{"name": "Địa chỉ đến", "icon": "", "link": "user_list"},
					{"name": "Lịch báo cáo", "icon": "", "link": "user_list"},
				],
			}
		]
	},
	{
		"name": "WORK ZONE",
		"menu": [
			{
				"name": "gggggggg",
				"icon": "",
				"navs": [
					{"name": "bbb", "icon": "", "link": "user_list"}
				]
			},
		]
	},

]


def global_templates_context_processors(request):
	current_view = request.resolver_match.url_name
	zones = []
	for zone in data:
		menus = []
		for menu in zone["menu"]:
			open_menu = False
			navs = []
			for nav in menu["navs"]:
				###################
				if current_view == nav["link"]:
					open_menu = True
				###################
				n = Nav(name=nav["name"], icon=nav["icon"], link=nav["link"])
				navs.append(n)
			m = Menu(menu["name"], child=navs, open=open_menu)
			menus.append(m)

		z = Zone(name=zone["name"], child=menus)
		zones.append(z)

	return {"ZONES": zones, "current_view": current_view}
