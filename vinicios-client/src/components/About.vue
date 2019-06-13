<template>
  <v-container class="cont1">
    <v-sheet class="ma-2 pa-3" elevation="12" color="rgb(255, 255, 255,0.6)">
      <v-img
        :src="require('../assets/vinicios.svg')"
        contain
        height="400"
      ></v-img>
      <div class="display-4">Project Report: Vinícios Wine App</div>
    </v-sheet>
    <v-layout>
      <v-flex xs12 md6>
        <v-img
          :src="require('../assets/about1.jpg')"
          stretch
          height="100%"
        ></v-img>
      </v-flex>
      <v-flex xs12 md6>
        <v-sheet class="pa-3 sh1">
          <div class="display-3">Introdução</div>
          <div class="body-1">
            A presente secção tem em vista a consolidação de todo o processo de
            desenvolvimento e utilização da aplicação desenvolvida no âmbito da
            unidade curricular de Processamento e Representação de Conhecimento,
            no ano letivo de 2018/2019. O enunciado do trabalho propôs o
            desenvolvimento de uma aplicação WEB capaz de explorar toda a
            informação proveniente de um dataset que, depois de convertido para
            a extensão .ttl, fosse incluido na instância local de um servidor
            GraphDB.
            <b>Vinícios</b> é o resultado final da submissão.
          </div>
          <div class="display-2">Dataset</div>
          <div class="body-1">
            O contexto da aplicação e todos os dados nela presentados são
            provenientes do dataset
            <a :href="'https://www.kaggle.com/zynicide/wine-reviews'"
              >Wine Reviews</a
            >
            que contém a informação relativa a reviews de cerca de 130 mil
            vinhos de todo o planeta. Os campos incluem a generalidade da
            descrição dos vinhos (preço, castas, designação), do enólogo que o
            descreveu e pontuou, Cooperativa e país de proveniência.
          </div>
        </v-sheet>
      </v-flex>
    </v-layout>
    <v-layout>
      <v-flex xs12 md6>
        <v-sheet class="pa-3 sh1">
          <div class="display-3">Ontologia</div>
          <div class="body-1">
            A análise de algumas entradas do dataset deu o mote para a descrição
            da Ontologia, criada através do Protégé.
          </div>
          <div class="display-2">Classes</div>
          <v-container grid-list-md>
            <v-layout>
              <v-flex md5 xs12 text-md-right>
                <v-card class="card1" height="100%">
                  <v-card-title>
                    <div class="display-1">Country</div>
                  </v-card-title>
                  <v-card-text>
                    <div class="body-2">Object Props</div>
                    <div class="body-1">countryHasWine(range:Wine)</div>
                    <div class="body-1">hasProvince(range:Province)</div>
                    <div class="body-1">hasWinery (range:Winery)</div>
                    <div class="body-2">Data Props</div>
                    <div class="body-1">countryName</div>
                  </v-card-text>
                </v-card>
              </v-flex>
              <v-flex md7 xs12 text-md-left>
                <v-card class="card1" height="100%">
                  <v-card-title>
                    <div class="display-1">Wine</div>
                  </v-card-title>
                  <v-card-text>
                    <div class="body-2">Object Props</div>
                    <div class="body-1">isFrom(range:Country)</div>
                    <div class="body-1">fromProvince(range:Province)</div>
                    <div class="body-1">fromProvince(range:Province)</div>
                    <div class="body-1">hasReview(range:Review)</div>
                    <div class="body-1">hasTaster(range:Taster)</div>
                    <div class="body-2">Data Props</div>
                    <div class="body-1">
                      designation, price, region_1, region_2, title, variety
                    </div>
                  </v-card-text>
                </v-card>
              </v-flex>
            </v-layout>
            <v-layout>
              <v-flex md7 xs12 text-md-right>
                <v-card class="card1" height="100%">
                  <v-card-title>
                    <div class="display-1">Winery</div>
                  </v-card-title>
                  <v-card-text>
                    <div class="body-2">Object Props</div>
                    <div class="body-1">hasWine(range:Wine)</div>
                    <div class="body-1">hasCountry(range:Country)</div>
                    <div class="body-2">Data Props</div>
                    <div class="body-1">wineryName</div>
                  </v-card-text>
                </v-card>
              </v-flex>
              <v-flex md5 xs12 text-md-left>
                <v-card class="card1" height="100%">
                  <v-card-title>
                    <div class="display-1">Review</div>
                  </v-card-title>
                  <v-card-text>
                    <div class="body-2">Object Props</div>
                    <div class="body-1">isReviewOf(range:Wine)</div>
                    <div class="body-2">Data Props</div>
                    <div class="body-1">description, points</div>
                  </v-card-text>
                </v-card>
              </v-flex>
            </v-layout>
            <v-layout>
              <v-flex md6 xs12 text-md-right>
                <v-card class="card1" height="100%">
                  <v-card-title>
                    <div class="display-1">Taster</div>
                  </v-card-title>
                  <v-card-text>
                    <div class="body-2">Object Props</div>
                    <div class="body-1">tastedWine(range:Wine)</div>
                    <div class="body-2">Data Props</div>
                    <div class="body-1">taster_name, taster_twitter_handle</div>
                  </v-card-text>
                </v-card>
              </v-flex>
              <v-flex md6 xs12 text-md-left>
                <v-card class="card1" height="100%">
                  <v-card-title>
                    <div class="display-1">Province</div>
                  </v-card-title>
                  <v-card-text>
                    <div class="body-2">Object Props</div>
                    <div class="body-1">fromCountry(range:Country)</div>
                    <div class="body-1">isOriginOf(range:Wine)</div>
                    <div class="body-2">Data Props</div>
                    <div class="body-1">provinceName</div>
                  </v-card-text>
                </v-card>
              </v-flex>
            </v-layout>
          </v-container>
        </v-sheet>
      </v-flex>
      <v-flex xs12 md6>
        <v-img
          :src="require('../assets/about2.jpg')"
          stretch
          height="100%"
        ></v-img>
      </v-flex>
    </v-layout>
    <v-layout>
      <v-flex xs12 md6>
        <v-img
          :src="require('../assets/about3.jpg')"
          stretch
          height="100%"
        ></v-img>
      </v-flex>
      <v-flex xs12 md6>
        <v-sheet class="pa-3 sh1">
          <div class="display-3">Conversão JSON-TTL</div>
          <div class="body-1">
            Dada a extensão do dataset obtido, foi necessária a sua conversão
            para um formato compatível com o GraphDB, neste caso, .ttl, seguindo
            os seguintes passos:
          </div>
          <div class="body-1">
            <ul>
              <li>
                <b>Tratamento de caracteres especiais:</b> os identificadores
                gerados apenas podem conter caracteres alfanuméricos e uma
                seleção de símbolos. Assim, com ajuda do módulo <b>re</b>, foram
                substituídos todos os caracteres indevidos, para nào causar
                conflito na importação do ficheiro final.
              </li>
              <li>
                <b>Leitura das entradas .JSON:</b> o ficheiro é fornecido
                automaticamente, desde que se encontre na pasta de execução do
                script (alternativamente, através da alteração do caminho
                pré-definido) e, para cada entrada, são preenchidos até 6
                dicionários, cada um correspondende a cada uma das classes da
                Ontologia. Isto assegura que, aquando da conversão final, todas
                as <i>Object Properties</i> de cada indivíduo serão incluídas.
              </li>
              <li>
                <b>Geração de ID de países:</b> de modo a fazer uso de uma API
                externa, foi adicionado um ID a cada país, de acordo com o
                protocolo em
                <a :href="'https://www.countryflags.io/'">Country Flags .io</a>
                . Posteriormente, este ID será utilizado para fazer corresponder
                a cada país a sua bandeira nacional.
              </li>
              <li>
                <b>Conversão de dicionários:</b> os dicionários de cada classe
                são convertidos em formato textual para a linguagem Turtle e
                concatenados com o ficheiro gerado pelo <b>Protégé</b>, que
                serve como cabeçalho da Ontologia. O número de entradas lidas
                foi limitado devido ao consumo energético e temporal do número
                original de entradas.
              </li>
            </ul>
            <div class="body-1">
              A importação para o GraphDB gerou cerca de 30 mil
              <i>statements</i>, dos quais, 25 mil são explícitos.
            </div>
          </div>
        </v-sheet>
      </v-flex>
    </v-layout>
    <v-layout>
      <v-flex xs12 md6>
        <v-sheet class="pa-3 sh1">
          <div class="display-3">Backend</div>
          <div class="body-1">
            Fazendo recurso da linguagem NodeJS, foi desenhado um servidor cuja
            funcionalidade é responder a todos os pedidos provenientes do
            Frontend da aplicação. As suas rotas são muito específicas e
            respondem apenas com informação JSON proveniente do envio de queries
            SPARQL.
          </div>
          <div class="display-3">Frontend</div>
          <div class="body-1">Por fim, a aplicação criada em VueJS.</div>
          <div class="body-1">
            O objetivo maior do Frontend da aplicação (a par com a conexão com o
            seu contexto) foi a inclusão de componentes diversos, de modo a
            explorar um pouco mais as possibilidades do desenvolvimento em Vue.
            Em vários componentes é visível o uso de componentes de Grelha em
            funcionamento com diferentes
            <i>breakpoints</i> da página, para que a sua visualização não seja
            afetada por diferentes tamanhos de ecrã.
          </div>
          <div class="body-1">
            Os componentes como
            <b>WineListing</b> ou <b>SelectedWine</b> dependem da correta
            utilização das rotas to backend e calculam as suas estruturas de
            dados aquando da criação do DOM da página. Inicialmente, é enviado
            um pedido get para receber os dados relativos ao componente, com a
            finalidade de os dispor em elementos ordenados (Tabelas,
            grelhas,...). Durante todo o processo de desenvolvimento houve um
            foco especial na estilização dos componentes, de modo a tentar
            tornar a aplicação o mais próxima possível de uma real iteração do
            problema.
          </div>
          <div class="body-1">
            Foi com o mesmo intuito que foi desenvolvido o logotipo, baseado em
            elementos alusivos ao contexto, como a garrafa de vinho e o copo de
            degustação.
          </div>
        </v-sheet>
      </v-flex>
      <v-flex xs12 md6>
        <v-img
          :src="require('../assets/about4.jpg')"
          stretch
          height="100%"
        ></v-img>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {};
</script>

<style scoped>
.cont1 {
  margin-top: 70px;
  background-color: rgb(150, 104, 52, 0.2);
}
.sh1 {
  background-color: rgb(255, 150, 71, 0.8);
}
.sh2 {
  background-color: rgb(204, 202, 189, 0.5);
  margin-left: 27%;
  margin-right: 27%;
}
.card1 {
  background-color: bisque;
}
</style>
