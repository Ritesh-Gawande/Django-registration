from django.db import models
import uuid
from datetime import datetime
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel


# Create your models here.
# class  PostModel(DjangoCassandraModel):
#     id = columns.UUID(primary_key=True, default=uuid.uuid4)
#      = columns.Text(required=True)
#     body = columns.Text(required=True)
    
#     created_at = columns.DateTime(default=datetime.now)

# class PostModels(DjangoCassandraModel):
#     id = columns.UUID(primary_key=True, default=uuid.uuid4)
#     f_name = columns.Text(required=True)
#     l_name = columns.Text(required=True)
#     mail = columns.Text(required=True)
#     mobile = columns.Text(required=True)
#     city = columns.Text(required=True)
#     state = columns.Text(required=True)
#     # password = columns.Text(required=True)
#     created_at = columns.DateTime(default=datetime.now)

class PostModelss(DjangoCassandraModel):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    f_name = columns.Text(required=True)
    l_name = columns.Text(required=True)
    mail = columns.Text(required=True)
    mobile = columns.Text(required=True)
    city = columns.Text(required=True)
    state = columns.Text(required=True)
    created_at = columns.DateTime(default=datetime.now)

 