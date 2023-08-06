(self["webpackChunkmoduextension"] = self["webpackChunkmoduextension"] || []).push([["lib_index_js"],{

/***/ "./lib/config/config.js":
/*!******************************!*\
  !*** ./lib/config/config.js ***!
  \******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "config": () => (/* binding */ config)
/* harmony export */ });
const config = {
    //baseUrl: 'http://localhost:5000/api/',
    //baseUrl: 'https://aivle-api-stg.moducoding.com/api/',
    baseUrl: 'https://aivle-api.moducoding.com/api/',
    chat: 'https://chat.codereet.com',
};


/***/ }),

/***/ "./lib/hooks/useCategorySelect.js":
/*!****************************************!*\
  !*** ./lib/hooks/useCategorySelect.js ***!
  \****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _types_category__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../types/category */ "./lib/types/category.js");
/* harmony import */ var _useGrayCenterContainer__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./useGrayCenterContainer */ "./lib/hooks/useGrayCenterContainer.js");



/**
 * https://flowbite.com/docs/components/card/#
 */
const CategorySelect = ({ onCategorySelected }) => {
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_useGrayCenterContainer__WEBPACK_IMPORTED_MODULE_1__["default"], null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "category-popup p-4 max-w-sm rounded-lg border shadow-md sm:p-6 bg-white border-gray-200" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("h5", { className: "mb-3 text-base font-semibold lg:text-xl text-gray-700" }, "\uC720\uD615 \uC120\uD0DD\uD558\uAE30"),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", { className: "text-sm font-normal text-gray-400" }, "\uAC15\uC88C\uB97C \uC120\uD0DD\uD558\uC5EC AI \uD559\uC2B5\uC744 \uC9C4\uD589\uD558\uAC70\uB098, AI \uD574\uCEE4\uD1A4\uC744 \uC120\uD0DD\uD558\uC5EC \uACBD\uC7C1\uC5D0 \uCC38\uC5EC\uD558\uC138\uC694."),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("ul", { className: "my-4 space-y-3" },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("li", null,
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("a", { href: "#", className: "flex items-center p-3 text-base font-bold rounded-lg group hover:bg-gray-100 border border-200", onClick: () => {
                            onCategorySelected(_types_category__WEBPACK_IMPORTED_MODULE_2__["default"].Lecture);
                        } },
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { className: "flex-1 ml-3 whitespace-nowrap" }, "AI \uAC15\uC88C \uD559\uC2B5\uD558\uAE30"))),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("li", null,
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("a", { href: "#", className: "flex items-center p-3 text-base font-bold rounded-lg group hover:bg-gray-100 border border-200", onClick: () => {
                            onCategorySelected(_types_category__WEBPACK_IMPORTED_MODULE_2__["default"].AIHackathon);
                        } },
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { className: "flex-1 ml-3 whitespace-nowrap" }, "AI \uD574\uCEE4\uD1A4\uC5D0 \uCC38\uAC00\uD558\uAE30")))))));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (CategorySelect);


/***/ }),

/***/ "./lib/hooks/useGrayCenterContainer.js":
/*!*********************************************!*\
  !*** ./lib/hooks/useGrayCenterContainer.js ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);

const GrayCenterContainer = ({ children }) => {
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("section", { className: "flex justify-center w-full gradient-form bg-gray-200 md:h-screen mx-auto" },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "container max-w-6xl py-12 px-6 container-h-full" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "flex justify-center items-center flex-wrap container-h-full g-6 text-gray-800" }, children))));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (GrayCenterContainer);


/***/ }),

/***/ "./lib/hooks/useHackathonCard.js":
/*!***************************************!*\
  !*** ./lib/hooks/useHackathonCard.js ***!
  \***************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _util_date__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../util/date */ "./lib/util/date.js");
/* eslint-disable @typescript-eslint/explicit-module-boundary-types */


const HackathonCard = ({ hackathon, onHackathonSelected }) => {
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("a", { href: "#", className: "hackathon-card flex flex-col items-center border-b-2 md:flex-row md:max-w-full border-gray-200 py-7 px-12", onClick: onHackathonSelected },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("img", { className: "object-cover w-full h-96 md:h-auto md:w-36 md:rounded-md", src: hackathon.thumbnailUrl, alt: hackathon.title }),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "flex flex-col justify-between py-4 leading-normal px-7" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "flex flex-start items-baseline" },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("h5", { className: "mb-6 text-lg font-bold tracking-tight" }, hackathon.title),
                hackathon.isSubmitted && (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { className: "inline-flex items-center justify-center h-6 px-2 py-0.5 ml-3 text-xs font-medium rounded bg-gray-400 text-gray-100" }, "\uC81C\uCD9C\uC644\uB8CC"))),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", { className: "mb-3 font-normal text-gray-400" },
                "\uC9C4\uD589 \uAE30\uAC04 :",
                ' ',
                (0,_util_date__WEBPACK_IMPORTED_MODULE_1__.getTimeBoxString)(`${hackathon.startDate}Z`, `${hackathon.endDate}Z`)))));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (HackathonCard);


/***/ }),

/***/ "./lib/hooks/useHackathonDetail.js":
/*!*****************************************!*\
  !*** ./lib/hooks/useHackathonDetail.js ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! axios */ "webpack/sharing/consume/default/axios/axios");
/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(axios__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _config_config__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../config/config */ "./lib/config/config.js");
/* harmony import */ var _util_date__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../util/date */ "./lib/util/date.js");
/* harmony import */ var _util_file__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../util/file */ "./lib/util/file.js");
/* eslint-disable @typescript-eslint/explicit-module-boundary-types */





const HackathonDetail = ({ getToken, hackathonId, onResetHackathonSelected, }) => {
    const [hackathon, setHackathon] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(null);
    const [files, setFiles] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(null);
    const [onProcess, setOnProcess] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(false);
    (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(() => {
        (async () => {
            try {
                const response = await axios__WEBPACK_IMPORTED_MODULE_1___default().get(`${_config_config__WEBPACK_IMPORTED_MODULE_2__.config.baseUrl}Test/${hackathonId}`, {
                    headers: {
                        Authorization: `Bearer ${getToken()}`,
                    },
                });
                const fileUrlResponse = await axios__WEBPACK_IMPORTED_MODULE_1___default().get(`${_config_config__WEBPACK_IMPORTED_MODULE_2__.config.baseUrl}Test/${hackathonId}/SubmittedFileUrl`, {
                    headers: {
                        Authorization: `Bearer ${getToken()}`,
                    },
                });
                const hackathonData = response.data.data;
                if (fileUrlResponse.data && fileUrlResponse.data.result) {
                    hackathonData.submittedFileUrl =
                        fileUrlResponse.data.submittedFileUrl;
                }
                // 기존 데이터 무시하고 새로 채우기
                setHackathon(hackathonData);
            }
            catch (err) {
                console.error(err);
            }
        })();
    }, []);
    const getSanitizedData = (data) => ({
        __html: data,
    });
    const isFileSelected = react__WEBPACK_IMPORTED_MODULE_0___default().useCallback(() => {
        return files && files.length > 0;
    }, [files]);
    const uploadNotebookFile = react__WEBPACK_IMPORTED_MODULE_0___default().useCallback(() => {
        (async () => {
            try {
                setOnProcess(true);
                const formData = new FormData();
                formData.append('testId', hackathon.testId);
                formData.append('notebookFiles', files.item(0));
                const response = await axios__WEBPACK_IMPORTED_MODULE_1___default().post(`${_config_config__WEBPACK_IMPORTED_MODULE_2__.config.baseUrl}Test/Submit`, formData, {
                    headers: {
                        Authorization: `Bearer ${getToken()}`,
                        'Content-Type': 'multipart/form-data',
                    },
                });
                if (response.data && response.data.result) {
                    alert('파일 업로드가 완료 되었습니다.');
                    setHackathon((prev) => (Object.assign(Object.assign({}, prev), { ['submittedFileUrl']: response.data.notebookFileUrl })));
                }
                else {
                    alert('파일 업로드 중 오류가 발생했습니다.');
                }
            }
            catch (err) {
                console.error(err);
                alert('파일 업로드 중 오류가 발생했습니다.');
            }
            finally {
                setOnProcess(false);
            }
        })();
    }, [files]);
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement((react__WEBPACK_IMPORTED_MODULE_0___default().Fragment), null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("button", { className: "mb-7 border border-gray-200 hover:bg-gray-100 text-gray-600 rounded px-2 py-1 disabled:bg-slate-50", onClick: onResetHackathonSelected },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("i", { className: 'mdi mdi-menu text-sm mr-1' }),
            "\uBAA9\uB85D\uC73C\uB85C"),
        hackathon && (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "relative py-7 pl-8 border-b-2 border-t-2 border-gray-200 sm:mx-auto sm:max-w-3/6 sm:px-10" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "w-full" },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "flex flex-row flex-start" },
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("img", { src: hackathon.thumbnailUrl, className: "h-50 w-60 rounded-md", alt: hackathon.title }),
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "flex-col ml-6" },
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "mt-10 text-4xl leading-7" },
                            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "flex flex-start items-center" },
                                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("h1", { className: 'font-bold text-xl' }, hackathon.title),
                                hackathon.submittedFileUrl && (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { className: "bg-gray-400 h-6 inline-flex items-center ml-3 px-2 py-0.5 rounded text-gray-100 text-xs" }, "\uC81C\uCD9C\uC644\uB8CC")))),
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { className: "font-semibold inline-block mt-6 text-gray-400" },
                            "\uC9C4\uD589 \uAE30\uAC04 :",
                            ' ',
                            (0,_util_date__WEBPACK_IMPORTED_MODULE_3__.getTimeBoxString)(`${hackathon.startDate}Z`, `${hackathon.endDate}Z`)))),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: 'divide-y divide-gray-100' },
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "py-8 text-base leading-7" },
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", { className: 'font-bold', dangerouslySetInnerHTML: getSanitizedData(hackathon.content) }),
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", { className: 'pt-5' },
                            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("a", { href: "#", className: "border rounded py-1 px-4 hover:bg-gray-100 text-gray-600 text-sm", onClick: () => {
                                    (0,_util_file__WEBPACK_IMPORTED_MODULE_4__.handleDownload)(hackathon.uploadFileUrl);
                                } },
                                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("i", { className: 'mdi mdi-arrow-down-bold-outline text-sm mr-1' }),
                                "\uB178\uD2B8\uBD81 \uD30C\uC77C \uB2E4\uC6B4\uB85C\uB4DC"))),
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "pt-8 text-base leading-7" },
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", { className: "text-xl font-bold" }, "\uACB0\uACFC \uD30C\uC77C \uC5C5\uB85C\uB4DC\uD558\uAE30"),
                        hackathon.submittedFileUrl && (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", { className: 'pt-5' },
                            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("a", { href: "#", className: "border rounded py-1 px-4 hover:bg-gray-100 text-gray-600 text-sm", onClick: () => {
                                    (0,_util_file__WEBPACK_IMPORTED_MODULE_4__.handleDownload)(hackathon.submittedFileUrl);
                                } },
                                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("i", { className: 'mdi mdi-arrow-down-bold-outline text-sm mr-1' }),
                                "\uC81C\uCD9C\uD55C \uD30C\uC77C \uB2E4\uC6B4\uB85C\uB4DC"))),
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "flex flex-row flex-start mt-6" },
                            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("input", { className: "block border-b w-2/6 text-sm cursor-pointer text-gray-400 focus:outline-none placeholder-gray-400", "aria-describedby": "file_input_help", id: "file_input", type: "file", accept: ".ipynb", onChange: (e) => setFiles(e.target.files) }),
                            isFileSelected() && (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("button", { className: "bg-gray-400 hover:bg-gray-500 text-white text-sm rounded px-1 disabled:bg-slate-50 ml-3 w-24", onClick: uploadNotebookFile, disabled: onProcess }, onProcess ? (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("svg", { role: "status", className: "inline w-4 h-4 mr-3 text-white animate-spin", viewBox: "0 0 100 101", fill: "none", xmlns: "http://www.w3.org/2000/svg" },
                                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("path", { d: "M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z", fill: "#E5E7EB" }),
                                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("path", { d: "M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z", fill: "currentColor" }))) : ('업로드 하기')))),
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", { className: "mt-1.5 text-sm text-blue-400", id: "file_input_help" }, "ipynb \uD30C\uC77C \uD615\uC2DD\uB9CC \uAC00\uB2A5\uD569\uB2C8\uB2E4."))))))));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (HackathonDetail);


/***/ }),

/***/ "./lib/hooks/useHackathonList.js":
/*!***************************************!*\
  !*** ./lib/hooks/useHackathonList.js ***!
  \***************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! axios */ "webpack/sharing/consume/default/axios/axios");
/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(axios__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _useHackathonCard__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./useHackathonCard */ "./lib/hooks/useHackathonCard.js");
/* harmony import */ var _config_config__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../config/config */ "./lib/config/config.js");
/* harmony import */ var _useHackathonDetail__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./useHackathonDetail */ "./lib/hooks/useHackathonDetail.js");
/* eslint-disable @typescript-eslint/explicit-module-boundary-types */





const HackathonList = ({ getToken, onResetCategory }) => {
    const [pageNo, setPageNo] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(1);
    const [hackathons, setHackathons] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)([]);
    const [hackathonId, setHackathonId] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(0);
    (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(() => {
        (async () => {
            await loadList();
        })();
    }, [pageNo]);
    const loadList = async () => {
        try {
            const response = await axios__WEBPACK_IMPORTED_MODULE_1___default().get(`${_config_config__WEBPACK_IMPORTED_MODULE_2__.config.baseUrl}Test?type=5`, {
                headers: {
                    Authorization: `Bearer ${getToken()}`,
                },
            });
            // 기존 데이터 무시하고 새로 채우기
            setHackathons([...response.data.result]);
        }
        catch (err) {
            if (axios__WEBPACK_IMPORTED_MODULE_1___default().isAxiosError(err) && err.response) {
                console.log(err);
            }
            else {
                console.log(err);
            }
        }
    };
    const onResetHackathonSelected = () => {
        setHackathonId(0);
    };
    const onRefreshList = async () => {
        await loadList();
    };
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "container mx-auto overflow-auto h-5/6" }, !hackathonId ? (react__WEBPACK_IMPORTED_MODULE_0___default().createElement((react__WEBPACK_IMPORTED_MODULE_0___default().Fragment), null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("button", { className: "mb-7 border border-gray-200 hover:bg-gray-100 text-gray-600 rounded px-2 ml-8 py-1 disabled:bg-slate-50", onClick: onResetCategory },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("i", { className: "mdi mdi-chevron-left text-sm mr-1" }),
            "\uC720\uD615 \uC120\uD0DD\uC73C\uB85C"),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("button", { className: "mb-7 border border-gray-200 hover:bg-gray-100 text-gray-600 rounded px-2 ml-5 py-1 disabled:bg-slate-50", onClick: onRefreshList },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("i", { className: "mdi mdi-refresh text-sm mr-1" }),
            "\uC0C8\uB85C \uACE0\uCE68"),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "grid grid-cols-1 ml-8 mr-8" }, hackathons.map((hackathon) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_useHackathonCard__WEBPACK_IMPORTED_MODULE_3__["default"], { key: hackathon.testId, hackathon: hackathon, onHackathonSelected: () => {
                setHackathonId(hackathon.testId);
            } })))))) : (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_useHackathonDetail__WEBPACK_IMPORTED_MODULE_4__["default"], { getToken: getToken, hackathonId: hackathonId, onResetHackathonSelected: onResetHackathonSelected }))));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (HackathonList);


/***/ }),

/***/ "./lib/hooks/useHeader.js":
/*!********************************!*\
  !*** ./lib/hooks/useHeader.js ***!
  \********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);

const Header = ({ lectureDrawerVisible, setIsOpen, getUser, lecture, lessons, handleBackToLectureList, }) => {
    const { email, name } = getUser();
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("header", { className: "flex justify-between p-4" },
        lectureDrawerVisible ? (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", null,
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("button", { className: "mb-5 border border-gray-200 hover:bg-gray-100 text-gray-600 rounded px-2 py-1 disabled:bg-slate-50", onClick: (e) => {
                    e.stopPropagation();
                    setIsOpen(true);
                }, disabled: !lectureDrawerVisible },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("i", { className: "mdi mdi-menu text-sm mr-1" }),
                "\uAC15\uC758 \uBAA9\uB85D"),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("button", { className: "ml-8 mb-5 border border-gray-200 hover:bg-gray-100 text-gray-600 rounded px-2 py-1 disabled:bg-slate-50", onClick: handleBackToLectureList, disabled: !lectureDrawerVisible },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("i", { className: "mdi mdi-check text-sm mr-1" }),
                "\uAC15\uC88C \uC120\uD0DD"))) : (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", null)),
        lecture && react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", { className: "text-bold" }, lecture.title),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("h1", { className: "font-medium" },
            name,
            "(",
            email,
            ")")));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (Header);


/***/ }),

/***/ "./lib/hooks/useLectureCard.js":
/*!*************************************!*\
  !*** ./lib/hooks/useLectureCard.js ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _util_date__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../util/date */ "./lib/util/date.js");


const LectureCard = ({ onLectureSelected, lecture }) => {
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "\n        card border border-gray-200 bg-white cursor-pointer p-5 rounded-md text-center\n        max-h-80 max-w-80", onClick: onLectureSelected },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("img", { src: lecture.thumbnailUrl, alt: lecture.title, className: "w-64 bg-gray-400 rounded-sm m-auto" }),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { className: "mt-3 font-large font-bold block" }, lecture.title),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { className: "mt-2 text-gray-400" },
            lecture.last_lesson_date &&
                `마지막 수강일: ${(0,_util_date__WEBPACK_IMPORTED_MODULE_1__.getDateStringOnly)(lecture.last_lesson_date)}`,
            !lecture.last_lesson_date && '수강기록 없음')));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (LectureCard);


/***/ }),

/***/ "./lib/hooks/useLectureDetail.js":
/*!***************************************!*\
  !*** ./lib/hooks/useLectureDetail.js ***!
  \***************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! axios */ "webpack/sharing/consume/default/axios/axios");
