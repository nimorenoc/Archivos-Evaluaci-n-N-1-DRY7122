def determinar_tipo_acl(numero_acl):
    if 1 <= numero_acl <= 99:
        return"ACL Estandar"
    elif 100 <= numero_acl <= 199:
        return"ACL Extendida"
    else:
        return "El numero no corresponde a una lista de acceso"

#solicitar acl

while True:
    try:
        numero_acl = int(input("Ingrese el numero de ACL IPv4: "))
        tipo_acl = determinar_tipo_acl(numero_acl)
        print ("El numero de ACL", numero_acl, "corresponde a:", tipo_acl)
        break
    except ValueError:
        print ("Ingrese un numero valido.")
