import csv
import json

# Open the input CSV file
with open('job_skills.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Open the output JSONL file
    with open('output.jsonl', 'w') as jsonl_file:
        for row in csv_reader:
            # Extract the relevant fields from the CSV row
            location = row['Location']
            responsibilities = row['Responsibilities']
            minimum_qualifications = row['Minimum Qualifications']
            title = row['Title']
            category = row['Category']

            # Construct the JSONL object
            jsonl_obj = {
                'prompt': f'Location: {location}\nResponsibilities: {responsibilities}\n Qualifications: {minimum_qualifications}',
                'completion': f'{title}\n{category}'
            }

            # Write the JSONL object to the output file
            jsonl_file.write(json.dumps(jsonl_obj) + '\n')
