<h1 align="center"> Projeto Nutricionista </h1>

<h2 align="center">Skills: <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=gree"/>  <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E"/>  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=whitehttps://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white"/>  <img src="https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=black">   <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/></h2>

<h3 align="justify">Objetivo: o Projeto Nutricionista que define como NUTRI LIFE, criei para aperfeiçoamento meus conhecimentos no curso Python Full na plataforma Hotmart. Dessa maneira, desenvolvi os aplicativos usando habilidades, determinei como:  autenticação dos usuários (Nutricionistas) que registrou e realizou login, e por fim,  na plataforma detalhará as informações sob cada paciente de um determinado nutricionista. </h3>

<h3>Desafios:</h3>
<ul style="list-style-type:square">
  <h4>Autenticação</h4>
  <li align="justify">Registrar-se: implementa no APP no views.py o def (função) de verificação se já existe emails ou usuários que retorna uma messagem de WARNING, no caso da senha foi definido letras maiuscula, minuscula e número, contendo no mínimo 6 caracteres, podendo retorna uma messagem de SUCCESS ou ERROR. Ressaltando, que gerará dentro da função ativar_conta no console o token/link para confirma o cadastramento do nutricionista.</li>
  <li align="justify">Loga-se: na views.py o def (função) de confirmação existe usuários e senha que retorna uma messagem de SUCCESS ou WARNING. Salientado, a preocupação que usuário mal intencionado poderá entrar na plataforma mesmo sem está logado, com isso, para resolver isso utilizei em cima das funções @login_required(login_url='/auth/logar/') e observação que está faltando implemnta a recuperação de senha.</li>
  <li align="justify">Sair: na views.py o def (função) só foi implementado auth.logout(request).</li>
  
  
  <h4>Plataforma</h4>
  <li align="justify">Paciente: estabelecido no APP no views.py o def (função) as variáveis como nome, sexo, idade, email, telefone e a imagem, relaziando uma verificação de espaçamento dentro de cada input dentro do formulário, assim, para válida as informações coloquei no pacientes.html {% csrf_token %}. Dessa maneira, definir os parâmetros na class (classe) em models.py para recebe no banco de dado (db.sqlite3), que cada nutricionista recebe CASCADE se apagar um, deleta todos os pacientes do mesmo. </li>
  <li align="justify">Dados: filtando pelo id do paciente e trazendo o formulário que receberá paciente(Foreignkey), peso, alutra, percentual gordura, percentual musculo, colesterol hdl, colesterol ldl, colesterol total e trigliceridios. Com isso, poderá obter os dados e amostrar na tabela e no gráfico. </li>
  <li align="justify">Refeição: que terá o título, horário, carboidratos, proteinas e as gorduras de cada paciente específico. Dessa maneira, poderá detalha no cárdapio qual será a alimentação, junto com a imagem e com as descrição do mesmo. Portanto, nutricionista poderá gerá o PDF( utilizdo a biblioteca do FPDF) com os cárdapios de cada pacientes. </li>

</ul>

<h3>Conclusão:</h3>
<p align="justify">Já estou tendo algumas facilidades de comados no Terminal(ubuntu) ou PowerShellFaltando(windows), agilizando e agregado no desenvolvimento do projeto. Conseguinte, ainda falta codificar a "imagem do paciente, trazer por data a tabela e juntamente o gráfico e organizar todas as informações gerado pelo o PDF".</p>
