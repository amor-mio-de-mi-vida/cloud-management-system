from django.http import JsonResponse
from backend.utils import *
from django.contrib.auth import logout as dj_logout, login as dj_login
import time
import logging

# 获取日志记录器
logger = logging.getLogger(__name__)

def log_view(request):
    # 记录不同级别的日志
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
    # ...

def register(request):
    password = request.POST["password"]
    password_again = request.POST["password_again"]
    if password != password_again:
        return JsonResponse({"status": 500, "content": "两次密码不一致"})

    username = request.POST["username"]
    if exist_username(username):
        return JsonResponse({"status": 500, "content": "用户已存在"})
    User.objects.create_user(username, password=password)
    return JsonResponse({"status": 200})


def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = User.objects.filter(username=username).first()

    if user and user.check_password(password):
        dj_login(request, user)
        request.session["username"] = username
        return JsonResponse({"status": 200})
    elif user:
        return JsonResponse({"status": 500, "msg": "密码错误"})


def logout(request):
    dj_logout(request)
    return JsonResponse({"status": 200})


def change_password(request):
    username = request.POST["username"]
    user = User.objects.filter(username=username).first()
    old_password = request.POST["old_password"]
    new_password = request.POST["new_password"]
    new_password_again = request.POST["new_password_again"]
    if new_password != new_password_again:
        return JsonResponse({"status": 500, "content": "两次密码不一致"})
    if user.check_password(old_password):
        user.set_password(new_password)
        user.save()
        return JsonResponse({"status": 200})
    else:
        return JsonResponse({"status": 500, "content": "旧密码错误"})


def get_all_models(request):
    return Model.objects.all()


def get_all_scenario(request):
    return Scenario.objects.all()

def train_model(request):
    pass

def get_all_dataset(request):
    return Dataset.objects.all()

def add_dataset(request):
    owner = User.objects.get(username=request.POST["username"])
    scenarios = request.POST["scenarios"]
    for scenario in scenarios:
        if not Scenario.objects.filter(name=scenario).exists():
            Scenario.objects.create(name=scenario)

    dataset = Dataset.objects.create(
        name=request.POST["name"],
        description=request.POST["description"],
        version=request.POST["version"],
        time= time.strftime('%Y%m%d%H%M%S'),
        type=request.POST["type"],
        owner=owner,
    )
    for scenario in scenarios:
        s = Scenario.objects.get(name=scenario)
        DatasetScenario.objects.create(dataset=dataset, scenario=s)
    return JsonResponse({"status": 200})


def delete_dataset(request):
    dataset = Dataset.objects.get(name=request.POST["name"])
    dataset.delete()
    return JsonResponse({"status": 200})

def modify_dataset(request):
    id = request.POST["id"]
    dataset = Dataset.objects.get(ID=id)
    dataset.version = request.POST["version"]
    dataset.name = request.POST["name"]
    dataset.description = request.POST["description"]
    dataset.time = time.strftime('%Y%m%d%H%M%S')
    dataset.type = request.POST["type"]

    dataset_scenarios = DatasetScenario.objects.filter(dataset=dataset)
    for ds in dataset_scenarios:
        ds.delete()
    scenarios = request.POST["scenarios"]
    for scenario in scenarios:
        s = Scenario.objects.get(name=scenario)
        if not s:
            s = Scenario.objects.create(name=scenario)
        DatasetScenario.objects.create(dataset=dataset, scenario=s)
    return JsonResponse({"status": 200})

def get_dataset_by_name(request):
    return Dataset.objects.get(name=request.POST["name"])

def get_dataset_by_type(request):
    return Dataset.objects.get(type=request.POST["type"])

def add_model(request):
    owner = User.objects.get(username=request.POST["username"])
    scenarios = request.POST["scenarios"]
    for scenario in scenarios:
        if not Scenario.objects.filter(name=scenario).exists():
            Scenario.objects.create(name=scenario)

    model = Model.objects.create(
        name=request.POST["name"],
        description=request.POST["description"],
        version=request.POST["version"],
        time= time.strftime('%Y%m%d%H%M%S'),
        url=request.POST["url"],
        owner=owner,
    )
    for scenario in scenarios:
        s = Scenario.objects.get(name=scenario)
        ModelScenario.objects.create(model=model, scenario=s)
    return JsonResponse({"status": 200})


def delete_model(request):
    model = Model.objects.get(name=request.POST["name"])
    model.delete()
    return JsonResponse({"status": 200})

def modify_model(request):
    id = request.POST["id"]
    model = Model.objects.get(ID=id)
    model.version = request.POST["version"]
    model.name = request.POST["name"]
    model.description = request.POST["description"]
    model.time = time.strftime('%Y%m%d%H%M%S')
    model.url = request.POST["url"]

    model_scenario = ModelScenario.objects.filter(dataset=model)
    for ms in model_scenario:
        ms.delete()
    scenarios = request.POST["scenarios"]
    for scenario in scenarios:
        s = Scenario.objects.get(name=scenario)
        if not s:
            s = Scenario.objects.create(name=scenario)
        ModelScenario.objects.create(model=model, scenario=s)
    return JsonResponse({"status": 200})

def get_model_by_name(request):
    return Model.objects.get(name=request.POST["name"])

def get_model_by_version(request):
    return Model.objects.get(version=request.POST["version"])

def get_model_by_scenario(request):
    scenario = Scenario.objects.get(name=request.POST["name"])
    return Model.objects.get(ID=scenario)

def get_model_by_owner(request):
    owner = User.objects.get(username=request.POST["name"])
    return User.objects.get(ID=owner)

def add_node(request):
    scenarios = request.POST["scenarios"]
    for scenario in scenarios:
        if not Scenario.objects.filter(name=scenario).exists():
            Scenario.objects.create(name=scenario)
    node = Node.objects.create(
        name=request.POST["name"],
        description=request.POST["description"],
        position=request.POST["position"],
        hardware=request.POST["hardware"],
    )
    for scenario in scenarios:
        s = Scenario.objects.get(name=scenario)
        NodeScenario.objects.create(node=node, scenario=s)
    return JsonResponse({"status": 200})

def get_all_nodes(request):
    return Node.objects.all()

def dispatch_model(request):
    pass