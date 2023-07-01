# FlaskProject
## このファイルは主にblogprojectとpicture_projectの２つに分かれる。
#

## 1.brogproject(個人ブログアプリ)
- apps
    - __pycacche__
    - crud
        - __pycache__
        - static_crud
            - style.css
        _ template
            - delete.html
            - login_delete.html
            - login.html
            - post1.html
        - __init__.py
        - forms.py
        - views.py
    - static
        - assets
            - img
            - favicon.ico
        - css
            - style.css
        - js
            - scripts.js
    - templates
        - base.html
        - contact_complete.html
        - index.html
        - post.html
        - send_mail.txt
    - __init__.py
    - blogapp.py
    - forms.py
    - modesl.py
    - settings.py
- migrarions
- .env
- blog.sqlite

## .picture_project(インスタもどきアプリ)
- apps
    - __pycacche__
    - authapp
        - __pycache__
        - static_auth
            - css
                - bootstrap.min.css
                - sigin.css
            - img
        _ template_auth
            - login.html
        - __init__.py
        - forms.py
        - views.py
    - images      -->投稿した写真がここに入る
    - pictapp
        - static_pict
            - bootstrap.bundle.min.js
        - templates_pict
            - base.html
            - detail.html
            - mypage.html
            - top.html
            - upload.html
            - userlist.html
        - __init__.py
        - forms.py
        - modesl.py
        - views.py
    - static
        - assets
            - img
            - favicon.ico
        - css
            -style.css
        - js
            -script.js
    - templates
        -index.html
    - __init__.py
    - app.py
    - forms.py
    - models.py
    - settings.py
- migrarions
- .env
- app.sqlite

##＃ 仮想環境
venv_webapp