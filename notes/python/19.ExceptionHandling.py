import json

try:
    f = open("/home/yashwanth/projects/daily-progress/notes/python/17.1.JsonFile.json", 'r')
    # var = bvar
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("The exception handling is working")