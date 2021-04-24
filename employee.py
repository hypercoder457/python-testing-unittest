class Employee:
    def __init__(self, first_name, last_name, salary_per_year):
        self.first_name = first_name
        self.last_name = last_name
        self.salary_per_year = salary_per_year

    def give_raise(self, amount=5000):
        if not amount:
            self.salary_per_year += 5000
        else:
            self.salary_per_year += amount
        return self.salary_per_year
