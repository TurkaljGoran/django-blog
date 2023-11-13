import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings" )
import django
django.setup()
import json
from blog.models import Post


if __name__ == '__main__':
    
 
    with open('posts.json') as file:
        posts_json = json.load(file)
        
        for post in posts_json:

            new_post = Post(
                title=post['title'], 
                content=post['content'],
                author_id=post['user_id']
            )
            new_post.save()

