from rich.console import Console
import datetime
import time
import sys
import oci

console = Console()

config = oci.config.from_file(file_location="./config")
compute = oci.core.ComputeClient(config)

tenancy_id = config["tenancy"]

# Get Availability Domains
identity = oci.identity.IdentityClient(config)

ads = identity.list_availability_domains(
    compartment_id=tenancy_id
).data

try:
    console.print("Starting monitor to checking the availability for [bold yellow]Ampere Instance[/bold yellow] in your specific region!\n")
    while True:
        for ad in ads:
            details = oci.core.models.CreateComputeCapacityReportDetails(
                compartment_id=tenancy_id,
                availability_domain=ad.name,
                shape_availabilities=[
                    oci.core.models.CreateCapacityReportShapeAvailabilityDetails(
                        instance_shape="VM.Standard.A1.Flex",
                        instance_shape_config=oci.core.models.CapacityReportInstanceShapeConfig(
                            ocpus=1,
                            memory_in_gbs=6
                        )
                    )
                ]
            )

            response = compute.create_compute_capacity_report(
                create_compute_capacity_report_details=details
            )

            result = response.data.shape_availabilities[0]
            
            if str(result.availability_status) == "OUT_OF_HOST_CAPACITY":
                console.print(f"Status: [bold red]{result.availability_status}[/bold red]")
            else:
                console.print(f"Status: [bold green]{result.availability_status}[/bold green]")
            console.print(f"Available count: {result.available_count}")
            console.print(f"Time: {datetime.datetime.now()}")
            console.print()
            
            # check again after 15 minutes
            time.sleep(900)

except KeyboardInterrupt:
    sys.exit(1)

except Exception as e:
    console.print(e, style="bold red")