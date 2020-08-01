class Company:

    def __init__(self, cmp_name, cmp_establishment_date, cmp_ceo):
        self.cmp_name = cmp_name
        self.cmp_establishment_date = cmp_establishment_date
        self.cmp_ceo = cmp_ceo

    def get_cmp_ceo(self):
        return self.cmp_ceo

    def get_cmp_name(self):
        return self.cmp_name

    def get_cmp_establishment_date(self):
        return self.cmp_establishment_date
