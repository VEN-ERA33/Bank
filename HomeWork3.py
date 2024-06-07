class Bank:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def moneyX(self):
        try:
            amount = float(input("Введите сумму для добавления на счет: "))
            if amount > 0:
                self.__balance += amount
                print(f"Сумма успешно добавлена. Текущий баланс: {self.__balance}")
            else:
                print("Сумма должна быть положительной.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")

    def _kill(self):
        self.__balance = 0
        print("Баланс обнулен.")

    def __jackpot(self):
        self.__balance *= 10
        print("Поздравляем! Вы выиграли джекпот. Текущий баланс: {self.__balance}")

    def _merge_balance(self, other):
        if isinstance(other, Bank):
            self.__balance += other.__balance
            other.__balance = 0
            print(f"Баланс успешно объединен. Новый баланс: {self.__balance}")
        else:
            print("Ошибка: можно объединить баланс только с другим объектом класса Bank.")
