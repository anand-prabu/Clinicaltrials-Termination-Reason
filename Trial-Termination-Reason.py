import pandas as pd
from tqdm import tqdm
import requests
df = pd.read_csv ('/Obesity_P1 to P3_2 July 2025.csv')

def get_why_stopped_reason(nct_id):
    """
    Fetches study data from the clinicaltrials.gov API and extracts
    the 'whyStopped' reason from the statusModule.
    """
    api_url = f"https://clinicaltrials.gov/api/v2/studies/{nct_id}"
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        status_module = data.get('protocolSection', {}).get('statusModule', {})
        why_stopped_reason = status_module.get('whyStopped')
        return why_stopped_reason
    except Exception:
        # Return None or a specific string if an error occurs
        return "Not Available"


#Create a DataFrame containing ONLY terminated trials
terminated_studies_df = df[df['Study Status'] == 'TERMINATED'].copy()

# Step 2: Now it's safe to apply your function to this new DataFrame.
# This is more efficient as it only runs API calls for the terminated trials.
tqdm.pandas(desc="Fetching 'Why Stopped' Info")
terminated_studies_df['Why Stopped'] = terminated_studies_df['NCT Number'].progress_apply(get_why_stopped_reason)


# --- Verification ---
print(f"Found {len(terminated_studies_df)} terminated trials.")
print("\n'Why Stopped' information for some of these trials:")
print(terminated_studies_df[['NCT Number', 'Study Status', 'Why Stopped']].head())

terminated_studies_df.to_excel ('Terminated trials.xlsx', index = False)
                                