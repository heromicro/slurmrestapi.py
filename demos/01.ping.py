# demo/ping_demo.py

import os

from slurmrestapi import ApiClient, Configuration, SlurmApi


def main():
    # Set up configuration for the API client
    
    jwt = os.getenv("SLURM_API_TOKEN")
    host = os.getenv("SLURM_HOST") # ip:port/domain:port
    config = Configuration(
        host=host,
        username="root",
        access_token=jwt,
    ) 

    # Initialize the API client with the given configuration
    api_client = ApiClient(configuration=config)

    # Initialize the Slurm API client with the configured API client
    slurm_api = SlurmApi(api_client=api_client)


    # Use the client to ping the API (assuming a /ping endpoint exists)
    try:
        response = slurm_api.slurm_v0040_get_ping()
        # response = slurm_api.slurm_v0041_get_ping()
        print(" response: ", response.to_dict())
        
    except Exception as e:
        print("Error during ping:", e)

if __name__ == "__main__":
    main()
