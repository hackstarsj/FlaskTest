from flask_sqlalchemy import SQLAlchemy

# initialize our db
db = SQLAlchemy()

from flask_bcrypt import Bcrypt
#######
# existing code remains #
#######
bcrypt = Bcrypt()

from src.models.UserModel import UserModel
from src.models.BlogpostModel import BlogpostModel