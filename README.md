## CVEFetcher

**CVEFetcher** simplifies CVE searches for cybersecurity professionals by leveraging the Vulners API. This script provides streamlined access to exploit descriptions and severity ratings, eliminating the need for manual online searches.

**New Features:**

* **Secure API Key Management:** CVEFetcher now reads the Vulners API key from a universally readable file, enhancing security and avoiding the need for repeated input.
* **User-driven API Key Management:** Users can choose to save their API key to the file for future use, saving time and effort.

**Functionality:**

* **CVE Search:** Search for exploits associated with specified CVEs.
* **Detailed Exploit Information Retrieval:** Access essential details like descriptions and severity ratings for identified exploits.

**Benefits:**

* **Streamlined Exploit Information Access:** Quickly retrieve critical exploit information without tedious manual searches.
* **Enhanced Vulnerability Assessment:** Simplify vulnerability assessments with immediate access to CVE details.
* **Secure API Key Handling:** Store your API key securely in a universally accessible location.
* **Improved User Experience:** Save your API key for future use and avoid repeated input.

**Setup:**
1. **Install Vulners API Client:** Install the Python library for accessing Vulners API using `pip install vulners`.
2. **Create a Vulners Account:** Sign up for a free plan on Vulners at [https://vulners.com/](https://vulners.com/).
3. **Generate API Key:** Generate an API key from your Vulners profile within the API Keys section.
4. **Auto-Configured API Key File:** Created a file named `vulners_api_key.txt` in a universally readable location `/etc/`.
5. **Save API Key (Optional):** Run the script and choose "y" when prompted to save your API key to the file. Otherwise, enter the key directly.

**Installation:**

1. Clone the repository: `git clone https://github.com/callgh0st/CVEFetcher.git`.
2. Navigate to the directory: `cd CVEFetcher`.
3. Run the script: `python3 cvefetcher.py`.
4. Enter CVE identifier: When prompted, enter the CVE identifier in the format CVE-XXXX-XXXX.

**Contributions:**

We welcome feedback and contributions from the cybersecurity community to improve CVEFetcher. Feel free to reach out with suggestions or collaboration opportunities.

**Thank you for using CVEFetcher!**
