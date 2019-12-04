from TaskOrganizer.myapp import app
from TaskOrganizer.myapp import db


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
