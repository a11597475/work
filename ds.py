import random
import re
from collections import defaultdict, Counter

class MicroDeepSeek:
    def __init__(self, n=2):
        self.n = n                     # n-gram 的阶数，n=2 即 bigram
        self.model = defaultdict(Counter)   # 存储 (前缀) -> {下一个词: 计数}
        self.start_tokens = []          # 记录所有可能的起始前缀（用于生成新句子）

    def train(self, text):
        """训练：将文本分词，构建 n-gram 转移计数"""
        # 简单分句：按标点切分
        sentences = re.split(r'[。！？.!?]', text)
        for sent in sentences:
            words = self._tokenize(sent)
            if len(words) < self.n:
                continue
            # 添加起始标记（用于生成时从开头开始）
            prefix = tuple(words[:self.n-1])
            self.start_tokens.append(prefix)
            # 统计所有 n-gram
            for i in range(len(words) - self.n + 1):
                prefix = tuple(words[i:i+self.n-1])
                next_word = words[i+self.n-1]
                self.model[prefix][next_word] += 1

    def _tokenize(self, text):
        """极简分词：按空格和标点拆分（实际是保留词和标点）"""
        # 将标点单独作为词，便于学习回复结构
        text = re.sub(r'([，。！？,.!?])', r' \1 ', text)
        return [w for w in text.split() if w.strip()]

    def generate(self, prompt, max_length=20, temperature=0.8):
        """根据用户输入的 prompt 生成回复"""
        # 对 prompt 分词，取最后 n-1 个词作为初始前缀
        prompt_words = self._tokenize(prompt)
        if len(prompt_words) < self.n - 1:
            # 如果 prompt 太短，随机选一个训练时见过的起始前缀
            prefix = random.choice(self.start_tokens) if self.start_tokens else None
            if not prefix:
                return "（我还没学过任何对话，请先用 train() 教我一些句子吧！）"
        else:
            prefix = tuple(prompt_words[-(self.n-1):])

        output = list(prefix)
        for _ in range(max_length):
            # 如果当前前缀不在模型中，尝试缩短前缀或停止
            if prefix not in self.model:
                # 尝试去掉最旧的一个词
                if len(prefix) > 0:
                    prefix = prefix[1:]
                    continue
                else:
                    break
            # 根据概率分布采样下一个词
            candidates = self.model[prefix]
            if not candidates:
                break
            # 温度调节：越低越保守，越高越随机
            total = sum(candidates.values())
            probs = {w: (c/total) ** (1.0/temperature) for w, c in candidates.items()}
            total_prob = sum(probs.values())
            probs = {w: p/total_prob for w, p in probs.items()}
            next_word = random.choices(list(probs.keys()), weights=probs.values())[0]
            output.append(next_word)
            # 更新前缀：滑动窗口
            prefix = tuple(output[-(self.n-1):])
            # 遇到句尾标点（。！？.!?）可提前结束
            if next_word in ['。', '！', '？', '.', '!', '?']:
                break
        # 将生成的词列表拼接成字符串
        return ''.join(output).replace(' ,', ',').replace(' .', '.').replace(' ?', '?').replace(' !', '!')

    def chat(self):
        """命令行交互"""
        print("微型 DeepSeek 已启动。输入 'quit' 退出，输入 'train: ' 开头来追加训练文本。")
        while True:
            user_input = input("\n你: ")
            if user_input.lower() == 'quit':
                break
            if user_input.startswith('train:'):
                new_text = user_input[6:].strip()
                self.train(new_text)
                print(f"已学习：{new_text[:30]}...")
                continue
            reply = self.generate(user_input)
            print(f"微DeepSeek: {reply}")


# 示例：用一小段对话数据训练它（你可以手动添加或交互时用 train: 命令）
example_dialogue = """
用户: 你好
助手: 你好呀！有什么可以帮你的吗？
用户: 你的原理是什么
助手: 我通过统计词与词之间的出现规律来生成回复，是一种 n-gram 语言模型。
用户: 你懂代码吗
助手: 懂一点，我可以帮你写简单的 Python 程序。
"""

if __name__ == "__main__":
    bot = MicroDeepSeek(n=2)   # 使用 Bigram
    bot.train(example_dialogue)
    print("=== 微型模型已用示例对话训练完成 ===\n")
    bot.chat()