################################ Task 1 ###################################################################

class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

def load_product_data(file_path):
    products_linked_list = LinkedList()
    
    with open(file_path, 'r') as file:
        for line in file:
            id, name, price, category = line.strip().split(', ')
            price = float(price)
            product = Product(id, name, price, category)
            
            # Storing the data in a linked list 
            products_linked_list.append(product)
    
    return products_linked_list

##### Example #####
product_data_file = "product_data.txt"
products_linked_list = load_product_data(product_data_file)

##### Printing the data using a linked list #####
print("\nData loaded into linked list:")
current = products_linked_list.head
while current:
    product = current.data
    print(product.id, product.name, product.price, product.category)
    current = current.next

############################################ Task 2 ##############################################################################################

def insert_product(products_linked_list, new_product):
    products_linked_list.append(new_product)

def update_product(products_linked_list, product_id, new_details):
    
    current = products_linked_list.head
    while current:
        if current.data.id == product_id:
            current.data.name = new_details.get('name', current.data.name)
            current.data.price = new_details.get('price', current.data.price)
            current.data.category = new_details.get('category', current.data.category)
            break
        current = current.next

def delete_product(products_linked_list, product_id):
    
    prev = None
    current = products_linked_list.head
    while current:
        if current.data.id == product_id:
            if prev:
                prev.next = current.next
            else:
                products_linked_list.head = current.next
            break
        prev = current
        current = current.next

def search_product(products_linked_list, key_attribute, value):
    
    result_linked_list = LinkedList()
    current = products_linked_list.head
    while current:
        if getattr(current.data, key_attribute) == value:
            result_linked_list.append(current.data)
        current = current.next
    
    return result_linked_list

##### Example #####
new_product = Product('12345', 'New Product', 470.10, 'Electronics')

##### Inseting a new product: #####
insert_product(products_linked_list, new_product)

print("\nNewly Inserted Product Details:")
print(new_product.id, new_product.name, new_product.price, new_product.category)

##### Updating an existing product: #####
update_product(products_linked_list, '12345', {'name': 'Updated Product', 'price': 798.50})

print("\nUpdated Product Details:")
updated_product = search_product(products_linked_list, 'id', '12345').head.data
print(updated_product.id, updated_product.name, updated_product.price, updated_product.category)

##### Deleting a product: #####
product_id_to_delete = '12345'

product_to_delete = None
current = products_linked_list.head
while current:
    if current.data.id == product_id_to_delete:
        product_to_delete = current.data
        break
    current = current.next
if product_to_delete:
    print("\nDetails of Product to be Deleted:")
    print(product_to_delete.id, product_to_delete.name, product_to_delete.price, product_to_delete.category)
  
    delete_product(products_linked_list, product_id_to_delete)
    
    print("Product Deleted Successfully!")
else:
    print("Product with ID {} not found.".format(product_id_to_delete))
##### Searching a product: #####
result_linked_list = search_product(products_linked_list, 'category', 'Electronics')

##### Printing the result of the search operation: ##### (Electronics)
print("\nSeaching for the category 'Electronics'")

print("\nSearch Result (Linked List):")
current = result_linked_list.head
while current:
    product = current.data
    print(product.id, product.name, product.price, product.category)
    current = current.next

############################################ Task 3 ##############################################################################################

def length_of_linked_list(linked_list):
    length = 0
    current = linked_list.head
    while current:
        length += 1
        current = current.next
    return length

def bubble_sort_by_price(products_linked_list):
    length = length_of_linked_list(products_linked_list)
    if length < 2:
        return

    ##### Outside loop (traversing the list) #####
    for i in range(length):
        ##### Inside loop (swapping adjacent elements) #####
        current = products_linked_list.head
        prev = None
        while current.next:
            next_node = current.next
            if current.data.price > next_node.data.price:
                ##### Swapping the nodes #####
                if prev:
                    prev.next = next_node
                else:
                    products_linked_list.head = next_node
                current.next = next_node.next
                next_node.next = current
                
                ##### Updating the pointers for the next iteration #####
                prev = next_node
            else:
                prev = current
                current = current.next

##### Example #####
bubble_sort_by_price(products_linked_list)

print("\nSorted Product Data by Price:")
current = products_linked_list.head
while current:
    product = current.data
    print(product.id, product.name, product.price, product.category)
    current = current.next

############################################ Task 4 ##############################################################################################

import time

##### Measuring the time taken to sort data using Bubble Sort #####
def measure_sorting_time(sorting_function, products_linked_list):
    start_time = time.time()
    sorting_function(products_linked_list)
    end_time = time.time()
    return end_time - start_time

##### Creating sorted data #####
def create_sorted_data(products_linked_list):
    return products_linked_list

##### Creating data in reverse order #####
def create_reverse_sorted_data(products_linked_list):
    reversed_list = LinkedList()
    current = products_linked_list.head
    while current:
        reversed_list.append(current.data)
        current = current.next
    return reversed_list

##### Generating sorted and reverse sorted data #####
sorted_products = create_sorted_data(products_linked_list)
reverse_sorted_products = create_reverse_sorted_data(products_linked_list)

##### Measuring the sorting time for sorted data #####
sorted_time = measure_sorting_time(bubble_sort_by_price, sorted_products)

##### Measuring the sorting time for reverse sorted data #####
reverse_sorted_time = measure_sorting_time(bubble_sort_by_price, reverse_sorted_products)

print("\n\nTime taken to sort already sorted data:", sorted_time)
print("Time taken to sort reverse sorted data:", reverse_sorted_time)

##### Assessing time complexities #####
print("\nTime Complexities:")
print("\nBest-case Time Complexity: O(n)")
print("Average-case Time Complexity: O(n^2)")
print("Worst-case Time Complexity: O(n^2)")
