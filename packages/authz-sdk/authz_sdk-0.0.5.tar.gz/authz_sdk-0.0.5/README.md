# Authz Python SDK

This is the Authz development kit for Python.

## Installation

You can install in your projects by importing the following dependency:

```bash
$ pip install authz-sdk
```

## Usage

You have to instanciate a new Authz Client in your code by doing:

```python
client = authz.Client('localhost:8081', '<client_id>', '<client_secret>')
```

Once the client is instanciate, you have access to all the gRPC methods under `stub` property.

In order to create a new Principal, you can use

```python
response = client.stub.PrincipalCreate(proto.PrincipalCreateRequest(
    id='user-123',
    attributes=[
        proto.Attribute(key='email', value='johndoe@acme.tld'),
    ],
))
```

To declare a new resource:

```python
response = client.stub.ResourceCreate(proto.ResourceCreateRequest(
    id='post.456',
    kind='post',
    value='456',
    attributes=[
        proto.Attribute(key='owner_email', value='johndoe@acme.tld'),
    ],
))
```

You can also declare a new policy this way:

```python
response = client.stub.PolicyCreate(proto.PolicyCreateRequest(
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
is_allowed = client.IsAllowed(
    principal='user-123',
    resource_kind='post',
    resource_value='123',
    action='edit',
)

if is_allowed:
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