/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(axios__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _config_config__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../config/config */ "./lib/config/config.js");
/* harmony import */ var _useLessonList__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./useLessonList */ "./lib/hooks/useLessonList.js");
/* eslint-disable @typescript-eslint/explicit-module-boundary-types */
/* eslint-disable react/no-unescaped-entities */




const LectureDetail = ({ lecture, getToken, onLessonSelected, onResetLessonSelected, onLessonLoaded, }) => {
    const [lessons, setLessons] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)([]);
    (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(() => {
        (async () => {
            const response = await axios__WEBPACK_IMPORTED_MODULE_1___default().get(`${_config_config__WEBPACK_IMPORTED_MODULE_2__.config.baseUrl}Lecture/${lecture.lectureId}/Lessons`, {
                headers: {
                    Authorization: `Bearer ${getToken()}`,
                },
            });
            // 주차 - 회차 - 강의 구조 구성
            const _lessons = [];
            let currentWeek = null;
            let currentChapter = null;
            for (const lesson of response.data.data) {
                if (lesson.type === 'week') {
                    _lessons.push(lesson);
                    currentWeek = lesson;
                }
                else if (lesson.type === 'chapter') {
                    if (!currentWeek.chapters) {
                        currentWeek.chapters = [];
                    }
                    currentWeek.chapters.push(lesson);
                    currentChapter = lesson;
                }
                else {
                    if (!currentChapter.lessons) {
                        currentChapter.lessons = [];
                    }
                    currentChapter.lessons.push(lesson);
                }
            }
            setLessons([]);
            // 기존 데이터를 무시하고 새 데이터만 넣는다.
            setLessons((prev) => [..._lessons]);
            onLessonLoaded(_lessons);
        })();
    }, [lecture]);
    const getSanitizedData = (data) => ({
        __html: data,
    });
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("section", { className: "text-gray-700 body-font overflow-hidden bg-white" },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "container-xl px-5 mx-auto" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "mx-auto flex flex-wrap" },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "w-full lg:pl-10 lg:py-6 mt-6 lg:mt-0" },
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("button", { className: "mb-5 border border-gray-200 hover:bg-gray-100 text-gray-600 rounded px-2 py-1 disabled:bg-slate-50", onClick: onResetLessonSelected },
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("i", { className: 'mdi mdi-chevron-left text-sm' }),
                        "\uAC15\uC88C \uBAA9\uB85D\uC73C\uB85C"),
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("h1", { className: "text-gray-900 text-xl title-font font-extrabold mb-5" }, lecture.title),
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", { className: "leading-relaxed text-xs", dangerouslySetInnerHTML: getSanitizedData(lecture.description) }),
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "flex items-center pb-5 border-b border-gray-200" },
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "flex ml-6 items-center" },
                            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "relative" },
                                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { className: "absolute right-0 top-0 h-full w-10 text-center text-gray-600 pointer-events-none flex items-center justify-center" })))),
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "flex" }, lessons.length > 0 && (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_useLessonList__WEBPACK_IMPORTED_MODULE_3__["default"], { weeks: lessons, onLessonSelected: onLessonSelected }))))))));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (LectureDetail);


/***/ }),

/***/ "./lib/hooks/useLectureDrawer.js":
/*!***************************************!*\
  !*** ./lib/hooks/useLectureDrawer.js ***!
  \***************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);

const LectureDrawer = ({ children, isOpen, setIsOpen }) => {
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("main", { className: ' absolute overflow-hidden z-10 bg-gray-900 bg-opacity-25 inset-0 transform ease-in-out ' +
            (isOpen
                ? ' transition-opacity opacity-100 duration-500 translate-x-0  '
                : ' transition-all delay-500 opacity-0 translate-x-full  ') },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("section", { className: ' w-screen max-w-lg left-0 absolute bg-white h-full shadow-xl delay-400 duration-500 ease-in-out transition-all transform  ' +
                (isOpen ? ' translate-x-0 ' : ' -translate-x-full ') },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("article", { className: "relative w-screen max-w-lg pb-10 flex flex-col space-y-6 overflow-y-scroll h-full" },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "flex justify-between p-4" },
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("header", { className: "font-bold text-lg" }, "\uAC15\uC88C \uBAA9\uB85D"),
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("button", { className: "border border-gray-200 hover:bg-gray-100 text-gray-600 rounded px-4 py-1", onClick: () => setIsOpen(false) }, "\uB2EB\uAE30")),
                children)),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("section", { className: " w-screen h-full cursor-pointer ", onClick: () => {
                setIsOpen(false);
            } })));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (LectureDrawer);


/***/ }),

/***/ "./lib/hooks/useLectureList.js":
/*!*************************************!*\
  !*** ./lib/hooks/useLectureList.js ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "LectureList": () => (/* binding */ LectureList),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! axios */ "webpack/sharing/consume/default/axios/axios");
/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(axios__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _config_config__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../config/config */ "./lib/config/config.js");
/* harmony import */ var _useLectureCard__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./useLectureCard */ "./lib/hooks/useLectureCard.js");
/* harmony import */ var _useLectureDetail__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./useLectureDetail */ "./lib/hooks/useLectureDetail.js");
/* eslint-disable react/prop-types */





// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
const LectureList = ({ getToken, onLectureSelected, onLessonSelected, onLessonLoaded, onResetCategory, }) => {
    const [pageNo, setPageNo] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)(1);
    const [lectures, setLectures] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)([]);
    const [lecture, setLecture] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)(null);
    const wait = (timeToDelay) => new Promise((resolve) => setTimeout(resolve, timeToDelay));
    // 컴포넌트가 로드될 때 실행 되고, 두번째 인자로 주어진 배열에 포함된 특정값이 업데이트될때마다 실행됨
    // 한 번만 실행되게 하려면 빈 배열을 사용
    (0,react__WEBPACK_IMPORTED_MODULE_1__.useEffect)(() => {
        async function loadLectureList() {
            try {
                const response = await axios__WEBPACK_IMPORTED_MODULE_0___default().get(`${_config_config__WEBPACK_IMPORTED_MODULE_2__.config.baseUrl}Lecture/Applied?pageNo=${pageNo}&useJupyter=1`, {
                    headers: {
                        Authorization: `Bearer ${getToken()}`,
                    },
                });
                setLectures([]);
                setLectures((prev) => [...prev, ...response.data.data]);
            }
            catch (err) {
                if (axios__WEBPACK_IMPORTED_MODULE_0___default().isAxiosError(err) && err.response) {
                    console.log(err);
                }
                else {
                    console.log(err);
                }
            }
        }
        loadLectureList();
    }, [pageNo]);
    const onResetLessonSelected = () => {
        setLecture(null);
    };
    return (react__WEBPACK_IMPORTED_MODULE_1___default().createElement("div", { className: "container mx-auto" },
        !lecture && (react__WEBPACK_IMPORTED_MODULE_1___default().createElement((react__WEBPACK_IMPORTED_MODULE_1___default().Fragment), null,
            react__WEBPACK_IMPORTED_MODULE_1___default().createElement("button", { className: "ml-8 mb-5 border border-gray-200 hover:bg-gray-100 text-gray-600 rounded px-2 py-1 disabled:bg-slate-50", onClick: onResetCategory },
                react__WEBPACK_IMPORTED_MODULE_1___default().createElement("i", { className: 'mdi mdi-chevron-left text-sm' }),
                "\uC720\uD615 \uC120\uD0DD\uC73C\uB85C"),
            react__WEBPACK_IMPORTED_MODULE_1___default().createElement("div", { className: "grid gap-8 grid-cols-3 ml-8 mr-8" }, lectures.map((lecture, index) => (react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_useLectureCard__WEBPACK_IMPORTED_MODULE_3__["default"], { key: lecture.lectureId, onLectureSelected: () => {
                    setLecture(lecture);
                    onLectureSelected(lecture);
                }, lecture: lecture })))))),
        lecture && (react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_useLectureDetail__WEBPACK_IMPORTED_MODULE_4__["default"], { lecture: lecture, getToken: getToken, onLessonSelected: onLessonSelected, onResetLessonSelected: onResetLessonSelected, onLessonLoaded: onLessonLoaded }))));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (LectureList);


/***/ }),

/***/ "./lib/hooks/useLessonList.js":
/*!************************************!*\
  !*** ./lib/hooks/useLessonList.js ***!
  \************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* eslint-disable react/prop-types */

// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
const LessonList = ({ weeks, onLessonSelected }) => {
    let weekCnt = 1;
    //let chapterCnt = 1;
    return weeks
        .filter((week) => week.chapters)
        .map((week) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("article", { className: "flex w-full items-start space-x-6 py-12 px-4", key: weekCnt },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", { className: "w-16 text-xl font-extrabold color-mint" },
            weekCnt++,
            "\uC8FC\uCC28"),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "min-w-0 relative flex-auto pl-6" }, week.chapters.map((chapter) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { key: chapter.lessonId, className: "w-full bg-white border-t-2 sm:p-6 dark:bg-gray-800 dark:border-gray-700 color-mint" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("h5", { className: "mb-3 text-base font-semibold text-teal-500 lg:text-xl dark:text-white" }, chapter.title),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("ul", { className: "my-5 space-y-3" }, chapter.lessons &&
                chapter.lessons.map((lesson) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("li", { key: lesson.lessonId },
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("a", { href: "#", className: "flex items-center p-3 text-base font-bold rounded-lg group border border-gray-200 bg-white hover:bg-gray-100 text-gray-900", onClick: () => onLessonSelected(lesson.lessonId) },
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { className: "flex-1 ml-3 whitespace-nowrap" }, lesson.title)))))))))))));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (LessonList);


/***/ }),

/***/ "./lib/hooks/useLogin.js":
/*!*******************************!*\
  !*** ./lib/hooks/useLogin.js ***!
  \*******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Login": () => (/* binding */ Login),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! axios */ "webpack/sharing/consume/default/axios/axios");
/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(axios__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _config_config__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../config/config */ "./lib/config/config.js");
/* harmony import */ var _style_login_view_css__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../style/login-view.css */ "./style/login-view.css");
/* harmony import */ var _useGrayCenterContainer__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./useGrayCenterContainer */ "./lib/hooks/useGrayCenterContainer.js");
/* eslint-disable @typescript-eslint/explicit-module-boundary-types */
/* eslint-disable react/no-unescaped-entities */





// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
// eslint-disable-next-line react/prop-types
const Login = ({ onLoggedIn }) => {
    const [inputs, setInputs] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)({
        email: "",
        password: "",
    });
    const [onProcess, setOnProcess] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(false);
    const { email, password } = inputs;
    const handleChange = (e) => {
        const { name, value } = e.target;
        setInputs((prevState) => (Object.assign(Object.assign({}, prevState), { [name]: value })));
    };
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_useGrayCenterContainer__WEBPACK_IMPORTED_MODULE_3__["default"], null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "xl:w-10/12" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "block bg-white shadow-lg rounded-lg" },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "lg:flex lg:flex-wrap g-0" },
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "lg:w-6/12 px-4 md:px-0" },
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "md:p-12 md:mx-6" },
                            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "text-center" },
                                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("i", { className: "mx-auto login-img" }),
                                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("h4", { className: "text-xl font-semibold mt-1 mb-12 pb-1" },
                                    "\uBAA8\uB450\uC758 \uCF54\uB529 ",
                                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("br", null),
                                    "\uC8FC\uD53C\uD130 \uD074\uB77C\uC774\uC5B8\uD2B8")),
                            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("form", null,
                                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", { className: "mb-4" }, "\uC774\uBA54\uC77C / \uD328\uC2A4\uC6CC\uB4DC\uB97C \uC785\uB825\uD574\uC8FC\uC138\uC694"),
                                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "mb-4" },
                                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("input", { type: "email", name: "email", className: "form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none", placeholder: "email@example.com", value: email, onChange: handleChange })),
                                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "mb-4" },
                                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("input", { type: "password", name: "password", className: "form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none", placeholder: "Password", value: password, onChange: handleChange })),
                                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "text-center pt-1 mb-12 pb-1" },
                                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("button", { className: "inline-block px-6 py-2.5 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:shadow-lg focus:outline-none focus:ring-0 active:shadow-lg transition duration-150 ease-in-out w-full mb-3", type: "button", "data-mdb-ripple": "true", "data-mdb-ripple-color": "light", style: {
                                            background: "linear-gradient(to right, #007fac, #199bc8, #19bdc8, #1abec9)",
                                        }, onClick: async () => {
                                            if (!email || !password) {
                                                return;
                                            }
                                            setOnProcess(true);
                                            //console.log(email, password);
                                            const param = {
                                                email,
                                                password,
                                            };
                                            try {
                                                const response = await axios__WEBPACK_IMPORTED_MODULE_1___default().post(`${_config_config__WEBPACK_IMPORTED_MODULE_4__.config.baseUrl}Token`, param);
                                                if (response.data && response.data.token) {
                                                    onLoggedIn(response.data);
                                                }
                                                //const token = response.data.token;
                                                //console.log(token);
                                                //const stateObj = { email, token };
                                            }
                                            catch (err) {
                                                if (axios__WEBPACK_IMPORTED_MODULE_1___default().isAxiosError(err) && err.response) {
                                                    setOnProcess(false);
                                                    if (err.response.status === 400) {
                                                        alert("패스워드는 8자 이상, 영문자, 숫자, 특수문자를 포함해야 합니다.");
                                                        return;
                                                    }
                                                    else if (err.response.status === 404) {
                                                        alert("이메일 또는 패스워드가 일치하지 않습니다.");
                                                        return;
                                                    }
                                                }
                                                else {
                                                    console.log(err);
                                                }
                                            }
                                        }, disabled: onProcess },
                                        onProcess && (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("svg", { role: "status", className: "inline w-4 h-4 mr-3 text-white animate-spin", viewBox: "0 0 100 101", fill: "none", xmlns: "http://www.w3.org/2000/svg" },
                                            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("path", { d: "M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z", fill: "#E5E7EB" }),
                                            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("path", { d: "M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z", fill: "currentColor" }))),
                                        "\uB85C\uADF8\uC778"))))),
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "lg:w-6/12 flex items-center lg:rounded-r-lg rounded-b-lg lg:rounded-bl-none", style: {
                            background: "linear-gradient(to right,  #007fac, #199bc8, #19bdc8, #1abec9)",
                        } },
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "text-white px-4 py-6 md:p-12 md:mx-6" },
                            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("h4", { className: "text-xl font-semibold mb-6" },
                                "\uB204\uAD6C\uB098 \uC27D\uAC8C Python\uACFC AI\uB97C \uD559\uC2B5\uD560 \uC218 \uC788\uC2B5\uB2C8\uB2E4. ",
                                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("br", null)),
                            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", { className: "text-sm" }, "\uBAA8\uB450\uC758 \uCF54\uB529 \uD074\uB77C\uC774\uC5B8\uD2B8\uB97C \uD1B5\uD574 python\uAE30\uBC18\uC758 \uB370\uC774\uD130 / AI \uD559\uC2B5\uACFC AI \uD574\uCEE4\uD1A4\uC5D0 \uCC38\uC5EC\uD558\uC138\uC694!")))))))
    // <div>
    //   <div id="wrap">
    //     <div className="join-wrap">
    //       <div className="join-top">
    //         <h3>로그인</h3>
    //         <p className="txt">"모두를 위한 코딩이 시작되는 곳"</p>
    //       </div>
    //       <div className="join-form">
    //         <form className="">
    //           <div className="input-set">
    //             <p>이메일</p>
    //             <div className="input-box">
    //               <input
    //                 type="email"
    //                 name="email"
    //                 placeholder="email@example.com"
    //                 value={email}
    //                 onChange={handleChange}
    //               />
    //               <i className="mdi mdi-email"></i>
    //             </div>
    //           </div>
    //           <div className="input-set">
    //             <p>비밀번호</p>
    //             <div className="input-box">
    //               <input
    //                 type="password"
    //                 name="password"
    //                 placeholder="password"
    //                 value={password}
    //                 onChange={handleChange}
    //               />
    //               <i className="mdi mdi-lock"></i>
    //             </div>
    //           </div>
    //           <input
    //             type="button"
    //             className="join-btn"
    //             value="로그인"
    //             onClick={async (): Promise<void> => {
    //               //console.log(email, password);
    //               const param = {
    //                 email,
    //                 password,
    //               };
    //               try {
    //                 const response = await axios.post(
    //                   `${config.baseUrl}Token`,
    //                   param
    //                 );
    //                 if (response.data && response.data.token) {
    //                   onLoggedIn(response.data);
    //                 }
    //                 //const token = response.data.token;
    //                 //console.log(token);
    //                 //const stateObj = { email, token };
    //               } catch (err) {
    //                 if (axios.isAxiosError(err) && err.response) {
    //                   if (err.response.status === 400) {
    //                     alert(
    //                       '패스워드는 8자 이상, 영문자, 숫자, 특수문자를 포함해야 합니다.'
    //                     );
    //                     return;
    //                   } else if (err.response.status === 404) {
    //                     alert('이메일 또는 패스워드가 일치하지 않습니다.');
    //                     return;
    //                   }
    //                 } else {
    //                   console.log(err);
    //                 }
    //               }
    //             }}
    //           ></input>
    //         </form>
    //       </div>
    //       <i className="login-img"></i>
    //     </div>
    //   </div>
    // </div>
    );
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (Login);


/***/ }),

/***/ "./lib/hooks/useVideoJS.js":
/*!*********************************!*\
  !*** ./lib/hooks/useVideoJS.js ***!
  \*********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "VideoJS": () => (/* binding */ VideoJS),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var video_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! video.js */ "webpack/sharing/consume/default/video.js/video.js?67b7");
/* harmony import */ var video_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(video_js__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var video_js_dist_video_js_css__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! video.js/dist/video-js.css */ "./node_modules/video.js/dist/video-js.css");
/* harmony import */ var videojs_youtube__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! videojs-youtube */ "webpack/sharing/consume/default/videojs-youtube/videojs-youtube");
/* harmony import */ var videojs_youtube__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(videojs_youtube__WEBPACK_IMPORTED_MODULE_3__);
/* eslint-disable react/prop-types */




// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
const VideoJS = (props) => {
    const videoRef = react__WEBPACK_IMPORTED_MODULE_0___default().useRef(null);
    const playerRef = react__WEBPACK_IMPORTED_MODULE_0___default().useRef(null);
    // eslint-disable-next-line react/prop-types
    const { options, onReady } = props;
    react__WEBPACK_IMPORTED_MODULE_0___default().useEffect(() => {
        // make sure Video.js player is only initialized once
        if (!playerRef.current) {
            const videoElement = videoRef.current;
            if (!videoElement) {
                return;
            }
            const player = (playerRef.current = video_js__WEBPACK_IMPORTED_MODULE_1___default()(videoElement, options, () => {
                console.log('player is ready');
                onReady && onReady(player);
            }));
        }
        else {
            // you can update player here [update player through props]
            const player = playerRef.current;
            player.autoplay(options.autoplay);
            player.src(options.sources);
        }
    }, [options, videoRef]);
    // Dispose the Video.js player when the functional component unmounts
    react__WEBPACK_IMPORTED_MODULE_0___default().useEffect(() => {
        const player = playerRef.current;
        return () => {
            if (player) {
                player.dispose();
                playerRef.current = null;
            }
        };
    }, [playerRef]);
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { "data-vjs-player": true },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("video", { ref: videoRef, className: "video-js vjs-big-play-centered" })));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (VideoJS);


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/launcher */ "webpack/sharing/consume/default/@jupyterlab/launcher");
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./widget */ "./lib/widget.js");




/**
 * The command IDs used by the react-widget plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.create = "create-react-widget";
})(CommandIDs || (CommandIDs = {}));
/**
 * Initialization data for the react-widget extension.
 */
const extension = {
    id: "modu-jupyter-extension",
    autoStart: true,
    optional: [_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_1__.ILauncher],
    activate: (app, launcher) => {
        const { commands } = app;
        // 커스텀 아이콘은 svg에서 생성가능.
        const moduIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.LabIcon({
            name: "moduIcon",
            svgstr: `<svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 23.98"><defs><style>.cls-1{fill:none;}.cls-2{fill:#212435;}.cls-3{fill:#495ef1;}.cls-4{fill:#d64c32;}</style></defs><rect class="cls-1" width="52" height="23.98"/><path class="cls-2" d="M463,141.7V140h1.17v1.74h3.2v1h-6.79v-1Zm1.94-.78a1.94,1.94,0,0,0,.34-.84,7.58,7.58,0,0,0,.06-.76h-4.13v-1h4.14v-1h-4.18v-1h5.32v3.09a4.93,4.93,0,0,1,0,.55,3.81,3.81,0,0,1-.12.51,1.08,1.08,0,0,1-.24.39Z" transform="translate(-422.13 -130.96)"/><path class="cls-2" d="M446.58,140.1a2.11,2.11,0,0,0,.71.43,3,3,0,0,0,.85.22,4.14,4.14,0,0,0,.94.05,5.74,5.74,0,0,0,.93-.08,5,5,0,0,0,.87-.22,3.63,3.63,0,0,0,.72-.31v-1a4.87,4.87,0,0,1-1.48.49,5,5,0,0,1-1.47.07,2.6,2.6,0,0,1-1.13-.33.77.77,0,0,1-.46-.72v-1.37h4.41v-1h-5.53v2.18a2,2,0,0,0,.18.89A1.83,1.83,0,0,0,446.58,140.1Z" transform="translate(-422.13 -130.96)"/><polygon class="cls-2" points="23.4 11.58 26.23 11.58 26.23 13.6 27.39 13.6 27.39 11.58 30.19 11.58 30.19 10.62 23.4 10.62 23.4 11.58"/><polygon class="cls-2" points="36.27 5.2 36.27 11.68 37.38 11.69 37.38 5.2 36.27 5.2"/><rect class="cls-2" x="30.8" y="10.62" width="5" height="0.93"/><path class="cls-2" d="M455.28,136.08a2.35,2.35,0,1,0,2.34,2.35A2.35,2.35,0,0,0,455.28,136.08Zm0,3.59a1.25,1.25,0,1,1,1.24-1.24A1.25,1.25,0,0,1,455.28,139.67Z" transform="translate(-422.13 -130.96)"/><path class="cls-2" d="M470.84,140.79a2.7,2.7,0,0,0,.68-.22,2.33,2.33,0,0,0,.57-.34v-1a3.39,3.39,0,0,1-1.22.51,2.33,2.33,0,0,1-1.05,0,1.17,1.17,0,0,1-.74-.42,1.11,1.11,0,0,1-.28-.79v-1.22h2.76v-1h-3.89v2.07a2.52,2.52,0,0,0,.14.91,1.74,1.74,0,0,0,.37.67,1.76,1.76,0,0,0,.55.46,1.92,1.92,0,0,0,.66.27,3.55,3.55,0,0,0,1.45,0Z" transform="translate(-422.13 -130.96)"/><path class="cls-2" d="M474.12,143h0v-6.81H473v5a2.16,2.16,0,1,0,1.12,1.9ZM472,144.06a1,1,0,1,1,1.05-1A1,1,0,0,1,472,144.06Z" transform="translate(-422.13 -130.96)"/><path class="cls-1" d="M443.09,138.93v-1.58H440v1.59a1,1,0,0,0,.33.83,1.34,1.34,0,0,0,.88.27h.63a1.55,1.55,0,0,0,.91-.27A1,1,0,0,0,443.09,138.93Z" transform="translate(-422.13 -130.96)"/><path class="cls-2" d="M442.17,141.62V141a2.38,2.38,0,0,0,1.38-.49,1.79,1.79,0,0,0,.66-1.49v-2.61h-5.35v2.51a1.89,1.89,0,0,0,.63,1.56A2.34,2.34,0,0,0,441,141v.64h-2.82v.95H445v-.95Zm-1-1.58a1.34,1.34,0,0,1-.88-.27,1,1,0,0,1-.33-.83v-1.59h3.12v1.58a1,1,0,0,1-.37.84,1.55,1.55,0,0,1-.91.27Z" transform="translate(-422.13 -130.96)"/><path class="cls-3" d="M435,137.19v1.29c0,.61.34.84.91,1a.86.86,0,0,1,0,1.65c-.61.13-.91.36-.91,1v1.25c0,1.09-.65,2.07-2.35,2.14-.41,0-.55-.23-.55-.59a.54.54,0,0,1,.53-.62,1,1,0,0,0,1-1v-1.37a1.35,1.35,0,0,1,1.21-1.56v-.05c-1.08-.2-1.21-.87-1.21-1.64v-1.36a1,1,0,0,0-1-1c-.4,0-.54-.31-.54-.66s.14-.56.47-.56C434.34,135,435,136.09,435,137.19Z" transform="translate(-422.13 -130.96)"/><path class="cls-3" d="M423.67,143.31V142c0-.62-.35-.85-.92-1a.74.74,0,0,1-.62-.82.72.72,0,0,1,.62-.83c.62-.13.92-.37.92-1v-1.25c0-1.09.65-2.07,2.35-2.13.41,0,.55.22.55.58a.55.55,0,0,1-.53.63,1,1,0,0,0-1,1v1.37a1.35,1.35,0,0,1-1.21,1.56v.06c1.08.19,1.21.86,1.21,1.64v1.35a1,1,0,0,0,1,1c.4,0,.54.3.54.65s-.14.57-.47.57C424.32,145.47,423.67,144.41,423.67,143.31Z" transform="translate(-422.13 -130.96)"/><circle class="cls-3" cx="5.41" cy="8.09" r="0.81"/><circle class="cls-3" cx="8.99" cy="8.02" r="0.81"/><path class="cls-3" d="M430.89,141.28a2,2,0,0,1-3.13,0c-.43-.48-1.13.23-.7.71a3,3,0,0,0,4.54,0c.43-.48-.28-1.19-.71-.71Z" transform="translate(-422.13 -130.96)"/><path class="cls-4" d="M50.22,17.18h0a.35.35,0,0,1,.35.35v.76a.35.35,0,0,1-.35.35H50a.15.15,0,0,1-.15-.15v-1A.35.35,0,0,1,50.22,17.18Z"/><path class="cls-4" d="M473.78,153.34h-.67a.42.42,0,0,1-.42-.42v-2.06h1.09a.35.35,0,0,0,0-.7h-1.62a.16.16,0,0,0-.16.16v2.58a1.36,1.36,0,0,0,0,.16,1.1,1.1,0,0,0,1.1,1h.67a.35.35,0,1,0,0-.69Z" transform="translate(-422.13 -130.96)"/><path class="cls-4" d="M471.07,150.47a1.46,1.46,0,0,0-1.19-.5,1.43,1.43,0,0,0-1.14.49,1.87,1.87,0,0,0-.43,1.32v.46a1.85,1.85,0,0,0,.44,1.32,1.5,1.5,0,0,0,1.2.47,2.29,2.29,0,0,0,.83-.14l.42-.2.07-.06,0,0a.31.31,0,0,0,.07-.21.32.32,0,0,0-.33-.32.31.31,0,0,0-.13,0h0a2.23,2.23,0,0,1-.31.15,1.57,1.57,0,0,1-.6.1.82.82,0,0,1-.68-.28,1.17,1.17,0,0,1-.26-.79h2a.44.44,0,0,0,.44-.48v0A2,2,0,0,0,471.07,150.47Zm-1.82.44a.74.74,0,0,1,.63-.28.82.82,0,0,1,.66.27,1.14,1.14,0,0,1,.26.76H469A1.24,1.24,0,0,1,469.25,150.91Z" transform="translate(-422.13 -130.96)"/><path class="cls-4" d="M458.24,150a1.73,1.73,0,0,0-1,.32v-1.8a.35.35,0,0,0-.35-.35h0a.35.35,0,0,0-.35.35v5.19a.35.35,0,0,0,.35.35h0a.35.35,0,0,0,.35-.35v-2h0a1,1,0,0,1,2,0v2a.35.35,0,0,0,.35.35h0a.35.35,0,0,0,.35-.35v-2A1.7,1.7,0,0,0,458.24,150Z" transform="translate(-422.13 -130.96)"/><path class="cls-4" d="M464.74,154a.35.35,0,0,0,.35-.35v-2h0a1,1,0,1,1,2,0v2a.36.36,0,0,0,.36.35h0a.35.35,0,0,0,.35-.35v-2a1.71,1.71,0,1,0-3.41,0h0v2a.36.36,0,0,0,.36.35Z" transform="translate(-422.13 -130.96)"/><path class="cls-4" d="M463.51,150.16a.35.35,0,0,0-.35.35v2h0a1,1,0,0,1-2,0v-2a.35.35,0,0,0-.35-.35h0a.35.35,0,0,0-.35.35v2a1.7,1.7,0,1,0,3.4,0h0v-2a.35.35,0,0,0-.35-.35Z" transform="translate(-422.13 -130.96)"/></svg>`,
        });
        app.shell.title.icon = moduIcon;
        //app.shell.title.label = "KT Aivle School";
        app.shell.title.label = "모두의 코딩";
        const command = CommandIDs.create;
        commands.addCommand(command, {
            // caption: "KT Aivle School",
            caption: "모두의 코딩",
            //label: (args) => (args["isPalette"] ? null : "KT Aivle School"),
            label: (args) => (args["isPalette"] ? null : "모두의 코딩"),
            icon: (args) => (args["isPalette"] ? null : moduIcon),
            execute: () => {
                const content = new _widget__WEBPACK_IMPORTED_MODULE_3__.ModuCodingWidget();
                const widget = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.MainAreaWidget({ content });
                //widget.title.label = "KT Aivle School";
                widget.title.label = "모두의 코딩";
                widget.title.icon = moduIcon;
                app.shell.add(widget, "main");
            },
        });
        if (launcher) {
            launcher.add({
                command,
            });
        }
    },
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (extension);


/***/ }),

/***/ "./lib/types/category.js":
/*!*******************************!*\
  !*** ./lib/types/category.js ***!
  \*******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
var Category;
(function (Category) {
    Category[Category["Lecture"] = 1] = "Lecture";
    Category[Category["AIHackathon"] = 2] = "AIHackathon";
})(Category || (Category = {}));
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (Category);


/***/ }),

/***/ "./lib/util/date.js":
/*!**************************!*\
  !*** ./lib/util/date.js ***!
  \**************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "getDateStringOnly": () => (/* binding */ getDateStringOnly),
/* harmony export */   "getTimeBoxString": () => (/* binding */ getTimeBoxString),
/* harmony export */   "getTimeStringOnly": () => (/* binding */ getTimeStringOnly)
/* harmony export */ });
const getTimeStringOnly = (dateString = null) => {
    const date = dateString ? new Date(dateString) : new Date();
    return [
        ('0' + date.getHours()).slice(-2),
        ('0' + date.getMinutes()).slice(-2),
    ].join(':');
};
const getDateStringOnly = (dateString) => {
    if (!dateString) {
        return null;
    }
    const date = new Date(dateString);
    return [
        date.getFullYear(),
        ('0' + (date.getMonth() + 1)).slice(-2),
        ('0' + date.getDate()).slice(-2),
    ].join('-');
};
const getTimeBoxString = (startDateString, endDateString) => {
    if (!startDateString || !endDateString) {
        return null;
    }
    return `${getDateStringOnly(startDateString)} ${getTimeStringOnly(startDateString)} ~ ${getDateStringOnly(endDateString)} ${getTimeStringOnly(endDateString)}`;
};


/***/ }),

/***/ "./lib/util/file.js":
/*!**************************!*\
  !*** ./lib/util/file.js ***!
  \**************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "handleDownload": () => (/* binding */ handleDownload)
/* harmony export */ });
/* eslint-disable @typescript-eslint/explicit-module-boundary-types */
const handleDownload = (fileUrl) => {
    try {
        if (!fileUrl.includes('___')) {
            return;
        }
        const filename = fileUrl.split('___')[1];
        const link = document.createElement('a');
        link.href = fileUrl;
        link.target = '_blank';
        link.setAttribute('download', filename);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
    catch (err) {
        console.log(err);
    }
};


/***/ }),

/***/ "./lib/util/url.js":
/*!*************************!*\
  !*** ./lib/util/url.js ***!
  \*************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "isValidUrl": () => (/* binding */ isValidUrl),
/* harmony export */   "isYoutubeUrl": () => (/* binding */ isYoutubeUrl)
/* harmony export */ });
/* eslint-disable no-irregular-whitespace */
/* eslint-disable no-useless-escape */
/* eslint-disable @typescript-eslint/explicit-module-boundary-types */
/* eslint-disable jsdoc/require-returns */
/**
 * 유효한 url인지 확인
 * @param {String} url 확인할 url 문자열
 */
const isValidUrl = (url) => {
    const regex = /(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/g;
    return regex.test(url);
};
/**
 * 유효한 youtube url인지 확인
 * @param {String} url 확인할 youtube url 문자열
 */
const isYoutubeUrl = (url) => {
    if (!url) {
        return false;
    }
    const youtubeUrlPattern = /http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?/gm;
    const found = url.match(youtubeUrlPattern);
    return found;
};


/***/ }),

/***/ "./lib/widget.js":
/*!***********************!*\
  !*** ./lib/widget.js ***!
  \***********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ModuCodingWidget": () => (/* binding */ ModuCodingWidget)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! axios */ "webpack/sharing/consume/default/axios/axios");
/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(axios__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _config_config__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./config/config */ "./lib/config/config.js");
/* harmony import */ var _hooks_useLectureList__WEBPACK_IMPORTED_MODULE_17__ = __webpack_require__(/*! ./hooks/useLectureList */ "./lib/hooks/useLectureList.js");
/* harmony import */ var _hooks_useLogin__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ./hooks/useLogin */ "./lib/hooks/useLogin.js");
/* harmony import */ var _hooks_useVideoJS__WEBPACK_IMPORTED_MODULE_16__ = __webpack_require__(/*! ./hooks/useVideoJS */ "./lib/hooks/useVideoJS.js");
/* harmony import */ var react_azure_mp__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-azure-mp */ "webpack/sharing/consume/default/react-azure-mp/react-azure-mp");
/* harmony import */ var react_azure_mp__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react_azure_mp__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _style_lecture_detail_css__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../style/lecture-detail.css */ "./style/lecture-detail.css");
/* harmony import */ var socket_io_client__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! socket.io-client */ "webpack/sharing/consume/default/socket.io-client/socket.io-client");
/* harmony import */ var socket_io_client__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(socket_io_client__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var dompurify__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! dompurify */ "webpack/sharing/consume/default/dompurify/dompurify");
/* harmony import */ var dompurify__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(dompurify__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _hooks_useLectureDrawer__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! ./hooks/useLectureDrawer */ "./lib/hooks/useLectureDrawer.js");
/* harmony import */ var _hooks_useHeader__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! ./hooks/useHeader */ "./lib/hooks/useHeader.js");
/* harmony import */ var _hooks_useLessonList__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! ./hooks/useLessonList */ "./lib/hooks/useLessonList.js");
/* harmony import */ var _hooks_useCategorySelect__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! ./hooks/useCategorySelect */ "./lib/hooks/useCategorySelect.js");
/* harmony import */ var _types_category__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! ./types/category */ "./lib/types/category.js");
/* harmony import */ var _hooks_useHackathonList__WEBPACK_IMPORTED_MODULE_18__ = __webpack_require__(/*! ./hooks/useHackathonList */ "./lib/hooks/useHackathonList.js");
/* harmony import */ var _util_date__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./util/date */ "./lib/util/date.js");
/* harmony import */ var _util_url__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./util/url */ "./lib/util/url.js");


//import 'tailwindcss/tailwind.css';
//import 'bootstrap/dist/css/bootstrap.css';

















/**
 * React component for a counter.
 *
 * @returns The React component
 */
