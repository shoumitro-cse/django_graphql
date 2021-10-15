# Building GraphQL APIs in Django with Graphene

GraphQL is an open-source data query and manipulation language for APIs, and a runtime for fulfilling queries with existing data. It was developed internally by Facebook in 2012 before being publicly released in 2015. It allows clients to define the structure of the data required, and the same structure of the data is returned from the server, therefore preventing unnecessary data from being returned.

GraphQL has three primary operations: Queries for reading data, Mutations for writing data, and Subscriptions for automatically receiving real-time data updates. A GraphQL server provides clients with a predefined schema – a model of the data that can be requested. The schema serves as common ground between the client and the server.

In this tutorial we will use Graphene, a GraphQL framework for Python, to build a Django API that uses queries and mutations. some query example are given below..


# API
python manage.py runserver 127.0.0.1:7000
http://127.0.0.1:7000/graphql

# Username & Password
USER: shoumitro
PW: QWERTYU12345678


##  The GraphQL code below is requesting all the books from the database.
query {
  allBooks {
    id
    title
    author
    yearPublished
    review
  }
}


##  single book by its id
query {
  book(bookId: 2) {
    id
    title
    author
  }
}


## Creating a book
mutation createMutation {
  createBook(bookData: {title: "Things Apart", author: "Chinua Achebe", yearPublished: "1985", review: 3}) {
    book {
      title,
      author,
      yearPublished,
      review
    }
  }
}


## Updating an existing book
mutation updateMutation {
  updateBook(bookData: {id: 6, title: "Things Fall Apart", author: "Chinua Achebe", yearPublished: "1958", review: 5}) {
    book {
      title,
      author,
      yearPublished,
      review
    }
  }
}


## Deleting a book
mutation deleteMutation{
  deleteBook(id: 6) {
    book {
      id
    }
  }
}


## We will use TokenAuth to authenticate the User with its username and password and obtain the JSON Web Token.
mutation {
  tokenAuth(username:"shoumitro", password: "QWERTYU12345678") {
    token
    payload
    refreshExpiresIn
  }
}


# We will use VerifyToken to verify that the token passed as an argument is a valid token.
mutation {
  verifyToken(token:"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InNob3VtaXRybyIsImV4cCI6MTYzNDI5Mjk4MCwib3JpZ0lhdCI6MTYzNDI5MjY4MH0.FHHJOJcleu1ukk8sXHvzwUFEgKKXjZlqRgBwSrqA3Hw") {
    payload
  }
}


# refreshToken to obtain a brand new token with renewed expiration time:
mutation {
  refreshToken(token:"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InNob3VtaXRybyIsImV4cCI6MTYzNDI5Mjk4MCwib3JpZ0lhdCI6MTYzNDI5MjY4MH0.FHHJOJcleu1ukk8sXHvzwUFEgKKXjZlqRgBwSrqA3Hw") {
    payload
    refreshExpiresIn
    token
  }
}


# show user list

query {
  users {
    id
    username
    email
    lastName
    firstName
    password
  }
}


## Creating a user
mutation createMutation {
  createUser(username:"test", password:"123456", email:"abc@gmail.com") {
    user {
      id
			username
      password
      email
      isSuperuser
      isStaff
      isActive
      firstName
      lastName
      lastLogin
      dateJoined
      __typename
    }
  }
}



mutation createUser {
  createUser(username: "test5", password: "1234", email: "ab@gmail.com") {
    token
    user {
      username
    }
  }
}


# get current user
query {
  me {
    id
    username
    email
    lastName
    firstName
    password
  }
}


# combine query
query {
  
  allBooks {
    id
    title
    author
    yearPublished
    review
  }, 
  users {
    id
    username
    email
    lastName
    firstName
    password
 },
 me {
    id
    username
    email
    lastName
    firstName
    password
  },
}




# What is JWT Authentication?
JSON Web Token (JWT) is a JSON encoded representation of a claim(s) that can be transferred between two parties. The claim is digitally signed by the issuer of the token, and the party receiving this token can later use this digital signature to prove the ownership on the claim.

JWTs can be broken down into three parts: header, payload, and signature. Each part is separated from the other by dot (.), and will follow the below structure:

https://www.softwaresecured.com/security-issues-jwt-authentication/

https://jwt.io/

Example:
Header.Payload.Signature

Encoded:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDJ9.X3In9n-G_bltl9jAcNiEB6j_JoZzqe5HiaUf0zLiMdw

Decoded:
1. HEADER:ALGORITHM & TOKEN TYPE
{
  "alg": "HS256",
  "typ": "JWT"
}

2. PAYLOAD:DATA
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}
3. VERIFY SIGNATURE
HMACSHA256(base64UrlEncode(header) + "." +base64UrlEncode(payload), your-256-bit-secret) secret base64 encoded



HEADER
The information contained in the header describes the algorithm used to generate the signature. The decoded version of the header from the above example looks like:

{

 “alg”: “HS256”,

 “typ”: “JWT”

}

HS256 is the hashing algorithm HMAC SHA-256 used to generate the signature in the above example.


PAYLOAD
All the claims within JWT authentication are stored in this part. Claims are used to provide authentication to the party receiving the token. For example, a server can set a claim saying ‘isAdmin: true’ and issue it to an administrative user upon successfully logging into the application. The admin user can now send this token in every consequent request he/she sends to the server to prove their identity.

The decoded version of the payload from the JWT example provided above looks like:

{

 “sub”: “1234567890”,

 “name”: “John Doe”,

 “iat”: 1516239022

}

The ‘name’ field is used to identify the user to whom the token was issued to. The ‘sub’ and ‘iat’ are examples of registered claims and are short for ‘subject’ and ‘issued at’.


SIGNATURE
The signature part of a JWT is derived from the header and payload fields. The steps involved in creating this signature are described below:

1. Combine the base64url encoded representations of header and payload with a dot (.)

base64UrlEncode(header) + “.” + base64UrlEncode(payload)
 
2. Hash the above data with a secret-key only known to the server issuing the token. The hashing algorithm is the one described inside the header.

hash_value = hash([base64UrlEncode(header) + “.” + base64UrlEncode(payload)], secret-key)

3. Base64Url encode the hash value obtained from the step above

Signature = base64UrlEncode(hash_value)

Because the ‘secret-key’ is only known to the server, only it can issue new tokens with a valid signature. Users can not forge tokens as producing a valid Signature for the token requires the knowledge of the ‘secret-key’.

JWT find their applications in various authentication mechanisms. These are typically passed in the Authorization header when a user submits a request to the client.

eg:
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0I joxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

