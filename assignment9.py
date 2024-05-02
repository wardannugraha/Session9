#Session 9
#Name : Wardan Nugraha Ahmad
#Student Number : 20230040071

class Product:
    def __init__(self, id, name) :
        self.id = id
        self.name = name

class ProductManager:
    def __init__(self):
        self.products = []

    def list_products(self):
        if not self.products:
            print("No products avaible")
        else:
            print("List of Products: ")
            for product in self.products:
                print(f"ID: {product.id}, Name : {product.name}")

    def add_product(self):
        id = input("Enter Product ID : ")
        name = input("Enter Product Name : ")
        product = Product(id, name)
        self.products.append(product)
        print("Product Added Successfully.")

    def delete_product(self):
        id = input("Enter product ID to delete: ")
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                print("Product Deleted Successfully.")
                return
        print("Product not Found.")

    def delete_by_index(self):
        index = int(input("Enter index of product to delete: "))
        if 0 <= index < len(self.products):
            del self.products[index]
            print("Product Deleted Successfully.")
        else:
            print("Invalid index.")

def main():
    product_manager = ProductManager()
    while True:
        print("\nMenu:")
        print("1. List Products")
        print("2. Add Product")
        print("3. Delete Product")
        print("4. Delete by Index")
        print("5. Exit")

        choice = input("Enter your Choice: ")

        if choice == '1' :
            product_manager.list_products()
        elif choice == '2' :
            product_manager.add_product()
        elif choice == '3' :
            product_manager.delete_product()
        elif choice == '4' :
            product_manager.delete_by_index()
        elif choice == '5' :
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()