# GQL File upload

A simple example that demonstrates file uploade powered by a React client and a graphql server created with Django.

## Getting started

This project uses [pipenv](https://pipenv.pypa.io/en/latest/install/) to manage virtual environments and dependencies.

To start your Django server, In one terminal window run the following commands:

`$ cd backend`

`$ pipenv shell`

`$ pipenv install`

`$ ./manage.py runserver`

To start your React client, in a separate terminal window and run the following commands:

`$ cd ui`

`$ yarn install`

`$ yarn start`

## Third party dependencies

This project requires access to a cloud vendor. It was built using [Digital Ocean Spaces](https://www.digitalocean.com/products/spaces/), but since Spaces is designed to work exactly like S3, it should be just as easy to have S3 be your storage layer to use this.

- Create a digital ocean account
- Create a new space on the **Manage > Spaces** tab.
- Go to **Account > API** and Generate a new Key
- Update the `.env` file with the name of your Space (`AWS_STORAGE_BUCKET_NAME`), location (`AWS_LOCATION`), its endpoint (`AWS_S3_ENDPOINT_URL`), the Access Key ID (`AWS_ACCESS_KEY_ID`), and Secret Access Key (`AWS_SECRET_ACCESS_KEY`).

### File structure

```
├── README.md
├── backend
│   ├── Pipfile
│   ├── Pipfile.lock
│   ├── api
│   ├── backend
│   └── manage.py
├── client
│   ├── README.md
│   ├── node_modules
│   ├── package.json
│   ├── public
│   ├── src
│   └── yarn.lock
└── docker-compose.yml
```
