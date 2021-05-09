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
