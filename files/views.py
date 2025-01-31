import base64

from django.core.files.base import ContentFile
from django.http import JsonResponse, FileResponse, HttpResponseNotFound, Http404
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt

from .models import Presentation, Author
import os
from django.conf import settings
import os
import unicodedata
from django.utils.text import slugify


# @csrf_exempt
# def upload_presentation(request):
#     if request.method == 'POST' and request.FILES['file'] and request.FILES['image']:
#         # Получаем данные из формы
#         title = request.POST.get('title')
#         department = request.POST.get('department')
#         creation_date = request.POST.get('creation_date')
#         descript = request.POST.get('descript')
#         author_id = request.POST.get('authorID')
#         image = request.FILES['image_name']
#         file = request.FILES['file_name']
#
#         # Проверяем, существует ли автор в базе
#         try:
#             author = Author.objects.get(id=author_id)
#         except Author.DoesNotExist:
#             return JsonResponse({'error': 'Author not found'}, status=404)
#
#         # Сохраняем изображение
#         fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'images'))
#         image_name = fs.save(image.name, image)
#
#         # Сохраняем файл презентации
#         fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'presentations'))
#         file_name = fs.save(file.name, file)
#
#         # Создаём запись о презентации в базе данных
#         presentation = Presentation(
#             title=title,
#             department=department,
#             creation_date=creation_date,
#             descript=descript,
#             image_name=image_name,
#             file_name=file_name,
#             author=author
#         )
#         presentation.save()
#
#         return JsonResponse({'message': 'Presentation uploaded successfully!', 'file_name': file_name})
#
#     return JsonResponse({'error': 'Invalid request'}, status=400)
# @csrf_exempt
# def upload_presentation(request):
#     if request.method == 'POST':
#         print("POST Data:", request.POST.dict())  # Вывод POST-данных
#         print("FILES Data:", request.FILES.dict())  # Вывод FILES-данных
#         print("Headers:", request.headers)
#
#         # Проверяем наличие файлов
#         file = request.FILES.get('file')
#         image = request.FILES.get('image')
#
#         if not file or not image:
#             return JsonResponse({'error': 'File or image is missing'}, status=400)
#
#         # Получаем остальные данные из формы
#         title = request.POST.get('title')
#         department = request.POST.get('department')
#         creation_date = request.POST.get('creation_date')
#         descript = request.POST.get('descript')
#         author_id = request.POST.get('authorID')
#
#         # Проверяем наличие обязательных полей
#         if not title or not department or not creation_date or not descript or not author_id:
#             return JsonResponse({'error': 'Missing required fields'}, status=400)
#
#         # Проверяем, существует ли автор в базе
#         try:
#             author = Author.objects.get(id=author_id)
#         except Author.DoesNotExist:
#             return JsonResponse({'error': 'Author not found'}, status=404)
#
#         fs_image = FileSystemStorage(location=settings.IMAGE_UPLOAD_PATH)
#         image_name = fs_image.save(image.name, image)
#
#         fs_file = FileSystemStorage(location=settings.PRESENTATION_UPLOAD_PATH)
#         file_name = fs_file.save(file.name, file)
#
#         # Создаём запись о презентации в базе данных
#         presentation = Presentation(
#             title=title,
#             department=department,
#             creation_date=creation_date,
#             descript=descript,
#             image_name=image_name,
#             file_name=file_name,
#             author=author
#         )
#         presentation.save()
#
#         return JsonResponse({'message': 'Presentation uploaded successfully!', 'file_name': file_name})
#
#     return JsonResponse({'error': 'Invalid request method'}, status=405)


# @csrf_exempt
# def upload_presentation(request):
#     if request.method == 'POST':
#         try:
#             # Логирование входящих данных
#             print("POST Data:", request.POST.dict())
#             print("FILES Data:", request.FILES.dict())
#             print("Headers:", request.headers)
#             print("Author ID:", request.author_id)
#
#             # Получаем данные из POST
#             title = request.POST.get('title')
#             department = request.POST.get('department')
#             creation_date = request.POST.get('creation_date')
#             descript = request.POST.get('descript')
#             author_id = request.POST.get('authorID')
#             presentation_file = request.FILES.get('file')  # Файл презентации
#
#             # Проверяем обязательные данные
#             if not (title and department and creation_date and descript and author_id and presentation_file):
#                 return JsonResponse({'error': 'Missing required fields'}, status=400)
#
#             # Проверяем существование автора
#             try:
#                 author = Author.objects.get(id=author_id)
#             except Author.DoesNotExist:
#                 return JsonResponse({'error': 'Author not found'}, status=404)
#
#             # Сохраняем файл презентации
#             fs_file = FileSystemStorage(location=settings.PRESENTATION_UPLOAD_PATH)
#             file_name = fs_file.save(presentation_file.name, presentation_file)
#
#             # Создаём запись в базе данных
#             presentation = Presentation(
#                 title=title,
#                 department=department,
#                 creation_date=creation_date,
#                 descript=descript,
#                 file_name=file_name,
#                 author=author
#             )
#             presentation.save()
#
#             return JsonResponse({'message': 'Presentation uploaded successfully!', 'file_name': file_name})
#
#         except Exception as e:
#             return JsonResponse({'error': f'Unexpected server error: {str(e)}'}, status=500)
#
#     return JsonResponse({'error': 'Invalid request method'}, status=405)


