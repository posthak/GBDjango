import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    html = """<!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Главная страница</title>
            </head>
            <body>
                <h1>Данные о моем первом Django-сайте</h1>
                <h2>Django-сайт Интернет-магазин</h2>
            </body>
        </html>"""
    logger.info('Открыта главная страница')
    return HttpResponse(html)

def about(request):
    html = """<!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Обо мне</title>
            </head>
            <body>
                <h1>Меня зовут Михаил</h1>
                <h2>На момем сайте вы сможете узнать обо мне</h2>
            </body>
        </html>"""
    logger.info('Открыта страница обо мне')
    return HttpResponse(html)


