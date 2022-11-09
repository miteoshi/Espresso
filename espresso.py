from initials import *
import os
import json


os.system("")

class symbols:
   TICK = "\u2713 "
   SPACE = '  '

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   NORMAL = '\033[0;37;40m'
   LIGHT = '\033[2m'
   ITALIC = '\033[3m'

class error_c:
   NAME = 'name can no longer contain capital letters'
   DATABSE = 'Oops!, "f" for Firebase or "m" for MongoDB Atlas or "s" for MySQL'
   YN = 'Bruh.., "y" for Yes and "n" for No'
   DIR_P = "Directory already present, use different name" 




def create_path(name):
   return os.path.join(os.getcwd(),name)


while True:
   project_name =input(f"{color.BOLD}{symbols.TICK}Project name: {color.NORMAL}")
   path = create_path(project_name)
   res = any(ele.isupper() for ele in project_name)
   
   if res:
      print(f'\n{color.RED}{symbols.SPACE}{error_c.NAME}{color.NORMAL}\n')
   elif os.path.isdir(path):
      print(f'\n{color.RED}{symbols.SPACE}{error_c.DIR_P}{color.NORMAL}\n')
   else:
      description = input(f"{color.BOLD}{symbols.TICK}Description {color.YELLOW}(Optional){color.NORMAL}: ")
      author = input(f"{color.BOLD}{symbols.TICK}Author{color.YELLOW} (Optional){color.NORMAL}: ")
      break
   

initial = {
  "name": project_name,
  "version": "1.0.0",
  "description": description,
  "main": "app.js",

  "scripts" : {
   "test": "echo \"Error: no test specified\" && exit 1",
   "start": "nodemon app.js",
   },

   "repository": {
      "type": "git",
      "url":"joshipiyush9969/Espresso",
   },

   "author":author,
   "license":"ISC"
}



while True:
   rest_bool = input(f"\n{symbols.TICK}Do you want it be to{color.CYAN} Restful {color.NORMAL}(y/n): ")
   if rest_bool.lower() != "y" and rest_bool.lower() != "n":
      print(f'\n{color.RED}{symbols.SPACE}{error_c.YN}{color.NORMAL}\n')
   else:
      break

if(rest_bool == "y"):
   while True:
      graphql_bool = input(f"\n{symbols.TICK}Do you want{color.PURPLE} GraphQL {color.NORMAL}initialized?(y/n): ")
      if graphql_bool.lower() != "y" and graphql_bool.lower() != 'n':
         print(f'\n{color.RED}{symbols.SPACE}{error_c.YN}{color.NORMAL}\n')
      else:
         break
else:
   graphql_bool = "n"


while True:
   database = input(f"\n{symbols.TICK}Database Programs:{color.YELLOW} Firebase(f) {color.NORMAL}/{color.BLUE} MySQL(s){color.NORMAL} /{color.GREEN} MongoDB Atlas(m){color.NORMAL}{color.YELLOW} (Optional){color.NORMAL}:")
   if database != "m" and database!= "f" and database!= "s" and database!= "":
      print(f'\n{color.RED}{symbols.SPACE}{error_c.DATABSE}{color.NORMAL}\n')
   else:
      break


try:
    os.makedirs(path, exist_ok = True)

except OSError as error:
    print(f"{color.RED}{symbols.SPACE}Directory '%s' can not be created{color.NORMAL}" % project_name)


