from django.shortcuts import render, redirect

# Create your views here.
from .models import Topic, Enntry, Pinlun
from .forms import TopicForm, EnntryForm



def xuexiao_index(request):
    """滨江校志的主页。"""
    return render(request, 'xuexiaoapp/xuexiao_index.html')

def jianjie(request):
    """学校简介。"""
    return render(request, 'xuexiaoapp/jianjie.html')

def dsj(request):
    """学校大事记。"""
    return render(request, 'xuexiaoapp/dsj.html')




def topics(request):
    """显示所有主题。"""
    topics = Topic.objects.order_by('date_added')

    pinluns = Pinlun.objects.order_by('date_added')

    context = {'topics':topics, 'pinluns':pinluns}
    return render(request, 'xuexiaoapp/topics.html', context)


def pinluns(request):
    """显示所有评论。"""
    """
    return render(request, 'xuexiaoapp/topics.html', context2)

    """



def topic(request, topic_id):
    """显示单个主题及其所有的条目。"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.enntry_set.order_by('-date_added')

    topics = Topic.objects.order_by('date_added')
    pinluns = Pinlun.objects.order_by('date_added')

    context = {'topic':topic, 'entries':entries, 'pinluns':pinluns, 'topics':topics}
    return render(request, 'xuexiaoapp/topic.html', context)


def new_topic(request):
    """添加新主题。"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单。
        form = TopicForm()
    else:
        # POST提交的数据：对数据进行处理。
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('xuexiaoapp:topics')

    # 显示空表单或指出表单数据无效。
    context = {'form':form}
    return render(request, 'xuexiaoapp/new_topic.html', context)

def new_enntry(request, topic_id):
    """在特定主题中添加新条目。"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 未提交数据：创建一个空表单。
        form = EnntryForm()
    else:
        # POST提交的数据：对数据进行处理。
        form = EnntryForm(data=request.POST)
        if form.is_valid():
            new_enntry = form.save(commit=False)
            new_enntry.topic = topic
            new_enntry.save()
            return redirect('xuexiaoapp:topic', topic_id=topic_id)

    # 显示空表单或指出表单数据无效。
    context = {'topic':topic, 'form':form}
    return render(request, 'xuexiaoapp/new_enntry.html', context)




def edit_enntry(request, enntry_id):
    """编辑既有条目。"""
    enntry = Enntry.objects.get(id=enntry_id)
    topic = enntry.topic

    if request.method != 'POST':
        # 初次请求：使用当前条目填充表单。
        form = EnntryForm(instance=enntry)
    else:
        # POST提交的数据：对数据进行处理。
        form = EnntryForm(instance=enntry, data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('xuexiaoapp:topic', topic_id=topic.id)


    context = {'enntry':enntry, 'topic':topic, 'form':form}
    return render(request, 'xuexiaoapp/edit_enntry.html', context)


