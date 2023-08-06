/* eslint-disable @typescript-eslint/explicit-module-boundary-types */
/* eslint-disable react/no-unescaped-entities */
import React, { useState } from "react";
import axios from "axios";
import { config } from "../config/config";
import "../../style/login-view.css";
import GrayCenterContainer from "./useGrayCenterContainer";

// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
// eslint-disable-next-line react/prop-types
export const Login = ({ onLoggedIn }) => {
  const [inputs, setInputs] = useState({
    email: "",
    password: "",
  });
  const [onProcess, setOnProcess] = useState(false);

  const { email, password } = inputs;

  const handleChange = (e) => {
    const { name, value } = e.target;
    setInputs((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  return (
    <GrayCenterContainer>
      <div className="xl:w-10/12">
        <div className="block bg-white shadow-lg rounded-lg">
          <div className="lg:flex lg:flex-wrap g-0">
            <div className="lg:w-6/12 px-4 md:px-0">
              <div className="md:p-12 md:mx-6">
                <div className="text-center">
                  <img
                        className="mx-auto w-48"
                        src="images/joinImg.png"
                        alt="logo"
                      />
                  {/* <i className="mx-auto login-img"></i> */}
                  <h4 className="text-xl font-semibold mt-1 mb-12 pb-1">
                    모두의 코딩 <br />
                    주피터 클라이언트
                  </h4>
                </div>
                <form>
                  <p className="mb-4">이메일 / 패스워드를 입력해주세요</p>
                  <div className="mb-4">
                    <input
                      type="email"
                      name="email"
                      className="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                      placeholder="email@example.com"
                      value={email}
                      onChange={handleChange}
                    />
                  </div>
                  <div className="mb-4">
                    <input
                      type="password"
                      name="password"
                      className="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                      placeholder="Password"
                      value={password}
                      onChange={handleChange}
                    />
                  </div>
                  <div className="text-center pt-1 mb-12 pb-1">
                    <button
                      className="inline-block px-6 py-2.5 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:shadow-lg focus:outline-none focus:ring-0 active:shadow-lg transition duration-150 ease-in-out w-full mb-3"
                      type="button"
                      data-mdb-ripple="true"
                      data-mdb-ripple-color="light"
                      style={{
                        background:
                          "linear-gradient(to right, #007fac, #199bc8, #19bdc8, #1abec9)",
                      }}
                      onClick={async (): Promise<void> => {
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
                          const response = await axios.post(
                            `${config.baseUrl}Token`,
                            param,
                          );

                          if (response.data && response.data.token) {
                            onLoggedIn(response.data);
                          }
                          //const token = response.data.token;
                          //console.log(token);
                          //const stateObj = { email, token };
                        } catch (err) {
                          if (axios.isAxiosError(err) && err.response) {
                            setOnProcess(false);

                            if (err.response.status === 400) {
                              alert(
                                "패스워드는 8자 이상, 영문자, 숫자, 특수문자를 포함해야 합니다.",
                              );
                              return;
                            } else if (err.response.status === 404) {
                              alert(
                                "이메일 또는 패스워드가 일치하지 않습니다.",
                              );
                              return;
                            }
                          } else {
                            console.log(err);
                          }
                        }
                      }}
                      disabled={onProcess}
                    >
                      {onProcess && (
                        <svg
                          role="status"
                          className="inline w-4 h-4 mr-3 text-white animate-spin"
                          viewBox="0 0 100 101"
                          fill="none"
                          xmlns="http://www.w3.org/2000/svg"
                        >
                          <path
                            d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                            fill="#E5E7EB"
                          />
                          <path
                            d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                            fill="currentColor"
                          />
                        </svg>
                      )}
                      로그인
                    </button>
                    {/* <a className="text-gray-500" href="#!">
                          Forgot password?
                        </a> */}
                  </div>
                  {/* <div className="flex items-center justify-between pb-6">
                        <p className="mb-0 mr-2">Don't have an account?</p>
                        <button
                          type="button"
                          className="inline-block px-6 py-2 border-2 border-red-600 text-red-600 font-medium text-xs leading-tight uppercase rounded hover:bg-black hover:bg-opacity-5 focus:outline-none focus:ring-0 transition duration-150 ease-in-out"
                          data-mdb-ripple="true"
                          data-mdb-ripple-color="light"
                        >
                          Danger
                        </button>
                      </div> */}
                </form>
              </div>
            </div>
            <div
              className="lg:w-6/12 flex items-center lg:rounded-r-lg rounded-b-lg lg:rounded-bl-none"
              style={{
                background:
                  "linear-gradient(to right,  #007fac, #199bc8, #19bdc8, #1abec9)",
              }}
            >
              <div className="text-white px-4 py-6 md:p-12 md:mx-6">
                <h4 className="text-xl font-semibold mb-6">
                  기업 실무형 AI 문제해결자를 <br />
                  양성하는 KT만의 차별화된 <br />
                  프로그램
                </h4>
                <p className="text-sm">
                  KT AIVLE School 클라이언트를 통해 python기반의 데이터 / AI
                  학습과 AI 해커톤에 참여하세요!
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </GrayCenterContainer>
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

export default Login;
