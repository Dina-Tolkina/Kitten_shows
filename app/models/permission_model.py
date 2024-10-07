from tortoise import fields, models
from models.user_model import User

class Permission(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='permissions')
    can_read = fields.BooleanField(default=True)
    can_write = fields.BooleanField(default=False)
    can_delete = fields.BooleanField(default=False)
    can_update = fields.BooleanField(default=False)

    class Meta:
        table = "permissions"
