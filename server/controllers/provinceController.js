var axios = require('axios');
const Province = module.exports;
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
    return err;
  }
}

Province.getByID = id => {
  const query = `PREFIX : <http://prc.di.uminho.pt/2019/a75870/>
    select ?tit ?ctn ?wine ?wnnm where {
        :${id} :provinceName ?tit;
        :fromCountry ?ctr;
        :isOriginOf ?wine.
        ?ctr :countryName ?ctn.
        ?wine :title ?wnnm.
    }`;
  return execQuery(query);
};
Province.getWines = title => {
  console.log('tou aqui');
  const query = `PREFIX : <http://prc.di.uminho.pt/2019/a75870/>
      select ?wine ?wnnm where {
        ?prov :provinceName ?name.
        ?prov :isOriginOf ?wine.
        ?wine :title ?wnnm.
        FILTER (?name="${title}"^^xsd:string)
      }`;
  return execQuery(query);
};
