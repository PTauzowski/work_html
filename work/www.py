# -*- coding: utf-8 -*-
class Page(object):
	def __init__(self,name):
		self.name = name + '.html'
		self.file = None
		self.createFile()
		self.content = None

	def templete(self,name):
		f = open(name+'.html')
		content = f.readlines()
		f.close()
		self.content = "".join(content)

	def createFile(self):
		path = self.name
		self.file = open(path,'w')

	def addCt(self,name):
		self.openFile(name)
		for line in self.content:
			self.file.write(line)

	def create(self,a,b,c):
		self.addCt(a)
		self.addCt(b);
		self.addCt(c);

	def replace(self,name,file):
		f = open('./data/'+file+'.html')
		temp = f.readlines()
		f.close()
		temp = "".join(temp)	
		self.content = self.content.replace(name,temp)

	def rtxt(self,name,file):
		self.content = self.content.replace(name,file)



	def close(self):
		self.replace('#footer','footer')
		txt = self.content.split('\n')
		for line in txt:
			self.file.write(line+'\n')
		self.file.close()

names =[]


p=Page('index');        
p.templete('main')
p.replace('#mainmenu','main_menu')
p.replace('#image','slider_index')
p.rtxt('<li><a href="index.html">Home</a></li>','<li><a class="menuclick" "href="index.html">Home</a></li>')
p.close()

################################################introduction
p=Page('objectives');        
p.templete('page')
p.replace('#mainmenu','main_menu')
p.replace('#menu','introduction_menu')
p.replace('#image','static_1')
p.replace('#content','objectives_content')
p.rtxt('<a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Introduction<b class="caret"></b></a>',
	'<a class="menuclick" href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Introduction<b class="caret"></b></a>')
p.close()

p=Page('conferencetopics');        
p.templete('page')
p.replace('#mainmenu','main_menu')
#p.replace('#image','slider_topics')
p.replace('#image','static_1')
p.replace('#menu','introduction_menu')
p.replace('#content','conferencetopics_content')
p.rtxt('<a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Introduction<b class="caret"></b></a>',
	'<a class="menuclick" href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Introduction<b class="caret"></b></a>')
p.close()

p=Page('previousconferences');        
p.templete('page')
p.replace('#mainmenu','main_menu')
p.replace('#image','static_1')
p.replace('#menu','introduction_menu')
p.replace('#content','previousconferences_content')
p.rtxt('<a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Introduction<b class="caret"></b></a>',
	'<a class="menuclick" href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Introduction<b class="caret"></b></a>')
p.close()




################################################committees
p=Page('internationaladvisoryboard');        
p.templete('page')
p.replace('#mainmenu','main_menu')
p.replace('#image','static_2')
p.replace('#menu','committees_menu')
p.replace('#content','internationaladvisoryboard_content')
p.rtxt('<a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Committees<b class="caret"></b></a>',
	'<a class="menuclick" href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Committees<b class="caret"></b></a>')
p.close()

p=Page('scientificcommittee');        
p.templete('page')
p.replace('#mainmenu','main_menu')
p.replace('#image','static_2')
p.replace('#menu','committees_menu')
p.replace('#content','scientificcommittee_content')
p.rtxt('<a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Committees<b class="caret"></b></a>',
	'<a class="menuclick" href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Committees<b class="caret"></b></a>')
p.close()

p=Page('organizingcommittee');        
p.templete('page')
p.replace('#mainmenu','main_menu')
p.replace('#image','static_2')
p.replace('#menu','committees_menu')
p.replace('#content','organizingcommittee_content')
p.rtxt('<a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Committees<b class="caret"></b></a>',
	'<a class="menuclick" href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Committees<b class="caret"></b></a>')
p.close()





################################################For Authors
p=Page('abstractsandpapers');        
p.templete('page')
p.replace('#mainmenu','main_menu')
p.replace('#image','static_3')
p.replace('#menu','forauthors_menu')
p.replace('#content','abstractsandpapers_content')
p.rtxt('<a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">For Authors<b class="caret"></b></a>',
	'<a class="menuclick" href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">For Authors<b class="caret"></b></a>')
p.close()

p=Page('registration');        
p.templete('page')
p.replace('#mainmenu','main_menu')
p.replace('#image','static_3')
p.replace('#menu','forauthors_menu')
p.replace('#content','registration_content')
p.rtxt('<a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">For Authors<b class="caret"></b></a>',
	'<a class="menuclick" href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">For Authors<b class="caret"></b></a>')
