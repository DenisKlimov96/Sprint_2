class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, rest_days):
        hours = (7 - rest_days) * 8
        return cls(hours, rest_days)

    @classmethod
    def get_email(cls, name):
        email = f"{name}@email.com"
        return cls(name, email)

    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment

    def salary(self):
        return self.hours * hourly_payment
