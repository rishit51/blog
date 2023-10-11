from packaging import version

# Read the input file
with open('req.txt', 'r') as file:
    lines = file.readlines()

# Create a dictionary to store the latest version of each package
latest_versions = {}

# Iterate through the lines and update the latest_versions dictionary
for line in lines:
    package, package_version = line.strip().split('==')
    if package in latest_versions:
        # Compare the versions using packaging.version
        if version.parse(package_version) > version.parse(latest_versions[package]):
            latest_versions[package] = package_version
    else:
        latest_versions[package] = package_version

# Write the latest versions back to the file
with open('req.txt', 'w') as file:
    for package, latest_version in latest_versions.items():
        file.write(f"{package}=={latest_version}\n")
