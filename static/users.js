async function buscarUsuarios() {
    const termo = document.getElementById("termo-busca").value.trim();
    const resultados = document.getElementById("resultados");

    if (!termo) {
        resultados.textContent = "Digite um nome ou username.";
        return;
    }

    const resposta = await fetch(`/api/users/search/${encodeURIComponent(termo)}`);
    const usuarios = await resposta.json();

    resultados.innerHTML = "";

    if (usuarios.length === 0) {
        resultados.textContent = "Nenhum usuário encontrado.";
        return;
    }

    usuarios.forEach(function(usuario) {
        const elemento = document.createElement("div");
        elemento.className = "usuario";

        const nome = document.createElement("h3");
        nome.textContent = usuario.nome;

        const username = document.createElement("p");
        username.textContent = "@" + usuario.username;

        const link = document.createElement("a");
        link.textContent = "Ver perfil";
        link.href = `/profile/${usuario.id}`;

        elemento.appendChild(nome);
        elemento.appendChild(username);
        elemento.appendChild(link);

        resultados.appendChild(elemento);
    });
}


async function carregarSessao() {
    const areaConta = document.getElementById("area-conta");

    const resposta = await fetch("/api/session");
    const dados = await resposta.json();

    if (dados.autenticado) {
        areaConta.innerHTML = "";

        const saudacao = document.createElement("span");
        saudacao.textContent = "Olá, " + dados.usuario.nome;

        const botaoLogout = document.createElement("button");
        botaoLogout.id = "botao-logout";
        botaoLogout.textContent = "Sair";
        botaoLogout.addEventListener("click", fazerLogout);

        areaConta.appendChild(saudacao);
        areaConta.appendChild(botaoLogout);
    }
}

async function fazerLogout() {
    const respostaSessao = await fetch("/api/session");
    const dadosSessao = await respostaSessao.json();

    const resposta = await fetch("/api/session", {
        method: "DELETE",
        headers: {
            "X-CSRF-Token": dadosSessao.csrf_token
        }
    });

    if (resposta.ok) {
        window.location.reload();
    }
}


document.getElementById("botao-buscar").addEventListener("click", buscarUsuarios);

carregarSessao();