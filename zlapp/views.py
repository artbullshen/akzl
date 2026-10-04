from django.shortcuts import render, redirect


from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import News, Topic, Entry
from .forms import TopicForm, EntryForm, NewsForm


# Create your views here.

def index(request):
    """张岭主页"""
    news = News.objects.order_by('-date_added').all()[:7]

    context = {'news':news}

    return render(request, 'zlapp/index.html', context)

def zhangling4(request):
    """张岭记忆4"""
    topic = Topic.objects.get(id=4)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topic':topic}

    return render(request, 'zlapp/zhangling4.html', context)


def zhangling1(request):
    """张岭记忆1"""
    topic = Topic.objects.get(id=1)
    news = News.objects.order_by('-date_added').all()[:25]
    context = {'news':news, 'topic':topic}

    return render(request, 'zlapp/zhangling1.html', context)

def zhangling2(request):
    """张岭记忆2"""
    topic = Topic.objects.get(id=2)
    news = News.objects.order_by('-date_added').all()[:15]
    context = {'news':news, 'topic':topic}

    return render(request, 'zlapp/zhangling2.html', context)

def zhangling3(request):
    """张岭记忆3"""
    topic = Topic.objects.get(id=3)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topic':topic}

    return render(request, 'zlapp/zhangling3.html', context)

@login_required
def sd3j1(request):
    """水电三局1：历史溯源"""
    topic = Topic.objects.get(id=5)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topic':topic}

    return render(request, 'zlapp/sd3j1.html', context)


def sd3j2(request):
    """水电三局2：安康水电站"""
    topic = Topic.objects.get(id=8)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topic':topic}

    return render(request, 'zlapp/sd3j2.html', context)

@login_required
def school(request):
    """学校专题"""
    topic = Topic.objects.get(id=3)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topic':topic}

    return render(request, 'zlapp/school.html', context)


def school2(request):
    """学校专题2：学校大事记"""
    topic = Topic.objects.get(id=3)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topic':topic}

    return render(request, 'zlapp/school2.html', context)

def school11(request):
    """学校专题11:"""
    topic = Topic.objects.get(id=17)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topic':topic}

    return render(request, 'zlapp/school11.html', context)

def school12(request):
    """学校专题12：辉煌与没落"""
    topic = Topic.objects.get(id=18)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topic':topic}

    return render(request, 'zlapp/school12.html', context)

def school13(request):    
    """学校专题13：生存和改制"""
    topic = Topic.objects.get(id=19)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topic':topic}

    return render(request, 'zlapp/school13.html', context)

def school14(request):
    """学校专题14：机遇和挑战"""
    topic = Topic.objects.get(id=20)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topic':topic}

    return render(request, 'zlapp/school14.html', context)

def school21(request):
    """学校专题21：学校大事记"""
    topic = Topic.objects.get(id=21)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topic':topic}

    return render(request, 'zlapp/school21.html', context)

def school22(request):
    """学校专题22：学校大事记"""
    topic = Topic.objects.get(id=22)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topic':topic}

    return render(request, 'zlapp/school22.html', context)

def school23(request):
    """学校专题23：学校大事记"""
    topic = Topic.objects.get(id=23)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topic':topic}

    return render(request, 'zlapp/school23.html', context)

def school24(request):
    """学校专题24：机遇和挑战"""
    topic = Topic.objects.get(id=24)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topic':topic}

    return render(request, 'zlapp/school24.html', context)


@login_required
def respect1(request):
    """致敬时代1：回望与守护"""
    topic = Topic.objects.get(id=11)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topic':topic}

    return render(request, 'zlapp/respect1.html', context)


def respect2(request):
    """致敬时代2：三线建设"""
    topic = Topic.objects.get(id=12)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topic':topic}
    return render(request, 'zlapp/respect2.html', context)

def respect3(request):
    """致敬时代3：荒凉的冷湖石油小镇"""
    topic = Topic.objects.get(id=13)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topic':topic}
    return render(request, 'zlapp/respect3.html', context)



def respect4(request):
    """致敬时代4：蜕变的北京798"""
    topic = Topic.objects.get(id=14)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topic':topic}
    return render(request, 'zlapp/respect4.html', context)


