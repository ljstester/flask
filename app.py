from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from apps.user.models import User
from apps import create_app
from exts import db

app = create_app()
manager = Manager(app=app)
migtate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
