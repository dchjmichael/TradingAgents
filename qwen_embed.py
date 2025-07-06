from llama_index.embeddings.dashscope import DashScopeEmbedding

import os
# os.environ["DASHSCOPE_API_KEY"] = "sk-7506130ea6d14edeb0d21447feb3582e"

# 初始化 Embedding 模型
embedder = DashScopeEmbedding(
    model_name="text-embedding-v2",
    api_key= "sk-7506130ea6d14edeb0d21447feb3582e"
)
text_to_embedding = ["风急天高猿啸哀", "渚清沙白鸟飞回", "无边落木萧萧下", "不尽长江滚滚来"]
# 调用 Embedding 模型
result_embeddings = embedder.get_text_embedding_batch(text_to_embedding)
# 显示 Embedding 后结果
for index, embedding in enumerate(result_embeddings):
    print("Dimension of embeddings: %s" % len(embedding))
    print(
        "Input: %s, embedding is: %s"
        % (text_to_embedding[index], embedding[:5])
    )