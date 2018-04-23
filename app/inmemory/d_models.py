from datetime import datetime


class Members():
	def __init__(self,username,age,id=0):
		self.name = username
		self.age = age
		self.id = id
		self.posts = []
	def __str__(self):
		return ("Name:{}, Age: {}".format(self.name,self.age))
	
	def __dict__(self):
		return{
			"id":self.id,
			"name":self.name,
			"age":self.age,
			"post":self.posts
		  }


class Post():
	def __init__(self,title,content,member_id=0,idd=0):
		self.title = title 
		self.content = content
		self.id = idd
		self.datetime = datetime.now()
		self.member_id= member_id
	def __str__(self):
		return ("Title: {} , Content: {} , Date: {}".format(self.title,self.content,self.datetime))

	def __dict__(self):
		return{

			"id":self.id,
			"title":self.title,
			"content":self.content,
			"member_id":self.member_id,
			"date":self.datetime
			}