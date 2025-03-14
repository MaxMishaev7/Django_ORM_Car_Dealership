from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'


GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)

DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)

# ПОЛЯ В МОДЕЛИ CAR
# id - первичный ключ;
# model - модель авто;
# year - год выпуска;
# color - цвет;
# mileage - пробег;
# volume - объём двигателя;
# body_type - тип кузова, варианты возможных значений взять из BODY_TYPE_CHOICES;
# drive_unit - привод, варианты возможных значений взять из DRIVE_UNIT_CHOICES;
# gearbox - коробка передач, варианты возможных значений взять из GEARBOX_CHOICES;
# fuel_type - тип топлива, варианты возможных значений взять из FUEL_TYPE_CHOICES;
# price - цена; Username = maxmishaev, Password = hecQWk1974Gmr
# image - изображение авто, сами картинки можно взять в папке images.

class Car(models.Model):
    model = models.CharField(max_length=40)
    year = models.IntegerField()
    color = models.CharField(max_length=40)
    mileage = models.DecimalField(max_digits=8, decimal_places=2)
    volume = models.DecimalField(max_digits=4, decimal_places=2)
    body_type = models.CharField(max_length=10, choices=BODY_TYPE_CHOICES, default='sedan')
    drive_unit = models.CharField(max_length=5, choices=DRIVE_UNIT_CHOICES, default='front')
    gearbox = models.CharField(max_length=10, choices=GEARBOX_CHOICES, default='automatic')
    fuel_type = models.CharField(max_length=8, choices=FUEL_TYPE_CHOICES, default='gasoline')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return f'{self.model}'


# ПОЛЯ ДЛЯ МОДЕЛИ SALE
# id - первичный ключ;
# client - связка с моделью Client;
# car - связка с моделью Car;
# created_at - дата и время продажи, для автозаполнения добавьте свойство auto_now_add=True.


class Sale(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.client} {self.car}\n{self.created_at}\n'

