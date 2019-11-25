from django.test import TestCase
from .models import Project,Profile,Rating

class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.award= Project()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.award,Project))

    # Testing Save Method
    def test_save_method(self):
        self.award.save_image()
        description= Project.objects.all()
        self.assertTrue(len(description) > 0)

        
       
class RatingTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.award= Rating()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.award,Rating))

   
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.award= Profile( )
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.award,Profile))

    
