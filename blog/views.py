import markdown
from .models import *
from django.contrib import auth
from django.db.models import Count
from django.views.generic import ListView
from django.contrib.auth.models import User
from djangoblog.form import LoginForm,RegForm
from django.shortcuts import render,get_object_or_404,redirect


class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 7

    def get_queryset(self):
        return Post.objects.all()

def article(request, pk):
    post = get_object_or_404(Post, pk=pk)
    author = User.objects.get(id=post.author_id)
    category = Category.objects.get(id=post.category_id)
    post.increase_views() # 阅读量加1
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    post.body = md.convert(post.body)
    post.toc = md.toc
    # 获取相关文章
    relative_posts = Post.objects.filter(category_id=post.category_id).exclude(pk = pk).order_by('?')[:4]

    context = {}
    context['post'] = post
    context['author'] = author
    context['category'] = category
    context['relative_posts'] = relative_posts
    return render(request, 'blog/article.html', context)

class ArchivesView(ListView):
    template_name = 'blog/archives.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-created_time')

#全站所有的标签
class TagsView(ListView):
    model = Tag
    template_name = 'blog/tags.html'
    context_object_name = 'tags'

#每个标签下的所有文章
class TagListView(ListView):
    template_name = 'blog/tag_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        tag = get_object_or_404(Tag,pk = self.kwargs.get('pk'))
        return Post.objects.filter(tag=tag).order_by('-created_time')

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context['tag_name'] = Tag.objects.get(pk = self.kwargs.get('pk'))
        return context

class CategoryView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return Post.objects.filter(category=cate).order_by('-created_time')

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['cate_name'] = Category.objects.get(pk=self.kwargs.get('pk'))
        return context

# 按分类展示文章
class Categories(ListView):
    model = Post
    template_name = 'blog/categories.html'
    context_object_name = 'posts'

class BooksView(ListView):
    template_name = 'blog/books.html'
    context_object_name = 'books'
    paginate_by = 8

    def get_queryset(self):
        return Book.objects.all().order_by('-pk')

class BookListView(ListView):
    template_name = 'blog/book_list.html'
    context_object_name = 'books'
    paginate_by = 8

    def get_queryset(self):
        tag = get_object_or_404(BookTag,pk = self.kwargs.get('pk'))
        return Book.objects.filter(tag=tag).order_by('-created_time')

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['tag_name'] = BookTag.objects.get(pk = self.kwargs.get('pk'))
        return context

def book_detail(request,pk):
    book = get_object_or_404(Book,pk=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    book.detail = md.convert(book.detail)
    book.toc = md.toc
    book.increase_views()  # 阅读量加1
    tags = BookTag.objects.annotate(posts_count = Count('book')).order_by('-posts_count')
    return render(request,'blog/book_detail.html',{'book':book,'tags':tags,})

class MoviesView(ListView):
    template_name = 'blog/movies.html'
    context_object_name = 'movies'
    paginate_by = 8

    def get_queryset(self):
        return Movie.objects.all().order_by('-created_time')

class MovieListView(ListView):
    template_name = 'blog/movies_list.html'
    context_object_name = 'movies'
    paginate_by = 8

    def get_queryset(self):
        tag = get_object_or_404(MovieTag,pk = self.kwargs.get('pk'))
        return Movie.objects.filter(tag=tag).order_by('-created_time')

    def get_context_data(self, **kwargs):
        context = super(MovieListView, self).get_context_data(**kwargs)
        context['tag_name'] = MovieTag.objects.get(pk = self.kwargs.get('pk'))
        return context

def movie_detail(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    movie.detail = md.convert(movie.detail)
    movie.toc = md.toc
    movie.increase_views()  # 阅读量加1

    tags = MovieTag.objects.annotate(movies_count = Count('movie')).order_by('-movies_count')
    return render(request,'blog/movie_detail.html',{'movie':movie,'tags':tags,})


# 显示登录页面、进行登录操作
def login(request):
    # 此处只有登录的操作，验证的部分在forms.py完成
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from',reverse('blog:index'))) # 重定向到上一个页面
    else:
        login_form = LoginForm()
    context = {}
    context['login_form'] = login_form
    return render(request, 'blog/login.html', context)


# 显示注册页面、进行注册操作
def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            password = reg_form.cleaned_data['password']
            email = reg_form.cleaned_data['email']

            # 注册用户
            user = User()
            user.username = username
            user.email = email
            user.set_password(password)
            user.save()

            # 注册后自动登录
            user = auth.authenticate(username=username,password=password)
            auth.login(request,user)

            # 跳转到进入注册页面之前的页面
            return redirect(request.GET.get('from',reverse('blog:index')))  # 重定向到上一个页面

    else:
        reg_form = RegForm()
    context = {}
    context['reg_form'] = reg_form
    return render(request,'blog/register.html',context)

def messages(request):
    messages = Messages.objects.get(pk=1)
    return render(request,'blog/messages.html',{'messages':messages})


class CoursesView(ListView):
    template_name = 'blog/courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Courses.objects.all().order_by('-created_time')

def course(request,pk):
    course = get_object_or_404(Courses, pk=pk)
    return render(request, 'blog/course.html', context={'course':course})
