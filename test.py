import unittest
import requests
test = 5
class TestStudentDetailsAPI(unittest.TestCase):
    student_id = None 
    def setUp(self):
        self.url = "http://127.0.0.1:8000/"
        self.student_data = {
            "name": "Foo",
            "email": "foo@example.com",
            "age": 20,
            "phone": 1234567890
        }
  #Need to change the numbers

    def test_post_studentdetails(self):
        response = requests.post(self.url + 'AddStudent', json=self.student_data)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        TestStudentDetailsAPI.student_id = response_data['student_id']['id']


    def test_getALLstudentdetails(self):
        response = requests.get(self.url + 'GetAllStudents')
        self.assertEqual(response.status_code, 200)
        response_data = response.json()


    def test_GetStudenbyid(self):
        if not hasattr(self, 'id'):
            self.skipTest("No student ID available for test_GetStudent")
        url = self.url + f'GetStudent?id={TestStudentDetailsAPI.student_id}'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200, f"Expected status code 200 but got {response.status_code}")
        response_data = response.json()

    def test_Update(self):
        url = self.url + 'v2/' + f'UpdateStudent?id={TestStudentDetailsAPI.student_id}'
        response = requests.patch(url,json={'name': 'Ganesh Gaitonde', 'email': 'Gopalmat@gmail.com', 'age': 0, 'phone': 0})
        self.assertEqual(response.status_code, 200, f"Expected status code 200 but got {response.status_code}")
        response_data = response.json()

    def test_DeleteStudent(self):
        if not hasattr(self, 'id'):
            self.skipTest("No student ID available for test_GetStudent")
        url = self.url + 'v2/' + f'DeleteStudent?id={TestStudentDetailsAPI.student_id}'
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200, f"Expected status code 200 but got {response.status_code}")
        response_data = response.json()




if __name__ == "__main__":
   suite = unittest.TestSuite()
   suite.addTest(TestStudentDetailsAPI('test_post_studentdetails'))
   suite.addTest(TestStudentDetailsAPI('test_GetStudenbyid'))
   suite.addTest(TestStudentDetailsAPI('test_getALLstudentdetails'))
   suite.addTest(TestStudentDetailsAPI('test_Update'))
   suite.addTest(TestStudentDetailsAPI('test_DeleteStudent'))
   runner = unittest.TextTestRunner()
   runner.run(suite)
