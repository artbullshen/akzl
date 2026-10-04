"""定义 xuexiaoapp（学校app)的 URL 模式。"""

from django.urls import path

from . import views

app_name = 'xuexiaoapp'

urlpatterns = [
    # 主  页
    path('', views.xuexiao_index, name='xuexiao_index'),
    # 学校简介。
    path('jianjie/', views.jianjie, name='jianjie'),
    # 学校大事记
    path('dsj/', views.dsj, name='dsj'),
    # 显示所有的主题。
    path('topics/', views.topics, name='topics'),
    # 显示所有的评论
    path('pinluns/', views.pinluns, name='pinluns'),
    # 特定主题的详细页面
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    #主题相应条目的添加、编辑。
    # 用于添加新主题的页面。
    path('new_topic/', views.new_topic, name='new_topic'),
    #用于添加新条目的页面。
    path('new_enntry/<int:topic_id>/', views.new_enntry, name='new_enntry'),
    # 用于编辑条目的页面。
    path('edit_enntry/<int:enntry_id>/', views.edit_enntry, name='edit_enntry'),


]


