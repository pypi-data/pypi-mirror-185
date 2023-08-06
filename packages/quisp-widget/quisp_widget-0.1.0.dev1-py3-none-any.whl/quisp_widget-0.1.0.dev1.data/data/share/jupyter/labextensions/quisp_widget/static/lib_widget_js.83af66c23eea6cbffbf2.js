(self["webpackChunkjupyter_quisp_widget"] = self["webpackChunkjupyter_quisp_widget"] || []).push([["lib_widget_js"],{

/***/ "./lib/iframeContent.js":
/*!******************************!*\
  !*** ./lib/iframeContent.js ***!
  \******************************/
/***/ ((__unused_webpack_module, exports) => {

"use strict";

Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.generateSource = void 0;
const DEFAULT_INI_CONTENT = `
[General]
seed-set = \\\${runnumber}
sim-time-limit = 100s
# Qnic
#**.buffers = intuniform(7,7)
image-path = "./quisp/images"
#**.logger.log_filename = "\\\${resultdir}/\\\${configname}-\\\${runnumber}.jsonl"
**.logger.log_filename = "/result.jsonl"
**.tomography_output_filename = "/result.output"

**.h_gate_error_rate = 1/2000
**.h_gate_x_error_ratio = 0
**.h_gate_y_error_ratio = 0
**.h_gate_z_error_ratio = 0

**.Measurement_error_rate = 1/2000
**.Measurement_x_error_ratio = 1
**.Measurement_y_error_ratio = 1
**.Measurement_z_error_ratio = 1

**.x_gate_error_rate = 1/2000
**.x_gate_x_error_ratio = 0
**.x_gate_y_error_ratio = 0
**.x_gate_z_error_ratio = 0

**.z_gate_error_rate = 1/2000
**.z_gate_x_error_ratio = 0
**.z_gate_y_error_ratio = 0
**.z_gate_z_error_ratio = 0


#Error on Target, Error on Controlled
**.cnot_gate_error_rate = 1/2000
**.cnot_gate_iz_error_ratio = 1 #checked
**.cnot_gate_zi_error_ratio = 1 #checked
**.cnot_gate_zz_error_ratio = 1 #checked
**.cnot_gate_ix_error_ratio = 1 #checked
**.cnot_gate_xi_error_ratio = 1 #checked
**.cnot_gate_xx_error_ratio = 1 #checked
**.cnot_gate_iy_error_ratio = 1 #checked
**.cnot_gate_yi_error_ratio = 1 #checked
**.cnot_gate_yy_error_ratio = 1 #checked


**.memory_x_error_rate = 1.11111111e-7
**.memory_y_error_rate = 1.11111111e-7
**.memory_z_error_rate = 1.11111111e-7
**.memory_energy_excitation_rate = 0.000198
**.memory_energy_relaxation_rate = 0.00000198
**.memory_completely_mixed_rate = 0

# when to start the BSA timing notification.
**.initial_notification_timing_buffer = 10 s
**.TrafficPattern = 1
**.LoneInitiatorAddress = 1



[Config Custom]
network = networks.Realistic_Layer2_Simple_MIM_MM_10km
seed-set = 0
**.number_of_bellpair = 7000
**.buffers = 100



**.emission_success_probability = 0.46*0.49

# Error on optical qubit in a channel
**.channel_loss_rate = 0.04500741397 # per km. 1 - 10^(-0.2/10)
**.channel_x_error_rate = 0.01
**.channel_z_error_rate = 0.01
**.channel_y_error_rate = 0.01

# Internal HOM in QNIC
**.internal_hom_loss_rate = 0
**.internal_hom_error_rate = 0 #Not inplemented
**.internal_hom_required_precision = 1.5e-9 #Schuck et al., PRL 96,
**.internal_hom_photon_detection_per_sec = 1000000000
**.internal_hom_darkcount_probability = 10e-8 #10/s * 10^-9

#Stand-alone HOM in the network
**.hom_loss_rate = 0
**.hom_error_rate = 0 #Not inplemented
**.hom_required_precision = 1.5e-9 #Schuck et al., PRL 96,
**.hom_photon_detection_per_sec = 1000000000
**.hom_darkcount_probability = 10e-8 #1%

**.link_tomography = false
**.EndToEndConnection = true
**.initial_purification = 2
**.purification_type = 1001`;
const generateSource = (wasmUrl, emscriptenModuleUrl, packageDataUrl, nedContent = '', iniContent = DEFAULT_INI_CONTENT) => `
      window.qtenvSkipRunSelection = true;
      const nedContent = \`${nedContent}\`;
      const iniContent = \`${iniContent}\`;
      const canvas = document.getElementById("main");
      canvas.style.width = '100%';
      canvas.style.height = '100%';
      canvas.oncontextmenu = (event) => {
        event.preventDefault();
      };
      canvas.contentEditable = 'true';
      console.log("hello world");
      Promise.all([loadWasm(), loadEmscriptenModule(), loadPackageData()])
      .then(([wasmModule, emscriptenSource, packageData]) => {
        console.log(wasmModule);
        window.Module = {
          instantiateWasm: (imports, callback) => {
            console.log('instantiate!');
            WebAssembly.instantiate(wasmModule, imports).then((instance) =>
              callback(instance, wasmModule)
            );
            return {};
          },
          localteFile: (filename) => {
            console.log('locateFile:', filename);
            return filename;
          },
          print: (msg) => console.log(msg),
          printErr: (msg) => console.error(msg),
          onAbort: (msg) => console.error('abort: ', msg),
          quit: (code, exception) => console.error('quit: ', { code, exception }),
          mainScriptUrlOrBlob: new Blob([emscriptenSource], { type: 'text/javascript' }),
          qtCanvasElements: [canvas],
          getPreloadedPackage: (_packageName, _packageSize) => packageData,
          setStatus: (msg) => {
            console.log('status changed: ', msg);
          },
          monitorRunDependencies: () => {},
          preRun: [
            () => {
              console.log(FS.readdir('/networks'));
              if (nedContent) FS.writeFile('/networks/custom.ned', nedContent);
              if (iniContent) FS.writeFile('/networks/omnetpp.ini', iniContent);
            },
          ],
        };
        window.qtenvReady = false;
        const timer = setInterval(() => {
          if (window.qtenvReady) {
            clearInterval(timer);
            console.log(this);
            window.qtenv = window.Module.getQtenv();
            window.mainWindow = window.qtenv.getMainWindow();
            console.log('qtenv ready');
          }
        }, 100);
        const args = [
          '-m', /* merge stderr into stdout */
          '-u', 'Qtenv',  /* ui */
          '-n', './networks:./channels:./modules', /* .ned file search path */
          '-f', './networks/omnetpp.ini', /* config file */
          '-c', 'Custom',
          '-r', '0',
          '--image-path=/quisp/images',
        ];
        console.log(JSON.stringify(args));

        self.eval(
          emscriptenSource.substring(
            emscriptenSource.lastIndexOf('arguments_=['),
            -1
          ) +
            'arguments_=' +
            JSON.stringify(args) +
            ';'
        );
      })
      function loadWasm() {
        const resp = fetch("${wasmUrl}");
        if (typeof WebAssembly.compileStreaming !== 'undefined') {
          return WebAssembly.compileStreaming(resp);
        } else {
          return resp.then((r) => r.arrayBuffer()).then(WebAssembly.compile);
        }
      }

      function loadEmscriptenModule() {
        return fetch("${emscriptenModuleUrl}").then((r) => r.text());
      }

      function loadPackageData() {
        return fetch("${packageDataUrl}").then((r) => r.arrayBuffer());
      }
    `;
exports.generateSource = generateSource;
//# sourceMappingURL=iframeContent.js.map

/***/ }),

/***/ "./lib/version.js":
/*!************************!*\
  !*** ./lib/version.js ***!
  \************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

"use strict";

// Copyright (c) zigen
// Distributed under the terms of the Modified BSD License.
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MODULE_NAME = exports.MODULE_VERSION = void 0;
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
// eslint-disable-next-line @typescript-eslint/no-var-requires
const data = __webpack_require__(/*! ../package.json */ "./package.json");
/**
 * The _model_module_version/_view_module_version this package implements.
 *
 * The html widget manager assumes that this is the same as the npm package
 * version number.
 */
exports.MODULE_VERSION = data.version;
/*
 * The current package name.
 */
exports.MODULE_NAME = data.name;
//# sourceMappingURL=version.js.map

/***/ }),

