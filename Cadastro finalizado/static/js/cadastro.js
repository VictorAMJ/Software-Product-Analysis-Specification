const form = document.getElementById('formulario_cadastro')

form.addEventListener('submit', function (event) {
    event.preventDefault()

    let nome = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let senha = document.getElementById('password').value;
    let confirma_senha = document.getElementById('confirm_password').value;
    let cpf = document.getElementById('cpf').value;
    let telefone = document.getElementById('telephone').value;

    if (senha != confirma_senha) {
        alert("Senhas não coincidem!")
        return
    }

    cpf = cpf.replace(/\D/g, '')
    if (cpf.length !== 11) {
        alert("CPF inválido! Deve ter 11 números")
        return
    }

    telefone = telefone.replace(/\D/g, '')
    if (telefone.length < 10 || telefone.length > 11) {
        alert("Telefone inválido! Deve conter 10 ou 11 números.")
        return
    }

    const formData = new FormData(form)

    fetch('/cadastrar', {
        method: 'POST',
        body: formData
    })
    .then(respostaHTTP => respostaHTTP.text())
    .then(mensagemServidor => {
        alert(mensagemServidor)    
    })
    .catch(erroHTTP => {
        alert("Erro ao enviar cadastro!" + erroHTTP.message)
    })
})
