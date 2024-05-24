# Object Storage

In a data lake architecture, data is ingested into object storage.
Object storage stores data with metadata, making it easier to locate and retrieve data and improving performance.
Object storage is also an optimal and secure way to exchange files on the cloud.

!!! warning

    Dumping all data into the lake will result in a "data swamp"

Few challenges with the object storage:

- optimizing storage
- improving observability
- hardening security

## **Challenge**: Ingest files into GCP cloud storage

In this example, we will ingest both structured and unstructured files into GCP cloud storage.
There are many ways to ingest files into GCP cloud storage, and we will use the bash script.

!!! warning

    You need to have Google Cloud Platform account to run below code.
    You can create [here](https://cloud.google.com/free/?utm_source=google&utm_medium=cpc&utm_campaign=emea-none-all-none-dr-sitelink-all-all-trial-e-gcp-1011340&utm_content=text-ad-none-any-DEV_c-CRE_500236788633-ADGP_Hybrid+%7C+BKWS+-+EXA+%7C+Txt+-+GCP+-+General+-+v3-KWID_43700060389294294-aud-606988878854:kwd-26415313501-userloc_1000013&utm_term=KW_google%20cloud%20platform-ST_google+cloud+platform-NET_g-&gad_source=1&gclid=CjwKCAjw9cCyBhBzEiwAJTUWNeR69VpTp2BDvmta6DiU61lqCoaob3T9RqRJqTn6fpm2bJrWWo5XgRoCf84QAvD_BwE&gclsrc=aw.ds)

1. Download the CSV files from a dataset called `on-time performance data`, which is about the air carrier's quality of service.

2. Unzip and inspect the file view some early records of the CSV.

```bash
curl https://www.bts.dot.gov/sites/bts.dot.gov/files/docs/legacy/additional-attachment-files/ONTIME.TD.201501.REL02.04APR2015.zip --output data.zip
apt-get install unzip
unzip data.zip
head ontime.td.201501.asc
```

3. Create a Google Cloud Storage bucket using the command

```bash
gsutil mb -l us-central1 gs://{bucket_name}
```

4. Ingest the file into the bucket using the command

```bash
gsutil -m cp ontime.td.201501.asc gs://{bucket_name}/raw
```
