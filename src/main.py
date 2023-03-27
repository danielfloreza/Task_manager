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
            passwordsaved=user.readline(1)
            passwordsaved=passwordsaved.strip()
            if passwordsaved==password:
                user.close()
                return True
            else:
                user.close()
                return False
    except:
        return False
        

def start(user):
    pass


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