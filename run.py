from app import app, db
from app.models import User, Score

@app.shell_context_processor
def make_shell_context():
    return {'db':db,'User':User, 'Score':Score}

# export FLASK_APP=run.py
# export FLASK_DEBUG=1
