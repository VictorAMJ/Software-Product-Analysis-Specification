async function carregarAtividades() {
  try {
    const resposta = await fetch("/api/atividades/suas_atividades", {
      method: "GET",
      headers: {"Content-Type": "application/json"},
      credentials: "include"
    }); 

    if (!resposta.ok){
      throw new Error("Erro ao buscar atividades");
    }

    const atividades = await resposta.json();

    const corpo = document.getElementById("corpo-tabela");
    corpo.innerHTML = ""; 

    if (atividades.length === 0) {
      corpo.innerHTML = `<tr><td colspan="4">Você ainda não possui atividades inscritas...</td></tr>`;
      return;
    }

    atividades.forEach(a => {
      const dataOriginal = new Date(a[4]);
      const dia = dataOriginal.getDate().toString().padStart(2, "0");
      const mes = (dataOriginal.getMonth() + 1).toString().padStart(2, "0");
      const ano = dataOriginal.getFullYear();
      const dataFormatada = `${dia}/${mes}/${ano}`;

      const linha = document.createElement("tr");

      linha.innerHTML = `
        <td>${a[1]}</td>
        <td>${a[2]}</td>
        <td>${dataFormatada}</td>
        <td>${a[5]}</td>
        <td>
          <button class="btn-atualizar" data-id="${a[0]}">Atualizar</button>
          <button class="btn-deletar" data-id="${a[0]}">Deletar</button>
        </td>
      `;

      corpo.appendChild(linha);
    });

    adicionarEventosBotoes(); 

  } catch (erro) {
    console.error("Erro ao carregar atividades:", erro);
    alert("Erro ao buscar dados da API.");
  }
}

window.addEventListener("load", carregarAtividades);


function adicionarEventosBotoes() {
  document.querySelectorAll(".btn-deletar").forEach(botao => {
    botao.addEventListener("click", async (e) => {
      const id = e.target.getAttribute("data-id");
      if (!confirm("Tem certeza que deseja excluir esta atividade?")) return;

      try {
        const resposta = await fetch(`/atividades/${id}`, { method: "DELETE" });
        const resultado = await resposta.json();
        alert(resultado.mensagem || "Atividade excluída com sucesso!");
        carregarAtividades();
      } catch (erro) {
        console.error("Erro ao excluir:", erro);
        alert("Erro ao excluir a atividade.");
      }
    });
  });

  document.querySelectorAll(".btn-atualizar").forEach(botao => {
    botao.addEventListener("click", (e) => {
      const id = e.target.getAttribute("data-id");
      const linha = e.target.closest("tr");
      const colunas = linha.querySelectorAll("td");

      document.getElementById("edit-id").value = id;
      document.getElementById("edit-nome").value = colunas[0].textContent;
      document.getElementById("edit-participantes").value = colunas[3].textContent;

      const titulo = document.getElementById("titulo-edicao");
      titulo.textContent = `Atualizar atividade: ${colunas[1].textContent}`;

      document.getElementById("form-edicao").style.display = "block";
    });
  });
}


document.getElementById("formAtualizar").addEventListener("submit", async (e) => {
  e.preventDefault();

  const id = document.getElementById("edit-id").value;
  const nome = document.getElementById("edit-nome").value;
  const participantes = document.getElementById("edit-participantes").value;

  try {
    const resposta = await fetch(`/atividades/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ nome, participantes })
    });

    const resultado = await resposta.json();
    alert(resultado.mensagem || "Atividade atualizada com sucesso!");
    document.getElementById("form-edicao").style.display = "none";
    carregarAtividades();

  } catch (erro) {
    console.error("Erro ao atualizar:", erro);
    alert("Erro ao atualizar a atividade.");
  }

});


document.getElementById("cancelar-edicao").addEventListener("click", () => {
  document.getElementById("form-edicao").style.display = "none";
});



