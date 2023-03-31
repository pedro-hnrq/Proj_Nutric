<h1 align="center"> Projeto Nutricionista </h1>

<h2 align="center">Skills: <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=gree"/>  <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E"/>  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=whitehttps://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white"/>  <img src="https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=black">   <img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/>   <img src="https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white"></h2>

<h2 align="center"> Prévia <h2>


![proj_Nutri](https://user-images.githubusercontent.com/74242717/226347115-6722947f-ed40-48c3-abc4-e8e80ff37098.gif)


<h3>Objetivo</h3>
<h4 align="justify"> Com meus conhecimentos em programação, bem como as habilidades adquiridas durante meu treinamento em Python Full na plataforma <a href="https://plataforma.pythonando.com.br/">Pythonando</a>, o Projeto Nutricionista, que nomeei de NUTRI LIFE, oferece uma plataforma que possua funcionalidades de autenticação, permitindo o login, registro e sair dos nutricionista, e de cadastro de pacientes, com detalhes importantes sobre cada um deles, além do plano alimentar prescrito pelo nutricionista responsável.</h4>

<h3>Etapas</h3>
<ul style="list-style-type:square">
  <h4><a href="https://github.com/pedro-hnrq/Proj_Nutric/tree/main/autenticacao">Autenticação</a></h4>
  <li align="justify">O sistema web em Django que requer autenticação de usuários. Para isso, estou utilizando as funcionalidades de autenticação do Django Auth, que me permite implementar o registro de usuário, o login e o logout. </li>
  <li align="justify">Registrar-se: para o registro de usuário, eu criei uma função que verifica se já existe um usuário ou email cadastrado e se a senha atende aos requisitos de segurança. Após isso, eu crio o usuário e envio um token/link de ativação da conta para o email cadastrado. Com isso, eu garanto que apenas usuários autenticados terão acesso à minha plataforma.</li>
  <li align="justify">Loga-se: criei uma função que autentica o usuário e faz o seu login. É importante lembrar que eu utilizei o decorador "@login_required" para impedir que usuários mal intencionados acessem a plataforma sem estar logados. </li>
  <li align="justify">Sair: criei uma função que faz o logout do usuário autenticado, permitindo que outro usuário possa realizar o login na plataforma.</li>
  <li align="justify">Com essas funcionalidades implementadas, eu tenho um sistema de autenticação de usuários seguro e eficiente em minha aplicação Django, garantindo a privacidade e segurança dos dados dos meus usuários.</li>
  
  <h4><a href="https://github.com/pedro-hnrq/Proj_Nutric/tree/main/plataforma">Plataforma</a></h4>
  
  <li align="justify">Cadastro do Paciente: foi estabelecido no APP um método no views.py para capturar as informações do paciente, como: nome, sexo, idade, email, telefone e uma foto. Nesse processo, foi realizada uma verificação de espaçamento dentro de cada input do formulário. Para validar as informações, foi utilizado {% csrf_token %} no arquivo pacientes.html. Além disso, defini os parâmetros na classe no models.py para receber as informações e armazená-las no banco de dados (db.sqlite3). Cada nutricionista é associado aos seus pacientes através de um CASCADE, de forma que, se um nutricionista é excluído, todos os seus pacientes também são excluídos. Isso garante a integridade dos dados e a facilidade na administração do sistema. </li>
  <li align="justify">Dados do Paciente: para obter os dados do paciente, foi utilizado o método GET para buscar todas as informações cadastradas e filtrar pelo ID do paciente. O formulário é preenchido com as informações do paciente, que é definido como uma chave estrangeira (Foreignkey na classe que ficou definida no models.py), e permite que sejam adicionados novos dados, como peso, altura, percentual de gordura, percentual de músculo, colesterol HDL, colesterol LDL, colesterol total e triglicerídeos.Com essas informações, é possível visualizar os dados do paciente na tabela e no gráfico utilizando o chart.js, proporcionando uma visualização mais clara e objetiva dos dados coletados. Essa funcionalidade ajuda no acompanhamento nutricional do paciente e na avaliação dos resultados obtidos com as orientações nutricionais recebidas. </li>
  <li align="justify">Plano Alimenta: é necessário selecionar o paciente pelo ID e, em seguida, clicar no botão "Nova Refeição". Nesse processo, o nutricionista poderá definir o título da refeição, o horário e a quantidade de carboidratos, proteínas e gorduras necessários para o paciente em questão. Ao clicar no botão "Nova Opção", o nutricionista poderá escolher entre as opções de refeições definidas anteriormente, selecionando o título da refeição e adicionando uma imagem dos alimentos e a descrição da alimentação para o paciente. Todos os detalhes cadastrados são exibidos no plano alimentar. Por fim, é possível gerar um PDF com todas as informações detalhadas de cada paciente, utilizando a biblioteca FPDF. Essa funcionalidade permite que o nutricionista possa fornecer um plano alimentar completo e de fácil acesso para o paciente, ajudando no acompanhamento nutricional e no alcance dos objetivos propostos. </li>

</ul>

<h3>Conclusão</h3>
<p align="justify">Durante o desenvolvimento do projeto, utilizei algumas facilidades de comandos no Terminal do Ubuntu ou PowerShell do Windows, juntamente com os comandos do framework Django e as bibliotecas específicas do Python. Essas ferramentas contribuíram significativamente para agilizar e aprimorar o desenvolvimento do projeto.

Apesar das dificuldades enfrentadas e de muita pesquisa realizada, consegui capturar as imagens dos pacientes e exibi-las na plataforma com a biblioteca PIL. Além disso, pude manipular a tabela com gráficos utilizando a biblioteca chart.js e gerar PDFs com várias informações do paciente do nutricionista, utilizando a biblioteca FPDF.

Com todas essas funcionalidades incorporadas ao projeto, a plataforma Nutri Life se tornou uma ferramenta completa e eficiente para nutricionistas que desejam gerenciar seus pacientes de forma prática e intuitiva..</p>
