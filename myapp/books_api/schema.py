import graphene
import api.schema
import authenticate.schema


# Query for getting the data from the server.
class Query(api.schema.Query, authenticate.schema.Query, graphene.ObjectType):
    pass


# Mutation for sending the data to the server.
class Mutation(api.schema.Mutation, authenticate.schema.Mutation, graphene.ObjectType):
    pass


# Create schema
schema = graphene.Schema(query=Query, mutation=Mutation)
