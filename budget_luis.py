from __future__ import annotations

class Category:


    def __init__(self,name:str):
        self.name = name
        self.ledger = list()
        self.funds = 0
        self.withdraws = 0

    def __str__(self):
      return self.print_essa_bosta()

    def deposit(self,amount:float,description:str = None) -> None:
        ledger_deposit = dict()
        ledger_deposit['amount'] = amount
        if not description:
            ledger_deposit['description'] = ''
        else:
            ledger_deposit['description'] = description
        self.ledger.append(ledger_deposit)
        self.funds += amount
    
    def get_balance(self):
        return self.funds

    def check_funds(self,amount:float) -> bool:
        if amount > self.get_balance():
            return False
        else:
            return True

    def withdraw(self,amount:float,description:str = None) -> bool:
        ledger_withdraw = dict()
        if self.check_funds(amount) == False:
            return False
        else:
            ledger_withdraw['amount'] = -amount
            if not description:
                ledger_withdraw['description'] = ''
            else:
                ledger_withdraw['description'] = description
            self.ledger.append(ledger_withdraw)
            self.funds += -amount
            self.withdraws += amount
            return True

    def transfer(self,amount:float,budget:Category) -> bool:
        if self.check_funds(amount) == False:
            return False
        else:
            self.withdraw(amount,f'Transfer to {budget.name}')
            budget.deposit(amount,f'Transfer from {self.name}')
            return True

    def list_of_items(self) -> str:
        lista = ''
        items = list()
        for dict in self.ledger:
            for key in dict:
                items.append(dict[key])
                if len(items) == 2:
                    lista += f'{items[1]:23.23}{items[0]:>7.2f}\n'
                    items.clear()
        return lista

    def total(self) -> str:
        return f'Total: {self.get_balance():.2f}'
                
    def print_essa_bosta(self) -> str:
        return f'{self.name:*^30}\n{self.list_of_items()}{self.total()}'

    def total_withdraw(self):
        return self.withdraws

def total_withdraws(category,category_2 = None,category_3 = None,category_4 = None):
    if category_2 == None and category_3 == None and category_4 == None:
        return category.total_withdraw()

    elif category_3 == None and category_4 == None:
        return category.total_withdraw() + category_2.total_withdraw()

    elif category_4 == None:
        return category.total_withdraw() + category_2.total_withdraw() + category_3.total_withdraw()

    else:
        return category.total_withdraw() + category_2.total_withdraw() + category_3.total_withdraw() + category_4.total_withdraw()

def percentual(category,category_2 = None,category_3 = None,category_4 = None):
    lista_percentual = list()
    if category_2 == None and category_3 == None and category_4 == None:
        div = category.total_withdraw()/total_withdraws(category)
        div = div*100
        div = int(div/10)
        div = div*10
        lista_percentual.append(div)
        return lista_percentual

    elif category_3 == None and category_4 == None:
        div = category.total_withdraw()/total_withdraws(category,category_2)
        div = div*100
        div = int(div/10)
        div = div*10
        div_2 = category_2.total_withdraw()/total_withdraws(category,category_2)
        div_2 = div_2*100
        div_2 = int(div_2/10)
        div_2 = div_2*10
        lista_percentual.append(div)
        lista_percentual.append(div_2)
        return lista_percentual

    elif category_4 == None:
        div = category.total_withdraw()/total_withdraws(category,category_2,category_3)
        div = div*100
        div = int(div/10)
        div = div*10
        div_2 = category_2.total_withdraw()/total_withdraws(category,category_2,category_3)
        div_2 = div_2*100
        div_2 = int(div_2/10)
        div_2 = div_2*10
        div_3 = category_3.total_withdraw()/total_withdraws(category,category_2,category_3)
        div_3 = div_3*100
        div_3 = int(div_3/10)
        div_3 = div_3*10
        lista_percentual.append(div)
        lista_percentual.append(div_2)
        lista_percentual.append(div_3)
        return lista_percentual

    else: 
        div = category.total_withdraw()/total_withdraws(category,category_2,category_3,category_4)
        div = div*100
        div = int(div/10)
        div = div*10
        div_2 = category_2.total_withdraw()/total_withdraws(category,category_2,category_3,category_4)
        div_2 = div_2*100
        div_2 = int(div_2/10)
        div_2 = div_2*10
        div_3 = category_3.total_withdraw()/total_withdraws(category,category_2,category_3,category_4)
        div_3 = div_3*100
        div_3 = int(div_3/10)
        div_3 = div_3*10
        div_4 = category_3.total_withdraw()/total_withdraws(category,category_2,category_3,category_4)
        div_4 = div_4*100
        div_4 = int(div_4/10)
        div_4 = div_4*10

        lista_percentual.append(div)
        lista_percentual.append(div_2)
        lista_percentual.append(div_3)
        lista_percentual.append(div_4)
        return lista_percentual

