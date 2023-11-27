# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.role import Role  # noqa
from app.models.user import User  # noqa
from app.models.user_role import UserRole  # noqa
from app.models.language import Language  # noqa
from app.models.category_name import CategoryName  # noqa
from app.models.category import Category  # noqa
from app.models.article import Article  # noqa
from app.models.article_title import ArticleTitle  # noqa
from app.models.article_content import ArticleContent  # noqa
