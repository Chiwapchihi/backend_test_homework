class Contact:
    def __init__(self,
                 name: str,
                 year_birthday: int,
                 is_programmer: bool) -> None:
        self.name = name
        self.year_birthday = year_birthday
        self.is_programmer = is_programmer

    def age_define(self) -> str:
        if 1946 < self.year_birthday < 1980:
            return 'Олдскул'
        if self.year_birthday >= 1980:
            return 'Молодой'
        return 'Старейшина'

    def programmer_define(self) -> str:
        if self.is_programmer:
            return 'Программист'
        return 'Нормальный'

    def show_contact(self) -> str:
        return (f'{self.name},'
                f'Категория: {self.age_define()}'
                f'Статус: {self.programmer_define()}')

    def print_contact(self) -> None:
        print(self.show_contact())


# Создаем новый контакт
contact = Contact("John Doe", 1985, False)

# Выводим информацию о контакте
contact.print_contact()