const ModuCodingComponent = () => {
    // useStyle(
    //   'https://cdn.jsdelivr.net/npm/video.js@7.10.2/dist/video-js.min.css'
    // );
    // useScript('https://cdn.jsdelivr.net/npm/video.js@7.10.2/dist/video.min.js');
    // useScript(
    //   'https://cdn.jsdelivr.net/npm/videojs-youtube@2.6.1/dist/Youtube.min.js'
    // );
    // const [videoUrl, setVideoUrl] = useState('');
    const [state, setState] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)({
        loggedIn: false,
        email: "",
        name: "",
        //memberId: 0,
        token: "",
        roles: [],
        currentCategory: 0,
        currentLecture: null,
        lectureSelected: false,
        lessonSelected: false,
        questionSelected: false,
        currentLectureLessons: null,
    });
    const [isLectureListOpen, setIsLectureListOpen] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)(false);
    const [lectureDrawerVisible, setLectureDrawerVisible] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)(false);
    const [lesson, setLesson] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)({
        title: "",
        description: "",
        extLiveStreamUrl: null,
        videoLink: "",
        videoFile: "",
        videoUrl: "",
        pdfUrl: "",
        notebookUrl: "",
    });
    const [ampSource, setAMPSource] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)([]);
    const [questions, setQuestions] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)([]);
    const setStateChanged = (prop, value, fn) => {
        fn((prevState) => (Object.assign(Object.assign({}, prevState), { [prop]: value })));
    };
    const [videoJsOptions, setVideoJsOptions] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)({
        // lookup the options in the docs for more options
        width: 720,
        height: 480,
        autoplay: true,
        controls: true,
        responsive: true,
        fluid: true,
        sources: [
        // {
        //   src: 'https://moduams-koct1.streaming.media.azure.net/b30382ca-1b9…6-e7a811f39798/ca4d5d93-8d59-44db-aa7f-5ea1c55c.ism/manifest', // 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4',
        //   type: 'application/vnd.ms-sstr+xml', //'video/mp4',
        // },
        ],
    });
    //const [descriptionMode, setDescriptionMode] = useState('description');
    const [chatMessages, setChatMessages] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)([]);
    const [socket, setSocket] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)(null);
    const [roomId, setRoomId] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)(null);
    const playerRef = react__WEBPACK_IMPORTED_MODULE_2___default().useRef(null);
    const chatListRef = react__WEBPACK_IMPORTED_MODULE_2___default().useRef();
    const { loggedIn, email, name, token, roles, currentCategory, currentLecture, currentLectureLessons, lessonSelected, questionSelected, } = state;
    const { videoUrl, videoLink, videoFile, pdfUrl, notebookUrl } = lesson;
    const handlePlayerReady = (player) => {
        playerRef.current = player;
        // you can handle player events here
        player.on("waiting", () => {
            console.log("player is waiting");
        });
        player.on("dispose", () => {
            console.log("player will dispose");
        });
    };
    const onLoggedIn = (stateObj) => {
        for (const [key, value] of Object.entries(stateObj)) {
            console.log(key, value);
            setStateChanged(key, value, setState);
        }
        setStateChanged("loggedIn", true, setState);
    };
    /**
     * 자식 컴포넌트에 이 함수가 전달되면,
     * state변화로 인해 부모 컴포넌트가 다시 렌더링 될 때 이 함수도 재정의된다.
     * 따라서 이 함수를 전달받는 자식 컴포넌트도 다시 렌더링 되어 성능 저하 발생
     * useCallback을 사용해서 해당 state가 변경될 때 만 함수를 다시 정의하도록 하여
     * 자식 컴포넌트가 매번 다시 렌더링 되는 것을 방지
     * https://blog.logrocket.com/optimizing-performance-react-application/   *
     */
    // const getToken = () => {
    //   return token;
    // };
    const getToken = react__WEBPACK_IMPORTED_MODULE_2___default().useCallback(() => {
        return token;
    }, [token]);
    const getUser = react__WEBPACK_IMPORTED_MODULE_2___default().useCallback(() => {
        return {
            email,
            name,
        };
    }, [email, name]);
    const loadLesson = async (lessonId) => {
        try {
            const response = await axios__WEBPACK_IMPORTED_MODULE_1___default().get(`${_config_config__WEBPACK_IMPORTED_MODULE_7__.config.baseUrl}Lesson/Applied/${lessonId}`, {
                headers: {
                    Authorization: `Bearer ${getToken()}`,
                },
            });
            // 여기서 비디오url말고 다른 것도 확인해봐야...
            // 만약에 비디오 없으면 영상을 표시하지 말아야지...-_-;;;
            const lesson = response.data;
            setStateChanged("title", lesson.title, setLesson);
            setStateChanged("description", lesson.description, setLesson);
            setStateChanged("extLiveStreamUrl", lesson.extLiveStreamUrl, setLesson);
            console.log(JSON.stringify(lesson, null, 2));
            if (lesson.questionsVM && lesson.questionsVM.length > 0) {
                setQuestions((prev) => [...prev, ...lesson.questionsVM]);
            }
            if (lesson.extLiveStreamUrl) {
                console.log("live!!!!!", lesson.extLiveStreamUrl);
                // 라이브의 경우 VideoJS로 유투브 라이브 표시
                setStateChanged("videoUrl", lesson.extLiveStreamUrl, setLesson);
                // playerRef.current.src({
                //   type: 'video/youtube',
                //   src: videoFile.url,
                // });
            }
            else {
                setStateChanged("videoUrl", "", setLesson);
            }
            if (lesson.lessonLinks) {
                setStateChanged("videoFile", "", setLesson);
                setStateChanged("videoLink", "", setLesson);
                const pdfFile = lesson.lessonLinks.find((link) => link.type.toLowerCase() === "pdffile");
                if (pdfFile && pdfFile.url) {
                    setStateChanged("pdfUrl", pdfFile.url, setLesson);
                }
                const notebookFile = lesson.lessonLinks.find((link) => link.type.toLowerCase() === "notebookfile");
                if (notebookFile && notebookFile.url) {
                    setStateChanged("notebookUrl", notebookFile.url, setLesson);
                }
                if (lesson.extLiveStreamUrl) {
                    return;
                }
                const videoFile = lesson.lessonLinks.find((link) => link.type.toLowerCase() === "videofile");
                // 라이브가 아닐 때만 videoFile 체크
                if (videoFile && videoFile.url) {
                    setStateChanged("videoFile", videoFile.url, setLesson);
                    // 화면에 다시 렌더링 될 때마다 AMP가 재설정되지 않으려면, 소스 객체를 상태에 저장해야 함.
                    //https://github.com/SidKH/react-azure-mp/issues/27
                    setAMPSource([
                        {
                            src: videoFile.url,
                            type: "application/vnd.ms-sstr+xml",
                        },
                    ]);
                }
                else {
                    // Azure Media Service가 아니면 youtube 영상
                    const videoLink = lesson.lessonLinks.find((link) => link.type.toLowerCase() === "videolink");
                    if (videoLink && videoLink.url) {
                        setStateChanged("videoLink", videoLink.url, setLesson);
                        if (!(0,_util_url__WEBPACK_IMPORTED_MODULE_8__.isYoutubeUrl)(lesson.extLiveStreamUrl)) {
                            setStateChanged("sources", {
                                type: "video/youtube",
                                src: videoLink.url,
                            }, setVideoJsOptions);
                        }
                    }
                }
            }
        }
        catch (err) {
            if (axios__WEBPACK_IMPORTED_MODULE_1___default().isAxiosError(err) && err.response) {
                console.log(err);
            }
            else {
                console.log(err);
            }
        }
    };
    const onCategorySelected = (category) => {
        setStateChanged("currentCategory", category, setState);
    };
    const onResetCategory = () => {
        setStateChanged("currentCategory", 0, setState);
    };
    const onLectureSelected = async (lecture) => {
        setStateChanged("lectureSelected", true, setState);
        setStateChanged("currentLecture", lecture, setState);
    };
    const onLessonSelected = async (lessonId) => {
        if (!currentLecture) {
            return;
        }
        // 헤더의 사이드 메뉴 버튼 표시
        setLectureDrawerVisible(true);
        setStateChanged("lessonSelected", true, setState);
        //setStateChanged('currentLecture', lecture, setState);
        try {
            /**
             * 화면에 표시할 공간이 없어서 일단 라이브 채팅 기능 비활성화
             */
            // if (currentLecture.isBroadcast) {
            //   // 1. 라이브 url 및 상태 체크
            //   const response = await axios.get(
            //     `${config.baseUrl}Lecture/${currentLecture.lectureId}/LiveStatus`,
            //     {
            //       headers: {
            //         Authorization: `Bearer ${getToken()}`,
            //       },
            //     }
            //   );
            //   const status = await response.data;
            //   if (!status.isBroadcast || !status.extLiveStreamUrl) {
            //     return;
            //   }
            //   if (currentLecture.liveToken) {
            //     const roomId = `${currentLecture.liveToken}-${currentLecture.liveToken}`;
            //     setRoomId(roomId);
            //   }
            // }
            await loadLesson(lessonId);
        }
        catch (err) {
            if (axios__WEBPACK_IMPORTED_MODULE_1___default().isAxiosError(err) && err.response) {
                console.log(err);
            }
            else {
                console.log(err);
            }
        }
    };
    const onLessonLoaded = (lessons) => {
        setStateChanged("currentLectureLessons", lessons, setState);
    };
    const handleBackToLectureList = () => {
        // 헤더의 사이드 메뉴 버튼 표시
        setLectureDrawerVisible(false);
        setStateChanged("lessonSelected", false, setState);
        setStateChanged("currentLecture", null, setState);
        setStateChanged("currentLectureLessons", null, setState);
    };
    const getSanitizedData = (data) => ({
        __html: data,
    });
    const onQuestionSelected = (questionId) => {
        console.log(questionId);
    };
    (0,react__WEBPACK_IMPORTED_MODULE_2__.useEffect)(() => {
        if (!videoUrl) {
            return;
        }
        if (lesson.extLiveStreamUrl) {
            console.log("useEffect", lesson.extLiveStreamUrl);
            let videoType = "video/youtube";
            if (!(0,_util_url__WEBPACK_IMPORTED_MODULE_8__.isYoutubeUrl)(lesson.extLiveStreamUrl)) {
                videoType = "application/x-mpegURL";
            }
            setStateChanged("sources", {
                type: videoType,
                src: videoUrl,
            }, setVideoJsOptions);
            // playerRef.current.src({
            //   type: 'video/youtube',
            //   src: videoUrl,
            // });
        }
    }, [videoUrl]);
    (0,react__WEBPACK_IMPORTED_MODULE_2__.useEffect)(() => {
        scrollToBottom();
    }, [chatMessages]);
    (0,react__WEBPACK_IMPORTED_MODULE_2__.useEffect)(() => {
        if (!roomId) {
            return;
        }
        chatStart();
    }, [roomId]);
    // useEffect(() => {
    //   if (!pdfUrl) {
    //     return;
    //   }
    //   //split-lesson
    //   //split-pdf
    // }, [descriptionMode]);
    const toggleChatPanel = () => {
        const chatPanel = document.querySelector(".chat-panel");
        const openBtn = document.querySelector(".open-btn");
        const closeBtn = document.querySelector(".close-btn");
        chatPanel.classList.toggle("hide");
        if (chatPanel.classList.contains("hide")) {
            openBtn.style.display = "block";
            closeBtn.style.display = "none";
        }
        else {
            openBtn.style.display = "none";
            closeBtn.style.display = "block";
        }
    };
    const handleDescriptionModeChanged = () => {
        const descEl = document.querySelector(".split-description");
        const pdfEl = document.querySelector(".split-pdf");
        if (!descEl || !pdfEl) {
            return;
        }
        descEl.classList.toggle("hide");
        pdfEl.classList.toggle("hide");
        //setDescriptionMode(descriptionMode);
    };
    const renderChatMessages = (chatMessages) => {
        const messages = [];
        for (const message of chatMessages) {
            if (message.type === "info") {
                messages.push(react__WEBPACK_IMPORTED_MODULE_2___default().createElement("li", { className: "msg-list" },
                    react__WEBPACK_IMPORTED_MODULE_2___default().createElement("p", null, message.content)));
            }
            else if (message.type === "sent") {
                messages.push(react__WEBPACK_IMPORTED_MODULE_2___default().createElement("li", { className: "msg-list msg-send" },
                    react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: "msg-item" },
                        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("i", { className: "tag" }),
                        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: "text-msg" }, message.content),
                        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("span", { className: "date" }, (0,_util_date__WEBPACK_IMPORTED_MODULE_9__.getTimeStringOnly)()))));
            }
            else {
                messages.push(react__WEBPACK_IMPORTED_MODULE_2___default().createElement("li", { className: "msg-list msg-receive" },
                    react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: "msg-info" },
                        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("i", { className: "user-img" }),
                        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("p", { className: "user-name" }, message.from)),
                    react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: "msg-item" },
                        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: "tag" }),
                        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: "text-msg" }, message.content),
                        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: "date" }, (0,_util_date__WEBPACK_IMPORTED_MODULE_9__.getTimeStringOnly)()))));
            }
        }
        return messages;
    };
    // let socket;
    // const roomid =
    //   'f0e86118-f95c-4e46-8103-c8b24aa092e0-f0e86118-f95c-4e46-8103-c8b24aa092e0';
    //const username = '데모학생2';
    const chatStart = () => {
        if (socket) {
            // 다른 강의를 선택할 수도 있지만, 한 번에 수강가능한 라이브 강의 1개 이므로 상관 없을 듯.
            // 다른 강의도 들을 수 있게 하려면, lessonid가 바뀔때 체크해야 할 듯.
            return;
        }
        const _socket = (0,socket_io_client__WEBPACK_IMPORTED_MODULE_5__.io)(_config_config__WEBPACK_IMPORTED_MODULE_7__.config.chat, { transports: ["websocket"] });
        _socket.on("connect", () => {
            _socket.emit("room:join", {
                roomid: roomId,
                username: name,
            });
        });
        _socket.on("server:message", (data) => {
            setChatMessages((prev) => [
                ...prev,
                {
                    type: "info",
                    content: dompurify__WEBPACK_IMPORTED_MODULE_6___default().sanitize(data.message),
                },
            ]);
            // if (codereet.userCount !== undefined && data.count !== undefined) {
            //   codereet.userCount = Number(data.count);
            // }
        });
        _socket.on("chat:message", (data) => {
            setChatMessages((prev) => [
                ...prev,
                {
                    type: "received",
                    from: data.username,
                    content: dompurify__WEBPACK_IMPORTED_MODULE_6___default().sanitize(data.message),
                },
            ]);
        });
        setSocket(_socket);
    };
    const sendMessage = () => {
        const message = document.getElementById("message");
        if (message && message.value) {
            const chatMessage = dompurify__WEBPACK_IMPORTED_MODULE_6___default().sanitize(message.value);
            socket.emit("chat:message", {
                roomid: roomId,
                username: name,
                obj: {},
                message: chatMessage,
            });
            message.value = "";
            setChatMessages((prev) => [
                ...prev,
                {
                    type: "sent",
                    content: dompurify__WEBPACK_IMPORTED_MODULE_6___default().sanitize(chatMessage),
                },
            ]);
        }
    };
    const handleKeyPress = (e) => {
        if (e.key === "Enter") {
            e.preventDefault();
            sendMessage();
        }
    };
    const scrollToBottom = () => {
        if (chatListRef.current) {
            chatListRef.current.scrollTop = chatListRef.current.scrollHeight;
        }
        // 이걸 ref로 바꿔서 한번 테스트 해보자....
        // const chatList = document.getElementById('chatList');
        // if (chatList) {
        //   chatList.scrollTop = chatList.scrollHeight;
        // }
    };
    const handleDownload = async (fileUrl) => {
        try {
            if (!fileUrl.includes("___")) {
                return;
            }
            const filename = fileUrl.split("___")[1];
            const response = await axios__WEBPACK_IMPORTED_MODULE_1___default()({
                url: `${_config_config__WEBPACK_IMPORTED_MODULE_7__.config.baseUrl}Files/GetFile`,
                method: "POST",
                responseType: "blob",
                data: {
                    fileUrl: encodeURIComponent(fileUrl),
                },
                headers: {
                    Authorization: `Bearer ${getToken()}`,
                },
            });
            const url = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement("a");
            link.href = url;
            link.target = "_blank";
            link.setAttribute("download", filename);
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }
        catch (err) {
            console.log(err);
        }
    };
    return (react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { style: { height: "100%" } },
        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("link", { href: "https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css", rel: "stylesheet" }),
        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("link", { rel: "stylesheet", href: "//cdn.jsdelivr.net/npm/@mdi/font@6.5.95/css/materialdesignicons.min.css" }),
        !loggedIn && (react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", null,
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_hooks_useLogin__WEBPACK_IMPORTED_MODULE_10__["default"], { onLoggedIn: onLoggedIn }))),
        loggedIn && (react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { style: { height: "100%" } },
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_hooks_useHeader__WEBPACK_IMPORTED_MODULE_11__["default"], { lectureDrawerVisible: lectureDrawerVisible, setIsOpen: setIsLectureListOpen, getUser: getUser, lecture: currentLecture, lessons: currentLectureLessons, handleBackToLectureList: handleBackToLectureList }),
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: "top-menu" }, currentLectureLessons && (react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_hooks_useLectureDrawer__WEBPACK_IMPORTED_MODULE_12__["default"], { isOpen: isLectureListOpen, setIsOpen: setIsLectureListOpen },
                react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_hooks_useLessonList__WEBPACK_IMPORTED_MODULE_13__["default"], { weeks: currentLectureLessons, onLessonSelected: onLessonSelected })))),
            !currentCategory && (react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_hooks_useCategorySelect__WEBPACK_IMPORTED_MODULE_14__["default"], { onCategorySelected: onCategorySelected })),
            currentCategory === _types_category__WEBPACK_IMPORTED_MODULE_15__["default"].Lecture && (react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: `split split-lesson lesson-container-full mx-5 overflow-auto ${lessonSelected ? "" : "overflow-y-auto overflow-x-hidden"}` },
                lessonSelected ? (react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: "lesson-panel h-full" },
                    react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { id: "lesson-container", className: "w-full max-w-4xl lesson-h-full flex-col" },
                        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { id: "lesson-video", className: "flex-1" },
                            videoFile && !lesson.extLiveStreamUrl && (react__WEBPACK_IMPORTED_MODULE_2___default().createElement(react_azure_mp__WEBPACK_IMPORTED_MODULE_3__.AzureMP, { skin: "amp-flush", src: ampSource })),
                            (videoLink || (lesson.extLiveStreamUrl && videoUrl)) && (react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_hooks_useVideoJS__WEBPACK_IMPORTED_MODULE_16__.VideoJS, { options: videoJsOptions, onReady: handlePlayerReady }))),
                        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { id: "lesson-split", className: "my-5 flex-none flex justify-between" },
                            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: "left" },
                                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("select", { className: "select-box light border-b", onChange: handleDescriptionModeChanged },
                                    react__WEBPACK_IMPORTED_MODULE_2___default().createElement("option", { value: "description" }, "\uAC15\uC758\uB0B4\uC6A9\uBCF4\uAE30"),
                                    pdfUrl && react__WEBPACK_IMPORTED_MODULE_2___default().createElement("option", { value: "pdf" }, "PDF \uBCF4\uAE30"))),
                            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: "right" }, notebookUrl && (react__WEBPACK_IMPORTED_MODULE_2___default().createElement("button", { className: "bg-green-600 hover:bg-green-700 text-white rounded px-4 py-1 disabled:bg-slate-50", onClick: async () => {
                                    handleDownload(notebookUrl);
                                } }, "\uB178\uD2B8\uBD81 \uB2E4\uC6B4\uB85C\uB4DC")))),
                        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { id: "lesson-content", className: "flex-1" },
                            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: "split split-description h-full" },
                                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("h1", null, lesson.title),
                                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { dangerouslySetInnerHTML: getSanitizedData(lesson.description) })),
                            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: "split split-pdf h-full hide" },
                                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("iframe", { className: "w-full h-full", 
                                    // style={{ width: '100%', height: '100%' }}
                                    src: pdfUrl, frameBorder: "0", allowFullScreen: true, onLoad: () => {
                                        document.getElementById("lesson-content").style.height = `${document.getElementById("lesson-container")
                                            .clientHeight -
                                            document.getElementById("lesson-video")
                                                .clientHeight -
                                            document.getElementById("lesson-split")
                                                .clientHeight +
                                            20}px`;
                                    } })))))) : (react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_hooks_useLectureList__WEBPACK_IMPORTED_MODULE_17__["default"], { getToken: getToken, onLectureSelected: onLectureSelected, onLessonSelected: onLessonSelected, onLessonLoaded: onLessonLoaded, onResetCategory: onResetCategory })),
                lessonSelected && lesson.extLiveStreamUrl && (react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: "chat-panel hide" },
                    react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: "chat-member hide" },
                        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: "tit" },
                            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("i", { className: "mdi mdi-school" }),
                            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("span", null, "\uCC38\uC5EC \uC778\uC6D0")),
                        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("ul", { className: "member-list" },
                            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("li", { className: "member-item" },
                                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("img", { src: "", alt: "" }),
                                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("span", { className: "name" }, "\uD559\uC0DD1")),
                            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("li", { className: "member-item" },
                                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("img", { src: "", alt: "" }),
                                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("span", { className: "name" }, "\uD559\uC0DD2")),
                            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("li", { className: "member-item" },
                                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("img", { src: "", alt: "" }),
                                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("span", { className: "name" }, "\uD559\uC0DD3")))),
                    react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: "chat-wrap" },
                        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { ref: chatListRef, className: "msg-box" },
                            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: "chat" },
                                react__WEBPACK_IMPORTED_MODULE_2___default().createElement("ul", null, renderChatMessages(chatMessages)))),
                        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: "send-box" },
                            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("textarea", { id: "message", className: "text-form", placeholder: "\uBA54\uC138\uC9C0\uB97C \uC785\uB825\uD574 \uC8FC\uC138\uC694", onKeyPress: handleKeyPress }),
                            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("button", { id: "sendButton", className: "send-btn", onClick: () => {
                                    sendMessage();
                                } }))))))),
            currentCategory === _types_category__WEBPACK_IMPORTED_MODULE_15__["default"].AIHackathon && (react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_hooks_useHackathonList__WEBPACK_IMPORTED_MODULE_18__["default"], { getToken: getToken, onResetCategory: onResetCategory }))))));
};
/**
 * A Counter Lumino Widget that wraps a CounterComponent.
 */
