from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Authors(db.Model):

    id: db.Mapped[int] = db.mapped_column(primary_key=True, autoincrement=True)
    name: db.Mapped[str] = db.mapped_column()
    birth_date: db.Mapped[str] = db.mapped_column()
    date_of_death: db.Mapped[str] = db.mapped_column()

    def __repr__(self):
        return f'Author(id = {self.id}, name = {self.name})'

    def __str__(self):
        dates = ""
        if self.birth_date:
            dates = f'({self.birth_date}'
        if self.date_of_death:
            dates += f' - {self.date_of_death})'
        else:
            dates += ')'
        return f'{self.id}. {self.name} {dates}'


class Books(db.Model):
    # __table_name__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String)
    title = db.Column(db.String)
    publication_year = db.Column(db.Integer)
    author_id: db.Mapped[int] = db.mapped_column(db.ForeignKey('authors.id'))

    def __str__(self):
        return f'{self.id}. {self.title} ({self.publication_year})'

    def __repr__(self):
        return f'Book(id={self.id}, isbn={self.isbn}, title={self.title}, publication_year={self.publication_year})'
