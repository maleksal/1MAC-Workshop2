import itertools
__metaclass__ = type
class BaseStore():

	def __init__(self,data_provider ,last_id):
		self._data_provider = data_provider
		self._last_id = last_id

	def get_all(self):
		return self._data_provider

	def add(self,item_instance):
		item_instance.id = self._last_id
		self._data_provider.append(item_instance)
		self._last_id += 1

	def get_by_id(self,id):
		for item in self.get_all() :
			if item.id == id :
				return item

	def entity_exist(self,item):
		if item == self.get_by_id(item.id):
			return True
		return False
	def delete(self,id):
		return (self._data_provider.remove(self.get_by_id(id)))

	def update(self, item):
		result = item
		all_items = self.get_all()
		for index, current_item in enumerate(all_items):
			print(index,current_item)
			if current_item.id == item.id:
				all_items[index] = item
				break
		return result

class MemberStore(BaseStore):
	Members = []
	last_id = 1

	def __init__(self):
		super(MemberStore,self).__init__(MemberStore.Members,MemberStore.last_id)

	def get_by_name(self,member_name):
		return (member for member in self.get_all() if member.name == member_name)

	def get_members_with_post(self,all_posts):
		all_members = self.get_all()
		for member , post in itertools.product(all_members,all_posts):
			if member.id == post.member_id:
				member.posts.append(post)
		for member in all_members:
			yield post in member.posts	
	def get_top_two(self, all_posts):
		all_members_posts = list(self.get_members_with_post(all_posts))
		all_members_posts.sort(key=lambda x: len(x.posts), reverse=True)
		yield all_members_posts[0]
		yield all_members_posts[1]
	def getMemberPosts(self,all_posts,Id):
		postsM =[]
		for e in all_posts:
			#print e.id
			#if e.member_id == Id:
			postsM.append(e)
		return postsM



#-------------Post Store------------------------

class PostStore(BaseStore):
	Posts = []
	last_id = 1

	def __init__(self):
		super(PostStore,self).__init__(PostStore.Posts,PostStore.last_id)
	def get_posts_by_date(self):
		all_posts = self.get_all() [:]
		all_posts.sort(key=lambda x: x.date, reverse=True)
		for post in all_posts:
		    yield post
