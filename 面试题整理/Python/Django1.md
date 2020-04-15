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

### 2. Django的migrate的原理
    1. makemigrations负责将模型更改打包到单个迁移文件中,migrate负责将这些更改应用于数据库
    2. makemigrations会扫描模型并将其与迁移文件中当前包含的版本进行比较,然后写出一组新的迁移. 还可以指定生成的迁移文件名
        eg:python manage.py makemigrations --name 自己指定生成的迁移文件名称
    3. 生成的迁移文件中
        dependencies，此列表依赖的迁移列表。
        operations，是Operation定义此迁移功能的类的列表。
    4. 执行migrate时执行四步操作
        1. 迁移判定: 将项目中所有未迁移的变动文件进行迁移(django去查询数据库django_migrations表判断是否有新的迁移变动)
        2. 迁移映射关系: 在数据库django_content_type表新增映射关系(app与模型(model表名)的关系)
        3. 迁移权限: 在auth_permission表中增加权限
        4. 执行迁移: 生成数据库表或变动
        migrate --fake 只执行第一步,并生成迁移记录
        migrate --fake-initial 执行前三步,不实际变动数据库
        migrate 全部依次执行所有步骤