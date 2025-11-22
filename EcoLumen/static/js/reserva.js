let imagem = document.getElementById("imagem-principal");
let titulo = document.getElementById("titulo-quarto");
let descricao = document.getElementById("descricao-quarto");

let quartos = [
    {src: "static/img/Quarto1.png", titulo: "Suíte <span>Contemporânea</span>", desc: "Com 28 m², esta suíte combina conforto e design minimalista. Equipada com cama king size, grandes janelas com vista para o jardim e decoração natural com plantas tropicais. O ambiente em tons de madeira clara e verde transmite frescor e bem-estar, ideal para quem busca relaxar em harmonia com a natureza."},
    {src: "static/img/Quarto2.png", titulo: "Suíte Rústica com <span>Vista Panorâmica</span>", desc: "Charmosa suíte de 24 m², com teto de madeira e decoração aconchegante. Dispõe de cama queen size, janelas amplas que revelam a paisagem das montanhas e iluminação suave para noites tranquilas. Perfeita para quem aprecia a rusticidade com um toque de romantismo."},
    {src: "static/img/Quarto3.png", titulo: "Suite Vista da <span>Montanha</span>", desc: "Aconchegante quarto de 26 m² com cama de casal e varanda envidraçada que proporciona vista exclusiva para as montanhas. O piso de madeira e a iluminação natural criam um ambiente acolhedor, perfeito para descansar em contato com a natureza."},
    {src: "static/img/Quarto4.png", titulo: "Suite Design <span>Moderno</span>", desc: "Espaçosa suíte de 30 m² com estilo sofisticado e minimalista. Equipada com cama king size, iluminação em LED embutida e amplas janelas que dão vista para o jardim vertical. Uma experiência de hospedagem que une conforto, tecnologia e elegância."},
    {src: "static/img/Quarto5.png", titulo: "Suite Floresta <span>Premium</span>", desc: "Suíte de 32 m² com decoração orgânica e parede viva de musgo natural. Oferece cama king size, sala de estar integrada e varanda privativa com vista para a floresta. Um refúgio exclusivo para quem busca luxo em meio à natureza."}
];

let index = 0;
const intervalo = 20000;

function trocaImagem(endereco, novoTitulo, novaDesc){
    imagem.src = endereco;
    titulo.innerHTML = novoTitulo;
    descricao.innerText = novaDesc;
    index = quartos.findIndex(q => q.src === endereco);

    document.querySelectorAll('.menu-quartos img').forEach(img => img.classList.remove('selecionado'));
    document.querySelectorAll('.menu-quartos img')[index].classList.add('selecionado');
}

setInterval(() => {
    index = (index + 1) % quartos.length;
    let atual = quartos[index];
    trocaImagem(atual.src, atual.titulo, atual.desc);
}, intervalo);

trocaImagem(quartos[0].src, quartos[0].titulo, quartos[0].desc);

function abrirFormulario(){
    let tituloTexto = titulo.textContent;
    document.getElementById("quarto-selecionado").textContent = tituloTexto;
    document.getElementById("form-reserva").style.display = "block";
    document.getElementById("quarto").value = tituloTexto
    document.getElementById("mensagem").textContent = "";

}

let reservas = [];

function conflitoReserva(quarto, checkIn, checkOut) {
    return reservas.some(r => {
        if (r.quarto !== quarto) return false;
        return !(checkOut <= r.checkIn || checkIn >= r.checkOut);
    });
}

function parseDataYYYYMMDD(input) {
    if (!input) return null;
    let partes = input.split('-');
    if (partes.length !== 3) return null;
    let ano = parseInt(partes[0], 10);
    let mes = parseInt(partes[1], 10) - 1;
    let dia = parseInt(partes[2], 10);
    return new Date(ano, mes, dia);
}

document.getElementById("reservaForm").addEventListener("submit", function(e) {
    e.preventDefault();

    let nome = document.getElementById("nome").value;
    let email = document.getElementById("email").value;
    let checkIn = document.getElementById("checkIn").value;
    let checkOut = document.getElementById("checkOut").value;
    let hospedes = document.getElementById("hospedes").value;
    let quarto = document.getElementById("quarto").value;

    let checkInDate = parseDataYYYYMMDD(checkIn);
    let checkOutDate = parseDataYYYYMMDD(checkOut);
    
    let hoje = new Date();
    hoje.setHours(0,0,0,0);
    let ultimoDiaAnoSeguinte = new Date(hoje.getFullYear() + 1, 11, 31);

    if (!checkInDate || !checkOutDate) {
        document.getElementById("mensagem").textContent = "Data inválida! Use o formato DD/MM/AAAA.";
        document.getElementById("mensagem").style.color = "red";
        return;
    }

    if (checkInDate < hoje || checkOutDate < hoje) {
        document.getElementById("mensagem").textContent = "Não é possível reservar para datas passadas!";
        document.getElementById("mensagem").style.color = "red";
        return;
    }

    if (checkInDate > ultimoDiaAnoSeguinte || checkOutDate > ultimoDiaAnoSeguinte) {
        document.getElementById("mensagem").textContent = "Não é possível reservar além de 31/12 do próximo ano!";
        document.getElementById("mensagem").style.color = "red";
        return;
    }

    if (checkOutDate < checkInDate) {
        document.getElementById("mensagem").textContent = "A data de check-out deve ser igual ou depois do check-in!";
        document.getElementById("mensagem").style.color = "red";
        return;
    }

    if (conflitoReserva(quarto, checkInDate, checkOutDate)) {
        document.getElementById("mensagem").textContent = "Quarto indisponível nessas datas. Escolha outra data ou outro quarto.";
        document.getElementById("mensagem").style.color = "red";
        return;
    }

    let form = document.getElementById("reservaForm");
    let formData = new FormData(form);

    fetch("/reserva", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("mensagem").textContent = data.mensagem;

        if (data.status === "sucesso") {
            mensagem.style.color = "green";
            document.getElementById("reservaForm").reset();

            setTimeout(() => {
                document.getElementById("form-reserva").style.display = "none";
                mensagem.textContent = "";
                window.location.href = "/home";
            }, 3500);

        } else {
            document.getElementById("mensagem").style.color = "red";
        }
        
    })
    .catch(err => console.error("Erro:", err))
});