def respect5(request):
    """致敬时代5："""
    topic = Topic.objects.get(id=15)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topic':topic}

    print("test")
    
    return render(request, 'zlapp/respect5.html', context)

def respect6(request):
    """致敬时代6：主角的拍摄地--西安风雷"""
    topic = Topic.objects.get(id=3)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topic':topic}
    return render(request, 'zlapp/respect6.html', context)

def respect7(request):
    """致敬时代7：蝶变的北京绿心城市公园"""
    topic = Topic.objects.get(id=16)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topic':topic}
    return render(request, 'zlapp/respect7.html', context)

def other(request):
    """其他专题"""
    
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news}

    return render(request, 'zlapp/other.html', context)

def features(request):
    """三餐四季"""
    news = News.objects.order_by('-date_added')
    context = {'news':news}

    return render(request, 'zlapp/features.html', context)


def bond(request):
    """天南地北专题"""
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news}

    return render(request, 'zlapp/bond.html', context)





def news(request):
    """显示全部News"""
    news = News.objects.order_by('-date_added')
    context = {'news':news, 'topic':topic}
    return render(request, 'zlapp/news.html', context)

@login_required
def wms(request):
    """网站管理（WMS）：评论主题管理（新增、修改、删除）"""
    topics = Topic.objects.order_by('date_added')
    topic = Topic.objects.get(id=3)
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news, 'topics':topics, 'topic':topic}

    return render(request, 'zlapp/wms.html', context)

def wms11(request):
    """News部分"""
    news = News.objects.order_by('-date_added')

    """网站管理：添加新主题。"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单。
        form = TopicForm()
    else:
        # POST 提交的数据：对数据进行处理。
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('zlapp:wms')

    # 显示空表单或指出表单数据无效。
    context = {'news':news, 'form': form}
    return render(request, 'zlapp/wms11.html', context)

def wms12(request, topic_id):
    """News部分"""
    news = News.objects.order_by('-date_added')

    """网站管理：修改主题。"""
    topic = Topic.objects.get(id=topic_id)
    print(topic_id)
    print(topic) # 输出主题对象
    if request.method != 'POST':
        # 未提交数据：创建一个新表单。
        form = TopicForm(instance=topic)
    else:
        # POST 提交的数据：对数据进行处理。
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('zlapp:wms')
        
    context = {'news':news, 'topic':topic, 'form': form}
    return render(request, 'zlapp/wms12.html', context)




def hope(request):
    """2026新年展望"""
    news = News.objects.order_by('-date_added')
    context = {'news':news}

    return render(request, 'zlapp/hope.html', context)

def pinluns(request):
    """News部分"""
    news = News.objects.order_by('-date_added')

    """网友评论页面"""
    liouyan1 = Topic.objects.get(id=1)
    pinluns = liouyan1.entry_set.order_by('-date_added')
    liouyan2 = Topic.objects.get(id=2)
    pinluns2 = liouyan2.entry_set.order_by('date_added')


    context = {'news':news, 'pinluns':pinluns, 'pinluns2':pinluns2}

    return render(request,'zlapp/pinluns.html', context)

@login_required
def topics(request):
    """News部分"""
    news = News.objects.order_by('-date_added')

    """显示所有的Topic"""
    topics = Topic.objects.order_by('date_added')
    context = {'news':news, 'topics':topics}

    return render(request, 'zlapp/topics.html', context)

def topic(request, topic_id):
    """News部分"""
    news = News.objects.order_by('-date_added')
    
    """显示特定主题的所有评论"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    
    context = {'news':news, 'topic':topic, 'entries':entries}

    return render(request, 'zlapp/topic.html', context)

def topic_2(request, topic_id):
    """News部分"""
    news = News.objects.order_by('-date_added')
    
    """显示特定主题的所有评论"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'news': news, 'topic': topic, 'entries': entries}

    return render(request, 'zlapp/topic.html', context)



def new_topic(request):
    """News部分"""
    news = News.objects.order_by('-date_added')

    """添加新主题。"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单。
        form = TopicForm()
    else:
        # POST 提交的数据：对数据进行处理。
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('zlapp:topics')

    # 显示空表单或指出表单数据无效。
    context = {'news':news, 'form': form}
    return render(request, 'zlapp/new_topic.html', context)


