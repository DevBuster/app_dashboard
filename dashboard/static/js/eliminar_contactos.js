const btn_eliminar_contactos = document.querySelectorAll(".btn_eliminar_contactos");

(function () {

    // notificacionSwal("LoadQuery", "Registros cargados con exito", "success", "Ok");


    btn_eliminar_contactos.forEach(btn => {
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