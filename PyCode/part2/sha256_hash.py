import hashlib

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# 示例调用
print(sha256_hash("Hello World"))
