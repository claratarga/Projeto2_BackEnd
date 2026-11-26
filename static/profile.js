async function carregarPerfil() {
    const caminho = window.location.pathname;
    const usuarioId = caminho.split("/").pop();

    const respostaUsuario = await fetch(`/api/users/${usuarioId}`);
    const usuario = await respostaUsuario.json();

    if (!respostaUsuario.ok) {
        document.getElementById("nome-usuario").textContent = usuario.erro;
        return;
    }

    document.getElementById("nome-usuario").textContent = usuario.nome;
    document.getElementById("username").textContent = "@" + usuario.username;

    const respostaPosts = await fetch(`/api/users/${usuarioId}/posts`);
    const publicacoes = await respostaPosts.json();

    const area = document.getElementById("publicacoes");
    area.innerHTML = "";

    if (publicacoes.length === 0) {
        area.textContent = "Este usuário ainda não possui publicações.";
        return;
    }

    publicacoes.forEach(function(postagem) {
        const elemento = document.createElement("div");
        elemento.className = "postagem";

        const conteudo = document.createElement("p");
        conteudo.textContent = postagem.conteudo;

        const data = document.createElement("small");
        data.textContent = postagem.data_criacao;

        elemento.appendChild(conteudo);
        elemento.appendChild(data);

        area.appendChild(elemento);
    });
}

carregarPerfil();