from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="название"
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категориии"



class HotelRoom(models.Model):
    number_room_hotel = models.PositiveSmallIntegerField(
        verbose_name="число номера"
    )
    number_bets = models.PositiveSmallIntegerField(
        verbose_name="число краватей"
    )
    number_withdrawals = models.PositiveSmallIntegerField(
        verbose_name="число ванн"
    )
    cover = models.ImageField(
        upload_to="media/hotel_cover",
        verbose_name="иконка"
    )
    photo_hotel_room = models.ImageField(
        upload_to="media/photo_hotel_room",
        verbose_name="фото номкра"
    )
    description = models.TextField(
        verbose_name="описание"
    )
    prise = models.PositiveSmallIntegerField(
        verbose_name="цена"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="категория"
    )
    number_room = models.PositiveSmallIntegerField(
        verbose_name="число комнат"
    )
    status = models.PositiveSmallIntegerField(
        choices=(
            (1,"Свободен"),
            (2,"Занят"),
        )
    )


    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Намера"


class Services(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Название"
    )
    smol_description = models.CharField(
        max_length=200,
        verbose_name="краткое описвнме"
    )
    description = models.TextField(
        verbose_name="полное описание"
    )

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"
