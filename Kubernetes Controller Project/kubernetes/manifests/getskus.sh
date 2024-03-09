# Initialize the CSV file with headers
echo "SKU,CPU,Memory" > skus.csv

# Get list of Azure regions
regions=$(az account list-locations --query "[].name" -o tsv)

# Loop through each region
for region in $regions; do
    echo "Processing region: $region"
    # Get SKUs for the current region and append to temporary file
    az vm list-sizes --location $region --output table | tail -n +3 | awk '{print $1","$4","$6}' >> skus_temp.csv
done

# Remove duplicate SKUs and append to final CSV file
sort -u skus_temp.csv >> skus.csv

# Clean up temporary file
rm skus_temp.csv
