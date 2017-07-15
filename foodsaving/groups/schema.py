import graphene
from graphene_django import DjangoObjectType

from foodsaving.groups.models import Group


class GroupType(DjangoObjectType):
    class Meta:
        model = Group


class Query(graphene.AbstractType):
    all_groups = graphene.List(GroupType)
    group = graphene.Field(GroupType, id=graphene.Int(), name=graphene.String())

    def resolve_all_groups(self, args, context, info):
        return Group.objects.all()

    def resolve_group(self, args, context, info):
        id = args.get('id')
        name = args.get('name')

        if id is not None:
            return Group.objects.get(id=id)

        if name is not None:
            return Group.objects.get(name=name)

        return None
