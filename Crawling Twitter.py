# Install pandas
!pip install pandas

# Install Node.js (required for tweet-harvest)
!sudo apt-get update
!sudo apt-get install -y ca-certificates curl gnupg
!sudo mkdir -p /etc/apt/keyrings
!curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg

!NODE_MAJOR=20 && echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list

!sudo apt-get update
!sudo apt-get install nodejs -y

# Check Node.js version
!node -v


CRAWLING X
import pandas as pd

# Twitter Auth Token
twitter_auth_token = 'xxxx'

# Crawling parameters
filename = 'motor_listrik.csv'
search_keyword = 'motor listrik lang:id since:2020-01-01 until:2024-01-01'
limit = 5000

# Run tweet-harvest
!npx -y tweet-harvest@2.6.1 -o "{filename}" -s "{search_keyword}" --tab "LATEST" -l {limit} --token {twitter_auth_token}

# Specify the path to your CSV file
file_path = f"tweets-data/{filename}"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Display the DataFrame
display(df)
