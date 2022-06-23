from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
# from django.db.models import Sum, F


class UserProfileManager(BaseUserManager):  # Kjo klase menaxhon profilet dhe krijon superuserin
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Every user must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.id_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):  # Klasa ruan ne databaze userat
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)  # Perdoret email unik me gjatesi karakteresh 255
    name = models.CharField(max_length=255)  # Emri i perdoruesit me gjatesi 255
    is_active = models.BooleanField(default=True)  # Fushe Booleane ku vlera default eshte 1
    is_staff = models.BooleanField(default=True)  # Keto dy fusha percaktojne nese useri eshte staff apo aktiv
    # ! Modifiko keto te fundit

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # ! Modifiko fushat e databazes te cilat duhen plotesuar patjeter

    def get_full_name(self):
        """Retrieve full name for user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        return self.email


class ProfileFeedItem(models.Model):  # Kjo klase lejon modifikimet e profileve
    """Profile status update"""
    user_profile = models.ForeignKey(  # Profili eshte Foreign Key
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE  # Kur fshihet useri, fshihet ne tere tabelat e databazes
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField()  # Percakton daten kur krijohet useri

    def __str__(self):
        """Return the model as a string"""
        return self.status_text


# Ketu mbaron krijimi dhe menaxhimi i userave te ndryshem. Ne vijim do ndertojme tabelat e tjera te databazes.
class Student(models.Model):
    st_ID = models.IntegerField(primary_key=True)
    st_name = models.CharField(max_length=55)
    st_family_name = models.CharField(max_length=55)
    st_course = models.CharField(max_length=55)
    st_undergraduate = models.BooleanField(default=True)
    st_year = models.IntegerField(default=1)
    st_age = models.IntegerField(default=18)
    st_birthdate = models.DateTimeField(auto_now_add=True)
    st_contact_number = models.IntegerField(blank=False)
    st_email = models.EmailField(max_length=30, unique=True)

    def __str__(self):
        return f'{self.st_name}, {self.st_family_name}, {self.st_course}, {self.st_year}, {self.st_email}'


class Book(models.Model):
    book_title = models.CharField(max_length=100, blank=False)
    book_edition = models.IntegerField(default=1)
    book_author = models.CharField(max_length=20, blank=False)
    book_publisher = models.CharField(max_length=30)
    book_copies = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return f'{self.book_title}, {self.book_author}, {self.book_copies}'


class Users(models.Model):
    staff_ID = models.IntegerField(primary_key=True)
    staff_name = models.CharField(max_length=15, blank=False)
    staff_family_name = models.CharField(max_length=15, blank=False)
    staff_contact = models.IntegerField(blank=False)
    staff_email = models.EmailField(max_length=30, unique=True, blank=False)
    staff_type = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.staff_ID}, {self.staff_name}, {self.staff_email}'


class BookType(models.Model):
    book_ID = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_type = models.CharField(max_length=20, blank=False)

    REQUIRED_FIELDS = ['book_type']

    def booktype(self):
        return self.book_type

    def __str__(self):
        return f'{self.book_ID}, {self.book_type}'


class Borrowers(models.Model):
    book_ID = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_title = models.CharField(max_length=100)
    st_ID = models.ForeignKey(Student, on_delete=models.CASCADE)
    release_date = models.DateTimeField(auto_now_add=True)
    return_date = models.IntegerField(default=30)

    def __str__(self):
        return f'{self.st_ID}, {self.borrow_title}, {self.release_date}, {self.return_date}'
