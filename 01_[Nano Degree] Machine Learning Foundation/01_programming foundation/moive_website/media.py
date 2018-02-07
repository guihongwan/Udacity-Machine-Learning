#coding:utf-8
import webbrowser

class Movie():
	""" This class provides a way to store movie related information, like title, storyline, ... """
	
	VALID_RATINGS = ["","*","**","***","****","*****"]

	
	def __init__(self, title, storyline, poster_image_url, trailer_video_url, rating):

		"""Constructer"""

		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image_url
		self.trailer_video_url = trailer_video_url
		self.rating = rating

	
	def show_trailer(self):
		"""Play the video"""
		webbrowser.open(self.trailer_video_url)

#=============================test the class
a = Movie("哆啦A梦",
	"哆啦A梦：大雄的南极冰冰凉大冒险",
	"https://imgsa.baidu.com/baike/c0%3Dbaike272%2C5%2C5%2C272%2C90/sign=8a75432764061d95694b3f6a1a9d61b4/4e4a20a4462309f7b326970d780e0cf3d7cad667.jpg",
	"http://maoyan.meituan.net/movie/videos/854x480206d5d1eda324f68a4ae0853581d99f4.mp4",
	4)

interstellar = Movie("Interstellar",
	"Interstellar is a 2014 British-American epic science fiction film.",
	"https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
	"http://vf1.mtime.cn/Video/2014/12/01/mp4/141201160911303936.mp4",
	5)


print Movie.__doc__
print Movie.__name__
print Movie.__module__
#print media.__class__
print Movie.__dict__ #the class name space
print Movie.__bases__
print "__init__:" + Movie.__init__.__doc__
print "show_trailer：" + Movie.show_trailer.__doc__
print "Interstellar Rating:" + Movie.VALID_RATINGS[interstellar.rating]
#interstellar.show_trailer()
