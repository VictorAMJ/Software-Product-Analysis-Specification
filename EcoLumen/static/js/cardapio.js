function salvarCardapio() {
    const refeicoes = document.querySelectorAll('nav#Refeicao');
    const refeicoesEscolhidas = [];

    refeicoes.forEach(ref => {
        const nomeRefeicao = ref.getAttribute('data-ref');

        const inputSim = ref.querySelector('input[value="Sim"]');
        const inputNao = ref.querySelector('input[value="Não"]');

        if (inputNao && inputNao.checked) {
            return;   
        }
        refeicoesEscolhidas.push(nomeRefeicao);
    });

    console.log("Refeições enviadas:", refeicoesEscolhidas);

    fetch("/cardapio_digital", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ refeicoes: refeicoesEscolhidas, email: document.body.dataset.email })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.mensagem || "Refeições Salvas com sucesso!");
    })
    .catch(err => {
        console.error(err);
        alert("Erro ao enviar");
    });
}