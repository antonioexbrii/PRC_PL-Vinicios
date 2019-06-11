var express = require('express');
var router = express.Router();
var countryController = require('../controllers/countryController.js');
var wineController = require('../controllers/wineController.js');
var wineryController = require('../controllers/wineryController.js');
var provinceController = require('../controllers/provinceController.js');
// WINES
router.get('/listWines', async (req, res, next) => {
  try {
    var data = await wineController.listWines();
    if (data) res.jsonp(data);
  } catch (err) {
    res.jsonp({ error: true, message: err });
  }
});
router.post('/wines/getWine', async (req, res, next) => {
  try {
    var data = await wineController.getByTitle(req.body.title);
    console.log(data)
    res.jsonp(data);
  } catch (err) {
    res.jsonp({ error: true, message: err });
  }
});
router.get('/wines/getTitle/:id', async (req, res, next) => {
  try {
    var data = await wineController.getByID(req.params.id);
    if (data) res.jsonp(data);
  } catch (err) {
    res.jsonp({ error: true, message: err });
  }
});
// WINERIES
router.get('/listWineries', async (req, res, next) => {
  try {
    var data = await wineryController.listWineries();
    if (data) res.jsonp(data);
  } catch (err) {
    res.jsonp({ error: true, message: err });
  }
});
router.post('/wineries/getWinery', async (req, res, next) => {
  try {
    var data = await wineryController.getByTitle(req.body.title);
    res.jsonp(data);
  } catch (err) {
    res.jsonp({ error: true, message: err });
  }
});
router.get('/wineries/getTitle/:id', async (req, res, next) => {
  try {
    var data = await wineryController.getByID(req.params.id);
    if (data) res.jsonp(data);
  } catch (err) {
    res.jsonp({ error: true, message: err });
  }
});
//COUNTRIES
router.get('/listCountries', async (req, res, next) => {
  try {
    var data = await countryController.listCountries();
    res.jsonp({ lst: data });
  } catch (err) {
    res.jsonp({ error: true, message: err });
  }
});

//PROVINCES
router.get('/provinces/getProvince/:id', async (req, res, next) => {
  try {
    var info = await provinceController.getByID(req.params.id);
    res.jsonp(info);
  } catch (err) {
    res.jsonp({ error: true, message: err });
  }
});
module.exports = router;
