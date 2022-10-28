const notificacionSwal = (titleText, text, icon, confirmButtonText) => {
    Swal.fire({
        titleText: titleText,
        text: text,
        icon: icon, // warnign, error, success, info
        confirmButtonText: confirmButtonText,
    });
};