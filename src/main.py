import os


def verificationanswer(uanswer,min,max):
    try:
        if int(uanswer) < int(min) or int(uanswer)>int(max):
            return False
        else:
            return True
    except:
        False


def verificationdata(user,password):
    try:
        with open("data/"+user+"/task.txt", "r") as user:
            userlist=user.readlines()
            passwordsaved=userlist[1]
            passwordsaved=passwordsaved.strip()
            if passwordsaved==password:
                user.close()
                return True
            else:
                user.close()
                return False
    except:
        return False
        

def showmenu():
    print("MENÚ\n")
    print("1. Ver todas tus tareas.")
    print("2. Ver tus pendientes.")
    print("3. Ver tus tareas completadas.")
    print("4. Agregar tarea.")
    print("5. Eliminar tarea.\n")
    uanswer=input(": ")
    is_valid=verificationanswer(uanswer,1,5)
    if is_valid:
        return uanswer
    else:
        print("Escoge una respuesta válida.\n")
        return showmenu()


def showtask(user,alltask,indicator):
    if int(indicator)==int(1):
        if len(alltask)!=0:
            print("Estas son todas tus tareas.\n")
            for task in alltask:
                print(task.strip())
            start(user)
        else:
            print("No tienes tareas aun.\n")
            start(user)
            
    elif int(indicator)==int(2):
        print("Estas son tus tareas pendientes:\n")
        for task in alltask:
            if task[1]==" ":
                print(task.strip())
        start(user)
    
    elif int(indicator)==(3):
        print("Estas son tus tareas completadas:\n")
        for task in alltask:
            if task[1]=="X":
                print(task.strip())
        start(user)
        

def addtask():
    pass


def deletetask():
    pass    
        

def start(user):
    task=open("data/"+user+"/task.txt", "r")
    tasklist=task.readlines()
    task.close()
    name=tasklist[2]
    name=name.strip()
    alltask=tasklist[3:]
    
    
    print("================================")
    print("\nBienvenido "+name)
    print("Qué quieres hacer hoy?\n")
    uanswer=showmenu()
    
    if int(uanswer)!=int(4) and int(uanswer)!=int(5):
        showtask(user,alltask,uanswer)
    else:
        if int(uanswer)==int(4):
            addtask()
        else:
            deletetask()
    
    
      
    


def login():
    user=input("Escribe tu usuario: ")
    password=input("Escribe tu contraseña: ")
    is_valid=verificationdata(user, password)
    
    if is_valid:
        start(user)
    else:
        print("Tus datos no están registrados o están equivocados.\n")
        run()
        

def singup():
    user=input("Escribe tu usuario:")
    
    if os.path.isdir("data/"+ user):
        print("Este usuario no está disponible, intenta otro.\n")
        singup()
    else:
        password=input("Escribe tu contraseña: ")
        name=input("Escribe tu nombre: ")
        
        os.mkdir("data/"+user)
        task=open("data/"+user+"/task.txt","w")
        task.write(user+"\n")
        task.write(password+"\n")
        task.write(name+"\n")
        task.close()
        
        print("Tu registro ha sido exitoso!\n")
        run()
        
        
def run():
    print("1. Iniciar sesión.")
    print("2. Crear cuenta.")
    uanswer=(input(": "))
    is_valid=verificationanswer(uanswer,1,2)
    
    if is_valid:
        if int(uanswer)==int(1):
            login()
        else:
            print("Iniciemos tu proceso de registro.\n")
            singup()
    else:
        print("Escribe una opción válida.\n")
        run()
        
    
if __name__ =='__main__':
    print("Bienvenido a task manager\n")
    run()