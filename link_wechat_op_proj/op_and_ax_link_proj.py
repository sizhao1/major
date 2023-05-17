from wxauto import *
import time
import pyautogui
import pyperclip
import openai


# 获取当前微信客户端
wx = WeChat()
num = 0
# 获取会话列表
wx.GetSessionList()

openai.api_key = "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"


###############################
# 1、获取默认窗口聊天信息
###############################
# 定义一个函数生成 ChatGPT 的回复
def generate_response(prompt):
    # 调用 OpenAI API 生成回复
    completions = openai.Completion.create(
        engine="text-davinci-003",  # 指定使用的引擎名称
        prompt=prompt,  # API 请求的提示信息
        max_tokens=1024,  # API 响应的最大令牌数
        n=1,  # API 请求的完成数
        stop=None,  # API 响应的终止标志
        temperature=0.5,  # API 请求的温度参数
    )

    # 从 API 响应中取得回复
    message = completions.choices[0].text
    return message


# 初始化一个变量来存储对话上下文
context = "请用中文回复"

# def data(newdata):
#     urldata = "https://api.ownth*ink.com/bot?appid=e94dc1b1833a7f57ceeeb593bddccd87&userid=1&spoken=" + newdata
#     sess = requests.get(urldata)
#     answer = sess.text
#     answer = json.loads(answer)
#     return answer["data"]["info"]["text"]


# def get_default_window_messages(context):


# if __name__ == '__main__':
while True:
    if num < 10:
        # 默认是微信窗口当前选中的窗口
        #   输出当前聊天窗口聊天消息
        msgs = WeChat()
        if msgs.GetLastMessage[0] != "二流摄影爱好者":
            print("检测到新消息")
            # 提示用户输入信息
            # 如果用户输入结束命令，退出循环
            # if user_input in ["结束", "退出", "end", "exit"]:
            #     break
            # 把用户输入信息添加到对话上下文中
            context = context + msgs.GetLastMessage[1] + "\n"
            # 调用 generate_response() 函数生成回复
            response = generate_response(context)
            # 显示 ChatGPT 的回复
            print("ChatGPT：" + response)
            # 把 ChatGPT 的回复添加到对话上下文中
            context = context + response + "\n"
            print(msgs.GetLastMessage[0], msgs.GetLastMessage[1])
            pyperclip.copy(response)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(10)  # 延迟时间,模拟真人回复
            wx.SendMsg(response)
            # pyautogui.hotkey('enter')
            num += 1
        else:
            print("正在检测中")
    else:
        num = 0
        context = ""

