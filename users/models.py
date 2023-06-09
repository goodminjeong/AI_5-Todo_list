from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import MinValueValidator, MaxValueValidator


class UserManager(BaseUserManager):
    def create_user(self, email, name, gender, age, introduction, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            gender=gender,
            age=age,
            introduction=introduction,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password,
            name="관리자",
            gender="non-choice",
            age="0",
            introduction="관리자 계정입니다"
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    GENDER_CHOICES = (
        ("male", "남자"),
        ("female", "여자"),
        ("unknown", "모름"),
        ("non-choice", "선택하지 않음")
    )

    email = models.EmailField("이메일", max_length=255, unique=True)
    name = models.CharField("이름", max_length=20)
    gender = models.CharField("성별", max_length=20, choices=GENDER_CHOICES)
    age = models.IntegerField(
        "나이", validators=[MinValueValidator(0), MaxValueValidator(120)])
    introduction = models.TextField("자기소개")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
