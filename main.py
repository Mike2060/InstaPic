from flask_migrate import Migrate, upgrade, migrate
from InstaPic import create_app, db

app = create_app()
migrates = Migrate(app=app, db=db)

@app.cli.command()
def test():
    import unittest
    import sys

    tests = unittest.TestLoader().discover("tests")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.errors or result.failures:
        sys.exit(1)
