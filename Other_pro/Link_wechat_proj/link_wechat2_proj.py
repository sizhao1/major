import itchat
import openai
from itchat.content import TEXT
import sys  # 导入sys模块
sys.setrecursionlimit(10000)  # 将默认的递归深度修改为3000
openai.api_key = "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"
def askbot(question):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": question}
    ]
    )
    return completion.choices[0].message.content
@itchat.msg_register(TEXT)
def wxreply(msg):
    itchat.send(askbot(msg.text), toUserName=msg.FromUserName)
itchat.login(enableCmdQR=2)
itchat.run()
