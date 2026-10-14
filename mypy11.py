a = {"name":"yuanhaoran","age":18}
print(a['name'])
print(a.get("hello",18))
print(a.items())
print(a.keys())
print(a.values())
print("name" in a)
a["job"]="python"
print(a)
b={"interest":"python","dream":"engeneer"}
a.update(b)
print(a)
print(b)
print(a.pop("name"))
print(a.popitem())
