from tortoise import fields, models
from models.kitten_model import Kitten
from models.user_model import User

class Rating(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='ratings')
    kitten = fields.ForeignKeyField('models.Kitten', related_name='ratings')
    score = fields.IntField() 

    class Meta:
        table = "ratings"
        unique_together = ('user', 'kitten')