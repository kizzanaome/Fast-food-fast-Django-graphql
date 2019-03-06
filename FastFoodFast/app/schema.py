import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Menu, Order


class MenuType(DjangoObjectType):
    class Meta:
        model = Menu


class Ordertype(DjangoObjectType):
    class Meta:
        model = Order


class Query(graphene.ObjectType):
    menu = graphene.List(MenuType)

    def resolve_menu(self, info, **kwargs):
        return Menu.objects.all()


class CreateMenu(graphene.Mutation):
    id = graphene.ID()
    food_name = graphene.String()
    price = graphene.Int()

    class Arguments:
        food_name = graphene.String()
        price = graphene.Int()

    def mutate(self, info, food_name, price):
        menu = Menu(food_name=food_name, price=price)
        menu.save()

        return CreateMenu(id=id, food_name=food_name, price=price)


class Mutation(graphene.ObjectType):
    create_menu = CreateMenu.Field()
