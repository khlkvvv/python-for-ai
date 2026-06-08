class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description}) 
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        title = self.name.center(30, '*') + '\n'
        items = ''
        for item in self.ledger:
            description = item['description'][:23].ljust(23)
            amount = f"{item['amount']:.2f}".rjust(7)
            items += description + amount + '\n'
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    spent = []
    for category in categories:
        total = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        spent.append(total)
    
    total_spent = sum(spent)
    percentages = [int((s / total_spent) * 100) // 10 * 10 for s in spent]
    
    chart = "Percentage spent by category\n"
    
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for percent in percentages:
            chart += "o  " if percent >= i else "   "
        chart += "\n"
    
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    names = [category.name for category in categories]
    max_len = max(len(name) for name in names)
    
    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += (name[i] if i < len(name) else " ") + "  "
        if i < max_len - 1:
            chart += "\n"
    
    return chart