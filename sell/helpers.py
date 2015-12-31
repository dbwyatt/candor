from datetime import datetime

def save_and_return_uploaded_image(img, user_id):
    file_name = datetime.now().strftime('%Y-%m-%d-%H-%M-%S_') + str(user_id) + '_' + str(img)
    with open('post_images/' + file_name, 'wb+') as destination:
        for chunk in img.chunks():
            destination.write(chunk)
    return file_name
