const MEDIA_ENERGIA = 50; 
const MEDIA_AGUA = 150;   

document.querySelectorAll(".quarto").forEach(quarto => {

    const energia = Number(quarto.dataset.energia); 
    const agua = Number(quarto.dataset.agua);       

    const barraEnergia = quarto.querySelector(".energia-barra");
    const barraAgua = quarto.querySelector(".agua-barra");

    const percEnergia = (energia / MEDIA_ENERGIA) * 100;
    const percAgua = (agua / MEDIA_AGUA) * 100;

    barraEnergia.style.width = percEnergia + "%";
    barraAgua.style.width = percAgua + "%";

    const infoEnergia = document.createElement("p");
    infoEnergia.classList.add("info-consumo");
    infoEnergia.innerHTML =
        `Consumo diário de energia: <strong>${energia} kWh</strong> 
        (${percEnergia.toFixed(0)}% da média por pessoa)`;

    const infoAgua = document.createElement("p");
    infoAgua.classList.add("info-consumo");
    infoAgua.innerHTML =
        `Consumo diário de água: <strong>${agua} L</strong> 
        (${percAgua.toFixed(0)}% da média por pessoa)`;

    const titulos = quarto.querySelectorAll(".titulo-bloco");
    titulos[0].insertAdjacentElement("afterend", infoEnergia);
    titulos[1].insertAdjacentElement("afterend", infoAgua);

    const premio = quarto.querySelector(".premio");

    const excedeu = energia > MEDIA_ENERGIA || agua > MEDIA_AGUA;

    if (excedeu) {
        premio.textContent = 
            "✗ Consumo diário acima da média — Metas não atingidas hoje";
        premio.classList.add("perda");
    } else {
        premio.textContent = 
            "✓ Consumo diário abaixo da média — Meta do dia atingida!";
        premio.classList.add("ganho");
    }
});
