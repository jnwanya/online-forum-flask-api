import os
import unittest

from datetime import datetime, timedelta

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.main import create_app, db
from app import blueprint
from app.main.service.bootloader import BootLoader


from app.main.model import (user, role, user_role, post_category, post, post_like, comment, post_view)


app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@app.before_first_request
def run_data_setup():
    print('*******app data setup runs***********')
    BootLoader.setup_app_data()
    # min_ago = datetime.now() - timedelta(minutes=15)
    # print(f'15 mins ago: {min_ago}')
    # post_view.PostView.delete_all_created_before_time(min_ago)


@manager.command
def run():
    app.run()


def test():
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
