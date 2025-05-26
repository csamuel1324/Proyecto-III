// Espera a que el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", function() {
    // Referencias a los elementos HTML
    const loginForm = document.querySelector("form");
    const rememberCheckbox = document.getElementById("remember");
    const usernameInput = document.getElementById("username");
    const passwordInput = document.getElementById("password");

    // Cargar datos de "Recordar contraseña" si existen
    if (localStorage.getItem("remember") === "true") {
        usernameInput.value = localStorage.getItem("username") || "";
        passwordInput.value = localStorage.getItem("password") || "";
        rememberCheckbox.checked = true;
    }

    // Actualizar el valor de "remember" en tiempo real
    rememberCheckbox.addEventListener("change", function() {
        if (rememberCheckbox.checked) {
            localStorage.setItem("remember", "true");
        } else {
            localStorage.setItem("remember", "false");
            localStorage.removeItem("username"); // Opcional: limpiar usuario
            localStorage.removeItem("password"); // Opcional: limpiar contraseña
        }
    });

    // Manejar el envío del formulario
    loginForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Evitar recarga de página

        const username = usernameInput.value;
        const password = passwordInput.value;

        // los datos correctos y se puede cambiar
        const usuarioCorrecto = "usuario";
        const contraseñaCorrecta = "1234";

        if (username === usuarioCorrecto && password === contraseñaCorrecta) {
            alert("Inicio de sesión exitoso");
        } else {
            alert("Usuario o contraseña incorrectos");
        }

        // Guardar datos si "Recordar contraseña" está activado
        if (rememberCheckbox.checked) {
            localStorage.setItem("remember", "true");
            localStorage.setItem("username", username);
            localStorage.setItem("password", password);
        } else {
            localStorage.setItem("remember", "false");
            localStorage.removeItem("username");
            localStorage.removeItem("password");
        }
    });
});

