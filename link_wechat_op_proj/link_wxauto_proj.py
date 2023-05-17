# 首先，将wxauto模块导入到我们的代码块中。
from wxauto import *

# 初始化我们已经登录的客户端对象WeChat。
wx_cli = WeChat()

# 获取当前的客户端的联系人列表。
wx_cli.GetSessionList()

# 输出当前所在的聊天窗口的信息。
messages = wx_cli.GetAllMessage
for message in messages:
    print('%s : %s' % (messages[0], messages[1]))

# 获取到当前的聊天信息，还可以获取更多，使用LoadMoreMessage函数就可以实现。
wx_cli.LoadMoreMessage()
more_messages = wx_cli.GetAllMessage
for more_message in more_messages:
    print('%s : %s' % (more_message[0], more_message[1]))

