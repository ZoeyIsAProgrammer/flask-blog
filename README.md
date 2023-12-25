# Flask Blog Project
Introduction:  
This is a simple blog website built with Flask, where you can register, login, logout a user, create, update, delete and view blogs.  

Technologies I used in this project:  
Flask  
Flask blueprint structure (to separate views into main function views and auth-ralated views)  
Flask-Bootstrap  
Flask-Login  
Flask-SQLAlchemy  
Flask-WTF  
Flask-Migrate  
Sqlite3
## Getting Started
First set up a venv on top of the 'project/requirements.txt' file.  
Then in the 'flask-blog' directory, just outside of 'project' folder, do migration commands:  
```
flask --app project db init &&
flask --app project db migrate &&
flask --app project db upgrade
```  
Then run the app with:  
```
flask --app project run
```  
The app will then be available at [http://127.0.0.1:5000](http://127.0.0.1:5000)  

Or you can set an environment variable 'FLASK_APP' as 'project', then do all Flask commands as `flask <command>` without the `--app <app name>` option.