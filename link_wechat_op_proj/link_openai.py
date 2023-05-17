import openai

# 初始化 OpenAI API 客户端
openai.api_key = "你的openai key"


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
context = ""

# 开始一个死循环来接受用户输入
while True:
    # 提示用户输入信息
    user_input = input("你：")
    # 如果用户输入结束命令，退出循环
    if user_input in ["结束", "退出", "end", "exit"]:
        break
    # 把用户输入信息添加到对话上下文中
    context = context + user_input + "\n"
    # 调用 generate_response() 函数生成回复
    response = generate_response(context)
    # 显示 ChatGPT 的回复
    print("ChatGPT：" + response)
    # 把 ChatGPT 的回复添加到对话上下文中
    context = context + response + "\n"
