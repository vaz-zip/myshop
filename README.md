1. Клонировать репозиторий
2. pip install Django
3. pip install Pillow
4. python manage.py makemigrations
5. python manage.py migrate

Используемые команды;
python manage.py shell
venv/scripts/activate
deactivate
python manage.py runserver
stripe listen --forward-to localhost:8000/payment/webhook/ (Запуск платёжного сервиса Stripe в отдельном окне из папки с файлом запуска)
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management (Запуск образа RabbitMQ вне виртуального пространства)
celery -A myshop worker -l info (Запуск Celery из виртуального пространства)
docker run -it --rm --name redis -p 6379:6379 redis (запуск образа redis из docker (преварительно нужно запустить Docker) 
запускается при наличии виртуального пространства из паки проекта)\
pip freeze > requirements.txt (Сохранение зависимостей)

from shop.models import Product
v1 = Product.objects.get(name='Вода')
v2 = Product.objects.get(name='Жидкость')
v3 = Product.objects.get(name='Лимонад')
v4 = Product.objects.get(name='Чай')

from shop.recommender import Recommender
r = Recommender()
r.products_bought([v1, v2])
r.products_bought([v1, v3])
r.products_bought([v2, v1, v4])
r.products_bought([v3, v4])
r.products_bought([v1, v4])
r.products_bought([v2, v3])

r.suggest_products_for([v1])
[<Product: Tea powder>, <Product: Red tea>, <Product: Green tea>]
r.suggest_products_for([v2])
[<Product: Black tea>, <Product: Tea powder>, <Product: Green tea>]
r.suggest_products_for([v3])
[<Product: Black tea>, <Product: Tea powder>, <Product: Red tea>]
r.suggest_products_for([4])
[<Product: Black tea>, <Product: Red tea>, <Product: Green tea>]