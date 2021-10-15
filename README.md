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


