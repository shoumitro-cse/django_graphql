import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Book
from graphene.types.generic import GenericScalar

# pip install graphene-django-cud==0.10.0
from graphene_django_cud import mutations


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = "__all__"


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    book = graphene.Field(BookType, book_id=graphene.Int())

    def resolve_all_books(self, info, **kwargs):
        return Book.objects.all()

    def resolve_book(self, info, book_id):
        return Book.objects.get(pk=book_id)


# class BookInput(graphene.InputObjectType):
#     id = graphene.ID()
#     title = graphene.String()
#     author = graphene.String()
#     year_published = graphene.String()
#     review = graphene.Int()
#     metadata = GenericScalar()


# class CreateBookMutation(graphene.Mutation):
#     class Arguments:
#         book_data = BookInput(required=True)
#
#     book = graphene.Field(BookType)
#
#     @staticmethod
#     def mutate(root, info, book_data=None):
#         book_instance = Book(
#             title=book_data.title,
#             author=book_data.author,
#             year_published=book_data.year_published,
#             review=book_data.review,
#             metadata=book_data.metadata,
#         )
#         book_instance.save()
#         return CreateBookMutation(book=book_instance)


# class UpdateBookMutation(graphene.Mutation):
#     class Arguments:
#         book_data = BookInput(required=True)
#
#     book = graphene.Field(BookType)
#
#     @staticmethod
#     def mutate(root, info, book_data=None):
#
#         book_instance = Book.objects.get(pk=book_data.id)
#
#         if book_instance:
#             book_instance.title = book_data.title
#             book_instance.author = book_data.author
#             book_instance.year_published = book_data.year_published
#             book_instance.review = book_data.review
#             book_instance.save()
#
#             return UpdateBookMutation(book=book_instance)
#         return UpdateBookMutation(book=None)


# class DeleteBookMutation(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID()
#
#     book = graphene.Field(BookType)
#
#     @staticmethod
#     def mutate(root, info, id):
#         book_instance = Book.objects.get(pk=id)
#         book_instance.delete()
#         return None


class CreateBookMutation(mutations.DjangoCreateMutation):
    class Meta:
        model = Book


class UpdateBookMutation(mutations.DjangoUpdateMutation):
    class Meta:
        model = Book


class DeleteBookMutation(mutations.DjangoDeleteMutation):
    class Meta:
        model = Book


class Mutation(graphene.ObjectType):
    create_book = CreateBookMutation.Field()
    update_book = UpdateBookMutation.Field()
    delete_book = DeleteBookMutation.Field()


# # pip install graphene-django-crud
# from graphene_django_crud.types import DjangoCRUDObjectType, resolver_hints
# class BookType1(DjangoCRUDObjectType):
#     class Meta:
#         model = Book
#         # exclude_fields = ("password",)
#         # input_exclude_fields = ("last_login", "date_joined")
#
#
# class Mutation(graphene.ObjectType):
#     create_book = BookType1.CreateField()
#     update_book = BookType1.UpdateField()
#     delete_book = BookType1.DeleteField()


schema = graphene.Schema(query=Query, mutation=Mutation)
