# Clinical Trials: "Trial Termination" Reason Extractor

This project provides a **Python script** to analyze clinical trial data from ClinicalTrials.gov, specifically focusing on trials with a status of **TERMINATED**. For each terminated trial, the script fetches the "Why Stopped" reason from the [ClinicalTrials.gov API](https://clinicaltrials.gov/), helping researchers and analysts better understand the causes of early trial termination.

WHY is this useful:
The CSV export from Clinicaltrials.gov provides the "Trial Status" info. We can know if a trial is TERMINATED. However, the reason for termination is available in the posting but not in the extract. Hence, this code 

I have used the same input file as in my other repositories.

Search query at CTG: https://clinicaltrials.gov/search?cond=Obesity&aggFilters=phase:3,status:rec Data retrieved on: 3 Jul 2025

This code pulled the Trial Termination reason for 140 trials in 57 seconds!

---

## Features

- **Filters** terminated studies from your dataset.
- **Automates API calls** to ClinicalTrials.gov for each terminated trial.
- **Appends** the "Why Stopped" reason to your DataFrame.
- **Exports** the results to an Excel file for further analysis.

---

## Getting Started

### Prerequisites

Make sure you have the following Python libraries installed:

- `pandas`
- `tqdm`
- `requests`

You can install them via pip:

pip install pandas tqdm requests


---

### How It Works

1. **Input:** The script reads a CSV file containing clinical trial data.  
2. **Filtering:** It selects only the trials with a status of `TERMINATED`.
3. **API Query:** For each terminated trial, it queries ClinicalTrials.gov to retrieve the "Why Stopped" reason.
4. **Output:** The script prints a summary and saves the results as `Terminated trials.xlsx`.

---

## Usage

1. Place your clinical trials CSV file in the project directory. Update the CSV file path in the script to match your file location: df = pd.read_csv('/path/to/your/input.csv')
2. Update the script with the correct path to your CSV file.
3. Run the script:

python terminated_trials_analysis.py


4. After execution, check the output Excel file (`Terminated trials.xlsx`) for results.

---

## Example Output

| NCT Number | Study Status | Why Stopped               |
|------------|--------------|---------------------------|
| NCT01977417 | TERMINATED  | No Funding                |
| NCT03991299 | TERMINATED   | Sponsor Decision.           |

---

## Notes

- Ensure your CSV contains columns named **"Study Status"** and **"NCT Number"**. Here the file used is a direct download from Clinicaltrials.gov and hence the column names. Ensure to use the same column names or adjust the reference in the code to NCT IDs as needed.
- API calls are limited by network speed and ClinicalTrials.gov rate limits.

---

## License

This project is open source and available under the MIT License.

---

## Contributions

Contributions, suggestions, and improvements are welcome! Please open an issue or submit a pull request.

---

*Happy analyzing!*
