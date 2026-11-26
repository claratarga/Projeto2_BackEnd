
async function cadastrarUsuario() {
    const dados = {
        nome: document.getElementById("cadastro-nome").value,
        username: document.getElementById("cadastro-username").value,
        email: document.getElementById("cadastro-email").value,
        senha: document.getElementById("cadastro-senha").value
    };

    const resposta = await fetch("/usuarios", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(dados)
    });

    const resultado = await resposta.json();

    alert(resultado.mensagem || resultado.erro);
}


async function fazerLogin() {
    const dados = {
        username: document.getElementById("login-username").value,
        senha: document.getElementById("login-senha").value
    };

    const resposta = await fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(dados)
    });

    const resultado = await resposta.json();

    alert(resultado.mensagem || resultado.erro);

    if (resposta.ok) {
        document.getElementById("area-login").style.display = "none";
        document.getElementById("area-cadastro").style.display = "none";
        document.getElementById("area-postagem").style.display = "block";

        carregarPostagens();
    }
}


async function criarPostagem() {
    const conteudo = document.getElementById("conteudo-postagem").value;

    const resposta = await fetch("/postagens", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ conteudo: conteudo })
    });

    const resultado = await resposta.json();

    alert(resultado.mensagem || resultado.erro);

    if (resposta.ok) {
        document.getElementById("conteudo-postagem").value = "";
        carregarPostagens();
    }
}


async function carregarPostagens() {
    const resposta = await fetch("/postagens");
    const postagens = await resposta.json();

    const area = document.getElementById("postagens");

    area.innerHTML = "";

    postagens.forEach(function(postagem) {
        const elemento = document.createElement("div");

        elemento.className = "postagem";

        elemento.innerHTML = `
            <strong>@${postagem.username}</strong>
            <p>${postagem.conteudo}</p>
            <small>${postagem.data_criacao}</small>
        `;

        area.appendChild(elemento);
    });
}


async function fazerLogout() {
    const resposta = await fetch("/logout", {
        method: "POST"
    });

    const resultado = await resposta.json();

    alert(resultado.mensagem);

    document.getElementById("area-login").style.display = "block";
    document.getElementById("area-cadastro").style.display = "block";
    document.getElementById("area-postagem").style.display = "none";
}