"""定义 zlapp 的 URL 模式。"""
from django.urls import path

from . import views

app_name = 'zlapp'
urlpatterns = [
    # 网站主页：张岭
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),

    # 岭上岁月部分
    path('zhangling4/', views.zhangling4, name='zhangling4'),
    path('zhangling1/', views.zhangling1, name='zhangling1'),
    path('zhangling2/', views.zhangling2, name='zhangling2'),
    path('zhangling3/', views.zhangling3, name='zhangling3'),

    # 水电三局部分
    path('sd3j1/', views.sd3j1, name='sd3j1'),
    path('sd3j2/', views.sd3j2, name='sd3j2'),
   

    # 学校专题部分
    path('school/', views.school, name='school'),
    path('school2/', views.school2, name='school2'),
    path('school11/', views.school11, name='school11'),
    path('school12/', views.school12, name='school12'),
    path('school13/', views.school13, name='school13'),
    path('school14/', views.school14, name='school14'),
    path('school21/', views.school21, name='school21'),
    path('school22/', views.school22, name='school22'),
    path('school23/', views.school23, name='school23'),
    path('school24/', views.school24, name='school24'),

    

    
           

    
    
    
    # 致敬时代部分
    path('respect1/', views.respect1, name='respect1'),
    path('respect2/', views.respect2, name='respect2'),
    path('respect3/', views.respect3, name='respect3'),
    path('respect4/', views.respect4, name='respect4'),
    path('respect5/', views.respect5, name='respect5'),
    path('respect6/', views.respect6, name='respect6'),
    path('respect7/', views.respect7, name='respect7'),

    # 其它专题部分
    path('other/', views.other, name='other'),

    # 三餐四季部分
    path('features/', views.features, name='features'),

    # 天南地北部分
    path('bond/', views.bond, name='bond'),  


    


    # 新闻部分
    path('news/', views.news, name='news'),
    path('hope/', views.hope, name='hope'),
    path('pinluns/',views.pinluns, name='pinluns'),

    path('topics/', views.topics, name='topics'),
    # 特定topic的详细页面。
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    
    path('new_topic/', views.new_topic, name='new_topic'),

    # 网站管理部分
    path('wms/', views.wms, name='wms'),# 管理主页面
    path('wms11/', views.wms11, name='wms11'),  # 新增评论主题
    path('wms12/<int:topic_id>/', views.wms12, name='wms12'),  # 编辑特定主题




    # 给指定topic增加新entry，并且采用两个参数的方法。
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),


    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('edit/', views.edit, name='edit'),
    path('add_news/', views.add_news, name='add_news'),
    path('edit_news/', views.edit_news, name='edit_news'),
    path('edit_new/<int:new_id>/', views.edit_new, name='edit_new'),
    path('del_new/', views.del_new, name='del_new'),

    # 测试：给指定topic增加新entry，并且采用两个参数的方法。
    path('test/<str:topic_url>/<int:topic_id>/', views.test, name='test'),
    path('test1/', views.test1, name='test1'),





]


