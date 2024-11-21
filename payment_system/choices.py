from django.db import models


class PaymentApplicationStatysEnum(models.TextChoices):
    IN_PROGRESS = "in_progress", "В обработке"
    DENIED = "denied", "Отклонино"
    ACCEPTED = "accepted", "Принято"