class ModuCodingWidget extends _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ReactWidget {
    /**
     * Constructs a new CounterWidget.
     */
    constructor() {
        super();
        //this.addClass('add-scroll');
        //this.addClass('jp-ReactWidget');
    }
    render() {
        return react__WEBPACK_IMPORTED_MODULE_2___default().createElement(ModuCodingComponent, null);
    }
}


/***/ }),

/***/ "./node_modules/css-loader/dist/cjs.js!./style/lecture-detail.css":
/*!************************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js!./style/lecture-detail.css ***!
  \************************************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/cssWithMappingToString.js */ "./node_modules/css-loader/dist/runtime/cssWithMappingToString.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/api.js */ "./node_modules/css-loader/dist/runtime/api.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/getUrl.js */ "./node_modules/css-loader/dist/runtime/getUrl.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _images_photoDefault_png__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../images/photoDefault.png */ "./images/photoDefault.png");
/* harmony import */ var _images_sendBtn_png__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../images/sendBtn.png */ "./images/sendBtn.png");
// Imports





var ___CSS_LOADER_EXPORT___ = _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default()((_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default()));
var ___CSS_LOADER_URL_REPLACEMENT_0___ = _node_modules_css_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_2___default()(_images_photoDefault_png__WEBPACK_IMPORTED_MODULE_3__["default"]);
var ___CSS_LOADER_URL_REPLACEMENT_1___ = _node_modules_css_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_2___default()(_images_sendBtn_png__WEBPACK_IMPORTED_MODULE_4__["default"]);
// Module
___CSS_LOADER_EXPORT___.push([module.id, "/* html,\nbody,\ndiv,\ndl,\ndt,\ndd,\nul,\nol,\nli,\nh1,\nh2,\nh3,\nh4,\nh5,\nh6,\nform,\nfieldset,\np,\nbutton {\n  margin: 0;\n  padding: 0;\n} */\nol,\nli {\n  list-style: none;\n} /*목록에 점 없애기*/\n\n/* common */\n.hide {\n  display: none !important;\n}\n.split-top {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n  width: 100%;\n  margin: 10px 0;\n}\n.select-box {\n  min-width: 142px;\n  padding: 6px 30px 6px 6px;\n  font-size: 14px;\n  line-height: 23px;\n  border-color: #ccc;\n  /* background: url(../img/arrow-down.svg) no-repeat right 11px center; */\n  outline: none;\n  /* appearance: none; */\n}\n.color-mint{\n  color: #19bec9 !important;\n}\n\n/***** 영상 강의화면 레이아웃 *****/\n.lesson-view {\n  padding-top: 30px;\n}\n.top-menu {\n  display: flex;\n  justify-content: space-between;\n  padding: 0 30px 20px;\n}\n.top-menu .btn {\n  border: 1px solid #ccc;\n  background: #fff;\n  border-radius: 0;\n  font-size: 14px;\n}\n.top-menu .btn:hover {\n  border-color: #b4b4b4;\n}\n.top-menu .close-btn {\n  display: none;\n}\n.top-menu .list-btn {\n  width: 50px;\n  height: 50px;\n  border: 1px solid #ccc;\n  background: #fff;\n  border-radius: 0;\n}\n.top-menu .list-btn i {\n  font-size: 24px;\n}\n\n.container-h-full {\n  height: calc(100% - 70px);\n}\n\n.lesson-container-full {\n  height: calc(100% - 81px);\n}\n\n.lesson-container-full .container button{\n  border: 1px solid #bec2cf;\n}\n\n.lesson-container-full .container .card:hover{\n  background-color: #19bec9;\n}\n\n.lesson-container-full .container .card:hover span{\n  color:#fff\n}\n\n.lesson-h-full {\n  height: calc(100% - 70px);\n  max-height: calc(100% - 70px);\n}\n\n.lesson-wrap {\n  position: relative;\n  /* display: flex;\n  align-items: flex-start; */\n  height: calc(100% - 70px);\n  overflow-y: hidden;\n}\n\n/* 강의 목록 */\n.lesson-wrap .lesson-list {\n  flex: 1;\n  padding: 0 30px;\n  height: 100%;\n  overflow-y: auto;\n  overflow-x: hidden;\n}\n.lesson-wrap .lesson-list .wrapper {\n  width: auto;\n}\n.lesson-wrap .lesson-list .wrapper .btn {\n  margin-left: auto;\n  margin-right: 20px;\n}\n\n/* 강의 내용 */\n.lesson-wrap .lesson-panel {\n  flex: 1;\n  height: 100%;\n  padding: 0 30px;\n  /* overflow: hidden; */\n  display: flex;\n  flex-direction: column;\n}\n.lesson-wrap .lesson-panel .btn {\n  padding: 0 10px;\n  line-height: 30px;\n  font-size: 12px;\n  border: 1px solid #dfdfdf;\n  border-radius: 0;\n}\n.lesson-wrap .lesson-panel .split-wrap {\n  overflow-y: hidden;\n}\n.lesson-wrap .lesson-panel .split {\n  width: 100%;\n  /* height: 100%; */\n  height: calc(100% - 66px);\n  box-sizing: border-box;\n  overflow-y: auto;\n  overflow-x: hidden;\n  padding: 30px 0;\n}\n.lesson-wrap .lesson-panel .split h1 {\n  padding-bottom: 15px;\n}\n\n/* 채팅창 */\n.chat-panel {\n  display: flex;\n  /* flex-direction: column; */\n  min-width: 250px;\n  max-width: 18%;\n  height: calc(100% - 50px);\n}\n.chat-member {\n  width: 100%;\n  height: 30%;\n  background: #fff;\n}\n.chat-member .tit {\n  padding: 12px 10px;\n  border-bottom: 1px solid #dfdfdf;\n}\n.chat-member .member-list {\n  height: calc(100% - 43px);\n  padding: 10px 20px;\n}\n.chat-member .member-list .member-item {\n  margin-top: 5px;\n}\n.chat-member .member-list .member-item img {\n  width: 20px;\n  height: 20px;\n  margin-right: 5px;\n  border: 1px solid #dfdfdf;\n  border-radius: 50%;\n  box-sizing: border-box;\n  display: inline-block;\n  vertical-align: middle;\n  overflow: hidden;\n}\n.chat-member .member-list .member-item .name {\n  font-size: 14px;\n  color: #666;\n  font-weight: 400;\n  display: inline-block;\n  vertical-align: middle;\n  line-height: 30px;\n}\n.chat-wrap {\n  position: relative;\n  width: 100%;\n  height: 100%;\n  background: #e1f1fc;\n}\n.chat-wrap .msg-box {\n  width: 100%;\n  height: 100%;\n  padding: 30px 15px;\n  box-sizing: border-box;\n  overflow-y: auto;\n  overflow-x: hidden;\n}\n.chat-wrap .msg-box .msg-list {\n  width: 100%;\n  margin-bottom: 15px;\n}\n.chat-wrap .msg-box .msg-list p {\n  margin: 5px 0;\n  text-align: center;\n}\n.chat-wrap .msg-box .msg-list .msg-item {\n  position: relative;\n  display: flex;\n  align-items: end;\n}\n.chat-wrap .msg-box .msg-list .msg-item .tag {\n  position: absolute;\n  top: 5px;\n  height: 0;\n  border-style: solid;\n  border-width: 5px;\n  border-color: #bce3ff transparent transparent #bce3ff;\n  border-radius: 3px;\n}\n.chat-wrap .msg-box .msg-list .msg-item .text-msg {\n  padding: 6px 8px;\n  width: 80%;\n  line-height: 25px;\n  font-size: 14px;\n  border-radius: 5px;\n  overflow-wrap: break-word;\n  background: #bce3ff;\n}\n.chat-wrap .msg-box .msg-list .msg-item .date {\n  font-size: 12px;\n  color: #000;\n  margin: 0 5px;\n  font-weight: bold;\n}\n/* 보내는 메세지 */\n.chat-wrap .msg-box .msg-send .msg-item {\n  flex-direction: row-reverse;\n  margin-left: 5px;\n}\n.chat-wrap .msg-box .msg-send .msg-item .tag {\n  right: -9px;\n}\n/* 받는 메세지 */\n.chat-wrap .msg-box .msg-receive .msg-info {\n  display: flex;\n  margin-bottom: 4px;\n  font-weight: bold;\n}\n.chat-wrap .msg-box .msg-receive .msg-info .user-img {\n  width: 30px;\n  height: 30px;\n  margin-right: 5px;\n  border-radius: 50%;\n  border: 1px solid #e2e2e2;\n  background: url(" + ___CSS_LOADER_URL_REPLACEMENT_0___ + ") no-repeat;\n  background-size: 26px;\n}\n.chat-wrap .msg-box .msg-receive .msg-info p {\n  font-size: 14px;\n}\n.chat-wrap .msg-box .msg-receive .msg-info span {\n  font-size: 10px;\n  color: #2eaef8;\n}\n.chat-wrap .msg-box .msg-receive .msg-item {\n  flex-direction: row;\n  margin-left: 20px;\n}\n.chat-wrap .msg-box .msg-receive .msg-item .tag {\n  left: -9px;\n  border-color: #fff #fff transparent transparent;\n}\n.chat-wrap .msg-box .msg-receive .msg-item .text-msg {\n  background: #fff;\n}\n/* 메세지 전송 */\n.chat-wrap .send-box {\n  width: 100%;\n  height: 50px;\n  position: relative;\n  border-radius: 4px;\n  background: #fff;\n  border-left: 1px solid #efefef;\n}\n.chat-wrap .send-box .text-form {\n  float: left;\n  padding: 10px;\n  width: calc(100% - 50px);\n  height: 50px;\n  color: #666;\n  border: 0;\n  resize: none;\n  outline: none;\n}\n.chat-wrap .send-box .send-btn {\n  width: 50px;\n  height: 50px;\n  border: 0;\n  cursor: pointer;\n  outline: none;\n}\n.chat-wrap .send-box .send-btn::after {\n  content: ' ';\n  display: block;\n  width: 100%;\n  height: 100%;\n  background: url(" + ___CSS_LOADER_URL_REPLACEMENT_1___ + ") no-repeat;\n}\n.chat-wrap .send-box .send-btn:hover::after {\n  background-color: #f2f2f2;\n}\n\n/*-----------------세부 강의 표시---------------*/\n.weekly_plan {\n  width: 100%;\n  position: relative;\n}\n.weekly_plan .weekly_plan_box {\n  width: 100%;\n  overflow: hidden;\n  margin-bottom: 30px;\n  position: relative;\n}\n.weekly_plan .weekly_plan_box > div {\n  float: left;\n}\n.weekly_plan .weekly_plan_box > .left_week {\n  width: 92px;\n}\n.weekly_plan .weekly_plan_box > .left_week p.circle {\n  width: 60px;\n  height: 60px;\n  background: #f9fafb;\n  border: 1px solid #eaeaea;\n  border-radius: 50%;\n  box-sizing: border-box;\n  text-align: center;\n  font-size: 12px;\n  color: #898989;\n  font-weight: 400;\n  position: relative;\n  z-index: 2;\n}\n.weekly_plan .weekly_plan_box > .left_week p.circle span {\n  display: block;\n  text-align: center;\n  width: 100%;\n  font-size: 23px;\n  color: #333;\n  font-weight: 500;\n  margin-top: 15px;\n  margin-bottom: 5px;\n}\n.weekly_plan .weekly_plan_box > .left_week span.dash_line {\n  position: absolute;\n  z-index: 1;\n  display: block;\n  width: 92px;\n  border-top: 1px dashed #dfdfdf;\n  top: 30px;\n  left: 0;\n}\n.weekly_plan .weekly_plan_box > .right_plan {\n  width: calc(100% - 92px);\n  border-left: 1px dashed #dfdfdf;\n  padding-left: 20px;\n  box-sizing: border-box;\n}\n.weekly_plan .weekly_plan_box > .right_plan > p.plan_tit {\n  font-size: 17px;\n  color: #333;\n  font-weight: 400;\n  margin-bottom: 5px;\n}\n.weekly_plan .weekly_plan_box > .right_plan > .plan_accordion {\n  width: 100%;\n  position: relative;\n}\n/*테스트용 강좌 테스트 목록 부분*/\n.weekly_plan .test_class_tit {\n  font-size: 23px;\n  line-height: 57px;\n  background: #fff;\n  width: 50px;\n  position: relative;\n  z-index: 2;\n}\n.weekly_plan .right_plan ul.test_list {\n  width: 100%;\n  display: block;\n  position: relative;\n}\n.weekly_plan .right_plan ul.test_list li {\n  width: 100%;\n  border-bottom: 1px solid #f4f4f4;\n  line-height: 50px;\n  overflow: hidden;\n}\n.weekly_plan .right_plan ul.test_list li a {\n  float: left;\n  width: 80%;\n  height: 100%;\n}\n.weekly_plan .right_plan ul.test_list li a span.order_number {\n  font-size: 15px;\n  color: #333;\n  font-weight: 400;\n  display: inline-block;\n  vertical-align: middle;\n}\n.weekly_plan .right_plan ul.test_list li a span.order_number b {\n  font-weight: 400 !important;\n}\n.weekly_plan .right_plan ul.test_list li a span.test_exam_tit {\n  width: 95%;\n  display: inline-block;\n  vertical-align: middle;\n  overflow: hidden;\n  text-overflow: ellipsis;\n  white-space: nowrap;\n  box-sizing: border-box;\n  font-size: 15px;\n  color: #333;\n  font-weight: 400;\n}\n.weekly_plan .right_plan ul.test_list li button {\n  float: right;\n  padding: 0 10px;\n  line-height: 30px;\n  font-size: 12px;\n  margin-right: 30px;\n  border: 1px solid #dfdfdf;\n  margin-top: 14px;\n  color: #ea302e;\n}\n.weekly_plan .right_plan ul.test_list li button:hover {\n  border: 1px solid #b4b4b4;\n  color: #333;\n}\n.weekly_plan .right_plan ul.test_list li button.passed_exam {\n  border: 1px solid #dfdfdf !important;\n  border-radius: 4px;\n  box-sizing: border-box;\n  color: #666;\n}\n\n.plan_accordion > ul > li {\n  width: 100%;\n  position: relative;\n  margin-bottom: 15px;\n}\n.plan_accordion > ul > li:last-of-type {\n  margin-bottom: 0;\n}\n.plan_accordion ul li > a.acc_btn {\n  display: block;\n  width: 100%;\n  border: 1px solid #eaeaea;\n  background: #f9fafb;\n  line-height: 50px;\n  padding-left: 25px;\n  box-sizing: border-box;\n  overflow: hidden;\n}\n.plan_accordion ul li > a.acc_btn span.nth {\n  display: inline-block;\n  vertical-align: middle;\n  margin-right: 50px;\n  font-size: 15px;\n  color: #333;\n  font-weight: 400;\n}\n.plan_accordion ul li > a.acc_btn p.nth_tit {\n  display: inline-block;\n  vertical-align: middle;\n  font-size: 15px;\n  color: #333;\n  font-weight: 400;\n}\n.plan_accordion ul li > a.acc_btn span.arrow {\n  float: right;\n  margin-right: 20px;\n  color: #898989 !important;\n  transition: all 0.4s;\n  transform: rotate(0deg);\n}\n.plan_accordion ul li > a.acc_btn:hover span.arrow {\n  color: #333 !important;\n}\n.plan_accordion ul li > a.acc_btn.open_acc span.arrow {\n  transform: rotate(180deg);\n}\n.plan_accordion ul li > div ul {\n  margin-left: 20px;\n}\n.plan_accordion ul li > div ul li {\n  width: 100%;\n  border-bottom: 1px solid #f4f4f4;\n  position: relative;\n  height: 60px;\n  overflow: hidden;\n}\n.plan_accordion ul li > div ul li span.depth {\n  position: absolute;\n  width: 20px;\n  height: 20px;\n  border-left: 1px solid #dfdfdf;\n  border-bottom: 1px solid #dfdfdf;\n  top: 15px;\n  left: 0;\n}\n.plan_accordion ul li > div ul li span.coding_include {\n  position: absolute;\n  color: #2eaef8;\n  font-size: 12px;\n  font-weight: 400;\n  left: 30px;\n  bottom: 7px;\n}\n.plan_accordion ul li > div ul li > p {\n  font-size: 14px;\n  color: #666;\n  font-weight: 400;\n  padding-left: 30px;\n  line-height: 65px;\n  float: left;\n}\n.plan_accordion ul li > div ul li div.right_part {\n  float: right;\n  margin-right: 20px;\n  height: 60px;\n}\n.plan_accordion ul li > div ul li div.right_part button {\n  padding: 0 10px;\n  line-height: 30px;\n  font-size: 12px; /*margin-right:30px;*/\n  border: 1px solid #dfdfdf;\n  margin-top: 14px;\n}\n.plan_accordion ul li > div ul li div.right_part button:hover {\n  border: 1px solid #b4b4b4;\n  color: #333;\n}\n.plan_accordion ul li > div ul li div.right_part span.video_length {\n  color: #898989 !important;\n  line-height: 60px;\n}\n.plan_accordion #appendAssignment #assignment1 p {\n  font-size: 15px;\n  color: #333;\n  font-weight: 400;\n  line-height: 22px;\n}\n\n/*--------------------AMP 스타일--------------------*/\n.amp-controlbaricons-middle {\n  margin-left: 30px;\n}\n.vjs-progress-control.vjs-control.outline-enabled-control {\n  width: 100px;\n}\n\n\n/* 해커톤 카드 리스트 */\n.hackathon-card:first-child{\n  border-top:2px solid #e5e7eb;\n}", "",{"version":3,"sources":["webpack://./style/lecture-detail.css"],"names":[],"mappings":"AAAA;;;;;;;;;;;;;;;;;;;;;GAqBG;AACH;;EAEE,gBAAgB;AAClB,EAAE,YAAY;;AAEd,WAAW;AACX;EACE,wBAAwB;AAC1B;AACA;EACE,aAAa;EACb,8BAA8B;EAC9B,mBAAmB;EACnB,WAAW;EACX,cAAc;AAChB;AACA;EACE,gBAAgB;EAChB,yBAAyB;EACzB,eAAe;EACf,iBAAiB;EACjB,kBAAkB;EAClB,wEAAwE;EACxE,aAAa;EACb,sBAAsB;AACxB;AACA;EACE,yBAAyB;AAC3B;;AAEA,yBAAyB;AACzB;EACE,iBAAiB;AACnB;AACA;EACE,aAAa;EACb,8BAA8B;EAC9B,oBAAoB;AACtB;AACA;EACE,sBAAsB;EACtB,gBAAgB;EAChB,gBAAgB;EAChB,eAAe;AACjB;AACA;EACE,qBAAqB;AACvB;AACA;EACE,aAAa;AACf;AACA;EACE,WAAW;EACX,YAAY;EACZ,sBAAsB;EACtB,gBAAgB;EAChB,gBAAgB;AAClB;AACA;EACE,eAAe;AACjB;;AAEA;EACE,yBAAyB;AAC3B;;AAEA;EACE,yBAAyB;AAC3B;;AAEA;EACE,yBAAyB;AAC3B;;AAEA;EACE,yBAAyB;AAC3B;;AAEA;EACE;AACF;;AAEA;EACE,yBAAyB;EACzB,6BAA6B;AAC/B;;AAEA;EACE,kBAAkB;EAClB;4BAC0B;EAC1B,yBAAyB;EACzB,kBAAkB;AACpB;;AAEA,UAAU;AACV;EACE,OAAO;EACP,eAAe;EACf,YAAY;EACZ,gBAAgB;EAChB,kBAAkB;AACpB;AACA;EACE,WAAW;AACb;AACA;EACE,iBAAiB;EACjB,kBAAkB;AACpB;;AAEA,UAAU;AACV;EACE,OAAO;EACP,YAAY;EACZ,eAAe;EACf,sBAAsB;EACtB,aAAa;EACb,sBAAsB;AACxB;AACA;EACE,eAAe;EACf,iBAAiB;EACjB,eAAe;EACf,yBAAyB;EACzB,gBAAgB;AAClB;AACA;EACE,kBAAkB;AACpB;AACA;EACE,WAAW;EACX,kBAAkB;EAClB,yBAAyB;EACzB,sBAAsB;EACtB,gBAAgB;EAChB,kBAAkB;EAClB,eAAe;AACjB;AACA;EACE,oBAAoB;AACtB;;AAEA,QAAQ;AACR;EACE,aAAa;EACb,4BAA4B;EAC5B,gBAAgB;EAChB,cAAc;EACd,yBAAyB;AAC3B;AACA;EACE,WAAW;EACX,WAAW;EACX,gBAAgB;AAClB;AACA;EACE,kBAAkB;EAClB,gCAAgC;AAClC;AACA;EACE,yBAAyB;EACzB,kBAAkB;AACpB;AACA;EACE,eAAe;AACjB;AACA;EACE,WAAW;EACX,YAAY;EACZ,iBAAiB;EACjB,yBAAyB;EACzB,kBAAkB;EAClB,sBAAsB;EACtB,qBAAqB;EACrB,sBAAsB;EACtB,gBAAgB;AAClB;AACA;EACE,eAAe;EACf,WAAW;EACX,gBAAgB;EAChB,qBAAqB;EACrB,sBAAsB;EACtB,iBAAiB;AACnB;AACA;EACE,kBAAkB;EAClB,WAAW;EACX,YAAY;EACZ,mBAAmB;AACrB;AACA;EACE,WAAW;EACX,YAAY;EACZ,kBAAkB;EAClB,sBAAsB;EACtB,gBAAgB;EAChB,kBAAkB;AACpB;AACA;EACE,WAAW;EACX,mBAAmB;AACrB;AACA;EACE,aAAa;EACb,kBAAkB;AACpB;AACA;EACE,kBAAkB;EAClB,aAAa;EACb,gBAAgB;AAClB;AACA;EACE,kBAAkB;EAClB,QAAQ;EACR,SAAS;EACT,mBAAmB;EACnB,iBAAiB;EACjB,qDAAqD;EACrD,kBAAkB;AACpB;AACA;EACE,gBAAgB;EAChB,UAAU;EACV,iBAAiB;EACjB,eAAe;EACf,kBAAkB;EAClB,yBAAyB;EACzB,mBAAmB;AACrB;AACA;EACE,eAAe;EACf,WAAW;EACX,aAAa;EACb,iBAAiB;AACnB;AACA,YAAY;AACZ;EACE,2BAA2B;EAC3B,gBAAgB;AAClB;AACA;EACE,WAAW;AACb;AACA,WAAW;AACX;EACE,aAAa;EACb,kBAAkB;EAClB,iBAAiB;AACnB;AACA;EACE,WAAW;EACX,YAAY;EACZ,iBAAiB;EACjB,kBAAkB;EAClB,yBAAyB;EACzB,6DAAqD;EACrD,qBAAqB;AACvB;AACA;EACE,eAAe;AACjB;AACA;EACE,eAAe;EACf,cAAc;AAChB;AACA;EACE,mBAAmB;EACnB,iBAAiB;AACnB;AACA;EACE,UAAU;EACV,+CAA+C;AACjD;AACA;EACE,gBAAgB;AAClB;AACA,WAAW;AACX;EACE,WAAW;EACX,YAAY;EACZ,kBAAkB;EAClB,kBAAkB;EAClB,gBAAgB;EAChB,8BAA8B;AAChC;AACA;EACE,WAAW;EACX,aAAa;EACb,wBAAwB;EACxB,YAAY;EACZ,WAAW;EACX,SAAS;EACT,YAAY;EACZ,aAAa;AACf;AACA;EACE,WAAW;EACX,YAAY;EACZ,SAAS;EACT,eAAe;EACf,aAAa;AACf;AACA;EACE,YAAY;EACZ,cAAc;EACd,WAAW;EACX,YAAY;EACZ,6DAAgD;AAClD;AACA;EACE,yBAAyB;AAC3B;;AAEA,2CAA2C;AAC3C;EACE,WAAW;EACX,kBAAkB;AACpB;AACA;EACE,WAAW;EACX,gBAAgB;EAChB,mBAAmB;EACnB,kBAAkB;AACpB;AACA;EACE,WAAW;AACb;AACA;EACE,WAAW;AACb;AACA;EACE,WAAW;EACX,YAAY;EACZ,mBAAmB;EACnB,yBAAyB;EACzB,kBAAkB;EAClB,sBAAsB;EACtB,kBAAkB;EAClB,eAAe;EACf,cAAc;EACd,gBAAgB;EAChB,kBAAkB;EAClB,UAAU;AACZ;AACA;EACE,cAAc;EACd,kBAAkB;EAClB,WAAW;EACX,eAAe;EACf,WAAW;EACX,gBAAgB;EAChB,gBAAgB;EAChB,kBAAkB;AACpB;AACA;EACE,kBAAkB;EAClB,UAAU;EACV,cAAc;EACd,WAAW;EACX,8BAA8B;EAC9B,SAAS;EACT,OAAO;AACT;AACA;EACE,wBAAwB;EACxB,+BAA+B;EAC/B,kBAAkB;EAClB,sBAAsB;AACxB;AACA;EACE,eAAe;EACf,WAAW;EACX,gBAAgB;EAChB,kBAAkB;AACpB;AACA;EACE,WAAW;EACX,kBAAkB;AACpB;AACA,oBAAoB;AACpB;EACE,eAAe;EACf,iBAAiB;EACjB,gBAAgB;EAChB,WAAW;EACX,kBAAkB;EAClB,UAAU;AACZ;AACA;EACE,WAAW;EACX,cAAc;EACd,kBAAkB;AACpB;AACA;EACE,WAAW;EACX,gCAAgC;EAChC,iBAAiB;EACjB,gBAAgB;AAClB;AACA;EACE,WAAW;EACX,UAAU;EACV,YAAY;AACd;AACA;EACE,eAAe;EACf,WAAW;EACX,gBAAgB;EAChB,qBAAqB;EACrB,sBAAsB;AACxB;AACA;EACE,2BAA2B;AAC7B;AACA;EACE,UAAU;EACV,qBAAqB;EACrB,sBAAsB;EACtB,gBAAgB;EAChB,uBAAuB;EACvB,mBAAmB;EACnB,sBAAsB;EACtB,eAAe;EACf,WAAW;EACX,gBAAgB;AAClB;AACA;EACE,YAAY;EACZ,eAAe;EACf,iBAAiB;EACjB,eAAe;EACf,kBAAkB;EAClB,yBAAyB;EACzB,gBAAgB;EAChB,cAAc;AAChB;AACA;EACE,yBAAyB;EACzB,WAAW;AACb;AACA;EACE,oCAAoC;EACpC,kBAAkB;EAClB,sBAAsB;EACtB,WAAW;AACb;;AAEA;EACE,WAAW;EACX,kBAAkB;EAClB,mBAAmB;AACrB;AACA;EACE,gBAAgB;AAClB;AACA;EACE,cAAc;EACd,WAAW;EACX,yBAAyB;EACzB,mBAAmB;EACnB,iBAAiB;EACjB,kBAAkB;EAClB,sBAAsB;EACtB,gBAAgB;AAClB;AACA;EACE,qBAAqB;EACrB,sBAAsB;EACtB,kBAAkB;EAClB,eAAe;EACf,WAAW;EACX,gBAAgB;AAClB;AACA;EACE,qBAAqB;EACrB,sBAAsB;EACtB,eAAe;EACf,WAAW;EACX,gBAAgB;AAClB;AACA;EACE,YAAY;EACZ,kBAAkB;EAClB,yBAAyB;EACzB,oBAAoB;EACpB,uBAAuB;AACzB;AACA;EACE,sBAAsB;AACxB;AACA;EACE,yBAAyB;AAC3B;AACA;EACE,iBAAiB;AACnB;AACA;EACE,WAAW;EACX,gCAAgC;EAChC,kBAAkB;EAClB,YAAY;EACZ,gBAAgB;AAClB;AACA;EACE,kBAAkB;EAClB,WAAW;EACX,YAAY;EACZ,8BAA8B;EAC9B,gCAAgC;EAChC,SAAS;EACT,OAAO;AACT;AACA;EACE,kBAAkB;EAClB,cAAc;EACd,eAAe;EACf,gBAAgB;EAChB,UAAU;EACV,WAAW;AACb;AACA;EACE,eAAe;EACf,WAAW;EACX,gBAAgB;EAChB,kBAAkB;EAClB,iBAAiB;EACjB,WAAW;AACb;AACA;EACE,YAAY;EACZ,kBAAkB;EAClB,YAAY;AACd;AACA;EACE,eAAe;EACf,iBAAiB;EACjB,eAAe,EAAE,qBAAqB;EACtC,yBAAyB;EACzB,gBAAgB;AAClB;AACA;EACE,yBAAyB;EACzB,WAAW;AACb;AACA;EACE,yBAAyB;EACzB,iBAAiB;AACnB;AACA;EACE,eAAe;EACf,WAAW;EACX,gBAAgB;EAChB,iBAAiB;AACnB;;AAEA,kDAAkD;AAClD;EACE,iBAAiB;AACnB;AACA;EACE,YAAY;AACd;;;AAGA,eAAe;AACf;EACE,4BAA4B;AAC9B","sourcesContent":["/* html,\nbody,\ndiv,\ndl,\ndt,\ndd,\nul,\nol,\nli,\nh1,\nh2,\nh3,\nh4,\nh5,\nh6,\nform,\nfieldset,\np,\nbutton {\n  margin: 0;\n  padding: 0;\n} */\nol,\nli {\n  list-style: none;\n} /*목록에 점 없애기*/\n\n/* common */\n.hide {\n  display: none !important;\n}\n.split-top {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n  width: 100%;\n  margin: 10px 0;\n}\n.select-box {\n  min-width: 142px;\n  padding: 6px 30px 6px 6px;\n  font-size: 14px;\n  line-height: 23px;\n  border-color: #ccc;\n  /* background: url(../img/arrow-down.svg) no-repeat right 11px center; */\n  outline: none;\n  /* appearance: none; */\n}\n.color-mint{\n  color: #19bec9 !important;\n}\n\n/***** 영상 강의화면 레이아웃 *****/\n.lesson-view {\n  padding-top: 30px;\n}\n.top-menu {\n  display: flex;\n  justify-content: space-between;\n  padding: 0 30px 20px;\n}\n.top-menu .btn {\n  border: 1px solid #ccc;\n  background: #fff;\n  border-radius: 0;\n  font-size: 14px;\n}\n.top-menu .btn:hover {\n  border-color: #b4b4b4;\n}\n.top-menu .close-btn {\n  display: none;\n}\n.top-menu .list-btn {\n  width: 50px;\n  height: 50px;\n  border: 1px solid #ccc;\n  background: #fff;\n  border-radius: 0;\n}\n.top-menu .list-btn i {\n  font-size: 24px;\n}\n\n.container-h-full {\n  height: calc(100% - 70px);\n}\n\n.lesson-container-full {\n  height: calc(100% - 81px);\n}\n\n.lesson-container-full .container button{\n  border: 1px solid #bec2cf;\n}\n\n.lesson-container-full .container .card:hover{\n  background-color: #19bec9;\n}\n\n.lesson-container-full .container .card:hover span{\n  color:#fff\n}\n\n.lesson-h-full {\n  height: calc(100% - 70px);\n  max-height: calc(100% - 70px);\n}\n\n.lesson-wrap {\n  position: relative;\n  /* display: flex;\n  align-items: flex-start; */\n  height: calc(100% - 70px);\n  overflow-y: hidden;\n}\n\n/* 강의 목록 */\n.lesson-wrap .lesson-list {\n  flex: 1;\n  padding: 0 30px;\n  height: 100%;\n  overflow-y: auto;\n  overflow-x: hidden;\n}\n.lesson-wrap .lesson-list .wrapper {\n  width: auto;\n}\n.lesson-wrap .lesson-list .wrapper .btn {\n  margin-left: auto;\n  margin-right: 20px;\n}\n\n/* 강의 내용 */\n.lesson-wrap .lesson-panel {\n  flex: 1;\n  height: 100%;\n  padding: 0 30px;\n  /* overflow: hidden; */\n  display: flex;\n  flex-direction: column;\n}\n.lesson-wrap .lesson-panel .btn {\n  padding: 0 10px;\n  line-height: 30px;\n  font-size: 12px;\n  border: 1px solid #dfdfdf;\n  border-radius: 0;\n}\n.lesson-wrap .lesson-panel .split-wrap {\n  overflow-y: hidden;\n}\n.lesson-wrap .lesson-panel .split {\n  width: 100%;\n  /* height: 100%; */\n  height: calc(100% - 66px);\n  box-sizing: border-box;\n  overflow-y: auto;\n  overflow-x: hidden;\n  padding: 30px 0;\n}\n.lesson-wrap .lesson-panel .split h1 {\n  padding-bottom: 15px;\n}\n\n/* 채팅창 */\n.chat-panel {\n  display: flex;\n  /* flex-direction: column; */\n  min-width: 250px;\n  max-width: 18%;\n  height: calc(100% - 50px);\n}\n.chat-member {\n  width: 100%;\n  height: 30%;\n  background: #fff;\n}\n.chat-member .tit {\n  padding: 12px 10px;\n  border-bottom: 1px solid #dfdfdf;\n}\n.chat-member .member-list {\n  height: calc(100% - 43px);\n  padding: 10px 20px;\n}\n.chat-member .member-list .member-item {\n  margin-top: 5px;\n}\n.chat-member .member-list .member-item img {\n  width: 20px;\n  height: 20px;\n  margin-right: 5px;\n  border: 1px solid #dfdfdf;\n  border-radius: 50%;\n  box-sizing: border-box;\n  display: inline-block;\n  vertical-align: middle;\n  overflow: hidden;\n}\n.chat-member .member-list .member-item .name {\n  font-size: 14px;\n  color: #666;\n  font-weight: 400;\n  display: inline-block;\n  vertical-align: middle;\n  line-height: 30px;\n}\n.chat-wrap {\n  position: relative;\n  width: 100%;\n  height: 100%;\n  background: #e1f1fc;\n}\n.chat-wrap .msg-box {\n  width: 100%;\n  height: 100%;\n  padding: 30px 15px;\n  box-sizing: border-box;\n  overflow-y: auto;\n  overflow-x: hidden;\n}\n.chat-wrap .msg-box .msg-list {\n  width: 100%;\n  margin-bottom: 15px;\n}\n.chat-wrap .msg-box .msg-list p {\n  margin: 5px 0;\n  text-align: center;\n}\n.chat-wrap .msg-box .msg-list .msg-item {\n  position: relative;\n  display: flex;\n  align-items: end;\n}\n.chat-wrap .msg-box .msg-list .msg-item .tag {\n  position: absolute;\n  top: 5px;\n  height: 0;\n  border-style: solid;\n  border-width: 5px;\n  border-color: #bce3ff transparent transparent #bce3ff;\n  border-radius: 3px;\n}\n.chat-wrap .msg-box .msg-list .msg-item .text-msg {\n  padding: 6px 8px;\n  width: 80%;\n  line-height: 25px;\n  font-size: 14px;\n  border-radius: 5px;\n  overflow-wrap: break-word;\n  background: #bce3ff;\n}\n.chat-wrap .msg-box .msg-list .msg-item .date {\n  font-size: 12px;\n  color: #000;\n  margin: 0 5px;\n  font-weight: bold;\n}\n/* 보내는 메세지 */\n.chat-wrap .msg-box .msg-send .msg-item {\n  flex-direction: row-reverse;\n  margin-left: 5px;\n}\n.chat-wrap .msg-box .msg-send .msg-item .tag {\n  right: -9px;\n}\n/* 받는 메세지 */\n.chat-wrap .msg-box .msg-receive .msg-info {\n  display: flex;\n  margin-bottom: 4px;\n  font-weight: bold;\n}\n.chat-wrap .msg-box .msg-receive .msg-info .user-img {\n  width: 30px;\n  height: 30px;\n  margin-right: 5px;\n  border-radius: 50%;\n  border: 1px solid #e2e2e2;\n  background: url(../images/photoDefault.png) no-repeat;\n  background-size: 26px;\n}\n.chat-wrap .msg-box .msg-receive .msg-info p {\n  font-size: 14px;\n}\n.chat-wrap .msg-box .msg-receive .msg-info span {\n  font-size: 10px;\n  color: #2eaef8;\n}\n.chat-wrap .msg-box .msg-receive .msg-item {\n  flex-direction: row;\n  margin-left: 20px;\n}\n.chat-wrap .msg-box .msg-receive .msg-item .tag {\n  left: -9px;\n  border-color: #fff #fff transparent transparent;\n}\n.chat-wrap .msg-box .msg-receive .msg-item .text-msg {\n  background: #fff;\n}\n/* 메세지 전송 */\n.chat-wrap .send-box {\n  width: 100%;\n  height: 50px;\n  position: relative;\n  border-radius: 4px;\n  background: #fff;\n  border-left: 1px solid #efefef;\n}\n.chat-wrap .send-box .text-form {\n  float: left;\n  padding: 10px;\n  width: calc(100% - 50px);\n  height: 50px;\n  color: #666;\n  border: 0;\n  resize: none;\n  outline: none;\n}\n.chat-wrap .send-box .send-btn {\n  width: 50px;\n  height: 50px;\n  border: 0;\n  cursor: pointer;\n  outline: none;\n}\n.chat-wrap .send-box .send-btn::after {\n  content: ' ';\n  display: block;\n  width: 100%;\n  height: 100%;\n  background: url(../images/sendBtn.png) no-repeat;\n}\n.chat-wrap .send-box .send-btn:hover::after {\n  background-color: #f2f2f2;\n}\n\n/*-----------------세부 강의 표시---------------*/\n.weekly_plan {\n  width: 100%;\n  position: relative;\n}\n.weekly_plan .weekly_plan_box {\n  width: 100%;\n  overflow: hidden;\n  margin-bottom: 30px;\n  position: relative;\n}\n.weekly_plan .weekly_plan_box > div {\n  float: left;\n}\n.weekly_plan .weekly_plan_box > .left_week {\n  width: 92px;\n}\n.weekly_plan .weekly_plan_box > .left_week p.circle {\n  width: 60px;\n  height: 60px;\n  background: #f9fafb;\n  border: 1px solid #eaeaea;\n  border-radius: 50%;\n  box-sizing: border-box;\n  text-align: center;\n  font-size: 12px;\n  color: #898989;\n  font-weight: 400;\n  position: relative;\n  z-index: 2;\n}\n.weekly_plan .weekly_plan_box > .left_week p.circle span {\n  display: block;\n  text-align: center;\n  width: 100%;\n  font-size: 23px;\n  color: #333;\n  font-weight: 500;\n  margin-top: 15px;\n  margin-bottom: 5px;\n}\n.weekly_plan .weekly_plan_box > .left_week span.dash_line {\n  position: absolute;\n  z-index: 1;\n  display: block;\n  width: 92px;\n  border-top: 1px dashed #dfdfdf;\n  top: 30px;\n  left: 0;\n}\n.weekly_plan .weekly_plan_box > .right_plan {\n  width: calc(100% - 92px);\n  border-left: 1px dashed #dfdfdf;\n  padding-left: 20px;\n  box-sizing: border-box;\n}\n.weekly_plan .weekly_plan_box > .right_plan > p.plan_tit {\n  font-size: 17px;\n  color: #333;\n  font-weight: 400;\n  margin-bottom: 5px;\n}\n.weekly_plan .weekly_plan_box > .right_plan > .plan_accordion {\n  width: 100%;\n  position: relative;\n}\n/*테스트용 강좌 테스트 목록 부분*/\n.weekly_plan .test_class_tit {\n  font-size: 23px;\n  line-height: 57px;\n  background: #fff;\n  width: 50px;\n  position: relative;\n  z-index: 2;\n}\n.weekly_plan .right_plan ul.test_list {\n  width: 100%;\n  display: block;\n  position: relative;\n}\n.weekly_plan .right_plan ul.test_list li {\n  width: 100%;\n  border-bottom: 1px solid #f4f4f4;\n  line-height: 50px;\n  overflow: hidden;\n}\n.weekly_plan .right_plan ul.test_list li a {\n  float: left;\n  width: 80%;\n  height: 100%;\n}\n.weekly_plan .right_plan ul.test_list li a span.order_number {\n  font-size: 15px;\n  color: #333;\n  font-weight: 400;\n  display: inline-block;\n  vertical-align: middle;\n}\n.weekly_plan .right_plan ul.test_list li a span.order_number b {\n  font-weight: 400 !important;\n}\n.weekly_plan .right_plan ul.test_list li a span.test_exam_tit {\n  width: 95%;\n  display: inline-block;\n  vertical-align: middle;\n  overflow: hidden;\n  text-overflow: ellipsis;\n  white-space: nowrap;\n  box-sizing: border-box;\n  font-size: 15px;\n  color: #333;\n  font-weight: 400;\n}\n.weekly_plan .right_plan ul.test_list li button {\n  float: right;\n  padding: 0 10px;\n  line-height: 30px;\n  font-size: 12px;\n  margin-right: 30px;\n  border: 1px solid #dfdfdf;\n  margin-top: 14px;\n  color: #ea302e;\n}\n.weekly_plan .right_plan ul.test_list li button:hover {\n  border: 1px solid #b4b4b4;\n  color: #333;\n}\n.weekly_plan .right_plan ul.test_list li button.passed_exam {\n  border: 1px solid #dfdfdf !important;\n  border-radius: 4px;\n  box-sizing: border-box;\n  color: #666;\n}\n\n.plan_accordion > ul > li {\n  width: 100%;\n  position: relative;\n  margin-bottom: 15px;\n}\n.plan_accordion > ul > li:last-of-type {\n  margin-bottom: 0;\n}\n.plan_accordion ul li > a.acc_btn {\n  display: block;\n  width: 100%;\n  border: 1px solid #eaeaea;\n  background: #f9fafb;\n  line-height: 50px;\n  padding-left: 25px;\n  box-sizing: border-box;\n  overflow: hidden;\n}\n.plan_accordion ul li > a.acc_btn span.nth {\n  display: inline-block;\n  vertical-align: middle;\n  margin-right: 50px;\n  font-size: 15px;\n  color: #333;\n  font-weight: 400;\n}\n.plan_accordion ul li > a.acc_btn p.nth_tit {\n  display: inline-block;\n  vertical-align: middle;\n  font-size: 15px;\n  color: #333;\n  font-weight: 400;\n}\n.plan_accordion ul li > a.acc_btn span.arrow {\n  float: right;\n  margin-right: 20px;\n  color: #898989 !important;\n  transition: all 0.4s;\n  transform: rotate(0deg);\n}\n.plan_accordion ul li > a.acc_btn:hover span.arrow {\n  color: #333 !important;\n}\n.plan_accordion ul li > a.acc_btn.open_acc span.arrow {\n  transform: rotate(180deg);\n}\n.plan_accordion ul li > div ul {\n  margin-left: 20px;\n}\n.plan_accordion ul li > div ul li {\n  width: 100%;\n  border-bottom: 1px solid #f4f4f4;\n  position: relative;\n  height: 60px;\n  overflow: hidden;\n}\n.plan_accordion ul li > div ul li span.depth {\n  position: absolute;\n  width: 20px;\n  height: 20px;\n  border-left: 1px solid #dfdfdf;\n  border-bottom: 1px solid #dfdfdf;\n  top: 15px;\n  left: 0;\n}\n.plan_accordion ul li > div ul li span.coding_include {\n  position: absolute;\n  color: #2eaef8;\n  font-size: 12px;\n  font-weight: 400;\n  left: 30px;\n  bottom: 7px;\n}\n.plan_accordion ul li > div ul li > p {\n  font-size: 14px;\n  color: #666;\n  font-weight: 400;\n  padding-left: 30px;\n  line-height: 65px;\n  float: left;\n}\n.plan_accordion ul li > div ul li div.right_part {\n  float: right;\n  margin-right: 20px;\n  height: 60px;\n}\n.plan_accordion ul li > div ul li div.right_part button {\n  padding: 0 10px;\n  line-height: 30px;\n  font-size: 12px; /*margin-right:30px;*/\n  border: 1px solid #dfdfdf;\n  margin-top: 14px;\n}\n.plan_accordion ul li > div ul li div.right_part button:hover {\n  border: 1px solid #b4b4b4;\n  color: #333;\n}\n.plan_accordion ul li > div ul li div.right_part span.video_length {\n  color: #898989 !important;\n  line-height: 60px;\n}\n.plan_accordion #appendAssignment #assignment1 p {\n  font-size: 15px;\n  color: #333;\n  font-weight: 400;\n  line-height: 22px;\n}\n\n/*--------------------AMP 스타일--------------------*/\n.amp-controlbaricons-middle {\n  margin-left: 30px;\n}\n.vjs-progress-control.vjs-control.outline-enabled-control {\n  width: 100px;\n}\n\n\n/* 해커톤 카드 리스트 */\n.hackathon-card:first-child{\n  border-top:2px solid #e5e7eb;\n}"],"sourceRoot":""}]);
// Exports
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (___CSS_LOADER_EXPORT___);


