## portal_cl bug & record

+ form没有执行submit也会刷新页面

  将<btn>改为<a>

+ required效果消失

  似乎是因为btn标签被去掉了

+ 点击登录按钮页面刷新

  woc 我多打了一个空格

  竟然要把form放在最外层

  可是register并没有在最外层啊

+ focus样式造成了麻烦

  什么都没做就解决了，啊不对，我去掉了autofocus

+ chrome说我密码泄露



+ 第二次全面检查
  1. 正常登录注册：密码泄露问题
  2. 空输入：无问题
  3. 错误输入：无问题

+ ~~密码泄露解决~~

  ~~settings.py里的DEBUG改成False~~



+ 背景图片django一直加载失败

  使用了static模板，完成度一半
  
  考虑试试在css部分用static模板，不行的话就改改css样式，查一下背景图片background的属性有哪些
  
  在css部分使用static模板成功！
  
  **后续：**woc!!! 居然是因为把debug改成了true才成功的吗
  
  实在不行就用http的方式加载吧
  
  **再续：**修改配置后debug==false时也没问题了
  
  
  
+ 然后密码泄露问题再次出现，在DEBUG改为false的情况下

  **密码泄露问题的猜想：**我没有退出就再次登录了，需要进一步的验证

  目前看来似乎是这样的

  

+ Page not found at /127.0.0.1

  加上标题就行了

+ icon加载失败

  使用static模板

+ debug=false时使用static 

  修改配置即可




+ 研究sqlite的**文件**这一数据类型✔
+ 修改数据库✔
+ 研究django上传文件的几个setting（文件是怎么通过前端发送到后端然后保存起来的）✔
+ 然后写一个上传文件的按钮试试行不行✔



+ 目前的问题：

  upload to= 还没设置（道理懂了，暂时可以不管）✔

  import写得和教程不太一样✔

  debug=false和教程不一样 static的import和教程不一样✔

  + 有两种static
  + 有两种urlpatterns修改方式
  + 决定使用和之前一样的方法先看看效果（目前OK）

  url和教程不一样✔

  form不是所有字段都由用户填写✔

  + 一个bug: dict需要用中括号[]不是小括号()
  
+ 新问题：

  admin站点突然加载不出CSS




+ 目前的问题：

  form的美化✔

  description为空的情况✔

  数据库要不要修改 暂时不改✔

  数据的展示，前端table
  
+ 新增的问题：

  前端没有验证了✔
  
  + 是因为我没有把field作为一个整体使用（已改）✔
  + error没加✔
  
  没有对错误情况的处理
  
  form有错误返回时需要显示



+ 目前的问题：

  form.is_bound为true时datafile没有填上，原因不明（认为是浏览器或者前端的问题）

  + 首先排查了不是逻辑的错误，bound和error都没错
+ 接下来缩小范围datafile.value存在
  
  需要确认是否没有其他添加error的方法✔

  复习一下当初点赞的实现（前端不能写的逻辑就写在后端）✔

  登录注册希望能改成用表单实现（不行，前端不好改）



+ 目前的问题：

  翻墙翻不出去了✔

  + SSR被封锁了，用V2ray翻
  
  不知道插件用起来能不能顺利
  
  + bootstrapTable需要确认一下django能不能给前端发送json数据✔
  + 暂定使用data tables插件，学习中，如果有什么不能克服的就用html的表格，其实也没什么✔
  
  ico显示不出来：浏览器的错误缓存



#### 0213-0217工作

+ 把数据展示页做起来
  + 位置修改✔
  
  + 改成多个html✔
  
  + 整合了上传文件与数据展示✔
  
  + 调整上传文件的按钮位置和其他样式✔
  
  + 修改data tables插件中的排序设置✔
  
  + 把checkbox加上✔
  
  + 上传成功就弹出提示框✔
  
  + 其他按钮样式修改✔
  
  + 文件大小展示✔
  
  + 未登录的用户部分功能禁用：如数据展示✔
    
    + 在后端，两个前端都设置了检查
    
  + 全选的checkbox✔
  
  + 删除按钮点击后弹窗问确定删除吗✔
  
  + 按下确认按钮提交表单✔
  
    

