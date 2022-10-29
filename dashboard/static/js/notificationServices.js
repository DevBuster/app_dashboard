const btn_eliminar_registro = document.querySelectorAll(".btn_eliminar_registro");
const btn_guardar_registro = document.querySelectorAll(".btn_guardar_registro");
const btn_actualizar_registro = document.querySelectorAll(".btn_actualizar_registro");
const btn_generar_grafica = document.querySelectorAll(".btn_generar_grafica");


let modalGraficaBarra = document.getElementById('modalGraficaBarra');
modalGraficaBarra.style.display = 'none';

(function () {

    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: 'btn btn-success',
            cancelButton: 'btn btn-danger'
        },
        buttonsStyling: false
    });
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
            }).then((result) => {
                if (result.isConfirmed) {
                    Swal.fire(
                        'Registro eliminado!',
                        'Nice!.',
                        'success'
                    )
                } else if (
                    /* Read more about handling dismissals below */
                    result.dismiss === Swal.DismissReason.cancel
                ) {
                    swalWithBootstrapButtons.fire(
                        'Eliminación cancelada',
                        'Su registro está intacto :)',
                        'error'
                    )
                }
            })
        })
    });

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

    // generar grafica de barra
    btn_generar_grafica.forEach(btn => {
        btn.addEventListener('click', function () {
            let timerInterval
            Swal.fire({
                title: 'Grafica de barra!',
                html: 'Generando grafica de barra...<b></b> milliseconds.',
                timer: 2000,
                timerProgressBar: true,
                didOpen: () => {
                    Swal.showLoading()
                    const b = Swal.getHtmlContainer().querySelector('b')
                    timerInterval = setInterval(() => {
                        b.textContent = Swal.getTimerLeft()
                    }, 100)
                },
                willClose: () => {
                    clearInterval(timerInterval)
                }
            }).then((result) => {
                /* Read more about handling dismissals below */
                if (result.dismiss === Swal.DismissReason.timer) {
                    modalGraficaBarra.style.display = 'block';
                }
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