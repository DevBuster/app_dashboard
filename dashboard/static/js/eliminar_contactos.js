(function () {
    // ------- ACCION DEL BOTON "ELIMINAR" CONTACTOS ------- //
    const btn_eliminar_contactos = document.querySelectorAll(".btn_eliminar_contactos");

    btn_eliminar_contactos.forEach(btn_eliminar_contactos => {
        btn_eliminar_contactos.addEventListener("click", (evento) => {
            const confirmar_eliminar_contactos = confirm("¿Seguro(a) que quiere eliminar éste registro?");

            if (!confirmar_eliminar_contactos) {
                evento.preventDefault();
            }
        });
    });
})();