var axios = require('axios');
const Winery = module.exports;
async function execQuery(query) {
  try {
    var encoded = encodeURIComponent(query);
    var resp = await axios.get(
      'http://localhost:7200/repositories/PRC-TP?query=' + encoded
    );
    var jsonLst = [];
    resp.data.results.bindings.forEach(element => {
      jsonLst.push(element);
    });

    return jsonLst;
  } catch (err) {
    console.log(err.message);
  }
}

Winery.listWineries = () => {
  const query = `PREFIX : <http://prc.di.uminho.pt/2019/a75870/>
      select ?s ?name ?ctn where {
          ?s a :Winery.
          ?s :wineryName ?name.
          ?s :hasCountry ?ctr.
          ?ctr :countryName ?ctn.
      }`;
  return execQuery(query);
};
Winery.getByID = id => {
  const query = `PREFIX : <http://prc.di.uminho.pt/2019/a75870/>
    select ?tit where {
      :${id} :wineryName ?tit.
    }`;
  return execQuery(query);
};
Winery.getByTitle = t => {
  const query = `PREFIX : <http://prc.di.uminho.pt/2019/a75870/>
  PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    select ?name ?wtit ?wn where {
      ?w a :Winery.
      ?w :wineryName ?name.
      ?w :hasWine ?wn.
      ?wn :title ?wtit.
      FILTER (?name="${t}"^^xsd:string)
    }`;
  return execQuery(query);
};
