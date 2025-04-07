class Category:
    def __init__(self, category):
        #Stores category name (like 'Food')
        self.category = category
        self.ledger = []

    def __str__(self):
        Output = ''

        #First time doing this kind of formatting so I chose 
        #to implement .center() myself
        split_title_len = len(self.category) // 2
        asterisks = (15 - split_title_len) * '*'
        Title = asterisks + self.category + asterisks
        if len(Title) > 30:
            Title = Title[1:]
        Output += Title + '\n'

        for transaction in self.ledger:
            trans = ''
            if len(transaction['description']) > 23:
                trans += transaction['description'][:23]
            else:
                trans += transaction['description']

            amount = f"{transaction['amount']:.2f}"

            if len(amount) > 7:
                amount = amount[:7]
            elif len(amount) < 7:
                amount = ' ' * (7 - len(amount)) + amount

            spaces = (30 - len(trans) - len(amount)) * ' '

            Output += trans + spaces + amount + '\n'

        Output += 'Total: ' + f'{self.get_balance():.2f}'
        return Output

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})

    def get_balance(self):
        balance = 0.00
        for transaction in self.ledger:
            balance += transaction['amount']
        return balance

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': float(amount*-1), 'description': description})
            return True
        else:
            return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, 'Transfer to ' + category.category)
            category.deposit(amount, 'Transfer from ' + self.category)
            return True
        else:
            return False

    def spent(self):
        spent = 0
        for transaction in self.ledger:
            if transaction['amount'] < 0 and 'Transfer' not in transaction['description']:
                spent += transaction['amount']
        return spent


def create_spend_chart(categories):
    graph = 'Percentage spent by category' + '\n'
    
    total_spent = 0
    for category in categories:
        total_spent += category.spent()

    #Dict where key:value = category:percentage spent over total expenses
    perc_spent_category = {}
    for category in categories:
        perc = ((category.spent()/total_spent) * 100 // 10) *10
        perc_spent_category[category.category] = int(perc)
    
    #Percentages axis of the bar plot
    percentages = [' ' * (3 - len(str(i))) + str(i) + '| ' for i in range (100, -10, -10)]
    for i in range(len(percentages)):
        #p is the number in the percentage list so ' 90| ' -> 90 (an int)
        p = int(percentages[i][:3].strip(' '))
        for category in categories:            
            if perc_spent_category[category.category] >= p:
                percentages[i] += 'o  '
            else:
                percentages[i] += '   '
        percentages[i] += '\n'    

    graph += ''.join(percentages)

    #Dashes
    graph += '    ' + '-' * (len(categories) * 3 + 1) + '\n'

    #Labels
    #Matrix to create the labels
    len_matrix = 5
    longest_category_name = len(max([i for i in perc_spent_category], key = len))

    #Formats categories name by adding spaces to make them all the same len (prevents list index out of range error in the following for loops)
    cat_names_formatted = [i + ' ' * (longest_category_name - len(i)) for i in perc_spent_category]
    
    labels = [[' ' * len_matrix] for i in range (longest_category_name)]
    for i in range(len(labels)):
        for j in range(len(cat_names_formatted)):
            labels[i] += cat_names_formatted[j][i]
            labels[i] += '  '
        #spend chart must not end with \n
        if i < len(labels) - 1:
            labels[i] += '\n'

    for label in labels:
        graph += ''.join(label)

    graph.rstrip('\n')
    return graph

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(10)
sport = Category('Sport')
sport.withdraw(10)
print(food)
print('\n')
categories = [food, clothing, sport]
print(create_spend_chart(categories))