#### 0217 BUG

+ Uncaught TypeError: Cannot read property 'submit' of null

  解决方式：把form往上一级移动

  原因猜测：form被浏览器省略了

  https://www.sitepoint.com/community/t/submit-a-form/251939/3

+ 全选按钮在翻页后出错了

  解决方式：多加了一重判断

+ checkbox的属性真的很怪

  于0219处理

+ data.id居然打印不出来

  检查过了id存在

  前端可以打印被选中的id

+ list居然是空的

  找到原因了，是form的tag放错了位置



+ 功能测试：
  + 未登录的用户使用数据展示功能✔
  + 将testform删除✔
  + showdata界面有两个form不知道submit会怎样记得测试
    + 普通上传✔
    + 普通删除✔
    + 复选框选了但是没点删除按钮，然后上传文件✔



#### 0218

+ 检查基本的checkbox操作，不要使劲折腾✔
+ 后端把要删除的id list处理后返回删除成功✔
+ 意识到upload to 的设置的必要性，给每个用户一个文件夹✔
  + https://meik2333.com/posts/django-dynamically-changes-file-upload-path/
+ 展示的时候不要展示文件夹的名字✔
  + 在model里定义了一个返回文件名的方法，感谢stackoverflow
+ 删除数据库的数据的同时想把文件一起删掉✔
  + https://blog.csdn.net/qq_38669698/article/details/88183248



#### 0219

+ 重命名的前端✔
  + 按钮点击后获取被选中的第一个复选框的值（文件的id)
  + 传给后端，试试能不能通过参数传（不行
  + 如果不能用参数传就得想办法放到form里面去，可以用hide
+ 重命名的后端✔
  + 修改数据库里的值✔
  + 修改真的文件名✔
  + http://cn.voidcc.com/question/p-wsjxlvqu-zb.html
  + 遇到了不少问题，比较重要的地方是os.path.join的使用，还有粗心没有加user_



#### 0220

+ task model✔

+ 修改delete功能，增加表单判断✔

+ 修改rename功能，增加required要求，增加表单判断✔

+ 修改弹窗，改为出错才弹窗✔

+ 测试：

  + 上传：✔
  + 删除：删除全部，删除单个，没选中删✔
  + 重命名：输入为空，选了不止一个，没选中✔



#### 0223

+ django template 继承
+ showtask.html做了一点点点



#### 0224

+ 发现重命名的表单错误提示做得不够好
  + 必须用.value='',用setAttribute('value','')不行，理由如下
  + https://www.jianshu.com/p/589a089a9a03

+ 决定研究checkbox form

  

#### 0225

+ taskform✔
+ 新建一个数据分析任务的前端✔



#### 0226

+ 找了好多教程为了做一个比较好看的复选，最后发现dropdown的修改方法只是在\<input>外加上\<a>✔
+ 发现重命名的一个Bug:必须禁止重名✔
  + 在后端except了异常

+ 想做更清楚的错误提示
  + toast比想象中难搞（完全搞不懂啊）

+ 新建一个数据分析任务的后端
  + form.isvalid()居然返回false



#### 0227

+ form.isvalid()终于对了，在form里加了init函数
  + https://stackoverflow.com/questions/38381994/multiplechoicefield-invalid-choice-error-select-a-valid-choice-somechoice-i

+ form的error一直不对
  + 原因是前端的class样式
  + 自己写error的样式

+ form的checkbox目前没有办法在bound的情况下保存上次的选择，暂时不管
+ 新建任务的前后端暂时完工✔
+ 展示任务暂时完工✔
+ 全选按钮✔
+ 重命名任务✔
+ 删除任务✔



+ 暂时把form设置为novalidate方便测试后端，之后记得改

+ 长远的问题：

  文件名相同的文件怎么处理

  测试

  需要学一下nginx吗
  
  对于debug=false设置admins发送邮件
  
  