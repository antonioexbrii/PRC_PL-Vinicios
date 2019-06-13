var axios = require('axios');
const Wine = module.exports;
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
    console.log(err);
  }
}

Wine.listWines = () => {
  const query = `PREFIX : <http://prc.di.uminho.pt/2019/a75870/>
    select ?w ?wine ?province ?points ?price where {
        ?w a :Wine.
        ?w :title ?wine.
        ?r :isReviewOf ?w.
        ?r :points ?points.
        ?w :price ?price
    }
    order by desc(?points) ?w`;
  return execQuery(query);
};
Wine.getByID = id => {
  const query = `PREFIX : <http://prc.di.uminho.pt/2019/a75870/>
    select * where {
      :${id} :title ?tit.
    }`;
  return execQuery(query);
};
Wine.getByTitle = t => {
  const query = `PREFIX : <http://prc.di.uminho.pt/2019/a75870/>
  PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    select * where {
      ?w a :Wine.
      ?w :title ?name.
      ?w :designation ?des.
      ?w :price ?price.
      ?w :variety ?variety.
      ?w :region_1 ?r1.
      ?w :region_2 ?r2.
      ?w :fromProvince ?prov.
      ?prov :provinceName ?provnm.
      ?w :fromWinery ?wn.
      ?wn :wineryName ?wnnm.
      ?s :isReviewOf ?w.
      ?s :points ?points.
      ?s :description ?descript.
      ?s :hasTaster ?taster.
      ?taster :taster_name ?tname.
      ?taster :taster_twitter_handle ?ttw.
      FILTER (?name="${t}"^^xsd:string)
    }
    ORDER BY ?name`;
  return execQuery(query);
};
