## portal_cl数据库设计

UserExtension(User)

id，邮箱，用户名（不允许重复），密码



```python
class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
```



File

id，文件（文件名，创建时间，路径，文件大小，描述），所有者，路径，类型

类型：导入的数据，生成的数据

操作：查看详情（数据的具体展示和修复只需要提供按钮外接，数据质量结果）



Task

id，任务名，备注，所有者，任务结果（文件），任务状态

任务状态：搭建分析流程成功，发布中，发布成功，发布失败，生成分析结果成功，分析结果失败

操作：查看详情，分析流程，数据发布，分析结果可视化展示

创建任务：填写任务名，备注，选择数据集

