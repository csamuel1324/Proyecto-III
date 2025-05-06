document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript cargado correctamente!");

    const form = document.getElementById("registerForm");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // para no hacer el envío automatico

        // obtener valores de los campos
        const nombre = document.getElementById("firstname").value.trim();
        const apellido = document.getElementById("lastname").value.trim();
        const fechaNacimiento = document.getElementById("birthdate").value;
        const sexo = document.getElementById("gender").value;
        const rol = document.getElementById("role").value;
        const usuario = document.getElementById("username").value.trim();
        const password = document.getElementById("password").value.trim();
        const confirmPassword = document.getElementById("confirm-password").value.trim();

        console.log("Verificando campos...");

        // validaciones básicas
        if (!nombre || !apellido || !fechaNacimiento || !sexo || !rol || !usuario || !password || !confirmPassword) {
            alert("Todos los campos son obligatorios.");
            console.log("Alerta activada: Campos vacíos");
            return;
        }

        // validación de fecha de nacimiento (mayores de 18 años)
        const fechaNac = new Date(fechaNacimiento);
        const fechaActual = new Date();
        const edad = fechaActual.getFullYear() - fechaNac.getFullYear();
        const diferenciaMeses = fechaActual.getMonth() - fechaNac.getMonth();
        const diferenciaDias = fechaActual.getDate() - fechaNac.getDate();

        if (edad < 18 || (edad === 18 && diferenciaMeses < 0) || (edad === 18 && diferenciaMeses === 0 && diferenciaDias < 0)) {
            alert("Debes tener al menos 18 años para registrarte.");
            return;
        }

        if (password.length < 8) {
            alert("La contraseña debe tener al menos 8 caracteres.");
            return;
        }

        if (password !== confirmPassword) {
            alert("Las contraseñas no coinciden.");
            return;
        }

        // simulacion de registro exitoso
        console.log("Registro validado correctamente, mostrando alerta...");
        alert("Registro exitoso. ¡Bienvenido, " + nombre + "!");
        form.reset();
    });
});




