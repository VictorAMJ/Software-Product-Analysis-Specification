let imagem = document.getElementById("img-principal");
let titulo = document.getElementById("titulo-atividade")
let descricao = document.getElementById("descricao-atividade")

let atividade = [
    {src: "static/img/trilha.png", titulo: "Trilha Ecológica", descricao: "Trilhas ecológicas guiadas, que percorrem áreas de mata nativa e apresentam a fauna e flora local."},
    {src: "static/img/yoga.png", titulo: "Aulas de yoga e meditação", descricao: "Aulas de yoga e meditação ao ar livre, ideais para relaxar e se harmonizar com o ambiente."},
    {src: "static/img/horta.png", titulo: "Oficinas de sustentabilidade", descricao: "O tema das oficnas pode ser compostagem, reaproveitamento de materiais e plantio de hortas orgânicas, pois nessa atividade cuidamos do nosso espaço ecológico proprio do hotel."},
    {src: "static/img/gastronomia.png", titulo: "Experiências gastronômicas", descricao: "Experiências gastronômicas, com workshops sobre culinária natural e orgânica."},
    {src: "static/img/criança.png", titulo: "Atividades infantis", descricao: "Atividades educativas infantis, voltadas para o aprendizado ambiental por meio de jogos e práticas ao ar livre."}
];

let index = 0;
const intervalo = 20000;

function trocaImagem(endereco, novoTitulo, novaDesc){
    imagem.src = endereco;
    titulo.innerHTML = novoTitulo;
    descricao.innerHTML = novaDesc;
    index = atividade.findIndex(q => q.src === endereco);

    document.querySelectorAll('.menu-atividades img').forEach(img => img.classList.remove('selecionado'));
    document.querySelectorAll('.menu-atividades img')[index].classList.add('selecionado');
}

setInterval(() =>{
    index = (index + 1) % atividade.length;
    let atual = atividade[index];
    trocaImagem(atual.src, atual.titulo, atual.descricao);
}, intervalo);

trocaImagem(atividade[0].src, atividade[0].titulo, atividade[0].descricao);


function abrirFormulario(){
    let tituloTexto = titulo.textContent;
    document.getElementById("atividade-selecionada").textContent = tituloTexto;
    document.getElementById("form-atividade").style.display = "block";
    document.getElementById("atividade").value = tituloTexto
    document.getElementById("mensagem").textContent = "";
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


document.getElementById("inscreverForm").addEventListener("submit", async function(e){
    e.preventDefault();

    const formData = new FormData(this);

    try {
        const resposta = await fetch("/atividades", {
            method: "POST",
            body: formData
        });

        const resultado = await resposta.json();
        if (resposta.ok) {
            document.getElementById("mensagem").textContent = resultado.mensagem || "Atividade reservada com sucesso!";
            document.getElementById("mensagem").style.color = "green";
        } else {
            document.getElementById("mensagem").textContent = resultado.erro || "Erro ao registrar atividade.";
            document.getElementById("mensagem").style.color = "red";
        }

    } catch (erro) {
        console.error("Erro na requisição:", erro);
        alert("Erro de conexão com o servidor.");
        
    }
})