1)databasi bağlamak için ana projedeki (burada main) settings in içinde DATABASE kısmına;

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'todo',
        'USER': 'posstgres',
        'PASSWORD': 'meleks61',
        'HOST': 'localhost',
        'PORT': '5432',
        
    }
}
ifadesini yazıyoruz.

2)pip install psycopg2 komutuyla psycopg2 yi install ediyoruz.
3)py manage.py migrate  komutunu çalıştırıyoruz