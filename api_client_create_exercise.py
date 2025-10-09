from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict  # Импорт клиента курсов
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict  # Импорт клиента упражнений
from testdata.files.files_client import get_files_client, CreateFileRequestDict  # Импорт клиента файлов
from clients.private_http_builder import AuthenticationUserDict  # Импорт словаря аутентификации пользователя
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict  # Импорт публичного клиента пользователей
from tools.fakers import get_random_email  # Импорт генератора случайного email

def main() -> None:
    """
    Главная функция для выполнения последовательности создания.
    """
    public_users_client = get_public_users_client()

    # Создать пользователя
    create_user_request: CreateUserRequestDict = CreateUserRequestDict(
        email=get_random_email(),
        password="string",
        lastName="string",
        firstName="string",
        middleName="string"
    )
    create_user_response = public_users_client.create_user(create_user_request)

    # Инициализировать клиенты
    authentication_user: AuthenticationUserDict = AuthenticationUserDict(
        email=create_user_request['email'],
        password=create_user_request['password']
    )
    files_client = get_files_client(authentication_user)
    courses_client = get_courses_client(authentication_user)
    exercises_client = get_exercises_client(authentication_user)

    # Загрузить файл
    create_file_request: CreateFileRequestDict = CreateFileRequestDict(
        filename="image.png",
        directory="courses",
        upload_file="./testdata/files/image.png"
    )
    create_file_response = files_client.create_file(create_file_request)
    print(f"Create file data: {create_file_response}")

    # Создать курс
    create_course_request: CreateCourseRequestDict = CreateCourseRequestDict(
        title="Python",
        maxScore=100,
        minScore=10,
        description="Python API course",
        estimatedTime="2 weeks",
        previewFileId=create_file_response['file']['id'],
        createdByUserId=create_user_response['user']['id']
    )
    create_course_response = courses_client.create_course(create_course_request)
    print(f"Create course data: {create_course_response}")

    # Создать упражнение
    create_exercise_request: CreateExerciseRequestDict = CreateExerciseRequestDict(
        title="Basic Python Exercise",
        courseId=create_course_response['course']['id'],
        maxScore=50,
        minScore=5,
        orderIndex=1,
        description="Introduction to Python basics",
        estimatedTime="1 hour"
    )
    create_exercise_response = exercises_client.create_exercise(create_exercise_request)
    print(f"Create exercise data: {create_exercise_response}")

if __name__ == "__main__":
    main()