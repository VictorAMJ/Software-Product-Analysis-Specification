function carregarCheckin() {
    fetch("/reserva/pre-checkin")
      .then(res => res.json())
      .then(data => {
        const msg = document.getElementById("mensagem-checkin");
  
        if (data.status === "sucesso" && Array.isArray(data.reservas) && data.reservas.length) {
          msg.innerHTML = "";
  
          data.reservas.forEach(r => {
            if (r.check_in) {
              const partes = r.check_in.split("-");
              if (partes.length === 3) {
                const [ano, mes, dia] = partes;
                const dataCheckin = new Date(ano, mes - 1, dia);
                msg.innerHTML += `
                  📅 ${dataCheckin.toLocaleDateString("pt-BR")} — Você (${r.nome}) tem um pré check-in no hotel.<br>
                  Realizar o check-in às 14:00 na recepção do hotel.<br><br>
                `;
              }
            }
          });
        } else if (data.status === "vazio") {
          msg.textContent = "Você ainda não possui reservas ativas. Faça sua reserva agora.";
        } else {
          msg.textContent = "Erro ao carregar informações de check-in.";
        }
      })
      .catch(() => {
        document.getElementById("mensagem-checkin").textContent = "Erro ao carregar informações de check-in.";
      });
  }
  
  carregarCheckin();
  