# Задание:
# Применение Принципа Открытости/Закрытости (Open/Closed Principle) в Разработке Простой Игры
# Цель:
# Цель этого домашнего задание - закрепить понимание и навыки применения принципа
# открытости/закрытости (Open/Closed Principle), одного из пяти SOLID принципов объектно-ориентированного
# программирования. Принцип гласит, что программные сущности (классы, модули, функции и т.д.)
# должны быть открыты для расширения, но закрыты для модификации.#
# Задача:
# Разработать простую игру, где игрок может использовать различные типы оружия
# для борьбы с монстрами. Программа должна быть спроектирована таким образом, чтобы легко
# можно было добавлять новые типы оружия, не изменяя существующий код бойцов или механизм боя.
# Исходные данные:
# Есть класс Fighter, представляющий бойца.
# Есть класс Monster, представляющий монстра.
# Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
# Шаг 1: Создайте абстрактный класс для оружия
# Создайте абстрактный класс Weapon, который будет содержать абстрактный метод attack().
# Шаг 2: Реализуйте конкретные типы оружия
# Создайте несколько классов, унаследованных от Weapon, например, Sword и Bow.
# Каждый из этих классов реализует метод attack() своим уникальным способом.
# Шаг 3: Модифицируйте класс Fighter
# Добавьте в класс Fighter поле, которое будет хранить объект класса Weapon.
# Добавьте метод changeWeapon(), который позволяет изменить оружие бойца.
# Шаг 4: Реализация боя
# Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.
# Требования к заданию:
# Код должен быть написан на Python.
# Программа должна демонстрировать применение принципа открытости/закрытости: новые типы оружия
# можно легко добавлять, не изменяя существующие классы бойцов и механизм боя.
# Программа должна выводить результат боя в консоль.
# Пример результата:
# Боец выбирает меч.
# Боец наносит удар мечом.
# Монстр побежден!
# Боец выбирает лук.
# Боец наносит удар из лука.
# Монстр побежден!

from abc import ABC, abstractmethod


class Fighter():
    def __init__(self, name, weapon=True):
        self.name = name
        self.weapon = weapon

    def changeWeapon(self, weapon, monster):
        self.weapon = weapon
        self.weapon.attack(self, monster)


class Monster():
    def __init__(self, name, health=30):
        self.name = name
        self._health = health

    def threat(self):
        print(f'Монстр {self.name} угрожает!\n')

    def defeated(self):
        print(f'Монстр {self.name} побежден!\n')

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if not isinstance(value, int):
            raise ValueError('Очки здоровья должны быть числом')
        self._health = value
        print(f'Очки здоровья монстра {self.name}: {self._health}.\n')
        if self._health <= 0:
            self.defeated()


class Weapon(ABC):
    @abstractmethod
    def attack(self, fighter, monster):
        pass


class Sword(Weapon):
    def attack(self, fighter, monster):
        print(f'Боец {fighter.name} выбирает меч.')
        print(f'Боец {fighter.name} наносит удар мечом.\n')
        monster.health = monster.health - 20


class Bow(Weapon):
    def attack(self, fighter, monster):
        print(f'Боец {fighter.name} выбирает лук.')
        print(f'Боец {fighter.name} наносит удар из лука.\n')
        monster.health = monster.health - 10


fighter1 = Fighter('Нео')
monster1 = Monster('Агент Смит')
monster2 = Monster('Саурон')

health1 = monster1.health
print(f'Очки здоровья монстра {monster1.name}: {health1}.\n')
monster1.threat()
fighter1.changeWeapon(Bow(), monster1)
fighter1.changeWeapon(Bow(), monster1)
fighter1.changeWeapon(Bow(), monster1)

health2 = monster2.health
print(f'Очки здоровья монстра {monster2.name}: {health2}.\n')
monster2.threat()
fighter1.changeWeapon(Sword(), monster2)
fighter1.changeWeapon(Sword(), monster2)
