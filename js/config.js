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

  // Medição de visitas e cliques (Umami, sem cookies). Cole o Website ID; "" desliga.
  umami: "",
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

// ============================================================
//  MEDIÇÃO (Umami): visitas e cliques, sem cookies
//  Eventos: "WhatsApp" (com serviço, seção e página), "Produto externo",
//  "Detalhe de solução" (em main.js) e "Rede social"
// ============================================================
const pagina = location.pathname.endsWith("links.html") ? "links" : "site";
const AREAS = { cta: "botao-principal", escolha: "escolha-de-servico", "servicos-bio": "servicos", "redes-bio": "redes", aviso: "faixa-do-topo", perfil: "perfil" };
const secaoDe = (el) => {
  const area = el.closest(Object.keys(AREAS).map((c) => `.${c}`).join(","));
  if (area) return AREAS[[...area.classList].find((c) => AREAS[c])];
  return el.closest("dialog")?.id || el.closest("section[id]")?.id ||
    el.closest("section, footer, header")?.className.split(" ")[0] || "outro";
};

document.querySelectorAll("[data-whatsapp], [data-servico]").forEach((el) => {
  el.dataset.umamiEvent = "WhatsApp";
  el.dataset.umamiEventServico = el.dataset.servico || "geral";
  el.dataset.umamiEventSecao = el.classList.contains("whats-flutuante") ? "botao-flutuante" : secaoDe(el);
  el.dataset.umamiEventPagina = pagina;
});
document.querySelectorAll('a[href^="http"]:not([href*="wa.me"])').forEach((el) => {
  const rede = el.dataset.rede;
  el.dataset.umamiEvent = rede ? "Rede social" : "Produto externo";
  el.dataset.umamiEventDestino = rede || new URL(el.href).hostname + new URL(el.href).pathname.replace(/\/$/, "");
  el.dataset.umamiEventPagina = pagina;
});

if (CONFIG.umami) {
  const s = document.createElement("script");
  s.defer = true;
  s.src = "https://cloud.umami.is/script.js";
  s.dataset.websiteId = CONFIG.umami;
  s.dataset.domains = "akyllastudio.github.io"; // não conta visitas de teste no computador
  document.head.appendChild(s);
}
