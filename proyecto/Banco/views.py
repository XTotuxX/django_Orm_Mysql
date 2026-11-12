from django.shortcuts import redirect, render

from .models import Cuenta  # Importamos tu modelo


def listar_cuentas(request):
    # Esto equivale a un: SELECT * FROM cuenta;
    cuentas = Cuenta.objects.all()

    # Enviamos los datos al HTML mediante el diccionario de contexto
    return render(request, "gestionCuentas.html", {"cuentas": cuentas})


# VISTA 2: Solo se encarga de insertar (INSERT)
def registrar_cuenta(request):
    if request.method == "POST":
        v_tipocuenta = request.POST.get("txtTipoCuenta")
        v_descripcion = request.POST.get("txtDescripcion")
        v_saldo = request.POST.get("txtSaldo")

        Cuenta.objects.create(
            tipo_cuenta=v_tipocuenta, descripcion=v_descripcion, saldo=v_saldo
        )
    # Al terminar de insertar, redirige a la vista de consultas para actualizar la tabla
    return redirect("listar_cuentas")


# Vista 3: Eliminar cuenta
def eliminar_cuenta(request, id):
    cuenta = Cuenta.objects.get(id=id)
    cuenta.delete()

    return redirect("listar_cuentas")


# Vista 4: Actualizar cuenta


def actualizar_cuenta(request, id):
    cuenta = Cuenta.objects.get(id=id)
    if request.method == "POST":
        cuenta.tipo_cuenta = request.POST.get("txtTipoCuenta")
        cuenta.descripcion = request.POST.get("txtDescripcion")
        cuenta.saldo = request.POST.get("txtSaldo")
        cuenta.save()

        return redirect("listar_cuentas")
    return render(request, "actualizarCuenta.html", {"cuenta": cuenta})
