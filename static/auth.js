async function fazerLogin() {
    const username = document.getElementById("login-username").value.trim();
    const senha = document.getElementById("login-password").value;
    const mensagem = document.getElementById("mensagem-login");

    if (!username || !senha) {
        mensagem.textContent = "Preencha username e senha.";
        return;
    }

    const respostaSessao = await fetch("/api/session");
    const dadosSessao = await respostaSessao.json();

    const resposta = await fetch("/api/session", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRF-Token": dadosSessao.csrf_token
        },
        body: JSON.stringify({
            username: username,
            password: senha
        })
    });

    const resultado = await resposta.json();

    if (!resposta.ok) {
        mensagem.textContent = resultado.erro;
        return;
    }

    mensagem.textContent = "Login realizado com sucesso!";

    window.location.href = "/";
}


document.getElementById("botao-login").addEventListener("click", fazerLogin);