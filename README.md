Django1.6/Bootstrap3/MySQL5.7/Python2等技术开发的船舶内部网站


/---------------------------------------------------------- 

实现：

1）网站首页显示，进入各个页面的链接。六个模块：机务信息（超链接）、新闻、视频模块（超链接）、航行动态、个人信息中心、联系管理员、登录按钮。

2）机务信息，链接到船上的机务模块。

3）新闻模块，可进行新闻、公告的查看，评论。登录用户方可使用。

4）视频模块，链接到船上的视频模块。

5）船舶航行动态信息，以弹窗形式表示出。

6）个人信息模块，登录用户可进行对自己的部分信息修改。

7）联系管理员，进行信息留言后自动发邮件到管理员邮箱中。登录用户方可使用。


/------------------------------------------------------------

前台部分：

系统前台模块表

编号	模块名称	子模块

W1	海监船首页	W11用户登录

W12 用户注册

W13 用户登出

W2	机务信息	W21 超链接船上机务系统

W3	新闻	      W31 新闻内容显示

W32 新闻标签筛选

W4	视频模块	W41 超链接船上视频系统

W5	船舶航行动态W51 所查船舶动态数据信息

W6	个人信息	W61 个人信息中心

W7	联系管理员  W71 联系管理员界面

/---------------------------------------------------------------

后台部分：

系统后台模块表

编号	模块名称	    子模块

W8	 管理员登录	      增改管理员账户，权限

W9	 管理员账户管理    增改数据

W10	 船舶动态数据管理  增改数据

W111 船员信息管理	     增改船员信息

W121 新闻发布	       新闻内容编写

