from __future__ import annotations
import math


class Category: 
    
    def __init__(self, name:str):

        self.name = name
        self.ledger = []
        self.balance = 0
        self.total_spent = 0

    def deposit(self, amount:float, description:str=None):

        ledger_entry = {'amount':amount, 'description': ''}
        if description:
            ledger_entry.update({'description': description})
        self.ledger.append(ledger_entry)


    def withdraw(self, amount:float, description:str=None):
        if self.check_funds(amount):
            ledger_entry = {'amount': -1*amount, 'description': ''}
            if description:
                ledger_entry.update({'description': description})
            self.ledger.append(ledger_entry)
            self.total_spent += amount
            return True
        else:
            return False


    def get_balance(self):
        return sum([ledger_entry['amount'] for ledger_entry in self.ledger])


    def transfer(self, amount:float, category:Category) -> bool:
        withdrawal = self.withdraw(amount, f"Transfer to {category.name}")
        if withdrawal:
            category.deposit(amount, f"Transfer from {self.name}")
        return withdrawal
        

    def check_funds(self, amount:str) -> bool:
        return amount <= self.get_balance()


    def __str__(self):

        name_length = len(self.name)
        star_length = round(math.ceil(30 - name_length)/2)
        header = "*"*star_length + self.name + "*"*star_length +'\n'

        body = ''

        for item in self.ledger:
            body += f'{item["description"][0:23]:<23}{item["amount"]:>7.2f}\n'

        footer = f'Total: {self.get_balance():.2f}'
        return header + body + footer


    def __repr__(self):
        return self.__str__()

def create_spend_chart(category_list:list) -> str:

    """
    Creates a chart that displays proportion of total budget each category is using.
    Chart creation gets divided into header, table, and footer
    
    """

    header = 'Percentage spent by category\n'
    table = create_table(category_list)
    divider = '    ' + '-'*len(category_list*3) + '-'
    footer = create_footer(category_list)
    full_chart = header + table + divider + footer

    return full_chart


def create_table(categories:list)->str:

    """Creates the table body of the chart by aggregating values to row"""

    total_spent = get_total_spent(categories)

    table = str()

    for row_num in range(11):
        row_label = 100 - row_num*10

        # Row label creation - ie 100| .. 90| ... 80| ...etc
        row = f"{row_label:>3}|"

        for category in categories:
            percentage = math.floor(category.total_spent/total_spent * 10) * 10
            if percentage >= row_label:
                row += ' o '
            else:
                row += '   '
        
        table += row + '\n'
    return table

            


def create_footer(categories):

    """Creates the bottom of the chart"""

    footer = '\n'
    row_len = max([len(category.name) for category in categories])
    for idx in range(row_len):
        footer += '    '
        for category in categories:
            try:
                footer += f' {category.name[idx]} '
            except IndexError:
                footer += '   '
        footer += '\n'
    return footer



def get_total_spent(categories):
    total_budget = sum([category.total_spent for category in categories])
    return total_budget

food = Category('Food')
entertainment = Category('Entertainment')
business = Category('Business')

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(633.40)
business.withdraw(10.99)

create_spend_chart([food, entertainment, business])