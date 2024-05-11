from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import CustomUser
# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name


class Authors(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'authors'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Languages(models.Model):
    language = models.CharField(max_length=3)

    class Meta:
        db_table = 'languages'

    def __str__(self):
        return self.language


class Books(models.Model):
    book_category = models.ForeignKey(to='Categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='library/', default='default_img/default_book_img.png')
    pages = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    language = models.ForeignKey(to="Languages", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return f"{self.book_category.name} {self.name}"


class BookAuthor(models.Model):
    author_name = models.ForeignKey(to="Authors", on_delete=models.CASCADE)
    book_name = models.ForeignKey(to="Books", on_delete=models.CASCADE)

    class Meta:
        db_table = 'book_author'

    def __str__(self):
        return f"{self.author_name}"


class Reviews(models.Model):
    comments = models.CharField(max_length=300)
    star_given = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(5),
            MaxValueValidator(0)
        ]
    )
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews'

    def __str__(self):
        return f"{self.star_given} {self.user.username} {self.book.name}"