/***/ "./lib/widget.js":
/*!***********************!*\
  !*** ./lib/widget.js ***!
  \***********************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

"use strict";

// Copyright (c) zigen
// Distributed under the terms of the Modified BSD License.
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.QuispIFrameView = exports.QuispIFrameModel = void 0;
const base_1 = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
const version_1 = __webpack_require__(/*! ./version */ "./lib/version.js");
const iframeContent_1 = __webpack_require__(/*! ./iframeContent */ "./lib/iframeContent.js");
// Import the CSS
__webpack_require__(/*! ../css/widget.css */ "./css/widget.css");
const baseUrl = 'https://aqua.sfc.wide.ad.jp/quisp-online/jupyter-quisp-widget/';
// const baseUrl = 'http://localhost:8000/';
const wasmUrl = baseUrl + 'quisp.wasm';
const emscriptenModuleUrl = baseUrl + 'quisp.js';
const packageDataUrl = baseUrl + 'quisp.data';
const readFile = (fs, filename) => {
    try {
        return fs.readFile(filename, { encoding: 'utf8' });
    }
    catch (_a) {
        return null;
    }
};
class QuispIFrameModel extends base_1.DOMWidgetModel {
    constructor(attributes, options) {
        super(attributes, options);
        this.iframe = document.createElement('IFRAME');
        this.currentViewId = null;
        // @ts-ignore
        this.on('msg:custom', this.handleMessages, this);
    }
    defaults() {
        return Object.assign(Object.assign({}, super.defaults()), { _model_name: QuispIFrameModel.model_name, _model_module: QuispIFrameModel.model_module, _model_module_version: QuispIFrameModel.model_module_version, _view_name: QuispIFrameModel.view_name, _view_module: QuispIFrameModel.view_module, _view_module_version: QuispIFrameModel.view_module_version, value: 'Hello World', iniContent: undefined, nedContent: undefined });
    }
    useIframe(viewId) {
        if (this.currentViewId === null) {
            this.setupIframe();
            this.currentViewId = viewId;
        }
        if (this.currentViewId === viewId) {
            return this.iframe;
        }
        return null;
    }
    reset() {
        this.iframe = document.createElement('IFRAME');
        this.setupIframe();
    }
    setupIframe() {
        const nedContent = this.get('nedContent');
        const iniContent = this.get('iniContent');
        const source = iframeContent_1.generateSource(wasmUrl, emscriptenModuleUrl, packageDataUrl, nedContent, iniContent);
        this.iframe.srcdoc = `<canvas id="main"><script>${source}</script>`;
        this.iframe.style.width = '100%';
        this.iframe.style.height = '897px';
    }
    handleMessages(content) {
        console.log('handle custome message: ', content, this);
        const mainWindow = 
        // @ts-ignore
        this.iframe.contentWindow.Module.getQtenv().getMainWindow();
        // @ts-ignore
        const RunMode = this.iframe.contentWindow.Module.RunMode;
        switch (content.msg) {
            case 'runNormal':
                // @ts-ignore
                mainWindow.runSimulation(RunMode.NORMAL);
                break;
            case 'runStep':
                // @ts-ignore
                mainWindow.runSimulation(RunMode.STEP);
                break;
            case 'runFast':
                // @ts-ignore
                mainWindow.runSimulation(RunMode.FAST);
                break;
            case 'stop':
                // @ts-ignore
                mainWindow.stopSimulation();
                break;
            case 'load':
                console.log('loading....');
                this.set('iniContent', content.ini);
                this.set('nedContent', content.ned);
                this.setupIframe();
                break;
            case 'readResult':
                // @ts-ignore
                const FS = this.iframe.contentWindow.FS;
                // @ts-ignore
                const jsonl = readFile(FS, '/result.jsonl');
                // @ts-ignore
                const output = readFile(FS, '/result.output');
                this.send({ jsonl, output }, (m) => console.log('model load callback', m));
                break;
        }
    }
}
exports.QuispIFrameModel = QuispIFrameModel;
QuispIFrameModel.serializers = Object.assign({}, base_1.DOMWidgetModel.serializers);
QuispIFrameModel.model_name = 'QuispIFrameModel';
QuispIFrameModel.model_module = version_1.MODULE_NAME;
QuispIFrameModel.model_module_version = version_1.MODULE_VERSION;
QuispIFrameModel.view_name = 'QuispIFrameView';
QuispIFrameModel.view_module = version_1.MODULE_NAME;
QuispIFrameModel.view_module_version = version_1.MODULE_VERSION;
class QuispIFrameView extends base_1.DOMWidgetView {
    initialize() { }
    render() {
        this.el.classList.add('custom-widget');
        if (this.el.children.length == 0) {
            const iframe = this.model.useIframe(this.cid);
            if (iframe) {
                this.el.appendChild(iframe);
                this.model.send({ state_change: 'rendered' }, () => { });
            }
            else {
                this.el.textContent = 'see other view';
            }
        }
    }
}
exports.QuispIFrameView = QuispIFrameView;
//# sourceMappingURL=widget.js.map

