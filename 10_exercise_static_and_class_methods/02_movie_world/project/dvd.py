import calendar


class DVD:
    def __init__(self, name, _id, creation_year: int, creation_month: int, age_restriction: int):
        self.name = name
        self.id = _id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, _id, name, date: str, age_restriction):
        month, year = [int(x) for x in date.split('.')[1:]]
        month_name = calendar.month_name[month]
        return cls(name, _id, year, month_name, age_restriction)

    def __repr__(self):
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) "
                f"has age restriction {self.age_restriction}. Status: {'' if self.is_rented else 'not '}rented")
