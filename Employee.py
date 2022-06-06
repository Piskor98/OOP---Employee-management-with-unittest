


class Employee:       #Create simply employee class

    raise_salary=1.05 #Every year every employee increase his salary by this 'raise_salary' factor

    def __init__(self,firstname,lastname,country,city,address,tel_number,salary):    #initialize the future object's attributes
        self.firstname=firstname
        self.lastname=lastname
        self.tel_number=tel_number
        self.address=address
        self.salary=salary
        self.country=country
        self.city=city

    @property          #property decorator used to return the property attributes
    def create_employee_email(self):  #Create a method for creating a new, permanent attribute of an object
        return f'{self.firstname}_{self.lastname}@gmail.com'

    @property
    def full_name(self):              #Create a method which is returning employee's fullname
        return f'{self.firstname} {self.lastname}'

    @property                         #Create a method which is returning employee's full address
    def full_address(self):
        return {
            'country': f'{self.country}',
            'city': f'{self.city}',
            'address': f'{self.address}'
        }

    @property
    def business_card(self):          #Create a method which is returning dictionary whith employee's business_card data
        return {
            'employee': f'{self.full_name}',
            'address': f'{self.full_address}',
            'contact': f'{self.tel_number}'
        }

    def apply_raise_salary(self):     #Create a method to increase employee's salary
        self.salary=int(self.salary*self.raise_salary)


#Simple examples of creating employees
Jan=Employee('Jan','Kowalski','Poland','Lubartów','Jesionowska 13', 123456789, 60000)
Katarzyna=Employee('Katarzyna','Twardowska','Poland','Warszawa','Jagiełły 27/3',987654321,78000)

print(Jan,Katarzyna)                                    #check if objects exist
print(Jan.business_card,Katarzyna.business_card)        #print information for clients
