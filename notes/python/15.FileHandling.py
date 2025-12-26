# with open('/home/yashwanth/projects/daily-progress/notes/python/test.txt', 'r') as f:
#     pass


# print(f.mode)
# print(f.closed)
# f = open("/home/yashwanth/projects/daily-progress/notes/python/test.txt", 'r')
# print(f.read())

# with open('/home/yashwanth/projects/daily-progress/notes/python/test.txt', 'r') as f:
    # for line in f:
    #     print(line, end = '')

    # f_contents = f.read(100)
    # print(f_contents)

    # f_contents = f.readlines()
    # print(f_contents)

    # f_contents = f.readline()
    # print(f_contents,end = '')

    # f_contents = f.readline()
    # print(f_contents,end = '')

# with open('/home/yashwanth/projects/daily-progress/notes/python/test.txt', 'r') as f:
#         size_to_read = 10
#         f_contents = f.read(size_to_read)
#         while len(f_contents) > 0:
#                 print(f_contents, end = '*')
#                 f_contents = f.read(size_to_read)

# with open ("/home/yashwanth/projects/daily-progress/notes/python/test2.txt", "w") as f:
#     f.write("hello there")

# with open ("/home/yashwanth/projects/daily-progress/notes/python/test2.txt", "r") as f:
#     f_contents = f.read()
#     print(f_contents)

# with open('/home/yashwanth/projects/daily-progress/notes/python/test.txt','r') as rf:
#     with open ('/home/yashwanth/projects/daily-progress/notes/python/test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)
#         print()

# with open('/home/yashwanth/Downloads/t5.jpg','rb') as rf:
#     with open ('/home/yashwanth/Downloads/Yashwanth&Vishaali', 'wb') as wf:
#         for line in rf:
#             wf.write(line)

with open('/home/yashwanth/Downloads/t5.jpg','rb') as rf:
    with open ('/home/yashwanth/Downloads/Yashwanth&Vishaali', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)