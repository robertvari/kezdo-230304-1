status = 1000

if status == 100:
    print("Continue")
elif status == 200:
    print("OK")
elif status == 300:
    print("Multiple Choices")
elif status == 400:
    print("Bad Request")
elif status == 500:
    print("Internal Server Error")
else:
    print("This status is not handled :((")