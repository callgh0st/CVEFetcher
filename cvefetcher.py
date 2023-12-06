import os
import vulners

# Define API key file path
API_KEY_FILE = "/etc/vulners_api_key.txt"

try:
    # Check if API key file exists
    if not os.path.exists(API_KEY_FILE):
        save_key = input("Save Vulners API Key (Y/N)? ").lower()
        if save_key == "y":
            api_key = input("Enter Vulners API Key: ")
            with open(API_KEY_FILE, "w") as f:
                f.write(api_key)
        else:
            api_key = input("Enter Vulners API Key: ")
    else:
        # Read API key from file
        with open(API_KEY_FILE, "r") as f:
            api_key = f.read().strip()

    # Connect to Vulners API
    vulners_api = vulners.VulnersApi(api_key=api_key)

except Exception as e:
    print(f"Error: {e}")
    exit(1)


def display_exploit_information(exploits, cve):
    # Check if exploit matches searched CVE
    for exploit in exploits:
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


def main():
    # Get CVE identifier from user
    cve = input("Enter the CVE identifier you want to search for: ")

    # Search for exploits
    exploits = vulners_api.find_exploit_all(cve)

    # Display exploit information
    display_exploit_information(exploits, cve)


if __name__ == "__main__":
    main()