# @csrf_exempt
# def upload_presentation(request):
#     if request.method == 'POST':
#         try:
#             # Логирование входящих данных
#             print("POST Data:", request.POST.dict())
#             print("FILES Data:", request.FILES.dict())
#             print("Headers:", request.headers)
#
#             # Получаем данные из POST
#             title = request.POST.get('title')
#             department = request.POST.get('department')
#             #creation_date = request.POST.get('creation_date')
#             descript = request.POST.get('descript')
#             author_name = request.POST.get('author')  # Получаем имя автора, не ID
#             presentation_file = request.FILES.get('file')  # Файл презентации
#
#             # Проверяем обязательные данные
#             if not (title and department and descript and author_name and presentation_file):
#                 return JsonResponse({'error': 'Missing required fields'}, status=400)
#
#             # Проверяем существование автора
#             try:
#                 author = Author.objects.get(fio=author_name)  # Ищем по имени автора
#             except Author.DoesNotExist:
#                 return JsonResponse({'error': 'Author not found'}, status=404)
#
#             # Сохраняем файл презентации
#             fs_file = FileSystemStorage(location=settings.PRESENTATION_UPLOAD_PATH)
#             file_name = fs_file.save(presentation_file.name, presentation_file)
#
#             # Создаём запись в базе данных
#             presentation = Presentation(
#                 title=title,
#                 department=department,
#
#                 descript=descript,
#                 file_name=file_name,
#                 author=author
#             )
#             presentation.save()
#
#             return JsonResponse({'message': 'Presentation uploaded successfully!', 'file_name': file_name})
#
#         except Exception as e:
#             return JsonResponse({'error': f'Unexpected server error: {str(e)}'}, status=500)
#
#     return JsonResponse({'error': 'Invalid request method'}, status=405)
PRESENTATION_UPLOAD_PATH = os.path.join(settings.MEDIA_ROOT, 'presentations')
os.makedirs(PRESENTATION_UPLOAD_PATH, exist_ok=True)

IMAGE_UPLOAD_PATH = os.path.join(settings.MEDIA_ROOT, 'images')
os.makedirs(IMAGE_UPLOAD_PATH, exist_ok=True)


@csrf_exempt
def upload_presentation(request):
    if request.method == 'POST':
        try:
            # Логирование входящих данных
            print("POST Data:", request.POST.dict())
            print("FILES Data:", request.FILES.dict())

            # Получаем данные из POST
            title = request.POST.get('title')
            department = request.POST.get('department')
            descript = request.POST.get('descript')
            author_name = request.POST.get('author')  # Имя автора
            presentation_file = request.FILES.get('file')
            image_file = request.FILES.get('image')


            # Проверяем обязательные данные
            if not (title and department and author_name and presentation_file):
                return JsonResponse({'error': 'Missing required fields'}, status=400)

            # Ищем или создаём автора
            author, created = Author.objects.get_or_create(fio=author_name)

            if created:
                print(f"Author '{author_name}' was created with ID {author.id}")
            else:
                print(f"Author '{author_name}' already exists with ID {author.id}")


            # Сохраняем файл презентации
            fs_file = FileSystemStorage(location=settings.PRESENTATION_UPLOAD_PATH)
            file_name = fs_file.save(presentation_file.name, presentation_file)
            file_url = os.path.join(PRESENTATION_UPLOAD_PATH, file_name)

            img_url = None
            if image_file:
                image_files = FileSystemStorage(location=settings.IMAGE_UPLOAD_PATH)
                image_name = image_files.save(image_file.name, image_file)
                img_url = os.path.join(settings.IMAGE_UPLOAD_PATH, image_name)

            # Создаём запись в базе данных
            presentation = Presentation.objects.create(
                title=title,
                department=department,
                descript=descript,
                file_name=file_url,
                image_name=img_url if img_url else '',
                author=author
            )

            return JsonResponse({'message': 'Presentation uploaded successfully!', 'file_name': file_name, 'image_name': img_url})

        except Exception as e:
            print("Error occurred:", str(e))
            return JsonResponse({'error': f'Unexpected server error: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


# def download_presentation(request, file_id):
#     try:
#         presentation = Presentation.objects.get(id=file_id)
#
#         # Получаем полный путь к файлу
#         file_path = os.path.join(settings.MEDIA_ROOT, 'presentations', presentation.file_name)
#
#         # Проверяем, существует ли файл
#         if not os.path.exists(file_path):
#             return JsonResponse({'error': 'File not found'}, status=404)
#
#         # Открываем файл для чтения
#         with open(file_path, 'rb') as f:
#             response = FileResponse(f, content_type='application/vnd.ms-powerpoint')
#             response['Content-Disposition'] = f'attachment; filename="{presentation.title}.ppt"'
#             return response
#
#     except Presentation.DoesNotExist:
#         return JsonResponse({'error': 'Presentation not found'}, status=404)


def download_presentation(request, presentation_id):
    try:
        # Ищем презентацию по ID
        presentation = Presentation.objects.get(id=presentation_id)
        file_path = os.path.join(settings.PRESENTATION_UPLOAD_PATH, presentation.file_name)

        # Проверяем, существует ли файл
        if not os.path.exists(file_path):
            raise Http404("File not found")

        # Отправляем файл пользователю
        return FileResponse(open(file_path, "rb"), as_attachment=True, filename=presentation.file_name)

    except Presentation.DoesNotExist:
        return Http404("Презентация не найдена")


def get_presentations(request):

    presentations = Presentation.objects.values('id', 'title')
    return JsonResponse(list(presentations), safe=False)