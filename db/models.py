
from sqlalchemy import BigInteger, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .db import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=True)
    vacancies: Mapped[list["Vacancy"]] = relationship("Vacancy",
                                                      back_populates="user",
                                                      cascade="all, delete-orphan")
    filters: Mapped[list["Filter"]] = relationship("Filter",
                                                    back_populates="user",
                                                    cascade="all, delete-orphan")

class Vacancy(Base):
    __tablename__ = "vacancies"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column(nullable=True)
    user: Mapped["User"] = relationship("User", back_populates="vacancies")

class Filter(Base):
    __tablename__ = "filters"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    keywords: Mapped[str] = mapped_column(String, nullable=False)
    experience: Mapped[str] = mapped_column(String, nullable=True)
    user: Mapped["User"] = relationship("User", back_populates="filters")