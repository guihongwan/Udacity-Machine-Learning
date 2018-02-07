#coding:utf-8
import media
import fresh_tomatoes

# Get the movies I like
# step1: initialize the film
# step2: store it in 'movies' which is a list
movies = []

a = media.Movie("哆啦A梦",
	"哆啦A梦：大雄的南极冰冰凉大冒险",
	"https://imgsa.baidu.com/baike/c0%3Dbaike272%2C5%2C5%2C272%2C90/sign=8a75432764061d95694b3f6a1a9d61b4/4e4a20a4462309f7b326970d780e0cf3d7cad667.jpg",
	"http://maoyan.meituan.net/movie/videos/854x480206d5d1eda324f68a4ae0853581d99f4.mp4",
	4)
movies.append(a)

interstellar = media.Movie("Interstellar",
	"Interstellar is a 2014 British-American epic science fiction film.",
	"https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
	"http://vf1.mtime.cn/Video/2014/12/01/mp4/141201160911303936.mp4",
	5)
movies.append(interstellar)

yongth = media.Movie("芳华",
	"讲述了在充满理想和激情的军队文工团，一群正值芳华的青春少年，经历着成长中的爱情萌发与充斥着变数的人生命运故事。",
	"https://imgsa.baidu.com/baike/c0%3Dbaike180%2C5%2C5%2C180%2C60/sign=086d0f7d1530e924dba994632d610563/91529822720e0cf3d8af5c8e0046f21fbe09aa6e.jpg",
	"http://vfx.mtime.cn/Video/2017/05/17/mp4/170517153754509087.mp4",
	2)
movies.append(yongth)

fresh_tomatoes.open_movies_page(movies)