/***/ }),

/***/ "./node_modules/css-loader/dist/cjs.js!./style/login-view.css":
/*!********************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js!./style/login-view.css ***!
  \********************************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/cssWithMappingToString.js */ "./node_modules/css-loader/dist/runtime/cssWithMappingToString.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/api.js */ "./node_modules/css-loader/dist/runtime/api.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/getUrl.js */ "./node_modules/css-loader/dist/runtime/getUrl.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _images_logo_extension_login_svg__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../images/logo_extension_login.svg */ "./images/logo_extension_login.svg");
/* harmony import */ var _images_logo_extension_login_svg__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_images_logo_extension_login_svg__WEBPACK_IMPORTED_MODULE_3__);
// Imports




var ___CSS_LOADER_EXPORT___ = _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default()((_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default()));
var ___CSS_LOADER_URL_REPLACEMENT_0___ = _node_modules_css_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_2___default()((_images_logo_extension_login_svg__WEBPACK_IMPORTED_MODULE_3___default()));
// Module
___CSS_LOADER_EXPORT___.push([module.id, "/* reset */\nbody,\nbutton,\ndd,\ndl,\ndt,\nfieldset,\nform,\nh1,\nh2,\nh3,\nh4,\nh5,\nh6,\ninput,\nlegend,\nli,\nol,\np,\nselect,\ntable,\ntd,\ntextarea,\nth,\nul {\n  margin: 0;\n  padding: 0;\n}\nh1,\nh2,\nh3,\nh4,\nh5,\nh6 {\n  font-size: inherit;\n  line-height: inherit;\n}\nbutton,\ninput {\n  -webkit-border-radius: 0;\n  border-radius: 0;\n  /* border: 0; */\n}\nbutton {\n  background-color: transparent;\n}\nfieldset,\nimg {\n  border: 0;\n}\nimg {\n  vertical-align: top;\n}\nol,\nul {\n  list-style: none;\n}\naddress,\nem {\n  font-style: normal;\n}\na {\n  color: inherit;\n  text-decoration: none;\n}\na:hover {\n  text-decoration: none;\n}\niframe {\n  overflow: hidden;\n  margin: 0;\n  border: 0;\n  padding: 0;\n  vertical-align: top;\n}\nmark {\n  background-color: transparent;\n}\ni {\n  font-style: normal;\n}\n\n/***** login *****/\n#wrap {\n  position: relative;\n  display: flex;\n  align-items: center;\n  width: 100%;\n  height: 100vh;\n}\n.join-wrap {\n  width: 360px;\n  margin: 0 auto;\n}\n.join-wrap .join-top {\n  text-align: center;\n}\n.join-wrap .join-top h3 {\n  font-size: 40px;\n  font-weight: 500;\n  line-height: 65px;\n  margin: 0;\n}\n.join-wrap .join-top .txt {\n  font-size: 17px;\n  font-weight: bold;\n}\n.join-form {\n  margin-top: 30px;\n  padding: 5px 0;\n}\n.join-form .input-set:first-child {\n  padding-bottom: 10px;\n}\n.join-form .input-set p {\n  padding: 5px 0;\n  font-size: 14px;\n  font-weight: bold;\n}\n.join-form .input-set .input-box {\n  position: relative;\n  display: inline-flex;\n  width: 360px;\n  font-weight: 400;\n  font-style: normal;\n  color: rgba(0, 0, 0, 0.87);\n}\n.join-form .input-set .input-box input {\n  width: 100%;\n  padding: 9px 14px 9px 37px;\n  font-weight: 500;\n  background-color: #fff;\n  border-radius: 4px;\n  border: 1px solid rgba(34, 36, 38, 0.15);\n  outline: none;\n}\n.join-form .input-set .input-box input::placeholder {\n  color: #aeaeae;\n}\n.join-form .input-set .input-box i {\n  position: absolute;\n  left: 10px;\n  top: 5px;\n  font-size: 18px;\n  color: #aeaeae;\n}\n.join-form .join-btn {\n  display: inline-block;\n  padding: 12px 0;\n  margin-top: 10px;\n  width: 100%;\n  font-size: 17px;\n  font-weight: 500;\n  border: 0;\n  border-radius: 4px;\n  text-align: center;\n  color: #fff;\n  background: #2eaef8;\n  cursor: pointer;\n}\n.login-img {\n  display: block;\n  content: \" \";\n  width: 225px;\n  height: 78px;\n  margin: 35px 0 30px 0;\n  background: url(" + ___CSS_LOADER_URL_REPLACEMENT_0___ + ") no-repeat;\n  background-size: 225px;\n}\n", "",{"version":3,"sources":["webpack://./style/login-view.css"],"names":[],"mappings":"AAAA,UAAU;AACV;;;;;;;;;;;;;;;;;;;;;;;;EAwBE,SAAS;EACT,UAAU;AACZ;AACA;;;;;;EAME,kBAAkB;EAClB,oBAAoB;AACtB;AACA;;EAEE,wBAAwB;EACxB,gBAAgB;EAChB,eAAe;AACjB;AACA;EACE,6BAA6B;AAC/B;AACA;;EAEE,SAAS;AACX;AACA;EACE,mBAAmB;AACrB;AACA;;EAEE,gBAAgB;AAClB;AACA;;EAEE,kBAAkB;AACpB;AACA;EACE,cAAc;EACd,qBAAqB;AACvB;AACA;EACE,qBAAqB;AACvB;AACA;EACE,gBAAgB;EAChB,SAAS;EACT,SAAS;EACT,UAAU;EACV,mBAAmB;AACrB;AACA;EACE,6BAA6B;AAC/B;AACA;EACE,kBAAkB;AACpB;;AAEA,kBAAkB;AAClB;EACE,kBAAkB;EAClB,aAAa;EACb,mBAAmB;EACnB,WAAW;EACX,aAAa;AACf;AACA;EACE,YAAY;EACZ,cAAc;AAChB;AACA;EACE,kBAAkB;AACpB;AACA;EACE,eAAe;EACf,gBAAgB;EAChB,iBAAiB;EACjB,SAAS;AACX;AACA;EACE,eAAe;EACf,iBAAiB;AACnB;AACA;EACE,gBAAgB;EAChB,cAAc;AAChB;AACA;EACE,oBAAoB;AACtB;AACA;EACE,cAAc;EACd,eAAe;EACf,iBAAiB;AACnB;AACA;EACE,kBAAkB;EAClB,oBAAoB;EACpB,YAAY;EACZ,gBAAgB;EAChB,kBAAkB;EAClB,0BAA0B;AAC5B;AACA;EACE,WAAW;EACX,0BAA0B;EAC1B,gBAAgB;EAChB,sBAAsB;EACtB,kBAAkB;EAClB,wCAAwC;EACxC,aAAa;AACf;AACA;EACE,cAAc;AAChB;AACA;EACE,kBAAkB;EAClB,UAAU;EACV,QAAQ;EACR,eAAe;EACf,cAAc;AAChB;AACA;EACE,qBAAqB;EACrB,eAAe;EACf,gBAAgB;EAChB,WAAW;EACX,eAAe;EACf,gBAAgB;EAChB,SAAS;EACT,kBAAkB;EAClB,kBAAkB;EAClB,WAAW;EACX,mBAAmB;EACnB,eAAe;AACjB;AACA;EACE,cAAc;EACd,YAAY;EACZ,YAAY;EACZ,YAAY;EACZ,qBAAqB;EACrB,6DAA6D;EAC7D,sBAAsB;AACxB","sourcesContent":["/* reset */\nbody,\nbutton,\ndd,\ndl,\ndt,\nfieldset,\nform,\nh1,\nh2,\nh3,\nh4,\nh5,\nh6,\ninput,\nlegend,\nli,\nol,\np,\nselect,\ntable,\ntd,\ntextarea,\nth,\nul {\n  margin: 0;\n  padding: 0;\n}\nh1,\nh2,\nh3,\nh4,\nh5,\nh6 {\n  font-size: inherit;\n  line-height: inherit;\n}\nbutton,\ninput {\n  -webkit-border-radius: 0;\n  border-radius: 0;\n  /* border: 0; */\n}\nbutton {\n  background-color: transparent;\n}\nfieldset,\nimg {\n  border: 0;\n}\nimg {\n  vertical-align: top;\n}\nol,\nul {\n  list-style: none;\n}\naddress,\nem {\n  font-style: normal;\n}\na {\n  color: inherit;\n  text-decoration: none;\n}\na:hover {\n  text-decoration: none;\n}\niframe {\n  overflow: hidden;\n  margin: 0;\n  border: 0;\n  padding: 0;\n  vertical-align: top;\n}\nmark {\n  background-color: transparent;\n}\ni {\n  font-style: normal;\n}\n\n/***** login *****/\n#wrap {\n  position: relative;\n  display: flex;\n  align-items: center;\n  width: 100%;\n  height: 100vh;\n}\n.join-wrap {\n  width: 360px;\n  margin: 0 auto;\n}\n.join-wrap .join-top {\n  text-align: center;\n}\n.join-wrap .join-top h3 {\n  font-size: 40px;\n  font-weight: 500;\n  line-height: 65px;\n  margin: 0;\n}\n.join-wrap .join-top .txt {\n  font-size: 17px;\n  font-weight: bold;\n}\n.join-form {\n  margin-top: 30px;\n  padding: 5px 0;\n}\n.join-form .input-set:first-child {\n  padding-bottom: 10px;\n}\n.join-form .input-set p {\n  padding: 5px 0;\n  font-size: 14px;\n  font-weight: bold;\n}\n.join-form .input-set .input-box {\n  position: relative;\n  display: inline-flex;\n  width: 360px;\n  font-weight: 400;\n  font-style: normal;\n  color: rgba(0, 0, 0, 0.87);\n}\n.join-form .input-set .input-box input {\n  width: 100%;\n  padding: 9px 14px 9px 37px;\n  font-weight: 500;\n  background-color: #fff;\n  border-radius: 4px;\n  border: 1px solid rgba(34, 36, 38, 0.15);\n  outline: none;\n}\n.join-form .input-set .input-box input::placeholder {\n  color: #aeaeae;\n}\n.join-form .input-set .input-box i {\n  position: absolute;\n  left: 10px;\n  top: 5px;\n  font-size: 18px;\n  color: #aeaeae;\n}\n.join-form .join-btn {\n  display: inline-block;\n  padding: 12px 0;\n  margin-top: 10px;\n  width: 100%;\n  font-size: 17px;\n  font-weight: 500;\n  border: 0;\n  border-radius: 4px;\n  text-align: center;\n  color: #fff;\n  background: #2eaef8;\n  cursor: pointer;\n}\n.login-img {\n  display: block;\n  content: \" \";\n  width: 225px;\n  height: 78px;\n  margin: 35px 0 30px 0;\n  background: url(../images/logo_extension_login.svg) no-repeat;\n  background-size: 225px;\n}\n"],"sourceRoot":""}]);
// Exports
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (___CSS_LOADER_EXPORT___);


