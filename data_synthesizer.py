import json
from faker import Faker



def generate_fake_data(schema, num_instances):
    fake = Faker()
    fake_data_list = []
    
    for _ in range(num_instances):
        fake_instance = {}
        for field, field_type in schema.items():
            if field_type == 'name':
                fake_instance[field] = fake.name()
            elif field_type == 'address':
                fake_instance[field] = fake.address()
            elif field_type == 'email':
                fake_instance[field] = fake.email()

        fake_data_list.append(fake_instance)

    return fake_data_list




def main():
    
    input_schema = input("Enter the schema in JSON format: ")

    schema = json.loads(input_schema)

    num_instances = int(input("Enter the number of instances: ")) 

    
    fake_data = generate_fake_data(schema, num_instances)

   
    with open('fake_data.json', 'w') as file:
        json.dump(fake_data, file, indent=4)

if __name__ == "__main__":
    main()