/***/ }),

/***/ "./node_modules/css-loader/dist/cjs.js!./css/widget.css":
/*!**************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js!./css/widget.css ***!
  \**************************************************************/
/***/ ((module, exports, __webpack_require__) => {

// Imports
var ___CSS_LOADER_API_IMPORT___ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/api.js */ "./node_modules/css-loader/dist/runtime/api.js");
exports = ___CSS_LOADER_API_IMPORT___(false);
// Module
exports.push([module.id, ".custom-widget {\n  background-color: lightseagreen;\n  padding: 0px 2px;\n}\n", ""]);
// Exports
module.exports = exports;


/***/ }),

/***/ "./node_modules/css-loader/dist/runtime/api.js":
/*!*****************************************************!*\
  !*** ./node_modules/css-loader/dist/runtime/api.js ***!
  \*****************************************************/
/***/ ((module) => {

"use strict";


/*
  MIT License http://www.opensource.org/licenses/mit-license.php
  Author Tobias Koppers @sokra
*/
// css base code, injected by the css-loader
// eslint-disable-next-line func-names
module.exports = function (useSourceMap) {
  var list = []; // return the list of modules as css string

  list.toString = function toString() {
    return this.map(function (item) {
      var content = cssWithMappingToString(item, useSourceMap);

      if (item[2]) {
        return "@media ".concat(item[2], " {").concat(content, "}");
      }

      return content;
    }).join('');
  }; // import a list of modules into the list
  // eslint-disable-next-line func-names


  list.i = function (modules, mediaQuery, dedupe) {
    if (typeof modules === 'string') {
      // eslint-disable-next-line no-param-reassign
      modules = [[null, modules, '']];
    }

    var alreadyImportedModules = {};

    if (dedupe) {
      for (var i = 0; i < this.length; i++) {
        // eslint-disable-next-line prefer-destructuring
        var id = this[i][0];

        if (id != null) {
          alreadyImportedModules[id] = true;
        }
      }
    }

    for (var _i = 0; _i < modules.length; _i++) {
      var item = [].concat(modules[_i]);

      if (dedupe && alreadyImportedModules[item[0]]) {
        // eslint-disable-next-line no-continue
        continue;
      }

      if (mediaQuery) {
        if (!item[2]) {
          item[2] = mediaQuery;
        } else {
          item[2] = "".concat(mediaQuery, " and ").concat(item[2]);
        }
      }

      list.push(item);
    }
  };

  return list;
};

function cssWithMappingToString(item, useSourceMap) {
  var content = item[1] || ''; // eslint-disable-next-line prefer-destructuring

  var cssMapping = item[3];

  if (!cssMapping) {
    return content;
  }

  if (useSourceMap && typeof btoa === 'function') {
    var sourceMapping = toComment(cssMapping);
    var sourceURLs = cssMapping.sources.map(function (source) {
      return "/*# sourceURL=".concat(cssMapping.sourceRoot || '').concat(source, " */");
    });
    return [content].concat(sourceURLs).concat([sourceMapping]).join('\n');
  }

  return [content].join('\n');
} // Adapted from convert-source-map (MIT)


function toComment(sourceMap) {
  // eslint-disable-next-line no-undef
  var base64 = btoa(unescape(encodeURIComponent(JSON.stringify(sourceMap))));
  var data = "sourceMappingURL=data:application/json;charset=utf-8;base64,".concat(base64);
  return "/*# ".concat(data, " */");
}

/***/ }),

