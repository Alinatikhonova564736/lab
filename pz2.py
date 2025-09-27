import copy

a = int(input())
b = float(input())
print(a + b, a - b, a * b, a / b)

a = int(input())
pi = 3.141596
c = float(pi*(a**2))
print('c = {:.2f}'.format(c))

text = " Hello, Python! "
text1 = text.strip()
text2 = text1.replace('!', '?')
text3 = text2.upper()
print(text3)

num = [7, 2, 5]
num.append(4)
num.insert(1,10)
num.extend([1, 1, 1])
num.remove(7)
num.pop()
num.sort()
num.reverse()
print (num.count(2))
print (num.index(1))
num1 = num.copy()
num2 = copy.deepcopy(num)
num.clear()
print (num)
print (num1)
print (num2)

t = (1, 2, 3)
t1 = (4,5)
t2 = t + t1
print(t2)
print(t2.count(3))
print(t2.index(4))
print(t)

val = [3, 1, 3, 2, 1, 5, 2]
un_val = set(val)
print(un_val, len(un_val))
other = {2, 4, 5}
print(un_val&other,un_val|other)
print(un_val-other, other-un_val)

scores = {"Alice": 85, "Bob": 90}
scores["Charlie"] = 78
scores["Bob"] = 95
print(scores.get("Dave"))
print(scores.get("Bob"))
scores.pop("Alice")
print(scores)
print(scores.keys(), scores.values())

text = """
    Python is a powerful programming language. 
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""
t = text.strip().lower()
t = t.replace("!", ".")
sentences = [s.strip() for s in t.split(".") if s.strip()]
print("Предложения:", sentences)
first = sentences[0]
words = first.split()
print("Слова первого предложения:", words)
print("Кол-во 'python':", words.count("python"))
print("startswith('python'):", first.startswith("python"))
print("endswith('language'):", first.endswith("language"))
print("Общее кол-во символов:", len(t))
print("Кол-во букв 'a':", t.count("a"))
print("Индекс слова 'data':", t.find("data"))

words_all = t.split()
print("Через '-':", "-".join(words_all))
freq = {}

freq = {}
for w in words_all:
    freq[w] = freq.get(w, 0) + 1
print("Частоты слов:", freq)
import string
def clean_text(txt):
    txt = txt.lower().strip()
    allowed = string.ascii_lowercase + " "
    cleaned = "".join(ch if ch in allowed else " " for ch in txt)
    return " ".join(cleaned.split())

print("Очищенный текст:", clean_text(text))