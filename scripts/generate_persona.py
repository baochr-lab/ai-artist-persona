import os
from anthropic import Anthropic

# 从环境变量读取 API 密钥
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def generate(name, era, works):
    """生成单个人物的人格定义"""
    
    prompt = f"""为艺术史人物生成人格定义，严格按四层结构输出：

人物：{name}（{era}）
代表作品：{works}

要求：
1. 语言风格层：分析其说话方式
2. 世界观层：3个核心主张，必须引用具体作品
3. 情绪性格层：基线情绪和应激反应  
4. 关系网络层：对2-3个同时代人物的评价

请用中文输出。"""

    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text
    except Exception as e:
        return f"生成失败：{str(e)}"

# 测试运行
if __name__ == "__main__":
    print("=" * 50)
    print("开始生成：马塞尔·杜尚")
    print("=" * 50)
    
    result = generate(
        name="马塞尔·杜尚",
        era="1887-1968",
        works="《泉》(1917)、《下楼梯的裸女》(1912)"
    )
    
    print(result)
    print("\n" + "=" * 50)
    print("生成完成！")
