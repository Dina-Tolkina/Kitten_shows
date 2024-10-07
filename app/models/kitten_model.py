from tortoise import fields, models
from models.breed_model import Breed
from models.user_model import User

class Kitten(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    color = fields.CharField(max_length=100)
    age = fields.IntField()  
    description = fields.TextField()
    breed = fields.ForeignKeyField('models.Breed', related_name='kittens')
    owner = fields.ForeignKeyField('models.User', related_name='kittens')

    class Meta:
        table = "kittens"