def new_entry(request, topic_id):
    """News部分"""
    news = News.objects.order_by('-date_added')

    """在特定主题中添加新的评论"""
    topic =Topic.objects.get(id=topic_id)
    username = request.user.username

    print("test")
    if username == "":
        username = "没有获取到用户名"
    print(username)
    
    # print(topic_url) # 输出URL
    print(topic_id) # 输出主题ID
    if request.method != 'POST':
        # 未提交数据，创建一个空表单。
        form = EntryForm(initial={'name':username})
        #form = EntryForm()
    else:
        # POST提交的数据，对数据进行处理。
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            print("test2")
            new_entry.ip = request.META['REMOTE_ADDR'] # 获取IP地址
            print("test3") # 输出IP地址
            print(new_entry.ip) # 输出IP地址
            new_entry.name = username
            print("test4") # 输出用户名
            print(new_entry.name) # 输出用户名
            print(new_entry) # 输出评论内容
            print(new_entry.topic) # 输出评论主题
            
            print(new_entry.date_added) # 输出评论时间
                        
            new_entry.save()

            # new_url = topic_url
            # print(new_url) # 输出URL
            
            new_url = "zlapp:zhangling" + str(topic_id)
            print(new_url) # 输出URL
            print(topic_id) # 输出主题ID
            #url = reverse(new_url)+ '#topic_link' # 重定向到特定主题页面

            #return redirect(url)
            return redirect('zlapp:topic', topic_id) # 重定向到特定主题页面)

    # 显示空表单或指出表单数据无效。
    context = {'news':news, 'topic':topic, 'form':form}
    return render(request, 'zlapp/new_entry.html', context)


def edit_entry(request):
    # 编辑既有评论（网友留言）
    entry = Entry.objects.get(id=1)
    topic = entry.topic

    if request.method != 'POST':
        # 初次请求：使用当前条目填充表单。
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据：对数据进行处理。
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('zlapp:topic')

    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'zlapp/edit_entry.html', context)

def edit(request):
    """ 编辑管理界面：张岭最新消息的编辑，留言主题的编辑等"""
    # 张岭最新消息
    news = News.objects.order_by('-date_added').all()[:10]
    context = {'news':news}

    return render(request, 'zlapp/edit.html', context)

def add_news(request):
    """ 增加新消息。"""
    # News部分。
    news = News.objects.order_by('-date_added')

    # 添加新消息部分。
    if request.method != 'POST':
        # 未提交数据：创建一个新表单。
        form = NewsForm()
    else:
        # POST 提交的数据：对数据进行处理。
        form = NewsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('zlapp:edit')

    # 显示空表单或指出表单数据无效。
    context = {'news':news, 'form': form}
    return render(request, 'zlapp/add_news.html', context)

def edit_news(request):
    """ 编辑修改消息。"""
    # News部分。
    news = News.objects.order_by('-date_added')

    # 修改或删除消息的显示页面。
    context = {'news':news}

    return render(request, 'zlapp/edit_news.html', context)

def edit_new(request, new_id):
    # News部分。
    news = News.objects.order_by('-date_added')
    """ 编辑修改某一消息。"""
    new = News.objects.get(id=new_id)

    if request.method != 'POST':
        # 初次请求：使用当前消息填充表单。
        form = NewsForm(instance=new)
    else:
        # POST 提交的数据：对数据进行处理。
        form = NewsForm(instance=new, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('zlapp:edit_news')

    context = {'news':news, 'new':new, 'form':form}
    return render(request,'zlapp/edit_new.html', context)

def del_new(request):
    """删除某一消息。"""
    return

def test(request, topic_url, topic_id):
    """测试页面"""
    print(topic_url) # parm1)
    print(topic_id) # 输出参数1和参数2

    result = 'url={}, id={}'.format(topic_url, topic_id) # 输出结果
    return render(request, 'zlapp/test.html', {'result':result}) # 返回结果

def test1(request):
    """测试页面"""
    print("test1") # 输出结果
    
    return render(request, 'zlapp/test1_url.html') # 返回结果


