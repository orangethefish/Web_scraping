import csv
def export_csv(names,sold,prices,reviews,gifts,categories,csv_name):
    data = []
    for i in range(len(names)):
        name_text = names[i] 
        price_text = prices[i] 
        sold_text = sold[i] 
        reviews_text = reviews[i] 
        gift_text = gifts[i] 
        categories_text = categories[i] 
        data.append({"Name": name_text, "Price": price_text, "Sold": sold_text, "Review": reviews_text, "Gift": gift_text, "Category": categories_text})

    # Write the data to a CSV file
    with open(csv_name, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Name', 'Price', 'Sold', 'Review', 'Gift', 'Category']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write the header row
        writer.writeheader()
        
        # Write the data rows
        for item in data:
            writer.writerow(item)

