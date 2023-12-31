from Arrays import Array
#Creacion de Array de dos dimensiones.
class Grid():
    def __init__(self, rows, columns, fill_values=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_values)
    
    def get_heigth(self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __str__(self):
        result = ''
        for row in range(self.get_heigth()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "
            result += "\n"
        return str(result)