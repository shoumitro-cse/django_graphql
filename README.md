# What is jWT Token?
Django REST Framework is an excellent tool for building APIs in Django. It comes with Authentication Classes that help to build secure APIs without spending a lot of time.

Django REST Framework comes with various default Authentication Classes. BasicAuthentication, SessionAuthentication, and TokenAuthentication to name a few.

Token-based authentication is the most preferred method of implementing authentication in modern APIs. In this mechanism, the server generates a token for the authenticated user and the user has to send the token along with all the HTTP requests to identify themselves.

DRF’s default TokenAuthentication class is a very basic version of this approach. It generates one token for each user and stores it into the database. While it is considered fine to use TokenAuthentication for Server-to-Server communication, it does not play well in modern scenarios with Single Page Applications.

The way TokenAuthentication is designed, it deletes the token every time the user logs out and generates a new one on login. This means making multi-device logins work is usually a pain. To get around this, one way is to choose to not delete the token on logout, but that is not recommended because it is an insecure approach to fix this problem.


JWT Primer:

JWT, short for JSON Web Token is an open standard for communicating authorization details between server and client. Unlike TokenAuthentication where the token is randomly generated and the authentication details are stored on the server, JWT is self-contained. This means that a JSON Web Token contains all the information needed for the server to authenticate the client, the server does not have to store anything.

src: 

https://www.remoteinning.com/blog/how-to-use-jwt-authentication-with-django-rest-framework

https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html


# JWT Authentication Workflow
A user, Bob, comes to your Web Application, he enters his username and password to log in. 

After verifying the credentials, the server issues two JSON Web Tokens to the user. One of them is an Access Token and the other is a Refresh Token.

The frontend of your application then stores the tokens securely and sends the Access Token in the Authorization header of all requests it then sends to the server.


The server then decodes and verifies the access token and identifies Bob as the logged-in user.

Access Tokens are short-lived, meaning they are only supposed to be used for 10-15 minutes (depending on the configuration). This is done to prevent misuse of the Access Token if an attacker gets hold of it using attacks like XSS. In such a case the token will stop working after it has expired.

After about 15 minutes, when the user tries to access something again, the frontend finds out that the access token is now expired. The frontend then proceeds to refresh the token by sending the refresh token to the “refresh” endpoint.


After refreshing the tokens, the frontend then stores and uses the new access token for further requests.


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

