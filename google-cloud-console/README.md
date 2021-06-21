# Deployment

This repository is set up to deploy to [Google Cloud SQL](https://cloud.google.com/sql) and
[Google Cloud Run](https://cloud.google.com/run). It uses an immutable CI/CD flow via
[Google Cloud Build](https://cloud.google.com/cloud-build). Deploying the backend is as simple as making a pull
request and merging it. With that being said, there are some prerequisites to fulfil before running your first
deployment.

---

### GitHub Setup

1. Navigate to your GitHub repository and create the following branches:
    - `production`
    - `development` (default)

---

### Google Cloud Console Setup

1. [Create a Google Cloud Console Account](https://console.cloud.google.com).
2. [Create a new Project Name and ID](https://console.cloud.google.com/projectcreate).
3. [Enable the Cloud Build API](https://console.cloud.google.com/apis/library/cloudbuild.googleapis.com).
4. [Enable the Google Cloud SQL Admin API](https://console.cloud.google.com/apis/library/sqladmin.googleapis.com).
5. [Enable the Google Cloud Run Admin API](https://console.developers.google.com/apis/library/run.googleapis.com).
6. [Enable the Google Container Registry API](https://console.cloud.google.com/apis/library/containerregistry.googleapis.com).

##### IAM

1. [Update the `@cloudbuild` service account to include the following roles](https://console.cloud.google.com/iam-admin/iam):
    - Service Account User
    - Cloud Build Service Agent
    - Cloud SQL Admin
    - Cloud Run Admin

##### Google Cloud SQL

1. [Create a development database instance](https://console.cloud.google.com/sql/create-instance-postgres) with the
   following settings:
   - Instance ID: `development`
   - Default user password: `xxxxxxxxxxxx`
   - Region: `us-central1 (lowa)`
   - Zone: `Any`
   - Database version: `PostgreSQL 12`
   - Additional options
      - Machine type and storage:
         - Cores: `1 shared vCPU`
         - Memory: `0.6GB`
         - Storage Type: `HDD`
         - Storage capacity: `10GB`
         - Enable automatic storage increases: `Unchecked`
         - Encryption: `Google-managed key`
      - Backups, recovery, and high availability
         - Backups: `Unchecked both`
         - Availability: `Single zone`


2. [Create a production database instance](https://console.cloud.google.com/sql/create-instance-postgres) with the
   following settings:
   - Instance ID: `production`
   - Default user password: `xxxxxxxxxxxx`
   - Region: `us-central1 (lowa)`
   - Zone: `Any`
   - Database version: `PostgreSQL 12`
   - Additional options
      - Machine type and storage:
         - Cores: `1 shared vCPU`
         - Memory: `0.6GB`
         - Storage Type: `SSD`
         - Storage capacity: `10GB`
         - Enable automatic storage increases: `Unchecked`
         - Encryption: `Google-managed key`
      - Backups, recovery, and high availability
         - Backups: `Unchecked both`
         - Availability: `Single zone`

##### Google Cloud Run

1. Domain mapping
2. ...
3. ...
4. ...
5. ...
6. ...

## Deploying to Development:

Create a new feature branch from `development`. Write some code, push it, and make a pull request back to
`development`. Creating a pull request automatically runs unit/integration tests via Cloud Build. Do not merge
this until all tests have passed. Once you merge your code, a build, db migration, and release will run via Cloud
Build. After that has finished, check the Cloud Build logs and you will see the URL of the newly deployed development
server.

## Deploying to Production:

Once you are satisfied with the state of your server in the development environment, you can promote it to the
production environment by making another pull request from `development -> production`. Once you merge your code, a
re-tag, db migration, and release will run via Cloud Build. After that has finished, check the Cloud Build logs and
you will see the URL of the newly deployed production server.
