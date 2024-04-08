import json
import os


def create_conversation(role, role_answer):
    """
    根据角色和答案创建一个新的会话字典。

    Parameters:
    - role: 角色名，例如 "gpt" 或 "human"。
    - role_answer: 角色的回答或消息内容。

    Returns:
    - 一个包含 'from' 和 'value' 键的字典。
    """
    return {
        "role": role,
        "content": role_answer
    }


def add_to_dataset(conversations, file_name, SYSTEM_PROMPT):
    if SYSTEM_PROMPT:
        share_gpt4_conversation_format = [{
            "conversations": conversations,
            "system": SYSTEM_PROMPT
        }]
    else:
        share_gpt4_conversation_format = [{
            "conversations": conversations
        }]

    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    existing_data.extend(share_gpt4_conversation_format)

    # 将更新后的数据列表写回文件
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=4)


