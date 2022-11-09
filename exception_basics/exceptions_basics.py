'''Demonstrate some basics of exceptions.'''

driving_age = 16 # years old
average_lifespan = 72 # years old, world wide

class Some_exception(Exception):
    pass

class SpecialDivisionError(ZeroDivisionError):
    pass

class ExpectedError(Exception):
    pass

class exception_basics:
    '''Basic exceptions...'''
    def __init__(self, new_name="no name given", new_age=0, new_gender_identity="no gender identity given"):
        self.name = new_name
        self.age = new_age # in years
        self.gender_identity = new_gender_identity


    def __str__(self):
        return f"name: {self.name}, age: {self.age}, gender identity: {self.gender_identity}"

    def driving_age_ratio(self):
        '''Return the ratio of age versus driving age.'''

        #one way to solve the problem of a variable not being assigned... is to just assign some default value...
        driving_age_reciprocal = -1
        try:
            driving_age_reciprocal = driving_age / self.age
        except:
            print("An exception has happened...")
        return 1 / driving_age_reciprocal

    def lifespan_age_ratio(self):
        '''Return the ratio of ager versus average lifespan.'''
        #lifespan_age_reciprocal = None
        try:
            raise ExpectedError # if an exception is raised, but is not caught, the exception is raised up to the code that called this code... up through your main file and if that is not caught, then Python crashes your program
            if self.age == -1:
                raise SpecialDivisionError
            lifespan_age_reciprocal = average_lifespan / self.age
            return 1 / lifespan_age_reciprocal
        except SpecialDivisionError:
            print("A SpecialDivisionError has happened")
        except ZeroDivisionError:
            print("A ZeroDivisionError exception has happened...")
            raise Some_exception
        #except:
        #    print("An unexpected exception has happened!")

        # continues executing the function after the except clause has happened
        return -42 # Joseph just picking an easy to identify default return value...