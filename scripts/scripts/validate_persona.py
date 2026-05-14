from pathlib import Path

def check(file_path):
    """检查 persona.md 是否结构完整"""
    
    # 检查文件是否存在
    if not Path(file_path).exists():
        print(f"❌ 文件不存在：{file_path}")
        return False
    
    with open(file_path, encoding='utf-8') as f:
        content = f.read()
    
    # 必须包含的四个层次
    checks = ["语言风格", "世界观", "情绪性格", "关系网络"]
    missing = [c for c in checks if c not in content]
    
    # 检查作品引用（《》或""）
    has_quotes = '《' in content or '"' in content
    
    if missing:
        print(f"❌ {file_path.name} 缺少层次：{', '.join(missing)}")
        return False
    if not has_quotes:
        print(f"⚠️ {file_path.name} 没有引用具体作品")
        return False
    
    print(f"✅ {file_path.name} 验证通过")
    return True

def check_all():
    """检查所有人物文件"""
    personas_dir = Path("personas")
    
    if not personas_dir.exists():
        print("⚠️ personas 文件夹不存在，请先生成人物")
        return
    
    files = list(personas_dir.glob("*/persona.md"))
    
    if not files:
        print("⚠️ 没有找到任何人物文件")
        return
    
    print(f"找到 {len(files)} 个人物文件，开始验证...\n")
    
    passed = 0
    for f in files:
        if check(f):
            passed += 1
    
    print(f"\n{'='*50}")
    print(f"验证完成：{passed}/{len(files)} 通过")

if __name__ == "__main__":
    check_all()