try:

   # Writing to package.json
   json_object = json.dumps(initial, indent=1)
   file = "./{p}/package.json".format(p = project_name)
   with open(file,'w') as outfile:
       outfile.write(json_object)


   os.system('cmd /c' "type NUL > ./{p}/app.js".format(p = project_name))
   os.system('cmd /c' "type NUL > ./{p}/.gitignore".format(p = project_name))

   #Writing to .gitignore
   file = "./{p}/.gitignore".format(p = project_name)
   with open(file,'w') as outfile:
       outfile.write("./node_modules\n./utils\n")

   #Writing to app.js
   appjs = "./{p}/app.js".format(p = project_name)
   starter(appjs)

   os.system('cmd /c "npm --prefix ./{p} install express body-parser bcryptjs jsonwebtoken"'.format(p = project_name))
   os.system('cmd /c "npm --prefix ./{p} install nodemon --save-dev"'.format(p = project_name))
   
   
   os.system('cmd /c' "git init ./{p}".format(p = project_name))

   
   
   os.makedirs(create_path('./{p}/controllers'.format(p = project_name)), exist_ok = True)
   os.makedirs(create_path('./{p}/middleware'.format(p = project_name)), exist_ok = True)
   os.makedirs(create_path('./{p}/models'.format(p = project_name)), exist_ok = True)
   os.makedirs(create_path('./{p}/routes'.format(p = project_name)), exist_ok = True)
   os.makedirs(create_path('./{p}/utils'.format(p = project_name)), exist_ok = True)

   if(rest_bool == 'n'):
      os.makedirs(create_path('./{p}/views'.format(p = project_name)), exist_ok = True)
      os.makedirs(create_path('./{p}/views/components'.format(p = project_name)), exist_ok = True)
      os.makedirs(create_path('./{p}/public'.format(p = project_name)), exist_ok = True)
      os.makedirs(create_path('./{p}/public/script'.format(p = project_name)), exist_ok = True)
      os.makedirs(create_path('./{p}/public/css'.format(p = project_name)), exist_ok = True)

      os.system('cmd /c "npm --prefix ./{p} install ejs jwt-decode"'.format(p = project_name))

      #Writing to app.js
      helperHeader('mvc',appjs)

      
   if(graphql_bool == 'y'):
      os.makedirs(create_path('./{p}/graphql'.format(p = project_name)), exist_ok = True)
      os.system('cmd /c' "type NUL > ./{p}/graphql/resolver.js".format(p = project_name))
      os.system('cmd /c' "type NUL > ./{p}/graphql/schema.js".format(p = project_name))

      os.system('cmd /c "npm --prefix ./{p} install express-graphql graphql express-validator validator"'.format(p = project_name))
      os.system('cmd /c "npm --prefix ./{p} install graphql"'.format(p = project_name))

      #Writing to app.js
      helperHeader('graph',appjs)

      #Handling Schema and Resolver
      resolver = "./{p}/graphql/resolver.js".format(p = project_name)
      schema = "./{p}/graphql/schema.js".format(p = project_name)
      
      with open(resolver,'w') as reso:
         reso.write('module.exports = {\n'
                       '  startInit: async function (args,req) {\n'
                       '    return "Hello from graphql"\n'
                       '   }\n'
                       '};\n')
      
         reso.close()
      
      with open(schema,'w') as sche:
         sche.write('const { buildSchema } = require("graphql");\n'
                    '\n'
                    'module.exports = buildSchema(`\n'
                    '\n'
                    '    type Init{\n'
                    '        word:String!\n'
                    '    }\n'
                    '\n'
                    '    type RootQuery {\n'
                    '        startInit:String!\n'
                    '    }\n'
                    '\n'
                    '    schema {\n'
                    '        query: RootQuery\n'
                    '    }\n'
                    '`);')
         sche.close()

      

   if(rest_bool == 'y' and graphql_bool == 'n'):
      
      #socket.js
      os.system('cmd /c' "type NUL > ./{p}/socket.js".format(p = project_name))
      socketjs = "./{p}/socket.js".format(p = project_name)
      socket_init(socketjs)

      #Writing to app.js
      helperHeader("rest",appjs)
      
      os.system('cmd /c "npm --prefix ./{p} install express-validator socket.io"'.format(p = project_name))


## App.js

   if(graphql_bool == 'y'):
      grap_mvc_end(appjs)
   elif(rest_bool == 'y'):
      rest_end(appjs)
   else:
      grap_mvc_end(appjs)



 ## Database Packages

   if(database == 's'):
      dbjs = "./{p}/utils/db.js".format(p = project_name)
      os.system('cmd /c' "type NUL >" + dbjs)
      os.system('cmd /c "npm --prefix ./{p} install mysql2 sequelize"'.format(p = project_name))
      
      #Writing to utils/db.js
      mysql_init(dbjs,appjs)

      

   elif(database == 'f'):
      os.system('cmd /c "npm --prefix ./{p} install firebase"'.format(p = project_name))
      dbjs = "./{p}/db.js".format(p = project_name)
      env_ = "./{p}/.env".format(p = project_name)
      config_ = "./{p}/config.js".format(p = project_name)

      os.system('cmd /c' "type NUL >"+dbjs)
      os.system('cmd /c' "type NUL >"+env_)
      os.system('cmd /c' "type NUL >"+config_)
      
      #Writing to db.js,.env,config.js
      firebase_init(dbjs,env_,config_,appjs)

      #Writing to .gitignore
      git_ = "./{p}/.gitignore".format(p = project_name)
      with open(git_,'a') as outfile:
         outfile.write("./db.js\n./.env\n./config.js\n")


   elif(database == "m"):
      os.system('cmd /c "npm --prefix ./{p} install mongoose"'.format(p = project_name))
      
      configjs = "./{p}/utils/config.js".format(p = project_name)
      os.system('cmd /c' "type NUL >" + configjs)
      
      #Writing to utils/db.js and app.js
      mongo_init(configjs,appjs)
   else:
      pass


   print(f"{color.CYAN}\n{symbols.SPACE}cd {project_name}\n{symbols.SPACE}npm start{color.NORMAL}")
      

except OSError as error:
   print(f"{color.RED}{symbols.SPACE}Couldn't perform the operation{color.NORMAL}")
   print(f"{color.RED}{symbols.SPACE}exiting{color.NORMAL}")
   exit()
