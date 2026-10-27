"""
Gera os detalhes de cada solução (janelas que abrem por cima do site) dentro do index.html,
entre os marcadores SOLUCOES:DETALHES.

Para mudar textos, recursos ou perguntas: edite a lista SOLUCOES abaixo e rode
    python _gerador/solucoes.py
na pasta do site. (Pastas que começam com "_" não são publicadas no GitHub Pages.)
"""
from html import escape
from pathlib import Path

SITE = "https://akyllastudio.github.io"
RAIZ = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- ícones
ICONES = {
    "pet": '<path d="M12 12c-3 0-5.5 3-5.5 5.3 0 1.6 1.3 2.2 2.7 2.2 1 0 1.8-.5 2.8-.5s1.8.5 2.8.5c1.4 0 2.7-.6 2.7-2.2C17.5 15 15 12 12 12z"/><circle cx="6" cy="8" r="1.8"/><circle cx="10" cy="5.5" r="1.8"/><circle cx="14" cy="5.5" r="1.8"/><circle cx="18" cy="8" r="1.8"/>',
    "rest": '<path d="M7 3v8M5 3v4a2 2 0 0 0 4 0V3M7 11v10M17 3c-2 1-3 4-3 7h3v11"/>',
    "painel": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4M7 9h4M7 12h7"/>',
    "bot": '<rect x="4" y="8" width="16" height="11" rx="3"/><path d="M12 4v4M9 13v.01M15 13v.01M9 16h6"/>',
    "oferta": '<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="7.5" r="1.5"/>',
    "video": '<rect x="3" y="5" width="13" height="14" rx="2"/><path d="M16 10l5-3v10l-5-3z"/>',
    "ia": '<path d="M12 3l1.8 4.7L18.5 9.5l-4.7 1.8L12 16l-1.8-4.7L5.5 9.5l4.7-1.8z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/>',
    "usuarios": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6"/>',
    "estoque": '<path d="M21 8l-9-5-9 5 9 5zM3 8v8l9 5 9-5V8M12 13v8"/>',
    "caixa": '<rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18M7 15h4"/>',
    "agenda": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "grafico": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    "escudo": '<path d="M12 3l7 3v6c0 4.5-3 7.7-7 9-4-1.3-7-4.5-7-9V6z"/><path d="M9 12l2 2 4-4"/>',
    "whats": '<path d="M12 3a9 9 0 0 0-7.8 13.5L3 21l4.6-1.2A9 9 0 1 0 12 3z"/>',
    "qr": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><path d="M14 14h3v3M21 14v.01M14 21h7v-4"/>',
    "cozinha": '<path d="M6 13a6 6 0 0 1 12 0v2H6zM4 15h16M12 7V4M9 19h6"/>',
    "estrela": '<path d="M12 2l2.6 6.3L21 9l-5 4.4L17.5 20 12 16.6 6.5 20 8 13.4 3 9l6.4-.7z"/>',
    "tv": '<rect x="2" y="5" width="20" height="13" rx="2"/><path d="M8 21h8"/>',
    "fila": '<circle cx="5" cy="7" r="2"/><circle cx="12" cy="7" r="2"/><circle cx="19" cy="7" r="2"/><path d="M3 14h18M3 19h12"/>',
    "raio": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
    "pix": '<path d="M12 3l4 4-4 4-4-4zM12 13l4 4-4 4-4-4zM3 12l4-4 4 4-4 4zM13 12l4-4 4 4-4 4z"/>',
    "telegram": '<path d="M21 4L3 11l6 2 2 6 3-4 5 4z"/><path d="M9 13l8-6"/>',
    "planilha": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M3 15h18M9 3v18"/>',
    "link": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
    "relogio": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "roteiro": '<path d="M6 3h9l4 4v14H6zM14 3v5h5M9 13h7M9 17h5"/>',
    "imagem": '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="M21 16l-5-5-9 9"/>',
    "envio": '<path d="M12 16V4M7 9l5-5 5 5M4 20h16"/>',
    "chat": '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>',
    "cardapio": '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 7h6M9 11h6M9 15h4"/>',
    "funil": '<path d="M3 4h18l-7 9v6l-4 2v-8z"/>',
}