def vertically_category(category_1:Category,category_2:Category = None,category_3:Category = None,category_4:Category = None) -> str:
    letter = f'---'
    category_list = list()
    category_1_list = list(str(category_1.name))

    if category_2 == None and category_3 == None and category_4 == None:
        letter += 0*letter
     
        while category_1_list != []:
            category_list.append(category_1_list[0])
            letter += f'\n{category_list[0]:>6}  '

            del category_1_list[0]
            if category_1_list == []:
                break

            category_list.clear()
    
    elif category_3 == None and category_4 == None:
        letter += 1*letter
        category_2_list = list(str(category_2.name))
        while category_1_list != [] or category_2_list != []:           
            category_list.append(category_1_list[0])
            category_list.append(category_2_list[0])
            letter += f'\n{category_list[0]:>6}{category_list[1]:>3}  '

            del category_1_list[0]
            del category_2_list[0]
            if category_1_list == [] and category_2_list == []:
                break

            category_list.clear()

            if category_1_list == []:
                category_1_list.append('')
            
            if category_2_list == []:
                category_2_list.append('')
     
    elif category_4 == None:

        letter += 2*letter
        category_2_list = list(str(category_2.name))
        category_3_list = list(str(category_3.name))
        while category_1_list != [] or category_2_list != [] or category_3_list != []:           
            category_list.append(category_1_list[0])
            category_list.append(category_2_list[0])
            category_list.append(category_3_list[0])
            letter += f'\n{category_list[0]:>6}{category_list[1]:>3}{category_list[2]:>3}  '

            del category_1_list[0]
            del category_2_list[0]
            del category_3_list[0]
            if category_1_list == [] and category_2_list == [] and category_3_list == []:
                break

            category_list.clear()

            if category_1_list == []:
                category_1_list.append('')
            
            if category_2_list == []:
                category_2_list.append('')

            if category_3_list == []:
                category_3_list.append('')

    else:

        letter += 3*letter
        category_2_list = list(str(category_2.name))
        category_3_list = list(str(category_3.name)) 
        category_4_list = list(str(category_4.name))
        while category_1_list != [] or category_2_list != [] or category_3_list != [] or category_4_list != []:           
            category_list.append(category_1_list[0])
            category_list.append(category_2_list[0])
            category_list.append(category_3_list[0])
            category_list.append(category_4_list[0])
            letter += f'\n{category_list[0]:>6}{category_list[1]:>3}{category_list[2]:>3}{category_list[3]:>3}  '

            del category_1_list[0]
            del category_2_list[0]
            del category_3_list[0]
            del category_4_list[0]
            if category_1_list == [] and category_2_list == [] and category_3_list == [] and category_4_list == []:
                break

            category_list.clear()

            if category_1_list == []:
                category_1_list.append('')
            
            if category_2_list == []:
                category_2_list.append('')

            if category_3_list == []:
                category_3_list.append('')
            
            if category_4_list == []:
                category_4_list.append('')

    return letter

def grafic(num:int,number:int,number_2:int,number_3:int,number_4:int) -> str:
    primeira_bolinha = f' o'
    primeiro_vazio = f'  '
    bolinha = f'  o'
    vazio = f'   '
    grafico = f''

    if num == number:
        grafico += primeira_bolinha
    else:
        grafico += primeiro_vazio
    
    if num == number_2:
        grafico += bolinha
    else:
        grafico += vazio

    if num == number_3:
        grafico += bolinha
    else:
        grafico += vazio

    if num == number_4:
        grafico += bolinha
    else:
        grafico += vazio
    
    return grafico[:-1]

def bolinha(number_list:list) -> str:
    contador = 1
    number = ''
    number_2 = ''
    number_3 = ''
    number_4 = ''
    for num in number_list:
        if contador == 1:
            number = num
            contador += 1 

        elif contador == 2:
            number_2 = num
            contador += 1

        elif contador == 3:
            number_3 = num
            contador += 1

        elif contador == 4:
            number_4 = num

    indice = [100,90,80,70,60,50,40,30,20,10,0]
    grafico = f'Percentage spent by category\n'
    for num in indice:

      grafico += f'{num:>3}|{grafic(num,number,number_2,number_3,number_4)}\n'
      
      if num == number:
        number = number - 10

      if num == number_2:
        number_2 = number_2 - 10

      if num == number_3:
        number_3 = number_3 - 10

      if num == number_4:
        number_4 = number_4 - 10

    return grafico

def create_spend_chart(categories:list) -> str:
    contador = 1
    category_1 = None
    category_2 = None
    category_3 = None
    category_4 = None
    for category in categories:
        if contador == 1:
            category_1 = category
            contador += 1 

        elif contador == 2:
            category_2 = category
            contador += 1

        elif contador == 3:
            category_3 = category
            contador += 1

        elif contador == 4:
            category_4 = category

    if not category_2 and category_3 and category_4:
        return f'{bolinha(percentual(category_1))}    -{vertically_category(category_1)}'

    elif category_3 == None and category_4 == None:
        return f'{bolinha(percentual(category_1,category_2))}    -{vertically_category(category_1,category_2)}'

    elif category_4 == None:
        return f'{bolinha(percentual(category_1,category_2,category_3))}    -{vertically_category(category_1,category_2,category_3)}'

    else:
        return f'{bolinha(percentual(category_1,category_2,category_3,category_4))}    -{vertically_category(category_1,category_2,category_3,category_4)}'

food = Category('Food')
drink = Category('Drink')
roupa = Category('Roupa')
outros = Category('Outros')
food.deposit(1000,'initial deposit')
food.withdraw(10.15,'groceries')
food.withdraw(15.89,'restaurant and more food for dessert')
food.transfer(100.70,drink)
food.total_withdraw()
drink.withdraw(100)
x = create_spend_chart([food,drink])
# print(x)

