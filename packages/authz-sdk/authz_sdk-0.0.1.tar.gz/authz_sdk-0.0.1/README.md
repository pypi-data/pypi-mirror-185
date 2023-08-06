# Authz Python SDK

This is the Authz development kit for Python.

## Installation

You can install in your projects by importing the following dependency:

```bash
$ pip install authz-python-sdk
```

## Usage

You have to instanciate a new Authz Client in your code by doing:

```python
client = authz.Client('localhost:8081', '<client_id>', '<client_secret>')
```

Once the client is instanciate, you have access to all the gRPC methods under `stub` property.

In order to create a new Principal, you can use

```python
response = client.stub.PrincipalCreate(api_pb2.PrincipalCreateRequest(
    id='user-123',
    attributes=[
        api_pb2.Attribute(key='email', value='johndoe@acme.tld'),
    ],
))
```

To declare a new resource:

```python
response = client.stub.ResourceCreate(api_pb2.ResourceCreateRequest(
    id='post.456',
    kind='post',
    value='456',
    attributes=[
        api_pb2.Attribute(key='owner_email', value='johndoe@acme.tld'),
    ],
))
```

You can also declare a new policy this way:

```python
response = client.stub.PolicyCreate(api_pb2.PolicyCreateRequest(
    id='post-owners',
    resources=['post.*'],
    actions=['edit', 'delete'],
    attribute_rules=[
        'principal.email == resource.owner_email',
    ],
))
```

Then, you can perform a check with:

```python
result = client.stub.Check(api_pb2.CheckRequest(
    checks=[
        api_pb2.Check(
            principal='user-123',
            resource_kind='post',
            resource_value='123',
            action='edit',
        )
    ]
))

if result.checks[0].is_allowed:
    # do something
```

Please note that you have access to all the gRPC methods [declared here](https://github.com/eko/authz/blob/master/backend/api/proto/api.proto) in the proto file.

## Configuration

This SDK connects over gRPC to the backend service. Here are the available configuration options:

| Property | Description |
| -------- | ----------- |
| ClientID | Your service account client id used to authenticate |
| ClientSecret | Your service account client secret key used to authenticate |
| GrpcAddr | Authz backend to connect to |
