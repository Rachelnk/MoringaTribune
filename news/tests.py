from django.test import TestCase
import datetime as dt 

# Create your tests here.
from .models import Editor, Article, tags

class EditorTestClass(TestCase):

    # Set up method that allows us to create an instance of the Editor class before every test
    def setUp(self):
        self.ray= Editor(first_name = 'ray', last_name ='kiarie', email ='ray@moringaschool.com')

    # Testing an instance of the Editor class before every test
    def test_instance(self):
        self.assertTrue(isinstance(self.ray,Editor))

        # Testing Save Method
    def test_save_method(self):
        self.ray.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class ArticleTestClass (TestCase):
    
    def setUp(self):

        # Creating a new editor and saving it
        self.ray = Editor ( first_name = 'Ray', last_name = 'Kiarie', email = 'kiarie@gmail.com')
        self.ray.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        # Creating a new tag and saving it
        self.new_article = Article( title = 'Code', post = 'coding is fun', editor = self.ray)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)