/***/ "./css/widget.css":
/*!************************!*\
  !*** ./css/widget.css ***!
  \************************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var api = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js");
            var content = __webpack_require__(/*! !!../node_modules/css-loader/dist/cjs.js!./widget.css */ "./node_modules/css-loader/dist/cjs.js!./css/widget.css");

            content = content.__esModule ? content.default : content;

            if (typeof content === 'string') {
              content = [[module.id, content, '']];
            }

var options = {};

options.insert = "head";
options.singleton = false;

var update = api(content, options);



module.exports = content.locals || {};

/***/ }),

/***/ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js":
/*!****************************************************************************!*\
  !*** ./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js ***!
  \****************************************************************************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var isOldIE = function isOldIE() {
  var memo;
  return function memorize() {
    if (typeof memo === 'undefined') {
      // Test for IE <= 9 as proposed by Browserhacks
      // @see http://browserhacks.com/#hack-e71d8692f65334173fee715c222cb805
      // Tests for existence of standard globals is to allow style-loader
      // to operate correctly into non-standard environments
      // @see https://github.com/webpack-contrib/style-loader/issues/177
      memo = Boolean(window && document && document.all && !window.atob);
    }

    return memo;
  };
}();

var getTarget = function getTarget() {
  var memo = {};
  return function memorize(target) {
    if (typeof memo[target] === 'undefined') {
      var styleTarget = document.querySelector(target); // Special case to return head of iframe instead of iframe itself

      if (window.HTMLIFrameElement && styleTarget instanceof window.HTMLIFrameElement) {
        try {
          // This will throw an exception if access to iframe is blocked
          // due to cross-origin restrictions
          styleTarget = styleTarget.contentDocument.head;
        } catch (e) {
          // istanbul ignore next
          styleTarget = null;
        }
      }

      memo[target] = styleTarget;
    }

    return memo[target];
  };
}();

var stylesInDom = [];

function getIndexByIdentifier(identifier) {
  var result = -1;

  for (var i = 0; i < stylesInDom.length; i++) {
    if (stylesInDom[i].identifier === identifier) {
      result = i;
      break;
    }
  }

  return result;
}

function modulesToDom(list, options) {
  var idCountMap = {};
  var identifiers = [];

  for (var i = 0; i < list.length; i++) {
    var item = list[i];
    var id = options.base ? item[0] + options.base : item[0];
    var count = idCountMap[id] || 0;
    var identifier = "".concat(id, " ").concat(count);
    idCountMap[id] = count + 1;
    var index = getIndexByIdentifier(identifier);
    var obj = {
      css: item[1],
      media: item[2],
      sourceMap: item[3]
    };

    if (index !== -1) {
      stylesInDom[index].references++;
      stylesInDom[index].updater(obj);
    } else {
      stylesInDom.push({
        identifier: identifier,
        updater: addStyle(obj, options),
        references: 1
      });
    }

    identifiers.push(identifier);
  }

  return identifiers;
}

function insertStyleElement(options) {
  var style = document.createElement('style');
  var attributes = options.attributes || {};

  if (typeof attributes.nonce === 'undefined') {
    var nonce =  true ? __webpack_require__.nc : 0;

    if (nonce) {
      attributes.nonce = nonce;
    }
  }

  Object.keys(attributes).forEach(function (key) {
    style.setAttribute(key, attributes[key]);
  });

  if (typeof options.insert === 'function') {
    options.insert(style);
  } else {
    var target = getTarget(options.insert || 'head');

    if (!target) {
      throw new Error("Couldn't find a style target. This probably means that the value for the 'insert' parameter is invalid.");
    }

    target.appendChild(style);
  }

  return style;
}

function removeStyleElement(style) {
  // istanbul ignore if
  if (style.parentNode === null) {
    return false;
  }

  style.parentNode.removeChild(style);
}
/* istanbul ignore next  */


