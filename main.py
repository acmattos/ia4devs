import json

from deep_seek import generate_data_for_fine_tuning

amazon_products = []

with open('trn.json', 'r', encoding='utf-8') as amazon_products_file:
    print("================================================ Reading products ================================================")
    for i, line in enumerate(amazon_products_file):
        if i >= 500:
            break
        json_data = json.loads(line)
        if json_data.get("title") and json_data.get("content"):
            clean_title = ' '.join(json_data["title"].split()).strip()
            clean_content = ' '.join(json_data["content"].split()).strip()

            amazon_products.append({
                'title': clean_title,
                'context': clean_content
            })
            print(amazon_products)

results = []

for product in amazon_products:
    response = generate_data_for_fine_tuning(product)
    try:
        # Extract JSON from the string
        json_start = response.find('{')
        json_end = response.rfind('}') + 1
        json_str = response[json_start:json_end]
        
        # Parse JSON and append to results
        json_data = json.loads(json_str)
        results.append(json_data)
        print(json_data)
    except (ValueError, AttributeError) as e:
        print(f"Error parsing JSON for product: {e}")

def save_results(json_results):
    with open('amazon_titles_reasoning2.json', 'w', encoding='utf-8') as result_file:
        print("================================================ Saving products ================================================")
        result_file.write(json.dumps(json_results, ensure_ascii=False, indent=4))

save_results(results)

print("================================================ Done ================================================")
