var axios = require('axios');
const Country = module.exports;
async function execQuery(query) {
  try {
    var encoded = encodeURIComponent(query);
    var resp = await axios.get(
      'http://localhost:7200/repositories/PRC-TP?query=' + encoded
    );
    var jsonLst = [];
    resp.data.results.bindings.forEach(element => {
      var flag = false;
      var id = element.prov.value.split('/').reverse()[0];
      for (var i = 0; i < jsonLst.length; i++) {
        if (jsonLst[i].country === element.ctn.value) {
          jsonLst[i].provinces.push({ name: element.provnm.value, id: id });
          flag = true;
        }
      }
      if (!flag) {
        jsonLst.push({
          country: element.ctn.value,
          countryKey: element.ctk.value,
          provinces: [{ name: element.provnm.value, id: id }]
        });
      }
    });
    return jsonLst;
  } catch (err) {
    console.log(err);
    return err;
  }
}
Country.listCountries = () => {
  const query = `PREFIX : <http://prc.di.uminho.pt/2019/a75870/>
      select * where {
          ?s a :Country.
          ?s :countryName ?ctn.
          ?s :countryKey ?ctk.
          ?s :hasProvince ?prov.
          ?prov :provinceName ?provnm.
      }`;
  return execQuery(query);
};
