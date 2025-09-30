window.addEventListener("DOMContentLoaded", () => {
    const email = document.getElementById("email")
    const senha = document.getElementById("senha")

    if (email) email.value = ""
    if (senha) senha.value = ""
})

window.addEventListener("pageshow", function(event) {
    if (event.persisted || (window.performance && window.performance.getEntriesByType("navigation")[0].type === "back_forward")) {
        const email = document.getElementById("email")
        const senha = document.getElementById("senha")

        if (email) email.value = ""
        if (senha) senha.value = ""
    }
})

const form = document.getElementById("formulario_login")

form.addEventListener("submit", function (event) {
    event.preventDefault();

    let email = document.getElementById("email").value
    let senha = document.getElementById("senha").value

    const formData = new FormData(form);

    fetch("login", {
        method: "POST",
        body: formData
    })
    .then(resposta => resposta.text())
    .then(mensagem => {
        if (mensagem.includes("sucesso")) {
            alert(mensagem)
            window.location.href = "/home"
        } else {
            alert(mensagem)
            form.reset()
        }
    })
    .catch(erro => {
        alert("Erro ao tentar logar: " + erro.mensagem)
    })
})