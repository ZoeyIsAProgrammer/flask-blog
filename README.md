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
First navigate to 'project' folder and set up a venv on top of the 'requirements.txt' file.  
Then do migrations:  
```
flask --app project db init &&
flask --app project db migrate &&
flask --app project db upgrade
```  
Then run the app with:  
```
flask --app project run
```
Or you can set an environment variable 'FLASK_APP' as 'project', then do all Flask commands as `flask <command>` without the `--app <app name>` option.