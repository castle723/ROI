class RentalProperty:
    def __init__(self, rental_income, laundry_income, storage_income, misc_income,
                 taxes, insurance, utilities, hoa_fee, landscaping, vacancy,
                 repairs, capex, property_management, mortgage, downpayment,
                 closing_costs, rehab_budget, misc_investment):
        self.rental_income = rental_income
        self.laundry_income = laundry_income
        self.storage_income = storage_income
        self.misc_income = misc_income

        self.taxes = taxes
        self.insurance = insurance
        self.utilities = utilities
        self.hoa_fee = hoa_fee
        self.landscaping = landscaping
        self.vacancy = vacancy
        self.repairs = repairs
        self.capex = capex
        self.property_management = property_management
        self.mortgage = mortgage

        self.downpayment = downpayment
        self.closing_costs = closing_costs
        self.rehab_budget = rehab_budget
        self.misc_investment = misc_investment

    def calculate_monthly_cashflow(self):
        monthly_income = self.rental_income + self.laundry_income + self.storage_income + self.misc_income
        monthly_expenses = self.taxes + self.insurance + self.utilities + self.hoa_fee + \
                           self.landscaping + self.vacancy + self.repairs + self.capex + \
                           self.property_management + self.mortgage

        return monthly_income - monthly_expenses

    def calculate_annual_cashflow(self):
        return 12 * self.calculate_monthly_cashflow()

    def calculate_total_investment(self):
        return self.downpayment + self.closing_costs + self.rehab_budget + self.misc_investment

    def calculate_roi(self):
        annual_cashflow = self.calculate_annual_cashflow()
        total_investment = self.calculate_total_investment()

        return (annual_cashflow / total_investment) * 100


# Example usage
property_example = RentalProperty(rental_income=3000, laundry_income=200, storage_income=100, misc_income=50,
                                  taxes=500, insurance=200, utilities=150, hoa_fee=100, landscaping=50,
                                  vacancy=200, repairs=150, capex=100, property_management=300, mortgage=1200,
                                  downpayment=50000, closing_costs=5000, rehab_budget=10000, misc_investment=2000)

roi_percentage = property_example.calculate_roi()
print(f"Return on Investment (ROI): {roi_percentage:.2f}%")
