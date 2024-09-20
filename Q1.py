#Que.1
class InvalidMarksException(Exception):
    def __init__(self, message="Invalid marks: Marks Must be from 0 to 100%"):
        self.message = message
        super().__init__(self.message)


def validate_marks(marks):
    try:
        
        if marks < 0 or marks > 100:
            raise InvalidMarksException()
        
        print(f"Your marks are: {marks}%")
    
    except InvalidMarksException as e:
        print(e)

validate_marks(90)
validate_marks(101)
validate_marks(25)
