import grpc
from course_service_pb2 import GetCourseRequest
from course_service_pb2_grpc import CourseServiceStub

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = CourseServiceStub(channel)
        response = stub.GetCourse(GetCourseRequest(course_id='api-course'))
        print(response)

if __name__ == '__main__':
    run()
