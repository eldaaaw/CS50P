mediaType = input("Enter the file name: ").lower().strip()

if ".gif" in mediaType:
    print("image/gif")
elif ".jpg" in mediaType or ".jpeg" in mediaType:
    print("image/jpeg")
elif ".png" in mediaType:
    print("image/png")
elif ".pdf" in mediaType :
    print("application/pdf")
elif ".txt" in mediaType:
    print("text/plain")
elif ".zip" in mediaType:
    print("application/zip")
else:
    print("application/octet-stream")
