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
    print("5. completar tarea.")
    print("6. Eliminar tarea.\n")
    print("7. Salir.\n")
    uanswer=input(": ")
    is_valid=verificationanswer(uanswer,1,7)
    if is_valid:
        return uanswer
    else:
        print("Escoge una respuesta válida.\n")
        return showmenu()


def showtask(user,alltask,indicator):
    if int(indicator)==int(1):
        if len(alltask)!=0:
            print("Estas son todas tus tareas.\n")
            print("____________________________")
            for task in alltask:
                print(task.strip())
            print("____________________________")
            input("Presiona una tecla y enter para regresar al menú principal.\n")
            start(user)
        else:
            print("No tienes tareas aun.\n")
            print("____________________________")
            input("Presiona una tecla y enter para regresar al menú principal.\n")
            start(user)
            
    elif int(indicator)==int(2):
        print("Estas son tus tareas pendientes:\n")
        print("____________________________")
        for task in alltask:
            if task[1]==" ":
                print(task.strip())
        print("____________________________")
        input("Presiona una tecla y enter para regresar al menú principal.\n")
        start(user)
    
    elif int(indicator)==(3):
        print("Estas son tus tareas completadas:\n")
        print("____________________________")
        for task in alltask:
            if task[1]=="X":
                print(task.strip())
        print("____________________________")
        input("Presiona una tecla y enter para regresar al menú principal.\n")
        start(user)
        

def addtask(user):
    task = input("Escribe la descripción de la tarea: ")
    os.system("clear")
    task = "| | " + task.strip() + "\n"
    with open("data/"+user+"/task.txt", "a") as taskfile:
        taskfile.write(task)
    print("La tarea ha sido agregada con éxito.\n")
    print("____________________________")
    input("Presiona una tecla y enter para regresar al menú principal.\n")
    start(user)
    

def completetask(user):
    with open("data/"+user+"/task.txt", "r") as taskfile:
        tasks = taskfile.readlines()
        print("Estas son tus tareas:\n")
        for i in range(len(tasks)-3):
            print(str(i+1) + ". " + tasks[i+3].strip())
    
    task_num = input("\nEscribe el número de la tarea que quieres completar: ")
    os.system("clear")
    task_num = int(task_num) - 1
    with open("data/"+user+"/task.txt", "r") as taskfile:
        tasks = taskfile.readlines()
    if task_num < len(tasks) - 3:
        task = tasks[task_num + 3].strip()
        task = "|X|" + task[3:]
        tasks[task_num + 3] = task + "\n"
        with open("data/"+user+"/task.txt", "w") as taskfile:
            taskfile.writelines(tasks)
        print("La tarea ha sido completada con éxito.\n")
        print("____________________________")
        input("Presiona una tecla y enter para regresar al menú principal.\n")
        start(user)
    else:
        print("El número de tarea no es válido.\n")
        print("____________________________")
        input("Presiona una tecla y enter para regresar al menú principal.\n")
        start(user)


def deletetask(user):
    with open("data/"+user+"/task.txt", "r") as taskfile:
        tasks = taskfile.readlines()

    print("Estas son tus tareas:\n")
    for i in range(len(tasks)-3):
        print(str(i+1) + ". " + tasks[i+3].strip())

    task_num = input("Escribe el número de la tarea que quieres eliminar: ")
    os.system("clear")
    is_valid = verificationanswer(task_num, 1, len(tasks)-3)
    
    if is_valid:
        task_num = int(task_num) - 1
        del tasks[task_num+3]
        with open("data/"+user+"/task.txt", "w") as taskfile:
            taskfile.writelines(tasks)
        print("La tarea ha sido eliminada con éxito.\n")
        print("____________________________")
        input("Presiona una tecla y enter para regresar al menú principal.\n")
        start(user)
    else:
        print("El número de tarea no es válido.\n")
        print("____________________________")
        input("Presiona una tecla y enter para regresar al menú principal.\n")
        start(user)    
        

def start(user):
    task=open("data/"+user+"/task.txt", "r")
    tasklist=task.readlines()
    task.close()
    name=tasklist[2]
    name=name.strip()
    alltask=tasklist[3:]
    
    
    print("================================")
    print("\nBienvenido "+name+"\n")
    print("¿Qué quieres hacer hoy?\n")
    uanswer=showmenu()
    os.system("clear")
    
    if int(uanswer)< int(4):
        showtask(user,alltask,uanswer)
    else:
        if int(uanswer)==int(4):
            addtask(user)
        elif int(uanswer)==int(5):
            completetask(user)
        elif int(uanswer)==int(6):
            deletetask(user)
        else:
            pass
    
    
def login():
    user=input("Escribe tu usuario: ")
    password=input("Escribe tu contraseña: ")
    is_valid=verificationdata(user, password)
    os.system("clear")
    
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
        
        os.system("clear")
        print("Tu registro ha sido exitoso!\n")
        run()
        
        
def run():
    print("1. Iniciar sesión.")
    print("2. Crear cuenta.")
    print("3. Salir.\n")
    uanswer=(input(": "))
    os.system("clear")
    is_valid=verificationanswer(uanswer,1,3)
    
    if is_valid:
        if int(uanswer)==int(1):
            login()
        elif int(uanswer)== int(2):
            print("Iniciemos tu proceso de registro.\n")
            singup()
        else:
            pass
    else:
        print("Escribe una opción válida.\n")
        run()
        
    
if __name__ =='__main__':
    print("Bienvenido a task manager\n")
    run()