var replaceText = function replaceText() {
  var textStore = [];
  return function replace(index, replacement) {
    textStore[index] = replacement;
    return textStore.filter(Boolean).join('\n');
  };
}();

function applyToSingletonTag(style, index, remove, obj) {
  var css = remove ? '' : obj.media ? "@media ".concat(obj.media, " {").concat(obj.css, "}") : obj.css; // For old IE

  /* istanbul ignore if  */

  if (style.styleSheet) {
    style.styleSheet.cssText = replaceText(index, css);
  } else {
    var cssNode = document.createTextNode(css);
    var childNodes = style.childNodes;

    if (childNodes[index]) {
      style.removeChild(childNodes[index]);
    }

    if (childNodes.length) {
      style.insertBefore(cssNode, childNodes[index]);
    } else {
      style.appendChild(cssNode);
    }
  }
}

function applyToTag(style, options, obj) {
  var css = obj.css;
  var media = obj.media;
  var sourceMap = obj.sourceMap;

  if (media) {
    style.setAttribute('media', media);
  } else {
    style.removeAttribute('media');
  }

  if (sourceMap && typeof btoa !== 'undefined') {
    css += "\n/*# sourceMappingURL=data:application/json;base64,".concat(btoa(unescape(encodeURIComponent(JSON.stringify(sourceMap)))), " */");
  } // For old IE

  /* istanbul ignore if  */


  if (style.styleSheet) {
    style.styleSheet.cssText = css;
  } else {
    while (style.firstChild) {
      style.removeChild(style.firstChild);
    }

    style.appendChild(document.createTextNode(css));
  }
}

