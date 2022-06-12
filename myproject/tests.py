from django.test import TestCase
from .models import *


class PosTestClass(TestCase):
    '''
    This is a class that perform unittest on the Post Model.
    '''
    
    def setUp(self):
        self.post = Post(id=1,title='new post',image='images/smoke.jpeg',description='the best of the best', link='https://link.com/',user_id=3)

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def test_save_method(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post)>0)
    
    def test_delete_method(self):
        self.post.save_post()
        self.post.delete_post()
        post = Post.objects.all()
        self.assertTrue(len(post) is 0)

    def tearDown(self):
        Post.objects.all().delete() 

class ProfileTestClass(TestCase):
    '''
    This is a class that perform unittest on the Profile Model.
    '''
    
    def setUp(self):
        self.profile = Profile(First_Name='paulette',Last_Name='nereah',Email='paulettenereah3@gmail.com', bio='test bio',user_id=3)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
        
    def test_save_method(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)

    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) is 0)
                        
    def test_update_method(self):
        self.profile.save_profile()
        new_name = 'Nereahp' 
        update = self.profile.update_name(self.profile.user_id,new_name)
        self.assertEqual(update,new_name)

    def test_single_project_method(self):
        self.profile.save_profile()
        profile = self.profile.get_user_profile(self.profile.user_id)
        self.assertTrue(profile.user_id  is 3)
        
        
        
        
    def tearDown(self):
        Profile.objects.all().delete()
