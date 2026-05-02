# Dictionary.py
# A simple dictionary implementation

class Dictionary:
    def __init__(self):
        """Initialize an empty dictionary"""
        self.data = {}
    
    def add(self, key, value):
        """Add a key-value pair to the dictionary"""
        self.data[key] = value
    
    def get(self, key):
        """Retrieve a value by key"""
        return self.data.get(key, "Key not found")
    
    def remove(self, key):
        """Remove a key-value pair"""
        if key in self.data:
            del self.data[key]
            return True
        return False
    
    def display(self):
        """Display all key-value pairs"""
        for key, value in self.data.items():
            print(f"{key}: {value}")


# Example usage
if __name__ == "__main__":
    my_dict = Dictionary()
    my_dict.add("name", "Vedika")
    my_dict.add("age", 25)
    my_dict.display()