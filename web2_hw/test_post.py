import mlab
from post import Post # import Post tu file post.py

#1.COnnect

mlab.connect()

#2. Create Data

p = Post(title = "C4E21", author = 'Quan', content = 'Hackaron',likes = 15)

print(p.title)
print(p.content)
print(p.likes)
print(p.author)
#3. Write Data
p.save()
