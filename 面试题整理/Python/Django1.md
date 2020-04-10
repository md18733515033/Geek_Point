### 1.Django解决跨域问题
    1. 安装cors-headers模块  pip3 install django-cors-headers
    2. setting中添加  
    INSTALLED_APPS = [
    ...
    'corsheaders'，
    ...
     ] 
    
    MIDDLEWARE_CLASSES = (
        ...
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware', # 注意顺序
        ...
    )
    #跨域增加忽略
    CORS_ALLOW_CREDENTIALS = True
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ORIGIN_WHITELIST = (
        '*'
    )
    
    CORS_ALLOW_METHODS = (
        'DELETE',
        'GET',
        'OPTIONS',
        'PATCH',
        'POST',
        'PUT',
        'VIEW',
    )
    
    CORS_ALLOW_HEADERS = (
        'XMLHttpRequest',
        'X_FILENAME',
        'accept-encoding',
        'authorization',
        'content-type',
        'dnt',
        'origin',
        'user-agent',
        'x-csrftoken',
        'x-requested-with',
        'Pragma',
    )