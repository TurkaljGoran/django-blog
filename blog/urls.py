from django.urls import path
from .views import BlogHome, AuthorBlogHome,  BlogAbout, PostDetail, PostCreate, PostUpdate, PostDelete

app_name = 'blog'


urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('author-posts/<int:author_id>/', AuthorBlogHome.as_view(), name='author-posts' ),
    path('about/', BlogAbout.as_view(), name='about'),
    path('post/<int:pk>/details/', PostDetail.as_view(), name='detail'),
    path('post/create/', PostCreate.as_view(), name='create'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='update'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name = 'delete')
]
