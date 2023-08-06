"use strict";
(self["webpackChunkmoduextension"] = self["webpackChunkmoduextension"] || []).push([["style_index_js"],{

/***/ "./node_modules/css-loader/dist/cjs.js!./style/base.css":
/*!**************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js!./style/base.css ***!
  \**************************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/cssWithMappingToString.js */ "./node_modules/css-loader/dist/runtime/cssWithMappingToString.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/api.js */ "./node_modules/css-loader/dist/runtime/api.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__);
// Imports


var ___CSS_LOADER_EXPORT___ = _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default()((_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default()));
// Module
___CSS_LOADER_EXPORT___.push([module.id, ".jp-ReactWidget {\n  color: var(--jp-ui-font-color1);\n  background: var(--jp-layout-color1);\n  font-size: 48px;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  text-align: center;\n}\n\n.video-container {\n  width: 720px;\n  height: 480px;\n}\n\n.add-scroll {\n  overflow: scroll;\n}\n\n/*------------------------강좌 아코디언----------------------*/\n/* body {\n  font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif;\n  line-height: 1.4;\n  padding: 30px;\n} */\n.wrapper {\n  width: 600px;\n  margin: 0 auto;\n}\n.accordion-wrapper + * {\n  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica,\n    Arial, sans-serif;\n  line-height: 1.4;\n  /* padding: 30px; */\n\n  margin-top: 0.5em;\n}\n.accordion-item2 {\n  overflow: hidden;\n  transition: max-height 0.3s cubic-bezier(1, 0, 1, 0);\n  height: auto;\n  max-height: 9999px;\n  border: 0;\n}\n.accordion-item2.collapsed {\n  max-height: 0;\n  transition: max-height 0.35s cubic-bezier(0, 1, 0, 1);\n}\n.accordion-title {\n  font-weight: 600;\n  cursor: pointer;\n  color: #666;\n  padding: 0.5em 1.5em;\n  border: solid 1px #ccc;\n  /* border-radius: 1.5em; */\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n}\n.accordion-title::after {\n  content: '';\n  width: 0;\n  height: 0;\n  border-left: 5px solid transparent;\n  border-right: 5px solid transparent;\n  border-top: 5px solid currentColor;\n}\n.accordion-title:hover,\n.accordion-title.open {\n  color: black;\n}\n.accordion-title.open::after {\n  content: '';\n  border-top: 0;\n  border-bottom: 5px solid;\n}\n.accordion-content {\n  padding: 1em 1.5em;\n}\n\n\n/*------------------------유형 선택하기----------------------*/\n.category-popup ul li a:hover{\n  color: #19bec9;\n}", "",{"version":3,"sources":["webpack://./style/base.css"],"names":[],"mappings":"AAAA;EACE,+BAA+B;EAC/B,mCAAmC;EACnC,eAAe;EACf,aAAa;EACb,mBAAmB;EACnB,uBAAuB;EACvB,kBAAkB;AACpB;;AAEA;EACE,YAAY;EACZ,aAAa;AACf;;AAEA;EACE,gBAAgB;AAClB;;AAEA,wDAAwD;AACxD;;;;GAIG;AACH;EACE,YAAY;EACZ,cAAc;AAChB;AACA;EACE;qBACmB;EACnB,gBAAgB;EAChB,mBAAmB;;EAEnB,iBAAiB;AACnB;AACA;EACE,gBAAgB;EAChB,oDAAoD;EACpD,YAAY;EACZ,kBAAkB;EAClB,SAAS;AACX;AACA;EACE,aAAa;EACb,qDAAqD;AACvD;AACA;EACE,gBAAgB;EAChB,eAAe;EACf,WAAW;EACX,oBAAoB;EACpB,sBAAsB;EACtB,0BAA0B;EAC1B,aAAa;EACb,8BAA8B;EAC9B,mBAAmB;AACrB;AACA;EACE,WAAW;EACX,QAAQ;EACR,SAAS;EACT,kCAAkC;EAClC,mCAAmC;EACnC,kCAAkC;AACpC;AACA;;EAEE,YAAY;AACd;AACA;EACE,WAAW;EACX,aAAa;EACb,wBAAwB;AAC1B;AACA;EACE,kBAAkB;AACpB;;;AAGA,wDAAwD;AACxD;EACE,cAAc;AAChB","sourcesContent":[".jp-ReactWidget {\n  color: var(--jp-ui-font-color1);\n  background: var(--jp-layout-color1);\n  font-size: 48px;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  text-align: center;\n}\n\n.video-container {\n  width: 720px;\n  height: 480px;\n}\n\n.add-scroll {\n  overflow: scroll;\n}\n\n/*------------------------강좌 아코디언----------------------*/\n/* body {\n  font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif;\n  line-height: 1.4;\n  padding: 30px;\n} */\n.wrapper {\n  width: 600px;\n  margin: 0 auto;\n}\n.accordion-wrapper + * {\n  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica,\n    Arial, sans-serif;\n  line-height: 1.4;\n  /* padding: 30px; */\n\n  margin-top: 0.5em;\n}\n.accordion-item2 {\n  overflow: hidden;\n  transition: max-height 0.3s cubic-bezier(1, 0, 1, 0);\n  height: auto;\n  max-height: 9999px;\n  border: 0;\n}\n.accordion-item2.collapsed {\n  max-height: 0;\n  transition: max-height 0.35s cubic-bezier(0, 1, 0, 1);\n}\n.accordion-title {\n  font-weight: 600;\n  cursor: pointer;\n  color: #666;\n  padding: 0.5em 1.5em;\n  border: solid 1px #ccc;\n  /* border-radius: 1.5em; */\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n}\n.accordion-title::after {\n  content: '';\n  width: 0;\n  height: 0;\n  border-left: 5px solid transparent;\n  border-right: 5px solid transparent;\n  border-top: 5px solid currentColor;\n}\n.accordion-title:hover,\n.accordion-title.open {\n  color: black;\n}\n.accordion-title.open::after {\n  content: '';\n  border-top: 0;\n  border-bottom: 5px solid;\n}\n.accordion-content {\n  padding: 1em 1.5em;\n}\n\n\n/*------------------------유형 선택하기----------------------*/\n.category-popup ul li a:hover{\n  color: #19bec9;\n}"],"sourceRoot":""}]);
// Exports
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (___CSS_LOADER_EXPORT___);


/***/ }),

/***/ "./style/base.css":
/*!************************!*\
  !*** ./style/base.css ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_cjs_js_base_css__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! !!../node_modules/css-loader/dist/cjs.js!./base.css */ "./node_modules/css-loader/dist/cjs.js!./style/base.css");

            

var options = {};

options.insert = "head";
options.singleton = false;

var update = _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default()(_node_modules_css_loader_dist_cjs_js_base_css__WEBPACK_IMPORTED_MODULE_1__["default"], options);



/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (_node_modules_css_loader_dist_cjs_js_base_css__WEBPACK_IMPORTED_MODULE_1__["default"].locals || {});

/***/ }),

/***/ "./style/index.js":
/*!************************!*\
  !*** ./style/index.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _base_css__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./base.css */ "./style/base.css");



/***/ })

}]);
//# sourceMappingURL=style_index_js.330725558f3e80102b0e.js.map