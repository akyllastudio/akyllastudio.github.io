// Menu no celular
const botaoMenu = document.querySelector(".menu-btn");
const menu = document.getElementById("menu");
botaoMenu.addEventListener("click", () => {
  // o menu começa logo abaixo do cabeçalho (a faixa de aviso muda essa altura)
  menu.style.top = `${document.querySelector(".topo").getBoundingClientRect().bottom}px`;
  const aberto = menu.classList.toggle("aberto");
  botaoMenu.setAttribute("aria-expanded", aberto);
  document.body.classList.toggle("sem-rolagem", aberto);
});
menu.querySelectorAll("a").forEach((a) =>
  a.addEventListener("click", () => {
    menu.classList.remove("aberto");
    botaoMenu.setAttribute("aria-expanded", false);
    document.body.classList.remove("sem-rolagem");
  })
);

// Sombra no cabeçalho ao rolar
const topo = document.querySelector(".topo");
const marcarRolagem = () => topo.classList.toggle("rolado", window.scrollY > 10);
window.addEventListener("scroll", marcarRolagem, { passive: true });
marcarRolagem();

// Animação de entrada das seções
const observador = new IntersectionObserver(
  (entradas) =>
    entradas.forEach((e) => {
      if (e.isIntersecting) {
        e.target.classList.add("visivel");
        observador.unobserve(e.target);
      }
    }),
  { threshold: 0.12 }
);
document.querySelectorAll(".cartao, .dor, .projeto, .diferencial, .passos li, .plano, .garantia, details").forEach((el) => {
  el.classList.add("revelar");
  observador.observe(el);
});

document.getElementById("ano").textContent = new Date().getFullYear();

// Detalhes das soluções: abre a janela do cartão clicado ou do endereço (#solucao-...)
const abrirDetalhe = (id) => {
  const d = document.getElementById(id);
  if (!d || typeof d.showModal !== "function") return;
  if (!d.open) d.showModal();
  d.scrollTop = 0;
  document.body.classList.add("com-detalhe");
  if (location.hash !== `#${id}`) history.replaceState(null, "", `#${id}`);
};
document.querySelectorAll("[data-abrir]").forEach((el) =>
  el.addEventListener("click", (e) => { e.preventDefault(); abrirDetalhe(el.dataset.abrir); })
);
document.querySelectorAll("dialog.detalhe").forEach((d) => {
  d.addEventListener("close", () => {
    document.body.classList.remove("com-detalhe");
    if (location.hash === `#${d.id}`) history.replaceState(null, "", "#solucoes");
  });
  d.addEventListener("click", (e) => { // clique fora da janela fecha
    const r = d.getBoundingClientRect();
    const fora = e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom;
    if (e.target === d && fora) d.close();
  });
  d.querySelector("[data-fechar]").addEventListener("click", () => d.close());
});
if (location.hash.startsWith("#solucao-")) {
  document.getElementById("solucoes")?.scrollIntoView();
  abrirDetalhe(location.hash.slice(1));
}

// Menu: destaca a seção que está na tela
const linksMenu = [...document.querySelectorAll('.menu a[href^="#"]:not(.btn)')];
const secoesMenu = linksMenu.map((a) => document.querySelector(a.getAttribute("href"))).filter(Boolean);
const marcarMenu = new IntersectionObserver((entradas) => {
  entradas.forEach((e) => {
    if (!e.isIntersecting) return;
    linksMenu.forEach((a) => a.classList.toggle("ativo", a.getAttribute("href") === `#${e.target.id}`));
  });
}, { rootMargin: "-45% 0px -50% 0px" });
secoesMenu.forEach((s) => marcarMenu.observe(s));

// Medição: qual solução as pessoas abrem (só funciona com o Umami ligado em config.js)
document.querySelectorAll("dialog.detalhe").forEach((d) =>
  new MutationObserver(() => { if (d.open) window.umami?.track("Detalhe de solução", { solucao: d.id.replace("solucao-", "") }); })
    .observe(d, { attributes: true, attributeFilter: ["open"] })
);