var singleton = null;
var singletonCounter = 0;

function addStyle(obj, options) {
  var style;
  var update;
  var remove;

  if (options.singleton) {
    var styleIndex = singletonCounter++;
    style = singleton || (singleton = insertStyleElement(options));
    update = applyToSingletonTag.bind(null, style, styleIndex, false);
    remove = applyToSingletonTag.bind(null, style, styleIndex, true);
  } else {
    style = insertStyleElement(options);
    update = applyToTag.bind(null, style, options);

    remove = function remove() {
      removeStyleElement(style);
    };
  }

  update(obj);
  return function updateStyle(newObj) {
    if (newObj) {
      if (newObj.css === obj.css && newObj.media === obj.media && newObj.sourceMap === obj.sourceMap) {
        return;
      }

      update(obj = newObj);
    } else {
      remove();
    }
  };
}

module.exports = function (list, options) {
  options = options || {}; // Force single-tag solution on IE6-9, which has a hard limit on the # of <style>
  // tags it will allow on a page

  if (!options.singleton && typeof options.singleton !== 'boolean') {
    options.singleton = isOldIE();
  }

  list = list || [];
  var lastIdentifiers = modulesToDom(list, options);
  return function update(newList) {
    newList = newList || [];

    if (Object.prototype.toString.call(newList) !== '[object Array]') {
      return;
    }

    for (var i = 0; i < lastIdentifiers.length; i++) {
      var identifier = lastIdentifiers[i];
      var index = getIndexByIdentifier(identifier);
      stylesInDom[index].references--;
    }

    var newLastIdentifiers = modulesToDom(newList, options);

    for (var _i = 0; _i < lastIdentifiers.length; _i++) {
      var _identifier = lastIdentifiers[_i];

      var _index = getIndexByIdentifier(_identifier);

      if (stylesInDom[_index].references === 0) {
        stylesInDom[_index].updater();

        stylesInDom.splice(_index, 1);
      }
    }

    lastIdentifiers = newLastIdentifiers;
  };
};

