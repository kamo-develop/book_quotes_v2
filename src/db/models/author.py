from sqlalchemy import VARCHAR, String
from sqlalchemy.orm import Mapped, mapped_column
from src.db import Base


class Author(Base):
    name: Mapped[str] = mapped_column(String)