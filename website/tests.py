from django.test import TestCase
from django.contrib.auth.models import User
from forum.models import ForumCategory, ForumThread, ForumPost 

class ForumModelTest(TestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='password')
        
        # Create category
        self.category = ForumCategory.objects.create(
            title="General Discussion", 
            description="Talk about anything here"
        )
        
        # Create thread
        self.thread = ForumThread.objects.create(
            category=self.category,
            title="Welcome to the Server",
            creator=self.user
        )

    def test_forum_models_str(self):
        """Check if __str__ returns correct values"""
        self.assertEqual(str(self.category), "General Discussion")
        self.assertEqual(str(self.thread), "Welcome to the Server")
        
        # Create post and check its __str__
        post = ForumPost.objects.create(
            thread=self.thread,
            author=self.user,
            content="Hello everyone!"
        )
        self.assertTrue("testuser" in str(post))
        self.assertTrue("Welcome" in str(post))

    def test_thread_count(self):
        """Check if thread is linked to category and exists in DB"""
        self.assertEqual(ForumThread.objects.count(), 1)
        self.assertEqual(self.category.threads.count(), 1)

    def test_post_creation(self):
        """Check post creation"""
        ForumPost.objects.create(
            thread=self.thread,
            author=self.user,
            content="This is a test post"
        )
        self.assertEqual(self.thread.posts.count(), 1)
        self.assertEqual(self.thread.posts.first().content, "This is a test post")