/***/ }),

/***/ "./images/photoDefault.png":
/*!*********************************!*\
  !*** ./images/photoDefault.png ***!
  \*********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (__webpack_require__.p + "be3bdb072422fcca72857398ef585f75605538ec7076d2bff66c92b4f73f2dca.png");

/***/ }),

/***/ "./images/sendBtn.png":
/*!****************************!*\
  !*** ./images/sendBtn.png ***!
  \****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (__webpack_require__.p + "cce90d4aada89def088094db7e8ac2b7096ddcf9cc768e21d143be06ba989b5a.png");

/***/ }),

/***/ "./style/lecture-detail.css":
/*!**********************************!*\
  !*** ./style/lecture-detail.css ***!
  \**********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_cjs_js_lecture_detail_css__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! !!../node_modules/css-loader/dist/cjs.js!./lecture-detail.css */ "./node_modules/css-loader/dist/cjs.js!./style/lecture-detail.css");

            

var options = {};

options.insert = "head";
options.singleton = false;

var update = _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default()(_node_modules_css_loader_dist_cjs_js_lecture_detail_css__WEBPACK_IMPORTED_MODULE_1__["default"], options);



/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (_node_modules_css_loader_dist_cjs_js_lecture_detail_css__WEBPACK_IMPORTED_MODULE_1__["default"].locals || {});

