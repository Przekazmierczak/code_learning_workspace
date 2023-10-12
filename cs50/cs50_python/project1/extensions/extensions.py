name = input("File name: ").lower()

if name.endswith(".gif"):
    print("image/gid")
elif name.endswith(".jpg") or name.endswith(".jpeg"):
    print("image/jpeg")
elif name.endswith(".png"):
    print("image/png")
elif name.endswith(".pdf"):
    print("application/pdf")
elif name.endswith(".txt"):
    print("text/plain")
elif name.endswith(".zip"):
    print("application/zip")