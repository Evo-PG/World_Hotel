from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# проверка юсера
class MyUserManager(BaseUserManager):
    def create_user(self, phon_number, first_name, email, password=None):

        user = self.model(
            phon_number=phon_number,
            first_name=first_name,
            email=email
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phon_number, first_name, email, password=None):

        user = self.create_user(
            phon_number=phon_number,
            first_name=first_name,
            email=email
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user


# кастом юсер
class MyUser(AbstractBaseUser):
    email = models.EmailField(unique=True, verbose_name="Адрес электронной почты")
    first_name = models.CharField(max_length=223, verbose_name="Имя")
    last_name = models.CharField(max_length=223, blank=True, null=True, verbose_name="Фамилия")
    phon_number = models.CharField(max_length=13, verbose_name="Номер телефона")
    statys = models.PositiveSmallIntegerField(
        choices=(
            (1,"Обычный Пользователь"),
            (2,"Менежер"),
            (3,"Бугалтер")
        ),
        default=1
    )
    create_date = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()
    # обязательные филды
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'phon_number']

    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def full_name(self):
        if not self.last_name:
            check_last_name = ''
        else:
            check_last_name = self.last_name
        return f"{check_last_name} {self.first_name}"

    @property
    def is_staff(self):
        return self.is_admin
    # настройка
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

