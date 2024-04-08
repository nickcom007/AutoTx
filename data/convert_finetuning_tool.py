import json

# 初始化一个空列表来存储所有转换后的字典
combined_conversations = []

# 读取.jsonl文件
with open('AutoTx_finetuning_tool.jsonl', 'r') as file:
    for line in file:
        # 将每行的JSON字符串转换为字典
        data = json.loads(line)

        # 如果存在'messages'键，则重命名为'conversations'
        if 'messages' in data:
            data['conversations'] = data.pop('messages')

        # 将修改后的字典添加到列表中
        combined_conversations.append(data)

# 将列表写入新的JSON文件
with open('AutoTx_finetuning_tool.json', 'w') as file:
    json.dump(combined_conversations, file, indent=4)

# 输出提示信息
print("Conversion completed. Data is saved in 'output.json'.")
