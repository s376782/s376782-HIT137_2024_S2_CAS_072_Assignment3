#https://github.com/s376782/HIT137_2024_S2_CAS_072_Assignment3/tree/main/Q1_source
from models.person import Person
from services.base_service import BaseService

class CustomerService(BaseService[Person]):
    """
    CustomerService is a service class for handling customer data.
    It extends the BaseService class and interacts with customer data stored in an Excel file.
    """

    __source = 'data/Customer.xlsx'
    '''(private) Path to the Excel file storing customer data.'''

    def __init__(self):
        """
        Initializes the CustomerService by loading the customer data from the Excel file.
        """
        super().__init__(CustomerService.__source)
