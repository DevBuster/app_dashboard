const btn_eliminar_registro = document.querySelectorAll(".btn_eliminar_registro");
const btn_guardar_registro = document.querySelectorAll(".btn_guardar_registro");
const btn_actualizar_registro = document.querySelectorAll(".btn_actualizar_registro");

(function () {

    // notificacionSwal("LoadQuery", "Registros cargados con exito", "success", "Ok");

    btn_guardar_registro.forEach(btn => {
        btn.addEventListener('click', function () {
            Swal.fire({
                titleText: "REGISTRO CREADO",
                text: "Nice!!",
                icon: "success", // warnign, error, success, info
                confirmButtonColor: "green",
                backdrop: true,
                showLoaderOnConfirm: true,
                confirmButtonText: "Nice!",
                allowOutsideClick: () => false,
                allowEscapeKey: () => false,
            })
        })
    });

    btn_actualizar_registro.forEach(btn => {
        btn.addEventListener('click', function () {
            Swal.fire({
                titleText: "REGISTRO ACTUALIZADO",
                text: "Nice!!",
                icon: "success", // warnign, error, success, info
                confirmButtonColor: "green",
                backdrop: true,
                showLoaderOnConfirm: true,
                confirmButtonText: "Nice!",
                allowOutsideClick: () => false,
                allowEscapeKey: () => false,
            })
        })
    });

    btn_eliminar_registro.forEach(btn => {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            Swal.fire({
                titleText: "ELIMINAR REGISTRO",
                text: "¿Segur@ que quiere eliminar este registro?",
                icon: "warning", // warnign, error, success, info
                showCancelButton: true,
                confirmButtonColor: "green",
                cancelButtonColor: "red",
                backdrop: true,
                showLoaderOnConfirm: true,
                confirmButtonText: "Confirmar",
                cancelButtonText: "Cancelar",
                preConfirm: () => {
                    location.href = e.target.href;
                },
                allowOutsideClick: () => false,
                allowEscapeKey: () => false,
            })
        })
    });

    // ------- ACCION DEL BOTON "ELIMINAR" CONTACTOS ------- //
    // const btn_eliminar_contactos = document.querySelectorAll(".btn_eliminar_contactos");

    // btn_eliminar_contactos.forEach(btn_eliminar_contactos => {
    //     btn_eliminar_contactos.addEventListener("click", (evento) => {
    //         const confirmar_eliminar_contactos = confirm("¿Seguro(a) que quiere eliminar éste registro?");

    //         if (!confirmar_eliminar_contactos) {
    //             evento.preventDefault();
    //         }
    //     });
    // });
})();