p.close()






################################################Programme
p=Page('invitedlectures');        
p.templete('page')
p.replace('#mainmenu','main_menu')
p.replace('#image','static_4')
p.replace('#menu','programme_menu')
p.replace('#content','invitedlectures_content')
p.rtxt('<a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Programme<b class="caret"></b></a>',
	'<a class="menuclick" href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Programme<b class="caret"></b></a>')
p.close()

p=Page('conferenceprogramme');        
p.templete('page')
p.replace('#mainmenu','main_menu')
p.replace('#image','static_4')
p.replace('#menu','programme_menu')
p.replace('#content','conferenceprogramme_content')
p.rtxt('<a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Programme<b class="caret"></b></a>',
	'<a class="menuclick" href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Programme<b class="caret"></b></a>')
p.close()

p=Page('thematicsessions');        
p.templete('page')
p.replace('#mainmenu','main_menu')
p.replace('#image','static_4')
p.replace('#menu','programme_menu')
p.replace('#content','thematicsessions_content')
p.rtxt('<a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Programme<b class="caret"></b></a>',
	'<a class="menuclick" href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Programme<b class="caret"></b></a>')
p.close()



################################################conference venu
p=Page('thevenue');        
p.templete('page')
p.replace('#mainmenu','main_menu')
p.replace('#image','static_5')
p.replace('#menu','conferencevenue_menu')
p.replace('#content','thevenue_content')
p.rtxt('<a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Conference venue<b class="caret"></b></a>',
	'<a class="menuclick" href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Conference venue<b class="caret"></b></a>')
p.close()

p=Page('warsawcity');        
p.templete('page')
p.replace('#mainmenu','main_menu')
p.replace('#image','static_5')
p.replace('#menu','conferencevenue_menu')
p.replace('#content','warsawcity_content')
p.rtxt('<a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Conference venue<b class="caret"></b></a>',
	'<a class="menuclick" href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Conference venue<b class="caret"></b></a>')
p.close()

p=Page('accommodation');        
p.templete('page')
p.replace('#mainmenu','main_menu')
p.replace('#image','static_5')
p.replace('#menu','conferencevenue_menu')
p.replace('#content','accommodation_content')
p.rtxt('<a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Conference venue<b class="caret"></b></a>',
	'<a class="menuclick" href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Conference venue<b class="caret"></b></a>')
p.close()


################################################Important information
p=Page('importantdates');        
p.templete('page')
p.replace('#mainmenu','main_menu')
p.replace('#image','static_6')
p.replace('#menu','importantinformation_menu')
p.replace('#content','importantdates_content')
p.rtxt('<a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Important information<b class="caret"></b></a>',
	'<a class="menuclick" href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Important information<b class="caret"></b></a>')
p.close()

p=Page('payments');        
p.templete('page')
p.replace('#mainmenu','main_menu')
p.replace('#image','static_6')
p.replace('#menu','importantinformation_menu')
p.replace('#content','payments_content')
p.rtxt('<a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Important information<b class="caret"></b></a>',
	'<a class="menuclick" href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Important information<b class="caret"></b></a>')
p.close()

p=Page('conferencefee');        
p.templete('page')
p.replace('#mainmenu','main_menu')
p.replace('#image','static_6')
p.replace('#menu','importantinformation_menu')
p.replace('#content','conferencefee_content')
p.rtxt('<a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Important information<b class="caret"></b></a>',
	'<a class="menuclick" href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Important information<b class="caret"></b></a>')
p.close()


################################################Contact
p=Page('scientificaspects');        
p.templete('page')
p.replace('#mainmenu','main_menu')
p.replace('#image','static_7')
p.replace('#menu','contact_menu')
p.replace('#content','scientificaspects_content')
p.rtxt('<a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Contact<b class="caret"></b></a>',
	'<a class="menuclick" href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Contact<b class="caret"></b></a>')
p.close()

p=Page('paymentandtravel');        
p.templete('page')
p.replace('#mainmenu','main_menu')
p.replace('#image','static_7')
p.replace('#menu','contact_menu')
p.replace('#content','paymentandtravel_content')
p.rtxt('<a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Contact<b class="caret"></b></a>',
	'<a class="menuclick" href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Contact<b class="caret"></b></a>')
p.close()