t, b = map(int, input().split())  # Read the number of package types and stores
store_package_counts = list(map(int, input().split()))  # Read the number of package types each store has

latest_versions = {}
for _ in range(t):
    package_name, version = input().split()
    latest_versions[package_name] = int(version)

version_steps = []
for i in range(b):
    store_packages = list(input().split())

    steps = 0
    for j in range(t):
        package_name, version = store_packages[j], int(store_packages[j + t])
        latest_version = latest_versions[package_name]

        if version < latest_version:
            steps += latest_version - version

    version_steps.append(steps)

for steps in version_steps:
    print(steps)
