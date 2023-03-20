<h1 align="center"> Projeto Nutricionista </h1>

<h2 align="center">Skills: <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=gree"/>  <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E"/>  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=whitehttps://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white"/>  <img src="https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=black">   <img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/>   <img src="https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white"></h2>

<h2 align="center"> Prévia <h2>
<<<<<<< HEAD
<img src="https://im.ezgif.com/tmp/ezgif-1-1331d4b262.gif">  
=======





<h3 align="justify">Objetivo: o Projeto Nutricionista que define como NUTRI LIFE, criei para aperfeiçoamento meus conhecimentos no curso Python Full na plataforma Hotmart. Dessa maneira, desenvolvi os aplicativos usando habilidades, determinei como:  autenticação dos usuários (Nutricionistas) que registrou e realizou login, e por fim,  na plataforma detalhará as informações sob cada paciente de um determinado nutricionista. </h3>
>>>>>>> 1d0f5d4ad65bad6e9c89254953d5abbba61f8ccb



<h3>Objetivo</h3>
<h4 align="justify"> o Projeto Nutricionista que define como NUTRI LIFE, criei para aperfeiçoamento meus conhecimentos no curso Python Full na plataforma Hotmart. Dessa maneira, desenvolvi os aplicativos usando habilidades, determinei como:  autenticação dos usuários (Nutricionistas) que registrou e realizou login, e por fim,  na plataforma detalhará as informações sob cada paciente de um determinado nutricionista. </h4>

<h3>Etapas</h3>
<ul style="list-style-type:square">
  <h4><a href="https://github.com/pedro-hnrq/Proj_Nutric/tree/main/autenticacao">Autenticação</a></h4>
  <li align="justify">O sistema web em Django que requer autenticação de usuários. Para isso, estou utilizando as funcionalidades de autenticação do Django Auth, que me permite implementar o registro de usuário, o login e o logout. </li>
  <li align="justify">Registrar-se: para o registro de usuário, eu criei uma função que verifica se já existe um usuário ou email cadastrado e se a senha atende aos requisitos de segurança. Após isso, eu crio o usuário e envio um token/link de ativação da conta para o email cadastrado. Com isso, eu garanto que apenas usuários autenticados terão acesso à minha plataforma.</li>
  <li align="justify">Loga-se: criei uma função que autentica o usuário e faz o seu login. É importante lembrar que eu utilizei o decorador "@login_required" para impedir que usuários mal intencionados acessem a plataforma sem estar logados. </li>
  <li align="justify">Sair: criei uma função que faz o logout do usuário autenticado, permitindo que outro usuário possa realizar o login na plataforma.</li>
  <li align="justify">Com essas funcionalidades implementadas, eu tenho um sistema de autenticação de usuários seguro e eficiente em minha aplicação Django, garantindo a privacidade e segurança dos dados dos meus usuários.</li>
  
  <h4><a href="https://github.com/pedro-hnrq/Proj_Nutric/tree/main/plataforma">Plataforma</a></h4>
  
  <li align="justify">Paciente: estabelecido no APP no views.py o def (função) as variáveis como nome, sexo, idade, email, telefone e a imagem, relaziando uma verificação de espaçamento dentro de cada input dentro do formulário, assim, para válida as informações coloquei no pacientes.html {% csrf_token %}. Dessa maneira, definir os parâmetros na class (classe) em models.py para recebe no banco de dado (db.sqlite3), que cada nutricionista recebe CASCADE se apagar um, deleta todos os pacientes do mesmo. </li>
  <li align="justify">Dados: filtando pelo id do paciente e trazendo o formulário que receberá paciente(Foreignkey), peso, alutra, percentual gordura, percentual musculo, colesterol hdl, colesterol ldl, colesterol total e trigliceridios. Com isso, poderá obter os dados e amostrar na tabela e no gráfico. </li>
  <li align="justify">Refeição: que terá o título, horário, carboidratos, proteinas e as gorduras de cada paciente específico. Dessa maneira, poderá detalha no cárdapio qual será a alimentação, junto com a imagem e com as descrição do mesmo. Portanto, nutricionista poderá gerá o PDF( utilizdo a biblioteca do FPDF) com os cárdapios de cada pacientes. </li>

</ul>

<h3>Conclusão</h3>
<p align="justify">Já estou tendo algumas facilidades de comados no Terminal(ubuntu) ou PowerShell(windows), agilizando e agregado no desenvolvimento do projeto. Conseguinte, ainda falta codificar a "imagem do paciente, trazer por data a tabela e juntamente o gráfico e organizar todas as informações gerado pelo o PDF".</p>
