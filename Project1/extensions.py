def get_media_type(file_name):
    file_name_lower = file_name.strip().lower()

    if file_name_lower.endswith(
        (".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip", ".PDF")
    ):
        return get_media_type_by_extension(file_name_lower)
    else:
        return "application/octet-stream"


def get_media_type_by_extension(file_name_lower):
    if file_name_lower.endswith(".gif"):
        return "image/gif"
    elif file_name_lower.endswith((".jpg", ".jpeg")):
        return "image/jpeg"
    elif file_name_lower.endswith(".png"):
        return "image/png"
    elif file_name_lower.endswith((".pdf", ".PDF")):
        return "application/pdf"
    elif file_name_lower.endswith(".txt"):
        return "text/plain"
    elif file_name_lower.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"


if __name__ == "__main__":
    file_name = input("File Name: ")
    media_type = get_media_type(file_name)
    print(f"{media_type}")
