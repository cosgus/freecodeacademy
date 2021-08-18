class Category:

    PRINT_SIZE = 30
    DESCRIPTION_SIZE = 23
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.withdraw_amount = 0

    def __str__(self):
        retorno = ''
        qtd_asteriscos = int((self.PRINT_SIZE - len(self.name))/ 2)
        cabecalho = self.name
        cabecalho = cabecalho.ljust(qtd_asteriscos + len(self.name), "*")
        cabecalho = cabecalho.rjust(self.PRINT_SIZE, "*")
        retorno = cabecalho + '\n'
        for register in self.ledger:
            retorno += self.formatted_register(register) + '\n'
        retorno += ('Total: ' + '{:.2f}'.format(self.balance))
        return retorno

    def formatted_register(self, register):
        amount = float(register["amount"])
        format_amount = "{:.2f}".format(amount)
        description = register["description"][0:self.DESCRIPTION_SIZE]
        format_description = description.ljust(self.PRINT_SIZE - len(format_amount))
        return format_description + format_amount

    def formatted_withdraw_graphic(self, total_withdraw):
        porcentagem = float(self.withdraw_amount / total_withdraw) * 100
        retorno = []
        for val in range(100, -1, -10):
            if(val <= porcentagem):
                retorno.append(' o')
            else:
                retorno.append('  ')
        return retorno

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": str(description)})
        self.balance += amount
    
    def withdraw(self, amount, description=""):
        if (amount > self.balance):
            return False
        self.ledger.append({"amount": -1*amount, "description": str(description)})
        self.balance -= amount
        self.withdraw_amount += amount
        return True
    
    def transfer(self, amount, category):
        if (self.withdraw(amount, 'Transfer to ' + category.get_name())):
            category.deposit(amount, 'Transfer from ' + self.name)
            return True
        return False

    def get_balance(self):
        return self.balance
    
    def get_withdraw(self):
        return self.withdraw_amount

    def get_name(self):
        return self.name
    
    def check_funds (self, amount):
        return amount <= self.balance

    def __repr__(self):
        return self.__str__()

def create_spend_chart(categories):

    retorno = 'Percentage spent by category' + '\n'
    total_withdraw = 0
    longest_name = 0

    for category in categories:
        total_withdraw += category.get_withdraw()
        longest_name = max(longest_name, len(category.get_name()))

    graphic_matrix = [['100|', ' 90|', ' 80|', ' 70|', ' 60|', ' 50|', ' 40|', ' 30|', ' 20|', ' 10|', '  0|']]
    for category in categories:
        graphic_matrix.append(category.formatted_withdraw_graphic(total_withdraw))
        graphic_matrix.append(formatted_array(11, ' '))
    graphic_matrix.append(formatted_array(11, ' '))
    
    transposed_matrix = [[graphic_matrix[j][i] for j in range(len(graphic_matrix))] for i in range(len(graphic_matrix[0]))]
    retorno += (formatted_matrix(transposed_matrix) + '\n')

    retorno += ('    ' + ''.ljust(3*len(categories),'-') + '-\n')

    name_matrix = []
    name_matrix.append(formatted_array(longest_name, '    '))
    for category in categories:
        name_matrix.append(formatted_array(longest_name, ' '))
        name_matrix.append(list(category.get_name().ljust(longest_name)))
        name_matrix.append(formatted_array(longest_name, ' '))
    name_matrix.append(formatted_array(longest_name, ' '))
    transposed_name_matrix = [[name_matrix[j][i] for j in range(len(name_matrix))] for i in range(len(name_matrix[0]))]

    retorno += formatted_matrix(transposed_name_matrix)

    return retorno

def formatted_matrix(matrix):
    retorno = ''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            retorno += matrix[i][j]
        if(i < len(matrix) - 1):
            retorno += '\n'
    return retorno

def formatted_array(size: int, character: str):
    arr = []
    for i in range(size):
        arr.append(character)
    return arr
