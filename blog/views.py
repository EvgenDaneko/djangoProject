from django.shortcuts import render

posts = [
    {
        'author':'Администратор',
        'title':'Это мой первый пост',
        'content':'Содержимое первого поста',
        'datepost':'12 января 2023'
    },
    {
        'author':'Пользователь',
        'title':'Это мой второй пост',
        'content':'Содержимое второго поста',
        'datepost':'12 января 2023'
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'О клубе Python'})


