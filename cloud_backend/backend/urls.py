from django.urls import path
from .views import *

urlpatterns = [
###################### 用户管理 ##########################
    path("register/", register),
    path("login/", login),
    path("logout/", logout),
    path("change_password/", change_password),
######################## 首页 ##########################
    path("get_all_models/", get_all_models),
    path("get_all_scenario/", get_all_scenario),
###################### 训练模型 #########################
    path("train_model/", train_model),
##################### 数据集管理 #########################
    path("get_all_dataset/", get_all_dataset),
    path("add_dataset/", add_dataset),
    path("delete_dataset/", delete_dataset),
    path("modify_dataset/", modify_dataset),
    path("get_dataset_by_name/", get_dataset_by_name),
    path("get_dataset_by_type/", get_dataset_by_type),
#################### 模型管理 ##############################
    path("add_model/", add_model),
    path("delete_model/", delete_model),
    path("modify_model/", modify_model),
    path("get_model_by_name/", get_model_by_name),
    path("get_model_by_version/", get_model_by_version),
    path("get_model_by_scenario/", get_model_by_scenario),
    path("get_model_by_owner/", get_model_by_owner),
###################### 模型分发 ###########################
    path("get_all_nodes/", get_all_nodes),
    path("dispatch_model/", dispatch_model),
##################### 节点管理 ############################
    path("add_node/", add_node)
]