/***/ }),

/***/ "./style/login-view.css":
/*!******************************!*\
  !*** ./style/login-view.css ***!
  \******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_cjs_js_login_view_css__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! !!../node_modules/css-loader/dist/cjs.js!./login-view.css */ "./node_modules/css-loader/dist/cjs.js!./style/login-view.css");

            

var options = {};

options.insert = "head";
options.singleton = false;

var update = _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default()(_node_modules_css_loader_dist_cjs_js_login_view_css__WEBPACK_IMPORTED_MODULE_1__["default"], options);



/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (_node_modules_css_loader_dist_cjs_js_login_view_css__WEBPACK_IMPORTED_MODULE_1__["default"].locals || {});

/***/ }),

/***/ "./images/logo_extension_login.svg":
/*!*****************************************!*\
  !*** ./images/logo_extension_login.svg ***!
  \*****************************************/
/***/ ((module) => {

module.exports = "data:image/svg+xml,%3Csvg id='Layer_1' data-name='Layer 1' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 225 78'%3E%3Cdefs%3E%3Cstyle%3E.cls-1%7Bfill:none;%7D.cls-2%7Bfill:%23212435;%7D.cls-3%7Bfill:%23495ef1;%7D.cls-4%7Bfill:%23d64c32;%7D%3C/style%3E%3C/defs%3E%3Crect class='cls-1' width='225' height='78'/%3E%3Cpath class='cls-2' d='M501.47,132.43v-6.25h4.18v6.25h11.51v3.43H492.75v-3.43Zm7-2.82a6.84,6.84,0,0,0,1.22-3,25.78,25.78,0,0,0,.21-2.75H495v-3.54h14.87v-3.47h-15v-3.57H514v11.11a18.56,18.56,0,0,1-.11,2,14,14,0,0,1-.43,1.83,3.78,3.78,0,0,1-.86,1.39Z' transform='translate(-335.63 -103.95)'/%3E%3Cpath class='cls-2' d='M442.58,126.66a7.45,7.45,0,0,0,2.54,1.54,11.73,11.73,0,0,0,3.07.82,14.81,14.81,0,0,0,3.36.18,21.42,21.42,0,0,0,6.47-1.11,13.74,13.74,0,0,0,2.61-1.1v-3.58a20.26,20.26,0,0,1-10.62,2,9.3,9.3,0,0,1-4.07-1.18,2.8,2.8,0,0,1-1.64-2.61v-4.91h15.86v-3.47h-19.9v7.85a7.4,7.4,0,0,0,.64,3.22A6.53,6.53,0,0,0,442.58,126.66Z' transform='translate(-335.63 -103.95)'/%3E%3Cpolygon class='cls-2' points='103.17 31.52 113.31 31.52 113.31 38.77 117.5 38.77 117.5 31.52 127.57 31.52 127.57 28.05 103.17 28.05 103.17 31.52'/%3E%3Cpolygon class='cls-2' points='149.42 8.57 149.42 31.88 153.43 31.91 153.43 8.57 149.42 8.57'/%3E%3Crect class='cls-2' x='129.77' y='28.05' width='17.98' height='3.36'/%3E%3Cpath class='cls-2' d='M473.84,112.21a8.44,8.44,0,1,0,8.44,8.44A8.44,8.44,0,0,0,473.84,112.21Zm0,12.9a4.47,4.47,0,1,1,4.46-4.46A4.46,4.46,0,0,1,473.84,125.11Z' transform='translate(-335.63 -103.95)'/%3E%3Cpath class='cls-2' d='M529.81,129.15a9.87,9.87,0,0,0,2.43-.79,8.36,8.36,0,0,0,2-1.22v-3.46a13.22,13.22,0,0,1-4.36,1.86,8.51,8.51,0,0,1-3.79,0,4.54,4.54,0,0,1-2.68-1.54,3.94,3.94,0,0,1-1-2.82v-4.39h9.93v-3.54h-14v7.47a9,9,0,0,0,.5,3.25,7.07,7.07,0,0,0,3.29,4.07,6.88,6.88,0,0,0,2.39,1,10.43,10.43,0,0,0,2.61.32A11,11,0,0,0,529.81,129.15Z' transform='translate(-335.63 -103.95)'/%3E%3Cpath class='cls-2' d='M541.6,137h0V112.53h-4v17.82a7.78,7.78,0,1,0,4,6.8S541.6,137.08,541.6,137Zm-7.77,3.87a3.76,3.76,0,1,1,3.75-3.76A3.75,3.75,0,0,1,533.83,140.91Z' transform='translate(-335.63 -103.95)'/%3E%3Cpath class='cls-1' d='M430,122.48V116.8H418.79v5.71a3.5,3.5,0,0,0,1.21,3,4.84,4.84,0,0,0,3.15,1h2.25a5.61,5.61,0,0,0,3.29-1A3.44,3.44,0,0,0,430,122.48Z' transform='translate(-335.63 -103.95)'/%3E%3Cpath class='cls-2' d='M426.73,132.12v-2.33a8.53,8.53,0,0,0,4.93-1.75,6.39,6.39,0,0,0,2.39-5.36v-9.4H414.83v9a6.83,6.83,0,0,0,2.25,5.61,8.32,8.32,0,0,0,5.47,1.89v2.3H412.4v3.43h24.41v-3.43Zm-3.58-5.67a4.84,4.84,0,0,1-3.15-1,3.5,3.5,0,0,1-1.21-3V116.8H430v5.68a3.44,3.44,0,0,1-1.32,3,5.61,5.61,0,0,1-3.29,1Z' transform='translate(-335.63 -103.95)'/%3E%3Cpath class='cls-3' d='M400.89,116.22v4.62c0,2.21,1.24,3,3.29,3.45a2.64,2.64,0,0,1,2.25,2.94c0,2.06-1,2.72-2.25,3-2.21.46-3.29,1.32-3.29,3.56v4.5c0,3.92-2.33,7.45-8.45,7.68-1.48,0-2-.82-2-2.09s.46-2.1,1.9-2.25c2-.24,3.57-1.32,3.57-3.69V133c0-2.56.58-4.85,4.34-5.62v-.2c-3.88-.69-4.34-3.1-4.34-5.89v-4.88c0-2.33-1.6-3.42-3.57-3.57-1.44-.08-1.94-1.09-1.94-2.37,0-1,.5-2,1.71-2C398.56,108.47,400.89,112.27,400.89,116.22Z' transform='translate(-335.63 -103.95)'/%3E%3Cpath class='cls-3' d='M360.19,138.2v-4.61c0-2.21-1.24-3-3.3-3.45a3.08,3.08,0,0,1,0-5.93c2.21-.47,3.3-1.32,3.3-3.57v-4.5c0-3.91,2.32-7.44,8.45-7.67,1.47,0,2,.81,2,2.09a2,2,0,0,1-1.9,2.25c-2,.23-3.57,1.32-3.57,3.68v4.93c0,2.56-.58,4.84-4.34,5.62v.19c3.88.7,4.34,3.1,4.34,5.9V138c0,2.33,1.59,3.41,3.57,3.57,1.43.08,1.94,1.08,1.94,2.36,0,1-.51,2-1.71,2C362.51,146,360.19,142.16,360.19,138.2Z' transform='translate(-335.63 -103.95)'/%3E%3Ccircle class='cls-3' cx='38.47' cy='18.97' r='2.91'/%3E%3Ccircle class='cls-3' cx='51.35' cy='18.71' r='2.91'/%3E%3Cpath class='cls-3' d='M386.16,130.91c-3.35,3.71-7.9,3.71-11.24,0-1.56-1.72-4.1.83-2.55,2.55a10.64,10.64,0,0,0,16.34,0c1.55-1.72-1-4.27-2.55-2.55Z' transform='translate(-335.63 -103.95)'/%3E%3Cpath class='cls-4' d='M199.16,51.62H200a.84.84,0,0,1,.84.84v3.59a.84.84,0,0,1-.84.84h-1.34a.36.36,0,0,1-.36-.36V52.46a.84.84,0,0,1,.84-.84Z'/%3E%3Cpath class='cls-4' d='M540.36,174.26H538a1.5,1.5,0,0,1-1.5-1.5v-7.41h3.89a1.26,1.26,0,1,0,0-2.51h-5.82a.58.58,0,0,0-.58.58v9.26s0,.35,0,.57a4,4,0,0,0,4,3.51h2.4a1.25,1.25,0,0,0,0-2.5Z' transform='translate(-335.63 -103.95)'/%3E%3Cpath class='cls-4' d='M530.63,164a5.26,5.26,0,0,0-4.27-1.78,5.17,5.17,0,0,0-4.13,1.74,6.81,6.81,0,0,0-1.54,4.74v1.67a6.66,6.66,0,0,0,1.58,4.74,5.42,5.42,0,0,0,4.31,1.7,7.93,7.93,0,0,0,3-.51,12,12,0,0,0,1.52-.73,1.71,1.71,0,0,0,.23-.19.73.73,0,0,0,.09-.1,1.16,1.16,0,0,0,.26-.73,1.18,1.18,0,0,0-1.18-1.18,1.21,1.21,0,0,0-.49.11l-.13.07a11.49,11.49,0,0,1-1.11.53,5.92,5.92,0,0,1-2.16.36,2.91,2.91,0,0,1-2.44-1,4.31,4.31,0,0,1-.94-2.86h7.28a1.58,1.58,0,0,0,1.59-1.72v-.11A7.23,7.23,0,0,0,530.63,164Zm-6.55,1.6a2.68,2.68,0,0,1,2.28-1,2.89,2.89,0,0,1,2.35,1,4.34,4.34,0,0,1,1,2.74h-6.45A4.36,4.36,0,0,1,524.08,165.55Z' transform='translate(-335.63 -103.95)'/%3E%3Cpath class='cls-4' d='M484.48,162.13a6.05,6.05,0,0,0-3.58,1.16v-6.48a1.27,1.27,0,0,0-1.27-1.27h0a1.27,1.27,0,0,0-1.27,1.27v18.64a1.27,1.27,0,0,0,1.27,1.27h0a1.27,1.27,0,0,0,1.27-1.27v-7.19h0a3.59,3.59,0,1,1,7.17,0v7.2a1.27,1.27,0,0,0,1.27,1.27h0a1.26,1.26,0,0,0,1.26-1.27v-7.2A6.12,6.12,0,0,0,484.48,162.13Z' transform='translate(-335.63 -103.95)'/%3E%3Cpath class='cls-4' d='M507.85,176.76a1.26,1.26,0,0,0,1.26-1.27V168.3h0a3.59,3.59,0,1,1,7.17,0v7.2a1.27,1.27,0,0,0,1.27,1.27h0a1.27,1.27,0,0,0,1.27-1.27v-7.2a6.12,6.12,0,1,0-12.24,0h0v7.2a1.27,1.27,0,0,0,1.27,1.27Z' transform='translate(-335.63 -103.95)'/%3E%3Cpath class='cls-4' d='M503.45,162.84a1.27,1.27,0,0,0-1.27,1.27v7.19h0a3.59,3.59,0,1,1-7.17,0v-7.2a1.27,1.27,0,0,0-1.27-1.27h0a1.27,1.27,0,0,0-1.27,1.27v7.2a6.12,6.12,0,1,0,12.24,0h0v-7.2a1.26,1.26,0,0,0-1.26-1.27Z' transform='translate(-335.63 -103.95)'/%3E%3C/svg%3E"

/***/ })

}]);
//# sourceMappingURL=lib_index_js.2c0f8f52c9b63b862769.js.map