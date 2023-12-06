import configparser
import vulners

# Read API key from configuration file
config = configparser.ConfigParser()
config_file = "/home/gh0st/Documents/vulns_config.txt"

try:
    config.read(config_file)
    api_key = config["VULNERABILITIES"]["VULN_API_KEY"]
except (KeyError, FileNotFoundError):
    print(f"Error reading API key from {config_file}. Please make sure the file exists and the key is stored correctly.")
    exit(1)

# Connect to Vulners API
vulners_api = vulners.VulnersApi(api_key=api_key)

# Prompt the user to enter the CVE
cve = input("Enter the CVE you want to search for: ")

# Search for exploits
exploits = vulners_api.find_exploit_all(cve)

# Check if exploits found
if exploits:
    for exploit in exploits:
        # Check if exploit matches searched CVE
        if cve not in exploit.get("cvelist", []):
            continue

        # Printing key details
        print("=" * 50)
        print(f"CVE Details: {exploit.get('cvelist', 'N/A')}")

        # Print affected systems if available
        affected_systems = exploit.get("affected_systems", [])
        if affected_systems:
            print("\nAffected Systems:")
            for system in affected_systems:
                print(f"- {system}")
            print("\n")

        # Print exploit availability if available
        availability = exploit.get("availability")
        if availability:
            print("Exploit Availability:")
            print(availability)
            print("\n")

        # Process and print description
        description = exploit.get("description", "N/A")
        description = description.strip().replace("\n", " ").replace(" ", " ")
        print("Exploit Description:")
        print(description)
        print("\n")

        # Print severity
        print("Severity:")
        print(exploit.get("cvss", {}).get("score", "N/A"))
        print("\n")

        # Break out of the loop after printing information for the specified CVE
        break
else:
    print(f"No exploits found for CVE: {cve}")
