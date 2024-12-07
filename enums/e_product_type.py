import enum


class Product_Type(enum.Enum):
    CUP = 'Cup'
    MILK_SHAKE = 'Milk_Shake'

    def to_dict(self):
        return {
            'name': self.name,
            'value': self.value
        }
