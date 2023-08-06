import { ReactWidget } from "@jupyterlab/apputils";
import axios from "axios";

//import 'tailwindcss/tailwind.css';
//import 'bootstrap/dist/css/bootstrap.css';

import React, { useState, useEffect } from "react";
import { config } from "./config/config";
import LectureList from "./hooks/useLectureList";
import Login from "./hooks/useLogin";
import { VideoJS } from "./hooks/useVideoJS";
import { AzureMP } from "react-azure-mp";
import "../style/lecture-detail.css";
import { io } from "socket.io-client";
import DOMPurify from "dompurify";
import LectureDrawer from "./hooks/useLectureDrawer";
import Header from "./hooks/useHeader";
import LessonList from "./hooks/useLessonList";
import CategorySelect from "./hooks/useCategorySelect";
import Category from "./types/category";
import HackathonList from "./hooks/useHackathonList";
import { getTimeStringOnly } from "./util/date";
import { isYoutubeUrl } from "./util/url";

/**
 * React component for a counter.
 *
 * @returns The React component
 */
const ModuCodingComponent = (): JSX.Element => {
  // useStyle(
  //   'https://cdn.jsdelivr.net/npm/video.js@7.10.2/dist/video-js.min.css'
  // );
  // useScript('https://cdn.jsdelivr.net/npm/video.js@7.10.2/dist/video.min.js');
  // useScript(
  //   'https://cdn.jsdelivr.net/npm/videojs-youtube@2.6.1/dist/Youtube.min.js'
  // );
  // const [videoUrl, setVideoUrl] = useState('');
  const [state, setState] = useState({
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

  const [isLectureListOpen, setIsLectureListOpen] = useState(false);
  const [lectureDrawerVisible, setLectureDrawerVisible] = useState(false);

  const [lesson, setLesson] = useState({
    title: "",
    description: "",
    extLiveStreamUrl: null,
    videoLink: "", // 유투브 링크
    videoFile: "", // Azure Media Servier 링크
    videoUrl: "", // 라이브 스트리밍 url
    pdfUrl: "",
    notebookUrl: "",
  });

  const [ampSource, setAMPSource] = useState([]);

  const [questions, setQuestions] = useState([]);

  const setStateChanged = (prop, value, fn) => {
    fn((prevState) => ({
      ...prevState,
      [prop]: value,
    }));
  };

  const [videoJsOptions, setVideoJsOptions] = useState({
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

  const [chatMessages, setChatMessages] = useState([]);

  const [socket, setSocket] = useState(null);

  const [roomId, setRoomId] = useState(null);

  const playerRef = React.useRef(null);
  const chatListRef = React.useRef<HTMLDivElement>();

  const {
    loggedIn,
    email,
    name,
    token,
    roles,
    currentCategory,
    currentLecture,
    currentLectureLessons,
    lessonSelected,
    questionSelected,
  } = state;

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

  const getToken = React.useCallback(() => {
    return token;
  }, [token]);

  const getUser = React.useCallback(() => {
    return {
      email,
      name,
    };
  }, [email, name]);

  const loadLesson = async (lessonId) => {
    try {
      const response = await axios.get(
        `${config.baseUrl}Lesson/Applied/${lessonId}`,
        {
          headers: {
            Authorization: `Bearer ${getToken()}`,
          },
        },
      );

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
      } else {
        setStateChanged("videoUrl", "", setLesson);
      }

      if (lesson.lessonLinks) {
        setStateChanged("videoFile", "", setLesson);
        setStateChanged("videoLink", "", setLesson);

        const pdfFile = lesson.lessonLinks.find(
          (link) => link.type.toLowerCase() === "pdffile",
        );
        if (pdfFile && pdfFile.url) {
          setStateChanged("pdfUrl", pdfFile.url, setLesson);
        }

        const notebookFile = lesson.lessonLinks.find(
          (link) => link.type.toLowerCase() === "notebookfile",
        );
        if (notebookFile && notebookFile.url) {
          setStateChanged("notebookUrl", notebookFile.url, setLesson);
        }

        if (lesson.extLiveStreamUrl) {
          return;
        }

        const videoFile = lesson.lessonLinks.find(
          (link) => link.type.toLowerCase() === "videofile",
        );

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
        } else {
          // Azure Media Service가 아니면 youtube 영상
          const videoLink = lesson.lessonLinks.find(
            (link) => link.type.toLowerCase() === "videolink",
          );

          if (videoLink && videoLink.url) {
            setStateChanged("videoLink", videoLink.url, setLesson);

            if (!isYoutubeUrl(lesson.extLiveStreamUrl)) {
              setStateChanged(
                "sources",
                {
                  type: "video/youtube",
                  src: videoLink.url,
                },
                setVideoJsOptions,
              );
            }
          }
        }
      }
    } catch (err: any) {
      if (axios.isAxiosError(err) && err.response) {
        console.log(err);
      } else {
        console.log(err);
      }
    }
  };

  const onCategorySelected = (category: Category) => {
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
    } catch (err) {
      if (axios.isAxiosError(err) && err.response) {
        console.log(err);
      } else {
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

  useEffect(() => {
    if (!videoUrl) {
      return;
    }

    if (lesson.extLiveStreamUrl) {
      console.log("useEffect", lesson.extLiveStreamUrl);

      let videoType = "video/youtube";

      if (!isYoutubeUrl(lesson.extLiveStreamUrl)) {
        videoType = "application/x-mpegURL";
      }

      setStateChanged(
        "sources",
        {
          type: videoType,
          src: videoUrl,
        },
        setVideoJsOptions,
      );
      // playerRef.current.src({
      //   type: 'video/youtube',
      //   src: videoUrl,
      // });
    }
  }, [videoUrl]);

  useEffect(() => {
    scrollToBottom();
  }, [chatMessages]);

  useEffect(() => {
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
    const openBtn = document.querySelector(".open-btn") as HTMLButtonElement;
    const closeBtn = document.querySelector(".close-btn") as HTMLButtonElement;

    chatPanel.classList.toggle("hide");

    if (chatPanel.classList.contains("hide")) {
      openBtn.style.display = "block";
      closeBtn.style.display = "none";
    } else {
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
        messages.push(
          <li className="msg-list">
            <p>{message.content}</p>
          </li>,
        );
      } else if (message.type === "sent") {
        messages.push(
          <li className="msg-list msg-send">
            <div className="msg-item">
              <i className="tag"></i>
              <div className="text-msg">{message.content}</div>
              <span className="date">{getTimeStringOnly()}</span>
            </div>
          </li>,
        );
      } else {
        messages.push(
          <li className="msg-list msg-receive">
            <div className="msg-info">
              <i className="user-img"></i>
              <p className="user-name">{message.from}</p>
            </div>
            <div className="msg-item">
              <div className="tag"></div>
              <div className="text-msg">{message.content}</div>
              <div className="date">{getTimeStringOnly()}</div>
            </div>
          </li>,
        );
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
    const _socket = io(config.chat, { transports: ["websocket"] });
    _socket.on("connect", () => {
      _socket.emit("room:join", {
        roomid: roomId, //DOMPurify.sanitize(codereet.roomid),
        username: name, //DOMPurify.sanitize(codereet.username),
      });
    });

    _socket.on("server:message", (data) => {
      setChatMessages((prev) => [
        ...prev,
        {
          type: "info",
          content: DOMPurify.sanitize(data.message), //DOMPurify.sanitize(data.message),
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
          content: DOMPurify.sanitize(data.message),
        },
      ]);
    });

    setSocket(_socket);
  };

  const sendMessage = () => {
    const message = document.getElementById("message") as HTMLTextAreaElement;
    if (message && message.value) {
      const chatMessage = DOMPurify.sanitize(message.value);

      socket.emit("chat:message", {
        roomid: roomId, // DOMPurify.sanitize(codereet.roomid),
        username: name, // DOMPurify.sanitize(codereet.username),
        obj: {},
        message: chatMessage,
      });

      message.value = "";

      setChatMessages((prev) => [
        ...prev,
        {
          type: "sent",
          content: DOMPurify.sanitize(chatMessage), //DOMPurify.sanitize(data.message),
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
      const response = await axios({
        url: `${config.baseUrl}Files/GetFile`,
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
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div style={{ height: "100%" }}>
      <link
        href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css"
        rel="stylesheet"
      />
      <link
        rel="stylesheet"
        href="//cdn.jsdelivr.net/npm/@mdi/font@6.5.95/css/materialdesignicons.min.css"
      />
      {!loggedIn && (
        <div>
          <Login onLoggedIn={onLoggedIn} />
        </div>
      )}
      {loggedIn && (
        <div style={{ height: "100%" }}>
          <Header
            lectureDrawerVisible={lectureDrawerVisible}
            setIsOpen={setIsLectureListOpen}
            getUser={getUser}
            lecture={currentLecture}
            lessons={currentLectureLessons}
            handleBackToLectureList={handleBackToLectureList}
          />
          <div className="top-menu">
            {currentLectureLessons && (
              <LectureDrawer
                isOpen={isLectureListOpen}
                setIsOpen={setIsLectureListOpen}
              >
                <LessonList
                  weeks={currentLectureLessons}
                  onLessonSelected={onLessonSelected}
                />
              </LectureDrawer>
            )}
            {/* {lessonSelected && lesson.extLiveStreamUrl && (
              <button
                className="btn open-btn"
                onClick={() => {
                  toggleChatPanel();
                }}
              >
                채팅창 열기
              </button>
            )}
            {lessonSelected && lesson.extLiveStreamUrl && (
              <button
                className="btn close-btn"
                onClick={() => {
                  toggleChatPanel();
                }}
              >
                채팅창 닫기
              </button>
            )} */}
          </div>
          {/* 1. 유형 선택하기(강좌, AI 해커톤) */}
          {!currentCategory && (
            <CategorySelect onCategorySelected={onCategorySelected} />
          )}
          {currentCategory === Category.Lecture && (
            <div
              className={`split split-lesson lesson-container-full mx-5 overflow-auto ${
                lessonSelected ? "" : "overflow-y-auto overflow-x-hidden"
              }`}
            >
              {/* 2. 강좌 선택하기 */}
              {lessonSelected ? (
                <div className="lesson-panel h-full">
                  <div
                    id="lesson-container"
                    className="w-full max-w-4xl lesson-h-full flex-col"
                  >
                    <div id="lesson-video" className="flex-1">
                      {videoFile && !lesson.extLiveStreamUrl && (
                        <AzureMP skin="amp-flush" src={ampSource} />
                      )}
                      {(videoLink || (lesson.extLiveStreamUrl && videoUrl)) && (
                        <VideoJS
                          options={videoJsOptions}
                          onReady={handlePlayerReady}
                        />
                      )}
                    </div>
                    <div id="lesson-split" className="my-5 flex-none flex justify-between">
                      <div className="left">
                        <select
                          className="select-box light border-b"
                          onChange={handleDescriptionModeChanged}
                        >
                          <option value="description">강의내용보기</option>
                          {pdfUrl && <option value="pdf">PDF 보기</option>}
                        </select>
                      </div>
                      <div className="right">
                        {notebookUrl && (
                          <button
                            className="bg-green-600 hover:bg-green-700 text-white rounded px-4 py-1 disabled:bg-slate-50"
                            onClick={async () => {
                              handleDownload(notebookUrl);
                            }}
                          >
                            노트북 다운로드
                          </button>
                        )}
                        {/* pdf다운로드시 pdf가 전체 화면으로 표시되는 문제 있음...  {pdfUrl && (
                        <button
                          className="btn"
                          onClick={async () => {
                            handleDownload(pdfUrl);
                          }}
                        >
                          PDF다운로드
                        </button>
                      )} */}
                      </div>
                    </div>
                    {/* <div
                    className={`split split-lesson ${
                      descriptionMode === 'description' ? '' : 'hide'
                    }`}
                  > */}
                    <div id="lesson-content" className="flex-1">
                      <div className="split split-description h-full">
                        <h1>{lesson.title}</h1>
                        <div
                          dangerouslySetInnerHTML={getSanitizedData(
                            lesson.description,
                          )}
                        ></div>
                      </div>
                      <div className="split split-pdf h-full hide">
                        {/* <div
                    className={`split split-pdf ${
                      descriptionMode === 'pdf' ? '' : 'hide'
                    }`}
                  > */}
                        <iframe
                          className="w-full h-full"
                          // style={{ width: '100%', height: '100%' }}
                          src={pdfUrl}
                          frameBorder="0"
                          allowFullScreen
                          onLoad={() => {
                            document.getElementById(
                              "lesson-content",
                            ).style.height = `${
                              document.getElementById("lesson-container")
                                .clientHeight -
                              document.getElementById("lesson-video")
                                .clientHeight -
                              document.getElementById("lesson-split")
                                .clientHeight +
                              20
                            }px`;
                          }}
                        ></iframe>
                      </div>
                    </div>
                  </div>
                </div>
              ) : (
                <LectureList
                  getToken={getToken}
                  onLectureSelected={onLectureSelected}
                  onLessonSelected={onLessonSelected}
                  onLessonLoaded={onLessonLoaded}
                  onResetCategory={onResetCategory}
                />
              )}
              {lessonSelected && lesson.extLiveStreamUrl && (
                <div className="chat-panel hide">
                  <div className="chat-member hide">
                    <div className="tit">
                      <i className="mdi mdi-school"></i>
                      <span>참여 인원</span>
                    </div>
                    <ul className="member-list">
                      <li className="member-item">
                        <img src="" alt="" />
                        <span className="name">학생1</span>
                      </li>
                      <li className="member-item">
                        <img src="" alt="" />
                        <span className="name">학생2</span>
                      </li>
                      <li className="member-item">
                        <img src="" alt="" />
                        <span className="name">학생3</span>
                      </li>
                    </ul>
                  </div>
                  <div className="chat-wrap">
                    <div ref={chatListRef} className="msg-box">
                      <div className="chat">
                        <ul>{renderChatMessages(chatMessages)}</ul>
                      </div>
                    </div>
                    <div className="send-box">
                      <textarea
                        id="message"
                        className="text-form"
                        placeholder="메세지를 입력해 주세요"
                        onKeyPress={handleKeyPress}
                      ></textarea>
                      <button
                        id="sendButton"
                        className="send-btn"
                        onClick={() => {
                          sendMessage();
                        }}
                      ></button>
                    </div>
                  </div>
                </div>
              )}
            </div>
          )}
          {currentCategory === Category.AIHackathon && (
            <HackathonList
              getToken={getToken}
              onResetCategory={onResetCategory}
            />
          )}
        </div>
      )}
    </div>
  );
};

/**
 * A Counter Lumino Widget that wraps a CounterComponent.
 */
export class ModuCodingWidget extends ReactWidget {
  /**
   * Constructs a new CounterWidget.
   */
  constructor() {
    super();
    //this.addClass('add-scroll');
    //this.addClass('jp-ReactWidget');
  }

  render(): JSX.Element {
    return <ModuCodingComponent />;
  }
}
