import grpc
import concurrent.futures as futures
from course_service_pb2 import GetCourseRequest, GetCourseResponse
from course_service_pb2_grpc import CourseServiceServicer, add_CourseServiceServicer_to_server

class CourseService(CourseServiceServicer):
    def GetCourse(self, request, context):
        return GetCourseResponse(
            course_id=request.course_id,
            title="Автотесты API",
            description="Будем изучать написание API автотестов"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_CourseServiceServicer_to_server(CourseService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC сервер CourseService запущен на порту 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
