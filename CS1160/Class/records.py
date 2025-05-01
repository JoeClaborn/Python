def main():
    records = {'name': 'Bob', 'age': 65, 'id': 12345}
    list_of_records = [{'name': 'Bob', 'age': 65, 'id': 12345},
                       {'name': 'Jack', 'age': 25, 'id': 304},
                       {'name': 'John', 'age': 40, 'id': 500},
                       {'name': 'Sophie', 'age': 25, 'id': 10}]

    for record in list_of_records:
        record_name = record['name']
        record_age = record['age']
        print(f"Name: {record_name} Age: {record_age}")
    #record_list = ['Bob', 65, 12345]

    #first_name = records['name']
    #first_name = record_list[0]
    
    #print(f"The record shows name is {first_name}")

if __name__ == "__main__":
    main()
