# Espresso ♨️

A NodeJS project setup tool

## Getting Started
Clone respository in your project folder

`python espresso.py`
  
### Architecture Support
Espresso gives Model View Controller, RESTful and Graphql architecture setup.

- MVC
  - Dependencies Installed

    ```
    bcryptjs
    body-parser
    ejs
    express
    jsonwebtoken
    jwt-decode
    ```
   - Project Architecture
   
   ```
   
    ├── controllers
    ├── middleware
    ├── models
    ├── node_modules
    ├── public
    │   ├── css
    │   ├── script
    ├── routes
    ├── utils
    │   ├── db.js (If chosen)
    ├── views
    ├── package-lock.json
    ├── package.json
    ├── app.js
    └── .gitignore

    ```
   
   
- RESTful
  - Dependencies Installed

    ```
    bcryptjs
    body-parser
    express
    express-validator
    jsonwebtoken
    socket.io 
    ```
   - Project Architecture
   
   ```
   
    ├── controllers
    ├── middleware
    ├── models
    ├── node_modules
    ├── routes
    ├── utils
    │   ├── db.js (If chosen)
    ├── package-lock.json
    ├── package.json
    ├── socket.js
    ├── app.js
    └── .gitignore

    ```
    
- Restful with GraphQL
  - Dependencies Installed

    ```
    bcryptjs
    body-parser
    express
    express-validator
    express-graphql
    graphql
    jsonwebtoken
    validator 
    ```
   - Project Architecture
   
   ```
   
    ├── controllers
    ├── graphql
    │   ├── resolver.js
    │   ├── schema.js
    ├── middleware
    ├── models
    ├── node_modules
    ├── routes
    ├── utils
    │   ├── db.js (If chosen)
    ├── package-lock.json
    ├── package.json
    ├── app.js
    └── .gitignore

    ```
    
### Database Support
Firebase, MySQL and MongoDB Atlas setup is provided, you can skip it by pressing ENTER when asked in terminal.
Note : Only for Firebase option, db.js is created in the root directory of your project

- Firebase
  - Additional Dependencies Installed
  
    ```
      firebase
    ```
  - Additional Files
  
   ```
    ├── config.js
    ├── db.js
    ├── .env
    ```
    
 - MongoDB Atlas
   - Additional Dependencies Installed
  
     ```
       mongoose
     ```
    - Additional Files
  
    ```
    ├── utils
    │   ├── config.js
    ``` 
 
 - MongoDB Atlas
   - Additional Dependencies Installed
  
    ```
      mysql2
      sequelize
    ```
    - Additional Files
     
       None
    
    
    

