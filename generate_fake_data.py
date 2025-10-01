
import csv
from faker import Faker

def generate_fake_data(num_rows=100):
    fake = Faker()
    data = []
    for _ in range(num_rows):
        data.append({
            "company_name": fake.company(),
            "acct_no": fake.bban(),
            "DIN": fake.unique.random_number(digits=8),
            "pred_3rd_party_check": fake.boolean(),
            "authorized_signer": fake.name(),
            "trans_am": fake.random_int(min=100, max=10000)
        })
    return data

def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["company_name", "acct_no", "DIN", "pred_3rd_party_check", "authorized_signer", "trans_am"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    fake_data = generate_fake_data()
    write_to_csv("fake_data.csv", fake_data)
