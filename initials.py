def graphHeader(path):
    with open(path,'a') as file:
        file.write( 'const graphqlSchema = require("./graphql/schema");\n'
                    'const graphqlResolver = require("./graphql/resolver");\n'
                    'const { graphqlHTTP } = require("express-graphql");\n'
                    'app.use((req, res, next) => {\n'
                    '  res.setHeader("Access-Control-Allow-Origin", "*");\n'
                    '  res.setHeader(\n'
                    '    "Access-Control-Allow-Methods",\n'
                    '    "OPTIONS, GET, POST, PUT, PATCH, DELETE"\n'
                    '  );\n'
                    '  res.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");\n'
                    '  if (req.method === "OPTIONS") {\n'
                    '    return res.sendStatus(200);\n'
                    ' }\n'
                    '  next();\n'
                    '});\n'
                    '\n'
                    'app.use(\n'
                    '  "/graphql",\n'
                    '  graphqlHTTP({\n'
                    '    schema: graphqlSchema,\n'
                    '    rootValue: graphqlResolver,\n'
                    '    graphiql: true,\n'
                    '  })\n'
                    ');\n')
        file.close()


def restHeader(path):
    with open(path,'a') as file:
        file.write( 'app.use((req, res, next) => {\n'
                    '  res.setHeader("Access-Control-Allow-Origin", "*");\n'
                    '  res.setHeader(\n'
                    '    "Access-Control-Allow-Methods",\n'
                    '    "OPTIONS, GET, POST, PUT, PATCH, DELETE"\n'
                    '  );\n'
                    '  res.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");\n'
                    '  next();\n'
                    '})\n')
        file.close() 

def mvcHeader(path):
    with open(path,'a') as file:
        file.write('const path = require("path");\n\n'
                   'app.use(express.static(path.join(__dirname, "/public")));\n\n'
                   'app.set("view engine", "ejs");\n'
                   'app.set("views", "views");\n'
                   'app.set("trust proxy", true)\n\n')
        file.close()


## HELPER FUNCTION REQUIRED IMPORTS AND HEADERS
def helperHeader(type,path):
    if(type == 'graph'):
        graphHeader(path)
    elif(type == 'rest'):
        restHeader(path)
    elif(type == 'mvc'):
        mvcHeader(path)
    else:
        pass


## Database

#MYSQL
def mysql_init(db_path,appjs_path):
    with open(db_path, "a") as file:
        file.write('const { Sequelize } = require("sequelize");\n'
                   '\n'
                   'const db = new Sequelize("databaseName", "user", "password", {\n'
                   '  dialect: "mysql",\n'
                   '  host: "localhost",\n'
                   '  timezone: "+05:30"\n'
                   '});\n\n\n'
                   'module.exports = db;')
        file.close()
    
    with open(appjs_path,'a') as file:
        file.write('\n//mySql\n'
                   'const sequelize = require("./utils/db");\n'
                   '//sequelize.sync({force:true}).then(()=>{app.listen(8080)})\n//.catch((err) => {console.log(err)});\n')
        file.close()

#FIREBASE
def firebase_init(path,env_path,config_path,appjs_path):
    with open(path,"a") as file:
        file.write('const firebase = require("firebase");\n'
                   'const config = require("./config")\n'
                   '\n'
                   'const db = firebase.initializeApp(config.firebaseConfig);\n'
                   '\n'
                   'module.exports = db\n')
        file.close()
    
    with open(appjs_path,"a") as file:
        file.write('\n\nconst cors = require("cors");\n'
                   'const config = require("./config");\n'
                   '\n//Use port from config file\n'
                   '//app.listen(config.port, () => console.log("App is listening on url http://localhost:" + config.port));\n')
        file.close()
    
    firebase_env_setup(env_path)
    firebase_config(config_path)


