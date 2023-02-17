## Description

This Python script converts data from a [job_skill](https://www.kaggle.com/datasets/niyamatalmass/google-job-skills) CSV file  to OpenAI finetuning format, specifically JSONL format. The script extracts relevant fields from each row of the CSV file and constructs a JSONL object containing a prompt and a completion. The prompt includes the location, responsibilities, and minimum qualifications for the job, while the completion includes the job title and category.

## Requirements

- Python 3.x
- The `csv` and `json` modules, which are included in Python by default
- The OpenAI API, which can be installed using `pip install openai`

## Usage

1. Ensure that the CSV file containing the data is in the same directory as the script.
2. Update the script with the appropriate filename for the CSV file and the desired filename for the output JSONL file.
3. Run the script in a terminal or command prompt using the command `python transform.py`.
4. After the script has finished running, prepare the data for finetuning using the OpenAI tools. In a terminal or command prompt, execute the following command:

    ```
    openai tools fine_tunes.prepare_data -f output.jsonl
    ```

    This command will prepare the data in the `output.jsonl` file for finetuning and store the prepared data in a new file.

## Output

The script will create a new file in JSONL format, containing one JSON object per line. Each object will have a prompt and a completion.

The format of each object is as follows:

```json
{
    "prompt": "Location: {location}\nResponsibilities: {responsibilities}\n Qualifications: {minimum_qualifications}",
    "completion": "{title}\n{category}"
}
```

## Next step

You can follow [Fine-tuning in Azure OpenAI (with example code)](https://medium.com/@warching/fine-tuning-in-azure-openai-with-example-code-3c0b4d3e4c1f) to fine-tune and test a Azure OpenAI model using this output
