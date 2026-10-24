// ============================================================
//  CONTATOS E REDES: edite aqui (vale para todas as páginas)
// ============================================================
const CONFIG = {
  // Só números, com DDI 55 + DDD. Ex: "5562999999999"
  whatsapp: "5562991657619",

  // Deixe "" para esconder o botão da rede no site
  instagram: "",  // ex: "https://instagram.com/akyllastudio"
  linkedin: "",   // ex: "https://linkedin.com/in/seu_usuario"
  facebook: "",   // ex: "https://facebook.com/akyllastudio"
  tiktok: "",     // ex: "https://tiktok.com/@akyllastudio"
  youtube: "",    // ex: "https://youtube.com/@akyllastudio"
  email: "",      // ex: "contato@akyllastudio.com.br"
  github: "https://github.com/akyllastudio",
};

// Links de WhatsApp: cada botão leva a mensagem do seu data-whatsapp
document.querySelectorAll("[data-whatsapp]").forEach((el) => {
  const msg = encodeURIComponent(el.dataset.whatsapp || "");
  el.href = `https://wa.me/${CONFIG.whatsapp}?text=${msg}`;
  el.target = "_blank";
  el.rel = "noopener";
});

// Redes sociais e e-mail (esconde as que não foram preenchidas)
document.querySelectorAll("[data-rede]").forEach((el) => {
  const valor = CONFIG[el.dataset.rede];
  if (!valor) return el.remove();
  el.href = el.dataset.rede === "email" ? `mailto:${valor}` : valor;
});

// Escolha de serviço: abre o WhatsApp com a mensagem já organizada
// <a data-servico="Loja virtual"> · a origem vem de <body data-origem="...">
document.querySelectorAll("[data-servico]").forEach((el) => {
  const origem = document.body.dataset.origem || "pelo site";
  const msg =
    `Olá! Vim ${origem} da Akylla Studio e quero um orçamento.\n\n` +
    `Preciso de: ${el.dataset.servico}\n` +
    `Meu objetivo é: `;
  el.href = `https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(msg)}`;
  el.target = "_blank";
  el.rel = "noopener";
});