def firebase_env_setup(path):
    with open(path,"a") as file:
        file.write('NODE_ENV=production\n'
                   '#express server config\n\n'
                   'PORT=8080\n'
                   'HOST=localhost\n'
                   'HOST_URL=http://localhost:8080\n\n\n'
                   '#firebase database config\n\n'
                   'API_KEY=\n'
                   'AUTH_DOMAIN=\n'
                   'DATABASE_URL=\n'
                   'PROJECT_ID=\n'
                   'STORAGE_BUCKET=\n'
                   'MESSAGING_SENDER_ID=\n'
                   'APP_ID=\n')
        file.close()

def firebase_config(path):
    with open(path,"a") as file:
        file.write(
                   'const dotenv = require("dotenv");\n'
                   'const assert = require("node:assert").strict\n\n'
                   'dotenv.config();\n\n'
                   'const {\n    PORT,\n    HOST,\n    HOST_URL,\n    API_KEY,\n    AUTH_DOMAIN,\n    DATABASE_URL,\n    PROJECT_ID,\n    STORAGE_BUCKET,\n    MESSAGING_SENDER_ID,\n    APP_ID\n} = process.env;\n'
                   '\n'
                   'assert(PORT, "PORT is required");\n'
                   'assert(HOST, "HOST is required");\n\n'
                   'module.exports = {\n'
                   '    port: PORT,\n    host: HOST,\n    url: HOST_URL,\n    firebaseConfig: {\n'
                   '        apiKey: API_KEY,\n       authDomain: AUTH_DOMAIN,\n        databaseURL: DATABASE_URL,\n        projectId: PROJECT_ID,\n        storageBucket: STORAGE_BUCKET,\n        messagingSenderId: MESSAGING_SENDER_ID,\n        appId: APP_ID\n    }\n}\n')
        file.close()


#MONGODB ATLAS

def mongo_init(config_path,appjs_path):
    with open(config_path,'a') as file:
        file.write('const API_KEY = "YOUR_API_KEY";\n'
                   'module.exports = {\n'
                   '  API_KEY: API_KEY,\n'
                   '};')
        file.close()
    
    with open(appjs_path,'a') as file:
        file.write('\nconst { API_KEY }  = require("./utils/config.js")\n'
                   'const mongoose = require("mongoose");\n\n'
                   '//mongoose.connect(URL).then(()=>{app.listen(8080);})\n//.catch((err) => console.log(err));\n')


## WRITES THE COMMON IMPORTS
def starter(path):
    with open(path,'a') as file:
        file.write('const express = require("express");\n\n'
                   'const bodyParser = require("body-parser");\n\n'
                   '\n'
                   '//routes\n\n'
                   '//models\n\n'
                   'const app = express();\n\n'
                   'app.use(bodyParser.json());\n\n')
        file.close()

## WRITES SOCKET REQUIREMENTS
def socket_init(path):
    with open(path,'a') as file:
        file.write('const {Server} = require("socket.io")\n\n'
                   '\n'
                   'let io;\n'
                   '\n'
                   'module.exports = {\n'
                   '  init: (httpServer) => {\n'
                   '    io = new Server(httpServer, {\n'
                   '      cors: {\n'
                   '        origin: "http://localhost:3000",\n'
                   '      },\n'
                   '    });\n'
                   '    return io;\n'
                   '  },\n'
                   '  getIO: () => {\n'
                   '    if (!io) {\n'
                   '      throw new Error("Socket.io not initialized!");\n'
                   '    }\n'
                   '    return io;\n'
                   '  },\n'
                   '};\n')
        file.close()

## WRITES CONNECTIONS
def rest_end(path):
    with open(path,'a') as file:
        file.write('const server = app.listen(8080);\n\n'
                   'const io = require("./socket").init(server);\n\n'
                   'io.on("connection", (socket) => {\n'
                   '    console.log("Socket is here :)")\n'
                   '});\n')
        file.close()

def grap_mvc_end(path):
    with open(path,'a') as file:
        file.write('app.listen(8080, () => {\n'
                   'console.log("Hello From Node!")\n'
                    '})')
        file.close()
