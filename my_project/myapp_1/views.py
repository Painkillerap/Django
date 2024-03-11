import datetime
import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)

http_text_hand = "<h1>Приветствую вас!</h1>"
http_text_footer = "<p>GeekBrains – образовательный портал. Мы учим людей с нуля осваивать программирование, веб-дизайн, маркетинг и другие\
              современные профессии. Проводим онлайн-курсы со стажировкой и бесплатные мастер-классы, развиваем сообщество, \
                сотрудничаем с компаниями по трудоустройству и непрерывно тестируем новые методики для поднятия эффективности\
                      обучения. </p>"
http_menu = "<h3>МЕНЮ</h3>\
        <a href='/'>Главная</a><br>\
        <a href='/about/'>Обо мне</a><br>"


def index(request):
    title = "<h2>Вы находитесь на главной странице</h2>"
    title_2 = "<h3>На нашем сайте вы можете познакомится с программированием</h3>"
    http_text = http_text_hand + http_menu + title + title_2 + http_text_footer
    logger.info(f'Посещение главной страницы - {datetime.datetime.now()}')
    return HttpResponse(http_text)


def about(request):
    title = "<h2>Вы находитесь на странице 'Обо мне'</h2>"
    title_2 = "<h3>Давайте познакомимся. Я студент GeekBrains</h3>"

    http_text = http_text_hand + http_menu + title + title_2 + http_text_footer
    logger.info(f'Посещение страницы обо мне - {datetime.datetime.now()}')
    return HttpResponse(http_text)
