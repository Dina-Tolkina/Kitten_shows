from tortoise import fields, models

class Breed(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100, unique=True)

    class Meta:
        table = "breeds"