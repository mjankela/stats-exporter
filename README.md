# stats-exporter
Small script to export GitHub traffic statistics.

GitHub only presents statistics for one week and retains statistics for the past two weeks. 
If not downloaded, the history gets lost.

This script allows you to download the statistics and store them on a local device.

To use this script:

(1) Make sure you have the requests library installed. You can install it using pip: pip install requests
(2) Replace YOUR_PERSONAL_ACCESS_TOKEN with your GitHub personal access token. 
    You can generate one in your GitHub account settings under "Developer settings" > "Personal access tokens"
(3) Replace YOUR_USERNAME with your GitHub username
(4) Replace YOUR_REPOSITORY with the name of the repository you want to fetch statistics for
(5) run python .\github-stats-export.py