def svg(nome, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<svg{c} viewBox="0 0 24 24" aria-hidden="true">{ICONES[nome]}</svg>'


# ---------------------------------------------------------------- conteúdo
SOLUCOES = [
    {
        "slug": "cardapio-digital", "nome": "Cardápio Digital", "icone": "cardapio", "segmento": "Delivery, mesas e balcão",
        "status": ("Pronto para implantar", "pronto"),
        "servico": "Solução Cardápio Digital (pedidos pelo WhatsApp)",
        "imagem": "assets/img/cardapio-digital.jpg", "imagem_url": "tanattos18.github.io/Cardapio_Digital",
        "demo_url": "https://tanattos18.github.io/Cardapio_Digital/", "demo_rotulo": "Ver os 30 modelos",
        "titulo": "Seu cardápio no celular do cliente, com <em>pedido direto no WhatsApp</em>",
        "descricao": "Uma página própria com produtos, fotos, preços, horários e endereço. O cliente monta o pedido, escolhe entrega, retirada ou mesa, e tudo chega organizado no seu WhatsApp. Sem aplicativo para baixar e sem comissão por pedido. São 30 modelos prontos para 10 tipos de negócio, todos com fotos nos produtos.",
        "seo": "Cardápio digital com pedido pelo WhatsApp e QR Code na mesa para hamburguerias, pizzarias, restaurantes, espetinhos, pamonharias, confeitarias, açaí, salgados para festa, marmitas fit e pastelarias. A partir de R$ 297.",
        "menu": [], "kpis": [], "lista": [],
        "dores": [
            ("Comissão em cada pedido", "Aplicativos de delivery ficam com uma parte de cada venda, todo mês."),
            ("Cardápio em PDF ou foto", "Difícil de ler no celular, desatualizado e sem botão para pedir."),
            ("Pedido incompleto no WhatsApp", "Falta endereço, troco ou adicional, e a conversa vai e volta."),
        ],
        "recursos": [
            ("whats", "Pedido pronto no WhatsApp", "Itens, adicionais, total, entrega, retirada ou mesa, endereço, pagamento e troco numa mensagem só."),
            ("qr", "QR Code nas mesas", "Plaquinhas para imprimir: o pedido chega com o número da mesa."),
            ("imagem", "Foto em cada produto", "Todos os produtos com foto, preço promocional, tamanhos, adicionais e selos como Mais pedido e Vegetariano."),
            ("relogio", "Aberto ou fechado na hora", "Mostra se está aberto pelos horários da semana, inclusive quem fecha de madrugada."),
            ("link", "Busca e categorias", "Busca e menu de categorias fixo no topo para o cliente achar rápido."),
            ("raio", "Pronto para divulgar", "Endereço com mapa, redes sociais, botão de compartilhar e prévia bonita nos links."),
        ],
        "para_quem": ["Hamburguerias", "Pizzarias", "Restaurantes", "Espetinhos", "Pamonharias", "Confeitarias", "Açaí e sorvete", "Salgados para festa", "Marmitas fit", "Pastelarias"],
        "inclui": ["Essencial (R$ 297): qualquer modelo com as suas cores e logo, até 40 produtos, QR Code do cardápio e 1 rodada de ajustes", "Completo (R$ 497): até 120 produtos, domínio próprio no primeiro ano, plaquinhas de QR Code por mesa e ajuste das fotos", "Manutenção opcional: R$ 49/mês, com até 10 alterações por mês"],
        "investimento": "Pagamento único a partir de R$ 297. O preço não depende do modelo: escolha qualquer um dos 30 e o plano conforme o tamanho do seu cardápio.",
        "faq": [
            ("Preciso pagar comissão por pedido?", "Não. O pedido vai direto para o seu WhatsApp, sem intermediário."),
            ("Funciona para mesa e para delivery?", "Sim. O cliente escolhe entrega, retirada ou consumo na mesa, e o QR Code da mesa já informa o número."),
            ("Posso mudar preços depois?", "Sim. Com a manutenção de R$ 49/mês você pede até 10 alterações por mês em preços, produtos e promoções."),
        ],
    },
    {
        "slug": "petflow", "nome": "PetFlow", "icone": "pet", "segmento": "Pet shops",
        "status": ("Pronto para implantar", "pronto"),
        "servico": "Solução PetFlow (gestão para pet shop)",
        "titulo": "Seu pet shop <em>organizado</em>, do cadastro do pet ao caixa do dia",
        "descricao": "PetFlow é um sistema online de gestão feito para pet shops de pequeno porte: clientes e animais, agenda de serviços, vendas no balcão, estoque e financeiro num lugar só, acessado pelo navegador.",
        "seo": "PetFlow: sistema de gestão para pet shop com cadastro de clientes e pets, agenda, PDV, estoque e caixa. Implantação pela Akylla Studio.",
        "menu": ["Painel", "Clientes e pets", "Agenda", "PDV", "Estoque", "Caixa"],
        "kpis": [("Vendas hoje", "R$ 1.284"), ("Agendados", "12"), ("Estoque baixo", "3")],
        "lista": [("Banho e tosa · Thor", "09:30", "a"), ("Consulta · Luna", "10:15", "c"), ("Ração 15kg · reposição", "baixo", "b")],
        "dores": [
            ("Agenda no caderno", "Horários de banho e tosa marcados no papel ou no WhatsApp, com esquecimentos e encaixes que não fecham."),
            ("Estoque no escuro", "Você só descobre que a ração acabou quando o cliente pede. Sem histórico de entradas e saídas."),
            ("Caixa que não bate", "No fim do dia ninguém sabe ao certo quanto entrou em dinheiro, cartão e PIX."),
        ],
        "recursos": [
            ("usuarios", "Clientes e pets", "Ficha do tutor com os animais: espécie, raça, sexo e histórico, com busca rápida."),
            ("agenda", "Serviços e agenda", "Catálogo de serviços com preço e duração, e a agenda do dia organizada."),
            ("caixa", "Frente de caixa (PDV)", "Venda por nome, SKU ou código de barras, com comprovante impresso pelo navegador."),
            ("estoque", "Estoque confiável", "Entradas, saídas e ajustes com histórico, e alerta automático de estoque baixo."),
            ("grafico", "Caixa e financeiro", "Abertura e fechamento por turno, diferença calculada pelo sistema e resumo por período."),
            ("escudo", "Acesso seguro", "Perfis de acesso por usuário, dados isolados por empresa e registro de cada operação."),
        ],
        "para_quem": ["Pet shops", "Banho e tosa", "Agropets", "Clínicas veterinárias com loja"],
        "inclui": ["Configuração com a sua marca", "Cadastro inicial de produtos e serviços", "Treinamento da equipe", "Suporte na implantação"],
        "faq": [
            ("Preciso instalar alguma coisa?", "Não. O PetFlow funciona pelo navegador, no computador do balcão, no notebook ou no tablet."),
            ("Dá para usar em mais de uma unidade?", "O sistema separa os dados por empresa. Para várias unidades, avaliamos o melhor formato na conversa."),
            ("Meus dados ficam seguros?", "Sim. Cada pet shop acessa apenas os próprios dados, com perfis de acesso por usuário e registro de cada operação."),
        ],
    },
    {
        "slug": "restaurante", "nome": "SaaS Restaurante", "icone": "rest", "segmento": "Restaurantes e lanchonetes",
        "status": ("Pronto para implantar", "pronto"),
        "servico": "Solução SaaS Restaurante",
        "titulo": "Do pedido no WhatsApp à <em>tela da cozinha</em>, sem papel e sem erro",
        "descricao": "Sistema de gestão para restaurantes e lanchonetes com atendimento automático pelo WhatsApp, cardápio digital por QR Code na mesa e tela de cozinha em tempo real.",
        "seo": "Sistema para restaurante e lanchonete com pedidos pelo WhatsApp, cardápio digital por QR Code, tela de cozinha (KDS) e fidelidade. Akylla Studio.",
        "menu": ["Pedidos", "Cozinha (KDS)", "Cardápio", "Clientes", "Fidelidade", "Relatórios"],
        "kpis": [("Pedidos hoje", "87"), ("Em preparo", "6"), ("Tempo médio", "14 min")],
        "lista": [("#1042 · X-Bacon + fritas", "pronto", "a"), ("#1043 · Mesa 7 · 3 itens", "em preparo", "b"), ("#1044 · WhatsApp · combo", "novo", "c")],
        "dores": [
            ("Pedido anotado errado", "Comanda de papel, letra ilegível e pedido trocado na hora do movimento."),
            ("WhatsApp sem dar conta", "Mensagens acumulando no horário de pico e cliente desistindo de esperar resposta."),
            ("Cozinha sem prioridade", "Ninguém sabe qual pedido está atrasado até o cliente reclamar."),
        ],
        "recursos": [
            ("whats", "Pedidos pelo WhatsApp", "Atendimento automático 24h: cardápio, pedido e pagamento direto na conversa."),
            ("qr", "Cardápio por QR Code", "Cardápio digital na mesa, com categorias, fotos, selos e carrinho de compras."),
            ("cozinha", "Tela da cozinha (KDS)", "Pedidos em colunas Pendentes, Em preparo e Prontos, com som e cronômetro colorido."),
            ("estoque", "Produtos e estoque", "Categorias, variações, preços promocionais e alerta de estoque mínimo."),
            ("estrela", "Clientes e fidelidade", "Cadastro de clientes com programa de pontos e níveis para fazer o cliente voltar."),
            ("grafico", "Painel de resultados", "Métricas e gráficos do restaurante para decidir com números."),
        ],
        "para_quem": ["Restaurantes", "Lanchonetes", "Hamburguerias", "Pizzarias", "Delivery"],
        "inclui": ["Cardápio cadastrado com a sua marca", "Bot de WhatsApp configurado", "QR Codes das mesas", "Treinamento da equipe e da cozinha"],
        "faq": [
            ("Funciona para delivery e para mesa?", "Sim. O cliente pode pedir pelo WhatsApp ou pelo QR Code na mesa, e tudo cai na mesma tela da cozinha."),
            ("Preciso de um número de WhatsApp separado?", "Recomendamos um número dedicado ao restaurante. Explicamos as opções na conversa."),
            ("E se o cliente quiser falar com uma pessoa?", "O bot transfere para um atendente quando o cliente pede ou quando não entende a mensagem."),
        ],
    },
    {
        "slug": "painel-digital", "nome": "Painel Digital", "icone": "painel", "segmento": "Clínicas, lojas e atendimento ao público",
        "status": ("Base adaptável", "pronto"),
        "servico": "Solução Painel Digital (filas e painéis)",
        "titulo": "Chega de senha perdida e cliente <em>chamado no grito</em>",
        "descricao": "Painel Digital é a base de um sistema de atendimento, filas e painéis de chamada em tempo real. Adaptamos para o fluxo de cada cliente: clínica, laboratório, loja, repartição ou qualquer lugar com sala de espera.",
        "seo": "Sistema de senhas, filas e painel de chamada em TV para clínicas, lojas e atendimento ao público. Base adaptável da Akylla Studio.",
        "menu": ["Recepção", "Filas", "Painéis", "Guichês", "Relatórios", "Configurações"],
        "kpis": [("Na fila", "9"), ("Espera média", "7 min"), ("Atendidos", "64")],
        "lista": [("Senha A-042 · Guichê 2", "chamando", "c"), ("Senha P-011 · Preferencial", "aguardando", "b"), ("Senha A-041 · Guichê 1", "atendido", "a")],
        "dores": [
            ("Fila sem controle", "Senhas de papel perdidas, disputa de lugar e clientes chamados de sala em sala."),
            ("Espera invisível", "Ninguém sabe quanto tempo o cliente está esperando, nem onde está o gargalo."),
            ("TV parada na recepção", "A TV da sala de espera não conversa com o atendimento e só passa programação."),
        ],
        "recursos": [
            ("fila", "Filas e senhas", "Emissão e controle de senhas, com filas separadas por tipo de atendimento ou prioridade."),
            ("tv", "Painel de chamada na TV", "A TV da recepção mostra a senha chamada e o guichê, em tempo real."),
            ("usuarios", "Recepção e guichês", "Cada atendente chama o próximo da fila com um clique, sem chamar o mesmo cliente duas vezes."),
            ("raio", "Tempo real", "Chamadas aparecem no painel na hora, sem precisar atualizar a tela."),
            ("grafico", "Relatórios de espera", "Tempo de espera e volume de atendimentos para melhorar o fluxo."),
            ("escudo", "Várias unidades", "Cada estabelecimento com seus próprios dados, painéis e configurações."),
        ],
        "para_quem": ["Clínicas", "Laboratórios", "Lojas", "Órgãos públicos", "Assistências técnicas"],
        "inclui": ["Levantamento do seu fluxo de atendimento", "Adaptação das filas e do painel", "Instalação dos painéis nas TVs", "Treinamento da recepção"],
        "faq": [
            ("O que significa base adaptável?", "É uma base já desenvolvida que ajustamos ao seu fluxo: tipos de fila, prioridades, guichês e visual do painel. Por isso cada projeto é orçado sob medida."),
            ("Preciso comprar uma TV especial?", "Não. Qualquer TV com navegador ou um computador ligado à TV já serve como painel."),
            ("Funciona para mais de uma recepção?", "Sim. Dá para ter várias filas, guichês e painéis no mesmo estabelecimento."),
        ],
    },
    {
        "slug": "burger-bot", "nome": "Burger Bot", "icone": "bot", "segmento": "Hamburguerias e delivery",
        "status": ("Pronto para implantar", "pronto"),
        "servico": "Solução Burger Bot (pedidos pelo WhatsApp)",
        "titulo": "Seu delivery recebendo pedidos no WhatsApp <em>enquanto você cozinha</em>",
        "descricao": "Burger Bot é um robô de pedidos para WhatsApp: o cliente monta o pedido sozinho, paga com PIX copia e cola e a cozinha recebe o aviso na hora. Ideal para hamburguerias e pequenos deliveries.",
        "seo": "Bot de pedidos pelo WhatsApp para hamburguerias e delivery, com PIX copia e cola automático e aviso para a cozinha. Akylla Studio.",
        "menu": ["Pedidos", "Cardápio", "Status", "Cozinha", "Clientes"],
        "kpis": [("Pedidos hoje", "52"), ("Pagos no PIX", "41"), ("Em preparo", "4")],
        "lista": [("Pedido #318 · 2 smash + coca", "pago", "a"), ("Pedido #319 · combo família", "em preparo", "b"), ("Pedido #320 · X-salada", "novo", "c")],
        "dores": [
            ("Atendente preso no celular", "Alguém da equipe passa a noite respondendo mensagem em vez de produzir."),
            ("Pedido incompleto", "Falta endereço, troco ou adicional, e o pedido volta para conferência."),
            ("PIX conferido na mão", "Copiar chave, esperar comprovante e conferir valor atrasa cada entrega."),
        ],
        "recursos": [
            ("whats", "Pedido completo no WhatsApp", "O cliente escolhe os itens, informa o endereço e confirma, tudo na conversa."),
            ("pix", "PIX copia e cola", "O bot gera o PIX com o valor do pedido automaticamente."),
            ("telegram", "Aviso para a cozinha", "Cada pedido novo chega na hora para a cozinha pelo Telegram."),
            ("painel", "Painel de pedidos", "Painel web com filtros por status: novo, confirmado, em preparo e saiu para entrega."),
            ("roteiro", "Cardápio personalizável", "Itens, preços e adicionais do seu cardápio, fáceis de atualizar."),
            ("relogio", "Atendimento 24h", "O bot responde a qualquer hora, inclusive no pico de sexta à noite."),
        ],
        "para_quem": ["Hamburguerias", "Lanchonetes", "Pizzarias", "Açaí", "Delivery em geral"],
        "inclui": ["Cardápio configurado", "Conexão com o seu WhatsApp", "Chave PIX e aviso da cozinha", "Treinamento rápido"],
        "faq": [
            ("Preciso pagar plataforma de delivery?", "Não. O bot funciona no seu próprio WhatsApp, sem comissão por pedido."),
            ("Posso mudar o cardápio depois?", "Sim. Preços, itens e adicionais podem ser atualizados quando você quiser."),
            ("E se o cliente quiser falar com alguém?", "Você continua com acesso à conversa e pode assumir o atendimento a qualquer momento."),
        ],
    },
    {
        "slug": "affiliate-bot", "nome": "Affiliate Bot", "icone": "oferta", "segmento": "Afiliados e canais de ofertas",
        "status": ("Pronto para implantar", "pronto"),
        "servico": "Solução Affiliate Bot (ofertas automáticas)",
        "titulo": "Seu canal de ofertas <em>publicando sozinho</em>, nos horários que vendem",
        "descricao": "Affiliate Bot automatiza a publicação de ofertas de afiliado da Shopee, Amazon e Mercado Livre no Telegram, a partir de uma fila numa planilha do Google, com links encurtados e horários programados.",
        "seo": "Bot que publica ofertas de afiliado da Shopee, Amazon e Mercado Livre automaticamente no Telegram. Akylla Studio.",
        "menu": ["Fila de ofertas", "Agendamento", "Canais", "Links", "Histórico"],
        "kpis": [("Na fila", "34"), ("Publicadas hoje", "18"), ("Próxima", "12:30")],
        "lista": [("Fone Bluetooth · 42% off", "publicada", "a"), ("Air fryer 4L · Amazon", "agendada", "c"), ("Kit skincare · Shopee", "pendente", "b")],
        "dores": [
            ("Postar na mão o dia todo", "Copiar link, encurtar, montar a mensagem e postar, oferta por oferta."),
            ("Perder o horário de pico", "As melhores ofertas saem quando você não está no celular."),
            ("Links bagunçados", "Links longos e sem padrão que derrubam a confiança do seguidor."),
        ],
        "recursos": [
            ("oferta", "Shopee, Amazon e Mercado Livre", "Ofertas dos três marketplaces com o seu link de afiliado."),
            ("planilha", "Fila por planilha", "Você só cola as ofertas numa planilha do Google; o bot cuida do resto."),
            ("telegram", "Publicação no Telegram", "Mensagens formatadas e publicadas automaticamente no seu canal."),
            ("relogio", "Horários de pico", "Modo agendado para publicar nos horários em que o público mais compra."),
            ("link", "Links encurtados", "Links curtos e padronizados em cada oferta."),
            ("escudo", "Modo teste", "Teste as mensagens antes de publicar de verdade."),
        ],
        "para_quem": ["Afiliados", "Canais de promoção", "Grupos de ofertas", "Criadores de conteúdo"],
        "inclui": ["Configuração do bot e do canal", "Planilha de ofertas pronta", "Conexão com as contas de afiliado", "Treinamento de uso"],
        "faq": [
            ("Preciso já ser afiliado?", "Sim, as contas de afiliado são suas. Ajudamos a conectar cada uma ao bot."),
            ("A Amazon funciona desde o início?", "A API da Amazon exige um mínimo de vendas qualificadas para liberar o acesso. Explicamos as alternativas até lá."),
            ("Posso publicar em mais de um canal?", "Sim. Avaliamos a quantidade de canais e o formato na conversa."),
        ],
    },
    {
        "slug": "tiktok-pipeline", "nome": "TikTok Pipeline", "icone": "video", "segmento": "Criadores e marcas",
        "status": ("Pronto para implantar", "pronto"),
        "servico": "Solução TikTok Pipeline (vídeos com IA)",
        "titulo": "Vídeos curtos com IA, <em>do roteiro à publicação</em>, em escala",
        "descricao": "TikTok Pipeline organiza a produção de vídeos curtos com inteligência artificial: roteiros em lote, thumbnails, vozes e pastas prontas para editar e publicar, com opções para diferentes orçamentos.",
        "seo": "Produção de vídeos curtos para TikTok com IA: roteiros em lote, thumbnails, vozes e publicação. Akylla Studio.",
        "menu": ["Roteiros", "Thumbnails", "Vozes", "Edição", "Publicação"],
        "kpis": [("Roteiros", "30"), ("Vídeos prontos", "12"), ("Contas", "3")],
        "lista": [("Vídeo 07 · gancho curiosidade", "publicado", "a"), ("Vídeo 08 · lista top 5", "editando", "b"), ("Lote 03 · 10 roteiros", "gerado", "c")],
        "dores": [
            ("Falta de ideia todo dia", "Pensar em roteiro novo diariamente trava a constância."),
            ("Produção lenta", "Escrever, gravar, criar capa e organizar arquivos toma horas por vídeo."),
            ("Postagem irregular", "Sem processo, a frequência cai e o algoritmo para de entregar."),
        ],
        "recursos": [
            ("roteiro", "Roteiros em lote", "Vários roteiros de uma vez, com ganchos pensados para prender a atenção."),
            ("imagem", "Thumbnails com IA", "Capas geradas por IA para cada vídeo."),
            ("chat", "Vozes geradas", "Narração gerada por IA para quem não quer aparecer ou gravar."),
            ("planilha", "Pastas organizadas", "Cada vídeo com roteiro, capa e áudio prontos na sua pasta."),
            ("envio", "Publicação", "Fluxo para publicar, inclusive em mais de uma conta."),
            ("grafico", "Modos por orçamento", "Opções do gratuito ao pago, conforme as ferramentas que você quer usar."),
        ],
        "para_quem": ["Criadores de conteúdo", "Marcas e lojas", "Agências", "Perfis de nicho"],
        "inclui": ["Configuração das ferramentas de IA", "Modelo de roteiro para o seu nicho", "Organização do fluxo de produção", "Treinamento de uso"],
        "faq": [
            ("Preciso aparecer nos vídeos?", "Não necessariamente. O fluxo funciona com narração por IA e imagens."),
            ("As ferramentas de IA são pagas?", "Há modos gratuitos e pagos. Mostramos o custo de cada opção antes de começar."),
            ("Serve para outras redes?", "Os vídeos verticais também servem para Reels e Shorts."),
        ],
    },
    {
        "slug": "atlasops-ai", "nome": "AtlasOps AI", "icone": "ia", "segmento": "Pequenas e médias empresas",
        "status": ("Em desenvolvimento", "dev"),
        "servico": "Solução AtlasOps AI (atendimento com IA)",
        "titulo": "Atendimento e operação com <em>inteligência artificial</em> para sua empresa",
        "descricao": "AtlasOps AI está em desenvolvimento: uma central de atendimento em vários canais com IA para triagem e respostas, registro de leads e acompanhamento por relatórios. Estamos conversando com empresas interessadas em ser projeto piloto.",
        "seo": "AtlasOps AI: atendimento omnichannel com inteligência artificial, triagem automática e registro de leads para pequenas e médias empresas. Em desenvolvimento.",
        "menu": ["Atendimentos", "Leads", "Automações", "IA", "Relatórios"],
        "kpis": [("Conversas", "128"), ("Resolvidas pela IA", "61%"), ("Leads novos", "23")],
        "lista": [("Maria · WhatsApp · orçamento", "lead", "c"), ("João · e-mail · suporte", "resolvido", "a"), ("Ana · chat do site", "triagem", "b")],
        "dores": [
            ("Mensagens em todo lugar", "WhatsApp, e-mail e chat do site separados, e cliente esquecido em algum deles."),
            ("Perguntas repetidas", "A equipe responde as mesmas dúvidas o dia inteiro."),
            ("Lead que esfria", "Contato interessado sem retorno rápido e sem acompanhamento."),
        ],
        "recursos": [
            ("chat", "Central multicanal", "WhatsApp, e-mail e chat do site reunidos numa só caixa de atendimento."),
            ("ia", "IA para triagem e respostas", "A IA classifica, responde dúvidas comuns e resume conversas."),
            ("funil", "Registro de leads", "Cada contato vira um lead registrado, com status e histórico."),
            ("raio", "Automações", "Fluxos que levam a informação do atendimento para a operação."),
            ("grafico", "Relatórios", "Painel para acompanhar volume, tempo de resposta e resultados."),
            ("escudo", "Seus dados com você", "Ferramentas de código aberto e dados sob controle da sua empresa."),
        ],
        "para_quem": ["Pequenas e médias empresas", "Prestadores de serviço", "Lojas com alto volume de mensagens"],
        "inclui": ["Diagnóstico do seu atendimento", "Projeto piloto sob medida", "Acompanhamento próximo na implantação"],
        "faq": [
            ("Já posso contratar?", "A solução está em desenvolvimento. Empresas interessadas podem conversar sobre um projeto piloto."),
            ("A IA substitui a equipe?", "Não. Ela responde o repetitivo e organiza a fila para a equipe focar no que precisa de pessoa."),
            ("Quais canais entram?", "O planejamento inclui WhatsApp, e-mail e chat do site."),
        ],
    },
]

# ---------------------------------------------------------------- modelo
INICIO = "<!-- SOLUCOES:DETALHES:INICIO (gerado por _gerador/solucoes.py, não edite à mão) -->"
FIM = "<!-- SOLUCOES:DETALHES:FIM -->"


def detalhe(s):
    nome = escape(s["nome"])
    status, status_cls = s["status"]
    dev = status_cls == "dev"
    cta = "Quero ser projeto piloto" if dev else "Quero essa solução"
    servico = escape(s["servico"], quote=True)

    menu = "".join(f"<li>{escape(m)}</li>" for m in s["menu"])
    kpis = "".join(f'<div class="app__kpi"><small>{escape(a)}</small><b>{escape(b)}</b></div>' for a, b in s["kpis"])
    lista = "".join(f'<div class="app__item"><span>{escape(a)}</span><span class="app__pill app__pill--{c}">{escape(b)}</span></div>' for a, b, c in s["lista"])
    dores = "".join(f'<article class="dor"><span class="dor__x">✕</span><h4>{escape(t)}</h4><p>{escape(d)}</p></article>' for t, d in s["dores"])
    recursos = "".join(f'<article class="recurso"><div class="recurso__icone">{svg(i)}</div><h4>{escape(t)}</h4><p>{escape(d)}</p></article>' for i, t, d in s["recursos"])
    para = "".join(f"<span>{escape(p)}</span>" for p in s["para_quem"])
    inclui = "".join(f"<li>{escape(i)}</li>" for i in s["inclui"])
    faq = "".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in s["faq"])
    texto_impl = ("Estamos selecionando empresas para os primeiros projetos piloto. Conte como é o seu atendimento e montamos uma proposta."
                  if dev else
                  "Como a base já existe, a implantação é mais rápida e o custo menor do que um sistema do zero. O valor depende do tamanho da operação e das adaptações, e você recebe tudo por escrito antes de começar.")

    demo = (f'\n            <a href="{s["demo_url"]}" class="btn btn--fantasma" target="_blank" rel="noopener">{escape(s["demo_rotulo"])} ↗</a>'
            if s.get("demo_url") else "")

    if s.get("imagem"):
        visual = f'''
          <div class="app app--print">
            <div class="app__barra"><i></i><i></i><i></i><span>{escape(s["imagem_url"])}</span></div>
            <a href="{s.get("demo_url", "#")}" target="_blank" rel="noopener" tabindex="-1"><picture><source type="image/webp" srcset="{s["imagem"].replace(".jpg", "-640.webp")} 640w, {s["imagem"].replace(".jpg", ".webp")} 1200w" sizes="(max-width: 860px) 100vw, 480px"><img src="{s["imagem"]}" alt="" width="1440" height="900" loading="lazy"></picture></a>
          </div>
          <p class="app__aviso">Vitrine real do projeto, no ar. Clique para abrir.</p>'''
    else:
        visual = f'''
          <div class="app">
            <div class="app__barra"><i></i><i></i><i></i><span>{s["slug"]}.akyllastudio</span></div>
            <div class="app__corpo">
              <div class="app__menu">
                <div class="app__logo"><span>{svg(s["icone"])}</span>{nome}</div>
                <ul>{menu}</ul>
              </div>
              <div class="app__conteudo">
                <div class="app__kpis">{kpis}</div>
                <div class="app__lista">{lista}</div>
              </div>
            </div>
          </div>
          <p class="app__aviso">Ilustração da interface. Dados fictícios.</p>'''

    return f'''
    <dialog class="detalhe" id="solucao-{s["slug"]}" aria-labelledby="titulo-{s["slug"]}">
      <button type="button" class="detalhe__fechar" data-fechar aria-label="Fechar">✕</button>
      <div class="detalhe__hero">
        <div>
          <div class="sol-hero__selos">
            <span class="selo">{svg(s["icone"], "selo__icone")} {nome} · {escape(s["segmento"])}</span>
            <span class="status-tag status-tag--{status_cls}">{escape(status)}</span>
          </div>
          <h2 id="titulo-{s["slug"]}">{s["titulo"]}</h2>
          <p class="detalhe__texto">{escape(s["descricao"])}</p>
          <div class="detalhe__acoes">
            <a href="#" class="btn" data-servico="{servico}">{svg("whats")} {cta}</a>{demo}
          </div>
        </div>
        <div>{visual}
        </div>
      </div>

      <h3 class="detalhe__titulo">Os problemas que o {nome} resolve</h3>
      <div class="sol-dores">{dores}</div>

      <h3 class="detalhe__titulo">O que vem incluso</h3>
      <div class="recursos">{recursos}</div>

      <h3 class="detalhe__titulo">Para quem é</h3>
      <div class="para-quem">{para}</div>

      <div class="investimento">
        <div>
          <p class="rotulo">Implantação e investimento</p>
          <h3>{"Projeto piloto sob medida" if dev else "Pronto em pouco tempo, com a sua marca"}</h3>
          <p>{s.get("investimento", texto_impl)}</p>
          <a href="#" class="btn" data-servico="{servico}">{svg("whats")} {cta}</a>
        </div>
        <ul>{inclui}<li>Proposta por escrito com escopo, prazo e valor</li><li>Pagamento em 2 etapas: 50% para iniciar e 50% na entrega aprovada</li></ul>
      </div>

      <h3 class="detalhe__titulo">Perguntas frequentes</h3>
      <div class="detalhe__faq">{faq}</div>
    </dialog>'''


if __name__ == "__main__":
    indice = RAIZ / "index.html"
    html = indice.read_text(encoding="utf-8")
    assert INICIO in html and FIM in html, "marcadores não encontrados no index.html"
    antes, resto = html.split(INICIO, 1)
    _, depois = resto.split(FIM, 1)
    blocos = "".join(detalhe(s) for s in SOLUCOES)
    indice.write_text(antes + INICIO + blocos + "\n    " + FIM + depois, encoding="utf-8")
    print(f"{len(SOLUCOES)} detalhes de solução atualizados no index.html")
