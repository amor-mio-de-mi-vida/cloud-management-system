from django.db import models
from django.contrib.auth import settings
from django.contrib.auth.models import User


# Create your models here.
class Scenario(models.Model):
    ID = models.AutoField(primary_key=True, db_column='scenario_id')
    name = models.CharField(max_length=128, db_column='name')
    def __str__(self):
        return self.ID
    class Meta:
        db_table = 'scenario'


class Model(models.Model):
    ID = models.AutoField(primary_key=True, db_column='model_id')
    name = models.CharField(max_length=128, db_column='name')
    version = models.CharField(max_length=128, db_column='version')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='owner')
    description = models.TextField(db_column='description')
    url = models.URLField(db_column='url')  # 推理文件
    time = models.CharField(max_length=128, db_column='name')

    def __str__(self):
        return self.ID

    class Meta:
        db_table = 'model'


class ModelScenario(models.Model):
    model_id = models.ForeignKey(Model, on_delete=models.CASCADE, db_column='model_id')
    scenario_id = models.ForeignKey(Scenario, on_delete=models.CASCADE, db_column='scenario')

    class Meta:
        db_table = 'model_scenario'


class Dataset(models.Model):
    ID = models.AutoField(primary_key=True, db_column='dataset_id')
    name = models.CharField(max_length=128, db_column='name')
    version = models.CharField(max_length=128, db_column='version')
    description = models.CharField(max_length=128, db_column='description')
    time = models.CharField(max_length=128, db_column='name')
    type = models.CharField(max_length=128, db_column='type')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='owner')

    def __str__(self):
        return self.ID

    class Meta:
        db_table = 'dataset'


class DatasetScenario(models.Model):
    dataset_id = models.ForeignKey(Dataset, on_delete=models.CASCADE, db_column='dataset_id')
    scenario_id = models.ForeignKey(Scenario, on_delete=models.CASCADE, db_column='scenario')

    class Meta:
        db_table = 'dataset_scenario'


class Node(models.Model):
    ID = models.AutoField(primary_key=True, db_column='node_id')
    name = models.CharField(max_length=128, db_column='name')
    description = models.CharField(max_length=128, db_column='description')

    def __str__(self):
        return self.ID

    class Meta:
        db_table = 'node'