/***/ }),

/***/ "./package.json":
/*!**********************!*\
  !*** ./package.json ***!
  \**********************/
/***/ ((module) => {

"use strict";
module.exports = JSON.parse('{"name":"jupyter-quisp-widget","version":"0.1.1","description":"A Custom Jupyter Widget Library","keywords":["jupyter","jupyterlab","jupyterlab-extension","widgets"],"files":["lib/**/*.js","dist/*.js","css/*.css"],"homepage":"https://github.com/sfc-aqua/jupyter-quisp-widget","bugs":{"url":"https://github.com/sfc-aqua/jupyter-quisp-widget/issues"},"license":"BSD-3-Clause","author":{"name":"zigen","email":"hrlclb@gmail.com"},"main":"lib/index.js","types":"./lib/index.d.ts","repository":{"type":"git","url":"https://github.com/sfc-aqua/jupyter-quisp-widget"},"scripts":{"build":"yarn run build:lib && yarn run build:nbextension && yarn run build:labextension:dev","build:prod":"yarn run build:lib && yarn run build:nbextension && yarn run build:labextension","build:labextension":"jupyter labextension build .","build:labextension:dev":"jupyter labextension build --development True .","build:lib":"tsc","build:nbextension":"webpack","clean":"yarn run clean:lib && yarn run clean:nbextension && yarn run clean:labextension","clean:lib":"rimraf lib","clean:labextension":"rimraf quisp_widget/labextension","clean:nbextension":"rimraf quisp_widget/nbextension/static/index.js","lint":"eslint . --ext .ts,.tsx --fix","lint:check":"eslint . --ext .ts,.tsx","prepack":"yarn run build:lib","test":"jest","watch":"npm-run-all -p watch:*","watch:lib":"tsc -w","watch:nbextension":"webpack --watch --mode=development","watch:labextension":"jupyter labextension watch ."},"dependencies":{"@jupyter-widgets/base":"^1.1.10 || ^2 || ^3 || ^4 || ^5 || ^6"},"devDependencies":{"@babel/core":"^7.5.0","@babel/preset-env":"^7.5.0","@jupyter-widgets/base-manager":"^1.0.2","@jupyterlab/builder":"^3.0.0","@lumino/application":"^1.6.0","@lumino/widgets":"^1.6.0","@types/jest":"^26.0.0","@types/webpack-env":"^1.13.6","@typescript-eslint/eslint-plugin":"^3.6.0","@typescript-eslint/parser":"^3.6.0","acorn":"^7.2.0","css-loader":"^3.2.0","eslint":"^7.4.0","eslint-config-prettier":"^6.11.0","eslint-plugin-prettier":"^3.1.4","fs-extra":"^7.0.0","identity-obj-proxy":"^3.0.0","jest":"^26.0.0","mkdirp":"^0.5.1","npm-run-all":"^4.1.3","prettier":"^2.0.5","rimraf":"^2.6.2","source-map-loader":"^1.1.3","style-loader":"^1.0.0","ts-jest":"^26.0.0","ts-loader":"^8.0.0","typescript":"~4.1.3","webpack":"^5.61.0","webpack-cli":"^4.0.0"},"jupyterlab":{"extension":"lib/plugin","outputDir":"quisp_widget/labextension/","sharedPackages":{"@jupyter-widgets/base":{"bundled":false,"singleton":true}}}}');

/***/ })

}]);
//# sourceMappingURL=lib_widget_js.83af66c23eea6cbffbf2.js.map