import subprocess
import random

# 定义命令参数列表，包括新增的变体
commands = [
    "Send 1 ETH to vitalik.eth",
    "Buy 100 USDC with ETH",
    "Swap ETH to 0.05 WBTC, then swap WBTC to 1000 USDC, and finally send 50 USDC to vitalik.eth",
    "Send 0.5 ETH to vitalik.eth",
    "Swap 2 ETH for DAI, then send 500 DAI to vitalik.eth",
    "Buy 50 LINK with ETH, then send 25 LINK to vitalik.eth",
    "Swap ETH to 0.1 WBTC, then swap WBTC to 5000 USDC, and finally send 100 USDC to vitalik.eth",
    "Swap 1.5 ETH for UNI, then send 200 UNI to vitalik.eth",
    "Buy 200 COMP with ETH, then send 50 COMP to vitalik.eth",
    "Send 2 ETH to vitalik.eth",
    "Swap ETH to 0.03 WBTC, then use WBTC to buy 1000 USDC, and finally send 500 USDC to vitalik.eth",
]

# 循环执行200次
for _ in range(200):
    # 从命令列表中随机选择一个命令
    command_to_run = random.choice(commands)

    # 构建完整的命令字符串
    full_command = f"poetry run ask --prompt \"{command_to_run}\""

    # 使用subprocess执行命令
    try:
        subprocess.run(full_command, check=True, shell=True)
        print(f"成功执行命令: {full_command}")
    except subprocess.CalledProcessError as e:
        print(f"执行命令失败: {e}")
