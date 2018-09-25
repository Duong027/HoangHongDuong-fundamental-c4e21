import mlab
from post import Post # import Post tu file post.py

#1.COnnect

mlab.connect()

#2. Create Data

#p = Post(title = "C4E21", author = 'Quan', content = 'Hackaron',likes = 15)

#print(p.title)
#print(p.content)
#print(p.likes)
#print(p.author)
#3. Write Data
#p.save()


#---------------------------------------------------
def test_load_data():
    #2. Load all document
    all_posts = Post.objects()  #lazy loading

    #3. Print all document
    for post in all_posts:
    
        print(post.title)
        print(post.content)
        print(post.author)
        print('--------------')
test_load_data()
#read
def test_load_one_data(post_id):
    post = Post.objects().with_id(post_id) #None
    if post is None:
        print('Not found')
    else:
        print(post.title)
        print(post.author)
        print(post.content)

test_load_one_data("5b9cd07d139a10389c0ce04f")

#delete

def delete_one_data(post_id):
    #1. Lay dc document ra

    post = Post.objects().with_id(post_id)

    #2. Delete document
    if post is None:
        print('Not found')
    else:
        post.delete()
delete_one_data('5ba0f1e0139a1030e4453c5a')

#update

def update_one(post_id,new_title):
    #1. Lay post ra
    post = Post.objects().with_id(post_id)

    #2.Update
    # Dung cau truc Slug

    post.update(set__title=new_title)

update_one("5ba0f8e4139a1006b4239c44","Duong")











