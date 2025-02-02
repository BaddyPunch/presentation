from django.http import JsonResponse, FileResponse, HttpResponseNotFound, Http404
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from .models import Presentation, Author
from django.conf import settings
import os


PRESENTATION_UPLOAD_PATH = os.path.join(settings.MEDIA_ROOT, 'presentations')
os.makedirs(PRESENTATION_UPLOAD_PATH, exist_ok=True)

IMAGE_UPLOAD_PATH = os.path.join(settings.MEDIA_ROOT, 'images')
os.makedirs(IMAGE_UPLOAD_PATH, exist_ok=True)


@csrf_exempt
def upload_presentation(request):

    """Функция загрузки файла, принимаемый из front, с загрузкой данных в базу."""

    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            department = request.POST.get('department')
            descript = request.POST.get('descript')
            author_name = request.POST.get('author')
            presentation_file = request.FILES.get('file')
            image_file = request.FILES.get('image')

            if not (title and department and author_name and presentation_file):
                return JsonResponse({'error': 'Missing required fields'}, status=400)

            author, created = Author.objects.get_or_create(fio=author_name)

            if created:
                print(f"Author '{author_name}' was created with ID {author.id}")
            else:
                print(f"Author '{author_name}' already exists with ID {author.id}")

            fs_file = FileSystemStorage(location=settings.PRESENTATION_UPLOAD_PATH)
            file_name = fs_file.save(presentation_file.name, presentation_file)
            file_url = os.path.join(PRESENTATION_UPLOAD_PATH, file_name)

            img_url = None
            if image_file:
                image_files = FileSystemStorage(location=settings.IMAGE_UPLOAD_PATH)
                image_name = image_files.save(image_file.name, image_file)
                img_url = os.path.join(settings.IMAGE_UPLOAD_PATH, image_name)

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


def download_presentation(request, presentation_id):

    """Функция скачивания файла."""

    try:
        presentation = Presentation.objects.get(id=presentation_id)
        file_path = os.path.join(settings.PRESENTATION_UPLOAD_PATH, presentation.file_name)

        if not os.path.exists(file_path):
            raise Http404("File not found")

        return FileResponse(open(file_path, "rb"), as_attachment=True, filename=presentation.file_name)

    except Presentation.DoesNotExist:
        return Http404("Презентация не найдена")


def get_presentations(request):

    """Функция для отображения данных для front."""

    presentations = Presentation.objects.values('id', 'title')
    return JsonResponse(list(presentations), safe=False)