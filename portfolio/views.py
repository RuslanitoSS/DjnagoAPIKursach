from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Student, Project, Event
from .serializers import StudentSerializer, ProjectSerializer, EventSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Поиск без icontains потому что sqlite не может сравнивать русские символы разных регистров Р !== р

    @action(methods=['GET'], detail=False)
    def search(self, request):
        query = request.query_params.get('q', '').strip().lower()  
        if query:
            students = self.get_queryset()
            students = [
                student for student in students
                if query in student.first_name.lower() or query in student.last_name.lower()
            ]
        else:
            students = self.get_queryset()

        serializer = self.get_serializer(students, many=True)
        return Response(serializer.data)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(methods=['GET'], detail=True)
    def students(self, request, pk=None):
        project = self.get_object()
        students = project.students.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(methods=['GET'], detail=True)
    def students(self, request, pk=None):
        event = self.get_object()
        students = event.students.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    


""" 
class StudentDetailView(APIView):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

class StudentListView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        students = Student.objects.all()
        if query:
            students = students.filter(
                Q(first_name__icontains=query) | 
                Q(last_name__icontains=query) | 
                Q(university__icontains=query) | 
                Q(faculty__icontains=query)
            )
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(students, request)
        student_data = StudentSerializer(result_page, many=True).data
        return render(request, 'student_list.html', {'students': student_data}) """
