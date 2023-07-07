import graphene
from graphene_django import DjangoObjectType
from books.models import Book

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "description", "author", "price")
        

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hola!")
    books = graphene.List(BookType)
    
    def resolve_books(self, info):
        return Book.objects.all()
    
schema = graphene.Schema(query=Query)