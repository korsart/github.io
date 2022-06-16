from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)

class UserManager(BaseUserManager):
    """Менеджер моделей для модели пользователя без поля имени пользователя."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Создание и сохранение пользователя с указанным адресом электронной почты и паролем."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Создание и сохранение обычного пользователя с указанным адресом электронной почты и паролем."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("role", User.USER)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Создание и сохранение администратора с указанным адресом электронной почты и паролем."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", User.SUPER_USER)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name='Почта', unique=True)
    name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Имя пользователя"
    )
    phone_number = models.CharField(
        default=None,
        null=True,
        unique=False,
        max_length=18,
        verbose_name="Номер телефона",
    )
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    USER = "user"
    SUPER_USER = "admin"
    MANAGER = 'manager'
    ROLE = \
        [
            (SUPER_USER, "Админ"),
            (USER, 'Пользователь'),
            (MANAGER, 'менеджер')
        ]
    role = models.CharField(
        max_length=32,
        choices=ROLE,
        default=None,
        null=True,  # some list of choices
        verbose_name="Роль",
    )
    objects = UserManager()

    class Meta:
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"
        ordering = ("id",)

    def __str__(self):
        return f"{self.name} {self.email}"


class Tegs(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тег')

    def __str__(self):
        return self.title

class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название книги')
    description = models.CharField(max_length=300, verbose_name='Описание книги')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    author = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    teg = models.ManyToManyField(Tegs)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title